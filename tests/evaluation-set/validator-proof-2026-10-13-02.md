# Validator proof 2, 13 October 2026

`tools/validate.py` as shipped in GRCnext™ Copilot v2.5.0, proved on the
maintainer's machine (Python 3.10.12, jsonschema 3.2.0, Draft 7) after the
second external evaluation of v2.4.0 reported four problems and the
session's own audit found three more. Method as in proof 1. Forty-four
proofs, forty-four passed: the twenty of proof 1 re-run, ten new rule
proofs, fourteen malformed-payload probes.

## Status

**INCOMPLETE.** The validator is a control on the interchange layer. ACCEPT
means the record follows the repository's written rules as far as they are
stated mechanically. It is not a readiness conclusion. Human review of every
readiness decision and every PASS is retained. Known gaps are listed in the
tool's docstring.

## What the second evaluation found, and the rule that now catches it

| Evaluation finding | v2.4.0 result | Rule | v2.5.0 result |
|---|---|---|---|
| Registry asserts ON while its only verified event establishes OFF | ACCEPT | R6: derive the newest evidenced execution event per switch from the log and compare with status | REJECT |
| Exit PASS includes an open ON request with no previous verified state | ACCEPT | E4 widened: any set `requested_state` under PASS is an open request; equal to history is a WARN (no-op), otherwise REJECT | REJECT |
| Conditionally Demonstrated despite a failed core gate | ACCEPT | A9 | REJECT |
| A gate entry is `null` | crash | shape filtering (`dicts`, `obj`) and a catch that reports "S0 malformed, policy rules not applied" | REJECT, no crash |

Found by the session's audit the same hour and also closed: A10
(Conditionally Demonstrated with tolerance Not Met), R5 (status against a
recorded `last_verified_state`), E5 (PASS with an unowned or undated
obligation), E6 (PASS with a missing switch). Added as warnings: A11 (a
core domain at level 0 under Demonstrated), E7 (PASS with `feasible_72h`
false).

## New rule proofs

| Rule | Level | Base | Defect constructed | Fired | Exit |
|---|---|---|---|---|---|
| A9 | REJECT | assessment-result | decision Conditionally Demonstrated, gate 6 Fail | yes | 1 |
| A10 | REJECT | assessment-result | decision Conditionally Demonstrated, tolerance Not Met | yes | 1 |
| A11 | WARN | assessment-result | exits 0, constraint 0 | yes | 0 |
| R5 | REJECT | switch-registry | status ON, last_verified_state OFF | yes | 1 |
| R6 | REJECT | switch-registry | status ON, only evidenced event ON->OFF | yes | 1 |
| E4 (no history) | REJECT | exit-prover | requested_state ON, last_verified_state absent | yes | 1 |
| E4 (no-op) | WARN | exit-prover | requested_state equal to last_verified_state | yes | 0 |
| E5 | REJECT | exit-prover | obligation owner Unknown under PASS | yes | 1 |
| E6 | REJECT | exit-prover | switch status missing under PASS | yes | 1 |
| E7 | WARN | exit-prover | feasible_72h false under PASS | yes | 0 |

## Malformed-payload probes (all: exit 1, no traceback, an S0 finding)

gate entry null; gates as strings; gates not a list; tolerance_result a
string; capability_profile a list; evidence_items as strings; evidence_items
a dict; gaps as strings; switches as strings; obligations with a null entry;
log as strings; registry switches as strings; log a dict; switch entry null.

## Regression

Clean bases: 3 of 3 ACCEPT. Policy-case fixtures C01 to C11: all as
`index.json` expects. Run 1 payloads under v2.5.0: 7 of 8 REJECT, S5 ACCEPT,
unchanged from v2.4.0. The four evaluation counterexamples are fixtures in
`fixtures/eval-2026-10-13-02/`.

Final Liability rests with the Human.
