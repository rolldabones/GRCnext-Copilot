# Schema policy cases

**Version 2.3.2 · 13 October 2026 · Status: [⇥ pending review]**

Regression cases for the evidence discipline that the interchange schemas enforce. Added in v2.3.0 after an external evaluation of v2.2.5 (commit `795e91a`) showed that two records violating the evidence standard passed structural validation. The cases below are specifications with a recorded run. No runner ships with the repository; the run below used the `jsonschema` Python package and can be repeated with any JSON Schema validator that implements `if`/`then`, `contains` and `not`.

A validator enforces the repository's own rules and required evidence references. It cannot establish that a document exists or that an event happened. Observation and source review remain necessary, and a record that passes these schemas has passed a format and policy check, not an assurance review.

## Cases

| Case | Finding | Schema | Input | Expected | Observed | Disposition |
|---|---|---|---|---|---|---|
| C1 | F03, evaluation counterexample 1 | `evidence-item` | Verified interview representation with no artifact, owner, date, source or freshness | REJECT | REJECT | match |
| C2 | F03, evaluation counterexample 2 | `exit-prover-output` | PASS with empty dependency, switch, obligation and gap arrays, no evidence items, feasible_72h true | REJECT | REJECT | match |
| C3 | F01 | `evidence-item` | Verified interview representation carrying every provenance field (specific attestation, no artifact) | REJECT | REJECT | match |
| C4 | F03 | `exit-prover-output` | PASS with one Provisional dependency and one Verified evidence item | REJECT | REJECT | match |
| C5 | F03 | `exit-prover-output` | PASS with one Verified dependency and evidence items all Provisional | REJECT | REJECT | match |
| C6 | F03 | `exit-prover-output` | PASS with evidence item lacking verification_status | REJECT | REJECT | match |
| C7 | F01, legitimate low-evidence output | `exit-prover-output` | PROVISIONAL PASS with Provisional dependency and a Provisional evidence item in evidence-item form, with its conversion action (fixture enriched in v2.4.0 for `tools/validate.py` rule E1) | ACCEPT | ACCEPT | match |
| C8 | F01, legitimate low-evidence output | `evidence-item` | Provisional interview representation with evidence_conversion_action | ACCEPT | ACCEPT | match |
| C9 | F02, version 1.0 registry remains readable | `switch-registry-output` | Registry and log emitted by tool version 1.0 (status ON/OFF, no event field) | ACCEPT | ACCEPT | match |
| C10 | F03, the full Verified item | `evidence-item` | Verified exercise record with artifact, owner, date, source and freshness | ACCEPT | ACCEPT | match |
| C11 | Run 1 of the advisory suite cases, v2.3.2 widening | `exit-prover-output` | FAIL proof whose switch entry carries `id`, `owner`, `requested_state`, `last_verified` and `last_verified_state` | ACCEPT | ACCEPT | match |

Expected results follow the rules in `methodology/evidence-standard.md` and the Phase 4 and CHECKPOINT rules of `advisory-tools/03-exit-prover.md`: an interview representation is Provisional at best; a Verified item carries artifact or observation, owner, date, source and freshness; PASS requires every material item Verified and at least one Verified evidence item; low-evidence outputs labeled Provisional or PROVISIONAL PASS remain valid.

## Recorded run

- Date: 13 October 2026 (KST).
- Schemas at: GRCnext™ Copilot v2.3.0 working tree, before commit.
- Validator: Python `jsonschema` 3.2.0, `Draft7Validator`. The schemas declare draft 2020-12; every keyword they use is also a Draft 7 keyword, and a 2020-12 validator was not available on the machine that ran the cases. A run under a 2020-12 validator is open.
- Result: 10 of 10 dispositions match. C11 added 13 October 2026 with the v2.3.2 schema widening; 11 of 11 on re-run the same day, same validator.
- Adjudication: none required.
- v2.4.0: the eleven cases ship as JSON in `evaluation-set/fixtures/policy-cases/` and run through `tools/validate.py`, which applies the schemas and the policy rules together; dispositions unchanged.

## Changing an expected result

An expected result changes only with a reason stated here and a changelog entry, never silently. Cases are versioned with the repository.

**Final Liability rests with the Human.**
