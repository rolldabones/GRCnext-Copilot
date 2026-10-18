#!/usr/bin/env python3
"""check_fixtures.py: run tools/validate.py over every fixture, example and
prompt sample GRCnext™ Copilot ships, against the verdict each is expected
to receive. Run by .github/workflows/validate.yml on every push.

Usage: python3 tools/check_fixtures.py [--verbose]

Checked:
  tests/evaluation-set/fixtures/clean-bases/*.json        expected ACCEPT
  tests/evaluation-set/fixtures/policy-cases/index.json   expected_schema_verdict
  tests/evaluation-set/fixtures/eval-2026-10-13-02/index.json   expected
  tests/evaluation-set/fixtures/v2.6.0/index.json         expected
  tests/evaluation-set/fixtures/run-inputs/E4-*.json      expected ACCEPT
  examples/*/assessment-result.json                        expected ACCEPT
  every ```json block in advisory-tools/0*.md              expected ACCEPT
Not checked: run 1 payloads and run 1 input registries (schema 2.5 records).

Exit code 0: every item received its expected verdict. 1: at least one
mismatch. 2: an expected file or block is missing.

Final Liability rests with the Human.
"""
import glob, json, os, re, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
sys.dont_write_bytecode = True  # leave no __pycache__ in the clone
import validate  # noqa: E402

EV = os.path.join(ROOT, "tests", "evaluation-set")


def items():
    for f in sorted(glob.glob(os.path.join(EV, "fixtures", "clean-bases", "*.json"))):
        yield f, "ACCEPT"
    for sub, key in (("policy-cases", "expected_schema_verdict"), ("eval-2026-10-13-02", "expected"), ("v2.6.0", "expected")):
        with open(os.path.join(EV, "fixtures", sub, "index.json"), encoding="utf-8") as fh:
            for case in json.load(fh):
                yield os.path.join(EV, case["file"]), case[key]
    for f in sorted(glob.glob(os.path.join(EV, "fixtures", "run-inputs", "E4-*.json"))):
        yield f, "ACCEPT"
    ex = sorted(glob.glob(os.path.join(ROOT, "examples", "*", "assessment-result.json")))
    if not ex:
        yield os.path.join(ROOT, "examples", "*", "assessment-result.json"), "MISSING"
    for f in ex:
        yield f, "ACCEPT"
    tmp = tempfile.mkdtemp(prefix="grcnext-samples-")
    prompts = sorted(glob.glob(os.path.join(ROOT, "advisory-tools", "0*.md")))
    for p in prompts:
        with open(p, encoding="utf-8") as fh:
            blocks = re.findall(r"```json\n(.*?)\n```", fh.read(), re.S)
        if not blocks:
            yield p + " (no json block)", "MISSING"
        for i, b in enumerate(blocks):
            out = os.path.join(tmp, "%s-%d.json" % (os.path.basename(p)[:-3], i + 1))
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(b)
            yield out, "ACCEPT"


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__)
        return 0
    verbose = "--verbose" in argv
    bad = missing = n = 0
    for path, expected in items():
        n += 1
        rel = os.path.relpath(path, ROOT) if path.startswith(ROOT) else path
        if expected == "MISSING" or not os.path.exists(path):
            print("MISSING  %s" % rel)
            missing += 1
            continue
        fx, kind = validate.validate_file(path, validate.DEFAULT_SCHEMAS)
        got = "REJECT" if fx.rejected else "ACCEPT"
        ok = got == expected
        if not ok:
            bad += 1
        if verbose or not ok:
            print("%s %s expected %s got %s (%s)" % ("ok      " if ok else "MISMATCH", rel, expected, got, kind))
            if not ok:
                for i in fx.items:
                    print("    %-6s %-40s %s" % (i["level"], i["rule"], i["message"]))
    print("%d checked, %d mismatched, %d missing" % (n, bad, missing))
    return 2 if missing else (1 if bad else 0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
