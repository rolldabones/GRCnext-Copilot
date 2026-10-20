# Schema policy cases

**Version 2.6.2 · 20 October 2026**

Regression cases for the evidence discipline that the interchange schemas enforce. Added in v2.3.0 after an external evaluation of v2.2.5 (commit `795e91a`) showed that two records violating the evidence standard passed structural validation. The cases below are specifications with a recorded run. The runner is `tools/validate.py`, which applies the schemas and the policy rules together; the schemas alone can be checked with any JSON Schema validator that implements `if`/`then`, `contains` and `not`.

A validator enforces the repository's own rules and required evidence references. It cannot establish that a document exists or that an event happened. Observation and source review remain necessary, and a record that passes these schemas has passed a format and policy check, not an assurance review.

## Cases

| Case | Finding | Schema | Input | Expected | Observed | Disposition |
|---|---|---|---|---|---|---|
| C1 | F03, evaluation counterexample 1 | `evidence-item` | Verified interview representation with no artifact, owner, date, source or freshness | REJECT | REJECT | match |
| C2 | F03, evaluation counterexample 2 | `exit-prover-output` | Demonstrated (PASS before 2.6) with empty dependency, switch, obligation and gap arrays, no evidence items | REJECT | REJECT | match |
| C3 | F01 | `evidence-item` | Verified interview representation carrying every provenance field (specific attestation, no artifact) | REJECT | REJECT | match |
| C4 | F03 | `exit-prover-output` | Demonstrated with one Provisional dependency and one Verified evidence item | REJECT | REJECT | match |
| C5 | F03 | `exit-prover-output` | Demonstrated with one Verified dependency and evidence items all Provisional | REJECT | REJECT | match |
| C6 | F03 | `exit-prover-output` | Demonstrated with evidence item lacking verification_status | REJECT | REJECT | match |
| C7 | F01, legitimate low-evidence output | `exit-prover-output` | Conditionally Demonstrated with Provisional dependency and a Provisional evidence item in evidence-item form, with its conversion action (fixture enriched in v2.4.0 for `tools/validate.py` rule E1) | ACCEPT | ACCEPT | match |
| C8 | F01, legitimate low-evidence output | `evidence-item` | Provisional interview representation with evidence_conversion_action | ACCEPT | ACCEPT | match |
| C9 | F02, version 1.0 registry remains readable | `switch-registry-output` | Registry and log emitted by tool version 1.0 (status ON/OFF, no event field) | ACCEPT | ACCEPT | match |
| C10 | F03, the full Verified item | `evidence-item` | Verified exercise record with artifact, owner, date, source and freshness | ACCEPT | ACCEPT | match |
| C11 | Run 1 of the advisory suite cases, v2.3.2 widening | `exit-prover-output` | Not Demonstrated proof whose switch entry carries `id`, `owner`, `requested_state`, `last_verified` and `last_verified_state` | ACCEPT | ACCEPT | match |

Expected results follow the rules in `methodology/evidence-standard.md` and the Phase 4 and CHECKPOINT rules of `advisory-tools/03-exit-prover.md`: an interview representation is Provisional at best; a Verified item carries artifact or observation, owner, date, source and freshness; Demonstrated requires every material item Verified and at least one Verified evidence item; low-evidence outputs labeled Provisional or Conditionally Demonstrated remain valid.

The eleven fixtures were migrated to interchange contract 2.6 on 18 October 2026 (KST) in v2.6.0 (`schema_version`, `tolerance_hours` and `milestones` in place of `feasible_72h`, the suite verdict scale, neutral actor labels); every case keeps its expected verdict and its rules, and the run below the table was repeated on the migrated set with the same dispositions.

## Cases added in v2.6.0

In `evaluation-set/fixtures/v2.6.0/`, with `index.json`. Expected and observed under the v2.6.0 validator on 18 October 2026 (KST); the v2.5.2 column is the result under the previous validator, where it differs.

| Case | Rule | Input | Expected | Observed | v2.5.2 |
|---|---|---|---|---|---|
| D1 | R6 | Drill-only completed event with evidence; production status unchanged | ACCEPT | ACCEPT | REJECT (R6 false rejection) |
| D2 | R6 | The same event as production | REJECT | REJECT | REJECT |
| M1 | M1 | 52 h critical path against a 48 h tolerance, not within, Not Demonstrated | ACCEPT | ACCEPT | n.a. |
| M2 | M1 | The same claimed within | REJECT | REJECT | n.a. |
| M3 | M1, M4 | 92 h observed against a 96 h tolerance, within, Demonstrated | ACCEPT | ACCEPT | n.a. |
| M4 | M2 | Interim limit 72 h against a 12 h tolerance | REJECT | REJECT | n.a. |
| M5 | M4 | Demonstrated with interim continuity outside tolerance | REJECT | REJECT | n.a. |
| M6 | M3 | Milestones out of order | REJECT | REJECT | n.a. |
| M7 | M1, M2 | Treasury plan, tolerance not supplied, every fit null | ACCEPT | ACCEPT | n.a. |
| M8 | M2 | Treasury plan, interim limit with no tolerance | REJECT | REJECT | n.a. |
| A1 | A5 | Demonstrated with a Provisional Pass on a core gate | REJECT | REJECT | ACCEPT with A5 WARN |
| S1 | S1, S0 | The v2.5.2 clean base unchanged (no `schema_version`, `feasible_72h`, PASS) | REJECT | REJECT | ACCEPT |

M1 and M3 rebuild the evaluation brief's 52-hour and 92-hour arithmetic cases to their totals; the brief's step data is not in the repository (Unknown).

## Recorded run

- Date: 13 October 2026 (KST).
- Schemas at: GRCnext™ Copilot v2.3.0 working tree, before commit.
- Validator: Python `jsonschema` 3.2.0, `Draft7Validator`. The schemas declare draft 2020-12; every keyword they use is also a Draft 7 keyword. The 2020-12 run, open here until v2.6.0, was made by the whole-account review of 15 October 2026 under `jsonschema` 4.26 `Draft202012Validator` with the same dispositions; from v2.6.0 the Actions workflow runs every case under the current `jsonschema` release on every push.
- Result: 10 of 10 dispositions match. C11 added 13 October 2026 with the v2.3.2 schema widening; 11 of 11 on re-run the same day, same validator.
- Adjudication: none required.
- v2.4.0: the eleven cases ship as JSON in `evaluation-set/fixtures/policy-cases/` and run through `tools/validate.py`, which applies the schemas and the policy rules together; dispositions unchanged.
- v2.6.0, 18 October 2026 (KST): the migrated eleven and the twelve new cases run through `tools/validate.py` v2.6.0 under `jsonschema` 3.2.0: 23 of 23 dispositions match.

## Changing an expected result

An expected result changes only with a reason stated here and a changelog entry, never silently. Cases are versioned with the repository.

Final Liability rests with the Human.
