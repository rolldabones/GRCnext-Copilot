#!/usr/bin/env python3
"""Run the GRCnext(TM) Copilot main-prompt suite against the Anthropic API.

The suite is twenty-six cases in three files: B1 to B10 in
tests/prompt-evaluation-cases.md, A1 to A9 in tests/adversarial-inputs.md and
SC1 to SC7 in tests/scoring-cases.md. Each case's run input (the ```text block
after "Run input, sent verbatim.") is sent as one user turn in a fresh
conversation. A line {{include <path>}} inside a run input is replaced by that
repository file, byte for byte (one trailing newline dropped).

What is sent as the system prompt: the prompt proper of
prompt/GRCnext-Copilot-v2.md, meaning everything below its first line that is
exactly ---, stripped of leading and trailing whitespace, and nothing else: no
methodology, template or example file. Its SHA-256 over the UTF-8 bytes is the
configuration's identity and is written into every transcript header.

This script does not score; tests/score_prompt_cases.py does, with a scorer
model other than the tested model. The rule a run is read under is ACCEPTANCE.md
in the profile repository (rolldabones/rolldabones).

Usage (from the repository root):
    python3 tests/run_prompt_cases.py --dry-run
    python3 tests/run_prompt_cases.py --model claude-opus-5-5 --stamp LABEL
    python3 tests/run_prompt_cases.py --model claude-opus-5-5 --stamp LABEL2 --only B9,A4

Transcripts go to tests/prompt-runs/transcripts/<stamp>_<model>_<case>.md with
a manifest <stamp>_<model>_run.json beside them. --only under a stamp whose
manifest exists is refused; rerun a subset under a new stamp.

The API key is read only from ANTHROPIC_API_KEY. It is never printed or written.
The user message is written inside a ~~~~text fence, so addresses in a run
input (case A1 carries an invented one) stay out of the account's external
link check, which skips fenced code. The default max_tokens is 32,000: in
run 20261027-R1 claude-sonnet-5-5 reached the 16,000 cap on B9 and B10.

Requires: pip install anthropic (not needed for --dry-run). Added in v2.7.0
(27 October 2026, KST).
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPT_FILE = REPO_ROOT / "prompt" / "GRCnext-Copilot-v2.md"
CASE_FILES = [REPO_ROOT / "tests" / f for f in
              ("prompt-evaluation-cases.md", "adversarial-inputs.md", "scoring-cases.md")]
RUNS_DIR = REPO_ROOT / "tests" / "prompt-runs"
TRANSCRIPTS_DIR = RUNS_DIR / "transcripts"
DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_MAX_TOKENS = 32000
EXPECTED_CASES = 26
EXPECTED_CRITICAL = 12
KST = datetime.timezone(datetime.timedelta(hours=9))
CASE_RE = re.compile(r"^## Case ((?:B|A|SC)\d+): (.+)$", re.MULTILINE)
INPUT_RE = re.compile(r"^Run input, sent verbatim\.\n\n```text\n(.*?)\n```\n", re.MULTILINE | re.DOTALL)
INCLUDE_RE = re.compile(r"^\{\{include ([^}]+)\}\}$", re.MULTILINE)
CRIT_RE = re.compile(r"^\*\*Critical cases:\*\*(.*?)(?:\n\n|\Z)", re.MULTILINE | re.DOTALL)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_system_prompt() -> str:
    text = PROMPT_FILE.read_text(encoding="utf-8")
    parts = re.split(r"^---$", text, maxsplit=1, flags=re.MULTILINE)
    if len(parts) != 2:
        sys.exit("ERROR - Guardrail Violation: no horizontal rule in prompt/GRCnext-Copilot-v2.md")
    return parts[1].strip()


def expand(raw: str) -> str:
    def repl(m):
        rel = m.group(1).strip()
        path = (REPO_ROOT / rel).resolve()
        if REPO_ROOT not in path.parents or not path.is_file():
            sys.exit(f"ERROR - Guardrail Violation: include {rel} is not a repository file")
        body = path.read_text(encoding="utf-8")
        return body[:-1] if body.endswith("\n") else body
    return INCLUDE_RE.sub(repl, raw)


def parse_critical(text: str) -> set:
    ids = set()
    for m in CRIT_RE.finditer(text):
        para = m.group(1)
        for a, lo, hi in re.findall(r"\b(B|A|SC)(\d+) to (?:B|A|SC)?(\d+)\b", para):
            ids |= {f"{a}{i}" for i in range(int(lo), int(hi) + 1)}
        ids |= set(re.findall(r"\b((?:B|A|SC)\d+)\b", para))
    return ids


def load_cases():
    """Return (cases, critical): cases is a list of dicts in suite order."""
    cases, critical = [], set()
    for f in CASE_FILES:
        text = f.read_text(encoding="utf-8")
        critical |= parse_critical(text)
        heads = list(CASE_RE.finditer(text))
        for i, h in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            section = text[h.start():end]
            section = re.split(r"\n---\n", section)[0].rstrip() + "\n"
            m = INPUT_RE.search(section)
            if not m:
                sys.exit(f"ERROR - Guardrail Violation: case {h.group(1)} in {f.name} has no run input")
            message = expand(m.group(1))
            spec = section[:m.start()] + "[Run input: sent to the assistant as the user message below.]\n" + section[m.end():]
            cases.append({"id": h.group(1), "name": h.group(2).strip(), "file": f.name,
                          "message": message, "spec": spec})
    ids = [c["id"] for c in cases]
    if len(set(ids)) != len(ids):
        sys.exit("ERROR - Guardrail Violation: duplicate case IDs")
    unknown = critical - set(ids)
    if unknown:
        sys.exit(f"ERROR - Guardrail Violation: critical IDs not in the suite: {sorted(unknown)}")
    if len(cases) != EXPECTED_CASES or len(critical) != EXPECTED_CRITICAL:
        print(f"WARNING: expected {EXPECTED_CASES} cases and {EXPECTED_CRITICAL} critical, "
              f"parsed {len(cases)} and {len(critical)}")
    return cases, critical


def safe(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "-", s)


def call(client, **kw):
    """One Messages request with backoff on 429, 529, 5xx and connection errors.

    Sent as a stream and read to the final message: the SDK refuses a
    non-streaming request whose max_tokens could run past ten minutes, which
    32,000 does (found 27 October 2026, KST, at the first call of run R2).
    The final message carries the same content, stop_reason and usage.
    """
    import anthropic
    for attempt in range(7):
        try:
            with client.messages.stream(**kw) as stream:
                return stream.get_final_message()
        except (anthropic.RateLimitError, anthropic.APIConnectionError, anthropic.InternalServerError) as e:
            wait = min(120, 5 * 2 ** attempt)
            print(f"    retry {attempt + 1} in {wait}s ({type(e).__name__})", flush=True)
            time.sleep(wait)
        except anthropic.APIStatusError as e:
            if e.status_code in (429, 529) or e.status_code >= 500:
                wait = min(120, 5 * 2 ** attempt)
                print(f"    retry {attempt + 1} in {wait}s (HTTP {e.status_code})", flush=True)
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("API retries exhausted")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--only", default="", help="Comma-separated case IDs, e.g. B9,A4")
    ap.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    ap.add_argument("--stamp", default="", help="Run label shared by several models (default: KST time now)")
    ap.add_argument("--dry-run", action="store_true", help="Parse and print; no API call")
    args = ap.parse_args()

    system_prompt = load_system_prompt()
    digest = sha(system_prompt)
    cases, critical = load_cases()
    chosen = {s.strip() for s in args.only.split(",") if s.strip()}
    if chosen:
        bad = chosen - {c["id"] for c in cases}
        if bad:
            sys.exit(f"ERROR - Guardrail Violation: unknown case IDs {sorted(bad)}")
        cases = [c for c in cases if c["id"] in chosen]
    print(f"Prompt proper SHA-256: {digest} ({len(system_prompt.split())} words)")
    print(f"Critical cases: {', '.join(c for c in [x['id'] for x in load_cases()[0]] if c in critical)}")

    if args.dry_run:
        for c in cases:
            print(f"{c['id']:<5}{'*' if c['id'] in critical else ' '} {len(c['message'].split()):>5} words | "
                  f"{c['message'][:80].replace(chr(10), ' ')}")
        print(f"Dry run: {len(cases)} case(s) parsed, * = critical. No API call made.")
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")
    try:
        import anthropic
    except ImportError:
        sys.exit("ERROR - Guardrail Violation: anthropic package missing. pip install anthropic")
    client = anthropic.Anthropic()
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = safe(args.stamp) if args.stamp else datetime.datetime.now(KST).strftime("%Y%m%d-%H%M%S")
    mlabel = safe(args.model)
    mpath = TRANSCRIPTS_DIR / f"{stamp}_{mlabel}_run.json"
    if chosen and mpath.exists():
        sys.exit(f"ERROR - Guardrail Violation: {mpath.name} exists; rerun the subset under a new --stamp")
    print(f"Model: {args.model}  Stamp: {stamp}  max_tokens: {args.max_tokens}")
    manifest = {"stamp": stamp, "model_requested": args.model, "max_tokens": args.max_tokens,
                "prompt_file": "prompt/GRCnext-Copilot-v2.md", "prompt_proper_sha256": digest,
                "attachments": "none", "started_kst": datetime.datetime.now(KST).isoformat(timespec="seconds"),
                "transcripts": []}
    truncated = []
    for c in cases:
        print(f"Running {c['id']} {c['name']} ...", flush=True)
        r = call(client, model=args.model, max_tokens=args.max_tokens, system=system_prompt,
                 messages=[{"role": "user", "content": c["message"]}])
        reply = "".join(b.text for b in r.content if b.type == "text")
        trunc = r.stop_reason == "max_tokens"
        if trunc:
            truncated.append(c["id"])
        out = TRANSCRIPTS_DIR / f"{stamp}_{mlabel}_{c['id']}.md"
        out.write_text(
            f"# {c['id']} {c['name']}\n\n"
            f"**Model requested:** {args.model}  **Model returned:** {r.model}  **Run:** {stamp}\n"
            f"**Prompt proper SHA-256:** {digest}\n"
            f"**Run input SHA-256:** {sha(c['message'])}  **Case file:** tests/{c['file']}  "
            f"**Critical:** {'yes' if c['id'] in critical else 'no'}\n"
            f"**max_tokens:** {args.max_tokens}  **stop_reason:** {r.stop_reason}  "
            f"**Input tokens:** {r.usage.input_tokens}  **Output tokens:** {r.usage.output_tokens}\n"
            f"**Truncated:** {'YES, do not score as complete' if trunc else 'no'}\n\n"
            f"## User message\n\n~~~~text\n{c['message']}\n~~~~\n\n## Assistant response\n\n{reply}\n\n"
            f"<!-- end of transcript; written by tests/run_prompt_cases.py -->\n", encoding="utf-8")
        manifest["transcripts"].append({"case": c["id"], "file": out.name, "model_returned": r.model,
                                        "stop_reason": r.stop_reason, "truncated": trunc,
                                        "input_tokens": r.usage.input_tokens,
                                        "output_tokens": r.usage.output_tokens})
        print(f"  -> stop_reason={r.stop_reason}{'  TRUNCATED' if trunc else ''}", flush=True)
    manifest["finished_kst"] = datetime.datetime.now(KST).isoformat(timespec="seconds")
    mpath.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\nDone. {len(cases)} transcript(s), manifest {mpath.relative_to(REPO_ROOT)}.")
    if truncated:
        print(f"TRUNCATED: {', '.join(truncated)}. A truncated case is not exercised (ACCEPTANCE.md (a)).")


if __name__ == "__main__":
    main()
