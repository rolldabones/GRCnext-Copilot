# Validator proof, 13 October 2026

`tools/validate.py` as shipped in GRCnext™ Copilot v2.4.0, proved against the
three clean bases in `fixtures/clean-bases/` on the maintainer's machine
(Python 3.10.12, jsonschema 3.2.0, Draft 7 validator). Method, per the
account's rule for any tool change: run the rule on a clean base and confirm
it is quiet; construct the defect; confirm the rule fires at the level it
claims and the exit code follows; remove the defect. Twenty proofs, twenty
passed. The proof script lived in session scratch and is not shipped; the
table is what it printed, with the mutation stated.

| Rule | Level | Base | Defect constructed | Fired | Exit code on defect |
|---|---|---|---|---|---|
| E1 evidence item form | REJECT | exit-prover | `claim_tested` removed from an evidence item | yes | 1 |
| E2 PASS on representation | REJECT | exit-prover | evidence item type set to interview representation while Verified | yes | 1 |
| E3 PASS gap without owner or due | WARN | exit-prover | `owner` removed from a gap | yes | 0 |
| E4 open request counted in PASS | REJECT | exit-prover | switch `requested_state` ON against `last_verified_state` OFF | yes | 1 |
| R1 execution event without evidence | REJECT | switch-registry | `evidence_ref` removed from a verified row | yes | 1 |
| R2 open request with asserted state | REJECT | switch-registry | `requested_state` ON with status OFF | yes | 1 |
| R3 declared state | WARN | switch-registry | log emptied under a status OFF | yes | 0 |
| R4 version 1.0 log row | WARN | switch-registry | `event` removed from a row | yes | 0 |
| A1 gate missing | REJECT | assessment-result | eighth gate removed | yes | 1 |
| A1 gate duplicated | REJECT | assessment-result | first gate appended again | yes | 1 |
| A2 constraint level | REJECT | assessment-result | `constraint_level` 4 against min 3 | yes | 1 |
| A3 unsupported Not Applicable | WARN | assessment-result | gate 8 Not Applicable without note, decision Conditionally Demonstrated | yes | 0 |
| A4 Demonstrated with failed or unknown gate | REJECT | assessment-result | gate 6 set to Fail | yes | 1 |
| A4 via A3 | REJECT | assessment-result | gate 8 Not Applicable without note, decision Demonstrated | yes | 1 |
| A5 Demonstrated with Provisional Pass | WARN | assessment-result | gate 3 Provisional Pass | yes | 0 |
| A6 Demonstrated without tolerance met | REJECT | assessment-result | tolerance result Not Tested | yes | 1 |
| A7 Demonstrated on low confidence | WARN | assessment-result | evidence confidence Low | yes | 0 |
| A8 tolerance result without clock events | REJECT | assessment-result | `clock_stop_event` removed | yes | 1 |
| S0 schema (enum) | REJECT | exit-prover | verdict PENDING | yes | 1 |
| S0 schema (type) | REJECT | switch-registry | log timestamp null | yes | 1 |

Clean bases: exit code 0 on all three. Unknown kind (`{"hello": 1}`): exit
code 2.

What the proof does not establish: that the rules are the right reading of
`methodology/scoring-method.md`. Each rule quotes its governing sentence in
the source so that reading can be checked; A5 and A7 are WARN because the
text's "material gate" and the confidence thresholds are not stated
mechanically.

Final Liability rests with the Human.
