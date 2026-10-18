#!/usr/bin/env python3
"""validate.py: structural and policy validation of GRCnext™ interchange payloads.

STATUS: INCOMPLETE. This validator is a control on the interchange layer, not a
readiness decision. An ACCEPT means the payload follows the repository's own
written rules as far as they are stated mechanically; it does not mean the
service is ready, the evidence is true or the conclusion is right. Human
review of every readiness decision and every Demonstrated proof is retained. Known gaps are
listed under KNOWN GAPS at the end of this docstring.

Usage:
  python3 tools/validate.py PAYLOAD.json [PAYLOAD.json ...]
  python3 tools/validate.py --schemas DIR PAYLOAD.json
  python3 tools/validate.py --json PAYLOAD.json      (machine-readable findings)

Exit code 0: every payload valid with no REJECT finding. Exit code 1: at least
one REJECT. Exit code 2: a payload could not be read or its kind could not be
determined. WARN findings never change the exit code.

What it does. Step 1 validates the payload against the schema its kind names
(the `tool` field for suite payloads; the field set for an assessment result,
a service dossier or an evidence item). Step 2 applies the policy rules JSON
Schema cannot express. Each rule quotes the governing sentence of the
repository text beside it so the reading can be checked. A rule the text does
not pin to a sentence is a WARN, never a REJECT.

What it cannot do. It establishes that a record follows the repository's own
rules. It cannot establish that a document exists or that an event happened.
Observation and source review remain necessary.

Dependencies: Python 3.8+, jsonschema (3.2 or 4.x). Reads files only; no network.

Added in GRCnext™ Copilot v2.4.0 on the maintainer's ruling of 13 October
2026, after run 1 of tests/advisory-suite-cases.md found that every payload
the advisory prompts emitted failed the schemas. v2.5.0 (same day): malformed
payloads no longer crash the policy step; six false acceptances closed (A9,
A10, R5, R6, E4 widened, E5, E6); two warnings added (A11, E7). Two of the
six were found by the maintainer's second external evaluation of v2.4.0
(status against the log's own execution evidence; an open request under
PASS with no recorded history); the crash was found by both. v2.6.0 (18
October 2026): interchange contract 2.6 (schema_version required on every
top-level payload; S1 names a pre-2.6 payload); R6 no longer counts drill
rows as execution events (drills never change production status); the
suite verdict scale is Demonstrated / Conditionally Demonstrated / Not
Demonstrated; A5 rejects, every core gate being material; the 72-hour
boolean is replaced by three milestones against the service's own
tolerance, checked by M1 to M4.

KNOWN GAPS (v2.6.0). Freshness is free text, so a Verified item whose
freshness_assessment says it is stale is not caught. "Material" items are not
machine-readable, so E3 warns where the text would fail (gates are all
material from v2.6.0, so A5 rejects).
Evidence confidence has no stated thresholds, so A7 warns. The validator reads
one payload at a time and does not cross-check a proof against the registry it
cites. None of these is a reason to skip human review; all of them are.

Final Liability rests with the Human.
"""
import argparse, json, os, sys

try:
    import jsonschema
except ImportError:
    sys.stderr.write("validate.py needs the jsonschema package: pip install jsonschema\n")
    sys.exit(2)

Validator = getattr(jsonschema, "Draft202012Validator", None) or jsonschema.Draft7Validator

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SCHEMAS = os.path.normpath(os.path.join(HERE, "..", "schemas"))

TOOL_SCHEMAS = {
    "exit_prover": "exit-prover-output.schema.json",
    "switch_registry": "switch-registry-output.schema.json",
    "pipes_mapper": "pipes-mapper-output.schema.json",
    "treasury_reroute_planner": "treasury-reroute-plan.schema.json",
    "data_switchboard_planner": "data-switchboard-plan.schema.json",
    "clean_market_exit_kit": "clean-market-exit.schema.json",
}
GATES = [
    "service_and_owner_defined", "tolerance_approved_and_measurable", "dependencies_mapped",
    "switch_authority_available", "executable_exit_for_leading_concentration",
    "severe_but_plausible_exercise_completed", "evidence_shows_tolerance_result",
    "corrective_actions_have_owners_and_dates",
]


def dicts(seq):
    """Items of seq that are objects. Non-object items are the structural step's to report."""
    return [x for x in (seq or []) if isinstance(x, dict)] if isinstance(seq, list) else []


def obj(x):
    return x if isinstance(x, dict) else {}


class Findings:
    def __init__(self, path):
        self.path = path
        self.items = []

    def reject(self, rule, where, msg, source=None):
        self.items.append({"level": "REJECT", "rule": rule, "path": where, "message": msg, "source": source})

    def warn(self, rule, where, msg, source=None):
        self.items.append({"level": "WARN", "rule": rule, "path": where, "message": msg, "source": source})

    @property
    def rejected(self):
        return any(i["level"] == "REJECT" for i in self.items)


def detect_kind(payload):
    if not isinstance(payload, dict):
        return None
    tool = payload.get("tool")
    if tool in TOOL_SCHEMAS:
        return tool
    if "readiness_decision" in payload and "gates" in payload:
        return "assessment_result"
    if "evidence_id" in payload and "verification_status" in payload:
        return "evidence_item"
    if "service_definition" in payload and "impact_tolerance" in payload:
        return "service_dossier"
    return None


KIND_SCHEMAS = dict(TOOL_SCHEMAS)
KIND_SCHEMAS.update({
    "assessment_result": "assessment-result.schema.json",
    "evidence_item": "evidence-item.schema.json",
    "service_dossier": "service-dossier.schema.json",
})


def load_schema(schemas_dir, name):
    with open(os.path.join(schemas_dir, name), encoding="utf-8") as f:
        return json.load(f)


def jpath(err):
    return "$" + "".join("[%d]" % p if isinstance(p, int) else "." + str(p) for p in err.absolute_path)


def structural(payload, schema, fx):
    """Step 1. Structural validation. Source: the schema file itself."""
    errs = sorted(Validator(schema).iter_errors(payload), key=lambda e: list(e.absolute_path))
    for e in errs:
        fx.reject("S0 schema", jpath(e), e.message[:200], schema.get("$id"))
    return not errs


# ---------------------------------------------------------------- policy rules

def policy_evidence_item(item, where, fx, ev_schema):
    """Apply evidence-item.schema.json to one item wherever it appears.
    Source: advisory-tools/03-exit-prover.md s6, 'Each entry in evidence_items is an
    evidence item in the form of schemas/evidence-item.schema.json'."""
    for e in Validator(ev_schema).iter_errors(item):
        fx.reject("E1 evidence item form", where + jpath(e)[1:], e.message[:200],
                  "03-exit-prover.md s6: each entry in evidence_items is an evidence item in the form of evidence-item.schema.json")


def policy_exit_prover(p, fx, schemas):
    ev = load_schema(schemas, "evidence-item.schema.json")
    items = dicts(p.get("evidence_items"))
    for i, item in enumerate(items):
        policy_evidence_item(item, "$.evidence_items[%d]" % i, fx, ev)
    verdict = p.get("verdict")
    if verdict == "Demonstrated":
        # Source: 03-exit-prover.md s5 CHECKPOINT: 'Demonstrated - no critical gaps, every material
        # item Verified under the Phase 4 rule. Demonstrated cannot rest on a representation.'
        for i, item in enumerate(items):
            if item.get("verification_status") == "Verified" and item.get("evidence_type") == "interview representation":
                fx.reject("E2 Demonstrated on representation", "$.evidence_items[%d]" % i,
                          "a Verified interview representation cannot support Demonstrated",
                          "03-exit-prover.md s5: Demonstrated cannot rest on a representation, including a detailed one")
        for i, g in enumerate(dicts(p.get("gaps"))):
            if not g.get("owner") or not g.get("due"):
                fx.warn("E3 Demonstrated gap without owner or due", "$.gaps[%d]" % i,
                        "Demonstrated carries no critical gaps; an unowned or undated gap is not shown to be non-critical",
                        "03-exit-prover.md s5: Not Demonstrated - one or more critical gaps. List each gap with owner and due date")
        for i, o in enumerate(dicts(p.get("obligations"))):
            owner, deadline = (o.get("owner") or "").strip(), (o.get("deadline") or "").strip()
            if not owner or owner.lower() == "unknown" or not deadline or deadline.lower() == "unknown":
                fx.reject("E5 Demonstrated with unowned or undated obligation", "$.obligations[%d]" % i,
                          "obligation owner or deadline missing or Unknown under Demonstrated",
                          "03-exit-prover.md s5 CHECKPOINT: every obligation has an owner and deadline")
        for i, s in enumerate(dicts(p.get("switches"))):
            if s.get("status") == "missing":
                fx.reject("E6 Demonstrated with missing switch", "$.switches[%d]" % i,
                          "a needed switch not found in the registry is a MISSING SWITCH finding, a gap under Demonstrated",
                          "03-exit-prover.md s5: where a needed switch does not exist, record a MISSING SWITCH finding; CHECKPOINT: every action has a switch or a documented manual step")
    policy_milestones(p, fx, "verdict")
    for i, s in enumerate(dicts(p.get("switches"))):
        rs, lvs = s.get("requested_state"), s.get("last_verified_state")
        if rs and verdict == "Demonstrated":
            if lvs == rs:
                fx.warn("E4 request matching verified state under Demonstrated", "$.switches[%d]" % i,
                        "requested_state equals last_verified_state; a no-op request, but still open until closed in the registry",
                        "02-switch-registry.md s5 MODE: FLIP (b): if identical, report no-op")
            else:
                fx.reject("E4 open request counted in Demonstrated", "$.switches[%d]" % i,
                          "switch has an open request (requested_state %s, last verified state %s); an active request is unresolved and is a gap, not a flipped switch" % (rs, lvs or "not recorded"),
                          "03-exit-prover.md s6: an entry with requested_state set ... is an open request and is reported as a gap; 02-switch-registry.md s7: a request is never consumed as an executed flip")


MILESTONES = ["containment", "interim_continuity", "final_exit"]
SRC_M = "03-exit-prover.md s5 Milestones against tolerance (v1.3); methodology: one tolerance, the service's own"


def policy_milestones(p, fx, verdict_field=None):
    """M1 to M4. The three milestones against the service's tolerance (schema 2.6).
    Source: the Milestones against tolerance step of 03, 04, 05 and 06 (v2.6.0)."""
    ms = dicts(p.get("milestones"))
    names = [m.get("milestone") for m in ms]
    if names and names != MILESTONES:
        fx.reject("M3 milestone set", "$.milestones",
                  "milestones are %s; exactly containment, interim_continuity, final_exit in that order" % names, SRC_M)
    tol = p.get("tolerance_hours")
    for i, m in enumerate(ms):
        e, lim, w = m.get("elapsed_hours"), m.get("limit_hours"), m.get("within_limit")
        num = lambda x: isinstance(x, (int, float)) and not isinstance(x, bool)
        if num(e) and num(lim):
            if w is not (e <= lim):
                fx.reject("M1 milestone arithmetic", "$.milestones[%d]" % i,
                          "within_limit %s but elapsed %s h against limit %s h" % (w, e, lim), SRC_M)
        elif w is not None:
            fx.reject("M1 milestone arithmetic", "$.milestones[%d]" % i,
                      "within_limit %s with elapsed %s and limit %s; it is null when either is null" % (w, e, lim), SRC_M)
        if m.get("basis") == "unknown" and e is not None:
            fx.reject("M1 milestone arithmetic", "$.milestones[%d]" % i,
                      "basis unknown with elapsed_hours %s; an unknown duration is null" % e, SRC_M)
        if m.get("milestone") == "interim_continuity":
            if num(tol) and lim != tol:
                fx.reject("M2 interim continuity limit", "$.milestones[%d].limit_hours" % i,
                          "limit %s h is not the tolerance %s h" % (lim, tol),
                          "interim continuity is measured against the service's impact tolerance")
            if tol is None and lim is not None:
                fx.reject("M2 interim continuity limit", "$.milestones[%d].limit_hours" % i,
                          "limit %s h with no tolerance supplied; the limit is the tolerance" % lim,
                          "interim continuity is measured against the service's impact tolerance")
            if verdict_field and p.get(verdict_field) == "Demonstrated":
                if w is False:
                    fx.reject("M4 Demonstrated outside tolerance", "$.milestones[%d]" % i,
                              "interim continuity not within the tolerance under Demonstrated",
                              "scoring-method.md D: Demonstrated requires execution within tolerance")
                elif w is None or m.get("basis") in ("assumed", "unknown"):
                    fx.warn("M4 Demonstrated with tolerance fit not shown", "$.milestones[%d]" % i,
                            "interim continuity fit is %s on basis %s under Demonstrated" % (w, m.get("basis")),
                            "scoring-method.md D: evidence shows execution within tolerance")


def policy_plan(p, fx, schemas):
    policy_milestones(p, fx, None)


def policy_kit(p, fx, schemas):
    policy_milestones(p, fx, "verdict")


def policy_switch_registry(p, fx, schemas):
    log = dicts(p.get("log"))
    evidenced, derived = {}, {}
    for i, row in enumerate(log):
        ev = row.get("event")
        if (ev in ("completed", "verified") and row.get("evidence_ref") and not row.get("drill")
                and row.get("action") in ("ON->OFF", "OFF->ON")):
            # newest evidenced production execution event per switch, by timestamp string order then
            # log order. Drill rows are excluded: 02-switch-registry.md s4, drill events never change
            # the production status (v2.6.0; the v2.5.0 derivation counted them, found by review 08 A6).
            key = (str(row.get("timestamp") or ""), i)
            prev = derived.get(row.get("switch_id"))
            if prev is None or key >= prev[0]:
                derived[row.get("switch_id")] = (key, row["action"].split("->")[1], i)
    for i, row in enumerate(log):
        ev = row.get("event")
        if ev in ("completed", "failed", "verified") and not row.get("evidence_ref"):
            fx.reject("R1 execution event without evidence", "$.log[%d]" % i,
                      "%s event carries no evidence_ref" % ev,
                      "02-switch-registry.md s4: evidence_ref (for completed, failed and verified events, the evidence item that establishes the result)")
        if ev in ("completed", "verified") and row.get("evidence_ref"):
            evidenced.setdefault(row.get("switch_id"), 0)
            evidenced[row.get("switch_id")] += 1
    for i, s in enumerate(dicts(p.get("switches"))):
        sid, st, rs, lvs = s.get("id"), s.get("status"), s.get("requested_state"), s.get("last_verified_state")
        if st in ("ON", "OFF") and lvs in ("ON", "OFF") and st != lvs and not rs:
            fx.reject("R5 status contradicts last verified state", "$.switches[%d]" % i,
                      "status %s against last_verified_state %s with no open request" % (st, lvs),
                      "02-switch-registry.md s4: status is the last verified actual state; last_verified_state is the state established by the newest verified or completed event with evidence")
        d = derived.get(sid)
        if d and st in ("ON", "OFF") and st != d[1] and not rs:
            fx.reject("R6 status contradicts execution evidence", "$.switches[%d]" % i,
                      "status %s but the newest evidenced production execution event (log[%d]) establishes %s" % (st, d[2], d[1]),
                      "02-switch-registry.md s4: status is the last verified actual state ... only a completed or verified event supported by a named evidence item sets status")
        if rs and st != "Unknown":
            fx.reject("R2 open request with asserted state", "$.switches[%d]" % i,
                      "requested_state is set but status is %s; status is Unknown while a request is open" % st,
                      "02-switch-registry.md s4: status (ON/OFF/Unknown: the last verified actual state; Unknown while a request is open ...)")
        if st in ("ON", "OFF") and not evidenced.get(sid):
            fx.warn("R3 declared state", "$.switches[%d]" % i,
                    "status %s has no completed or verified log event with evidence_ref; read as a declared state (version 1.0 registry or unevidenced)" % st,
                    "02-switch-registry.md s4: a row with no event field ... is read as a declared flip: it establishes that a flip was recorded, not that it was executed")
    for i, row in enumerate(log):
        if not row.get("event"):
            fx.warn("R4 version 1.0 log row", "$.log[%d]" % i, "row has no event field; a declared flip, not evidence of execution",
                    "02-switch-registry.md s4")


def policy_assessment_result(p, fx, schemas):
    gates = dicts(p.get("gates"))
    names = [g.get("gate") for g in gates]
    # Source: scoring-method.md, Readiness gates: 'Eight core gates ... Classify each gate exactly
    # once per service ... do not issue split or hybrid gate states.'
    src_gates = "scoring-method.md Readiness gates: eight core gates; classify each gate exactly once per service"
    for g in GATES:
        c = names.count(g)
        if c == 0:
            fx.reject("A1 gate missing", "$.gates", "gate %s absent" % g, src_gates)
        elif c > 1:
            fx.reject("A1 gate duplicated", "$.gates", "gate %s appears %d times" % (g, c), src_gates)
    cp = obj(p.get("capability_profile"))
    try:
        m = min(int(cp["pipes"]), int(cp["switches"]), int(cp["exits"]))
        if int(p.get("constraint_level")) != m:
            fx.reject("A2 constraint level", "$.constraint_level",
                      "constraint_level %s is not min(pipes, switches, exits) = %d" % (p.get("constraint_level"), m),
                      "scoring-method.md B: Constraint Level = minimum of Pipes, Switches and Exits")
    except (KeyError, TypeError, ValueError):
        pass  # structural step reports the missing or ill-typed field
    status = {g.get("gate"): g for g in gates}
    effective = {}
    for g, row in status.items():
        st = row.get("status")
        if st == "Not Applicable" and not (row.get("note") or "").strip():
            fx.warn("A3 unsupported Not Applicable", "$.gates[%s]" % g, "Not Applicable without a note; treated as Unknown",
                    "scoring-method.md Gate effect: an unsupported Not Applicable is treated as Unknown")
            st = "Unknown"
        effective[g] = st
    decision = p.get("readiness_decision")
    if decision == "Demonstrated":
        for g, st in effective.items():
            if st in ("Fail", "Unknown"):
                fx.reject("A4 Demonstrated with failed or unknown gate", "$.readiness_decision",
                          "gate %s is %s" % (g, st),
                          "scoring-method.md Gate effect: any core gate at Fail or Unknown prevents a Demonstrated decision")
            elif st == "Provisional Pass":
                fx.reject("A5 Demonstrated with Provisional Pass", "$.readiness_decision",
                          "gate %s is Provisional Pass; every core gate is material, so the decision is capped at Conditionally Demonstrated" % g,
                          "scoring-method.md Gate effect: every core gate is material; a Provisional Pass on any core gate caps the decision at Conditionally Demonstrated")
        tr = obj(p.get("tolerance_result")).get("result")
        if tr != "Met":
            fx.reject("A6 Demonstrated without tolerance met", "$.tolerance_result.result",
                      "tolerance result is %s" % tr,
                      "scoring-method.md D: Demonstrated. Core gates pass, the capability has been exercised, and evidence shows execution within tolerance")
        if p.get("evidence_confidence") in ("Low", "Indeterminate"):
            fx.warn("A7 Demonstrated on low confidence", "$.evidence_confidence",
                    "evidence_confidence %s with a Demonstrated decision" % p.get("evidence_confidence"),
                    "evidence-standard.md: Low signals heavy reliance on drafts, representations, assumptions or stale evidence")
        for dom in ("pipes", "switches", "exits"):
            if cp.get(dom) == 0:
                fx.warn("A11 Demonstrated with a core domain at level 0", "$.capability_profile.%s" % dom,
                        "%s is at level 0 under a Demonstrated decision; the text does not state a floor mechanically" % dom,
                        "scoring-method.md B: optionality requires all three; a mapped dependency you cannot switch or exit is not optionality")
    if decision == "Conditionally Demonstrated":
        for g, st in effective.items():
            if st == "Fail":
                fx.reject("A9 Conditionally Demonstrated with failed gate", "$.readiness_decision",
                          "gate %s is Fail; a failed core gate is Not Demonstrated" % g,
                          "scoring-method.md D: Not Demonstrated. A core gate fails, critical evidence is absent, or execution has not been shown within tolerance")
        if obj(p.get("tolerance_result")).get("result") == "Not Met":
            fx.reject("A10 Conditionally Demonstrated with tolerance not met", "$.tolerance_result.result",
                      "tolerance Not Met; execution not shown within tolerance is Not Demonstrated",
                      "scoring-method.md D: Not Demonstrated ... execution has not been shown within tolerance")
    tr = obj(p.get("tolerance_result"))
    if tr.get("result") in ("Met", "Not Met") and not (tr.get("clock_start_event") and tr.get("clock_stop_event")):
        fx.reject("A8 tolerance result without clock events", "$.tolerance_result",
                  "result %s without clock_start_event and clock_stop_event" % tr.get("result"),
                  "scoring-method.md E: a tolerance result with no clock-start and clock-stop event is incomplete")


POLICY = {
    "exit_prover": policy_exit_prover,
    "switch_registry": policy_switch_registry,
    "assessment_result": policy_assessment_result,
    "treasury_reroute_planner": policy_plan,
    "data_switchboard_planner": policy_plan,
    "clean_market_exit_kit": policy_kit,
}


def validate_file(path, schemas_dir):
    fx = Findings(path)
    try:
        with open(path, encoding="utf-8") as f:
            payload = json.load(f)
    except (OSError, ValueError) as e:
        fx.reject("S0 unreadable", "$", str(e)[:200])
        return fx, None
    kind = detect_kind(payload)
    if kind is None:
        fx.reject("S0 unknown kind", "$", "no tool field in the suite set and no recognizable field set")
        return fx, None
    schema = load_schema(schemas_dir, KIND_SCHEMAS[kind])
    if kind != "evidence_item" and "schema_version" not in payload:
        fx.reject("S1 pre-2.6 payload", "$", "no schema_version; the payload predates interchange contract 2.6",
                  "schemas/README.md: migrate per the 2.5 to 2.6 rules")
    structural(payload, schema, fx)
    rule = POLICY.get(kind)
    if rule:
        try:
            rule(payload, fx, schemas_dir)
        except Exception as e:  # a malformed payload must report, never crash
            fx.reject("S0 malformed, policy rules not applied", "$",
                      "%s: %s" % (type(e).__name__, str(e)[:120]),
                      "validate.py: the structural findings above describe the malformation")
    return fx, kind


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--schemas", default=DEFAULT_SCHEMAS)
    ap.add_argument("--json", action="store_true", help="machine-readable findings")
    a = ap.parse_args(argv)
    out, exit_code = [], 0
    for path in a.paths:
        fx, kind = validate_file(path, a.schemas)
        verdict = "REJECT" if fx.rejected else "ACCEPT"
        if kind is None:
            exit_code = max(exit_code, 2)
        elif fx.rejected:
            exit_code = max(exit_code, 1)
        out.append({"file": path, "kind": kind, "verdict": verdict, "findings": fx.items})
        if not a.json:
            print("%s %s (%s): %d finding(s)" % (verdict, path, kind or "unknown", len(fx.items)))
            for i in fx.items:
                print("  %-6s %-40s %-28s %s" % (i["level"], i["rule"], i["path"], i["message"]))
    if a.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
