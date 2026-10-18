# Interchange schemas

Nine JSON Schemas (draft 2020-12) define the payloads GRCnext™ Copilot and its advisory suite exchange. `tools/validate.py` applies them together with the policy rules JSON Schema cannot express; `tools/check_fixtures.py` runs the validator over every fixture, example and prompt sample, and `.github/workflows/validate.yml` runs that on every push.

| Schema | Payload | Emitted by |
|---|---|---|
| `assessment-result.schema.json` | `assessment_result` | GRCnext™ Copilot |
| `service-dossier.schema.json` | `service_dossier` | GRCnext™ Copilot |
| `evidence-item.schema.json` | one evidence item, standalone or inside a proof | Copilot and suite |
| `pipes-mapper-output.schema.json` | `pipes_mapper` | Pipes Mapper |
| `switch-registry-output.schema.json` | `switch_registry` | Switch Registry |
| `exit-prover-output.schema.json` | `exit_prover` | Exit Prover |
| `treasury-reroute-plan.schema.json` | `treasury_reroute_planner` | Treasury Reroute Planner |
| `data-switchboard-plan.schema.json` | `data_switchboard_planner` | Data Switchboard Planner |
| `clean-market-exit.schema.json` | `clean_market_exit_kit` | Clean Market Exit Kit |

## Contract version

Every top-level payload carries `"schema_version": "2.6"` as its first field; the eight top-level schemas require it and the evidence item allows it. The version names the interchange contract, not the repository: it changes only when a schema changes, and a payload names the contract it was written to. The validator rejects a top-level payload without the field (rule S1) and tells the reader to migrate it.

## Migration from 2.5 (no field) to 2.6

Version 2.6 shipped in GRCnext™ Copilot v2.6.0 on 18 October 2026 (KST). A 2.5 payload becomes a 2.6 payload by these rules, applied in order:

1. Add `"schema_version": "2.6"` as the first field (not required on an evidence item).
2. Exit Prover and Clean Market Exit Kit verdicts: PASS and READY become `Demonstrated`; PROVISIONAL PASS and PROVISIONAL become `Conditionally Demonstrated`; FAIL and NOT READY become `Not Demonstrated`.
3. Evidence state `Not demonstrated` becomes `Not evidenced` wherever an evidence status appears.
4. Exit Prover `feasible_72h`, and `72h_feasible` in the treasury plan, the data plan and the Kit, are removed. Add `tolerance_hours` (the service's approved impact tolerance in hours, or null) and `milestones`: exactly three objects, `containment`, `interim_continuity` and `final_exit`, each with `elapsed_hours`, `basis`, `limit_hours`, `limit_source` and `within_limit`. The boolean cannot be converted: it was a sum against a constant, so rebuild the milestones from the durations, and where they are not to hand set `elapsed_hours` null, `basis` unknown and `within_limit` null.
5. Assessment result: add `binding_constraint` (`kind` clock_phase, gate or none_identified; `name`; `scenario`; `basis`).

A record emitted under 2.5 and kept as evidence of what was emitted, such as the run 1 payloads under `tests/evaluation-set/payloads/`, is not migrated: it is a record, and changing it would falsify it.

## Rules the validator adds (v2.6.0)

M1 milestone arithmetic (`within_limit` is `elapsed_hours <= limit_hours`, null when either is null; an unknown basis has a null duration). M2 the interim continuity limit is the tolerance. M3 the three milestones, once each, in order. M4 a Demonstrated proof or Kit verdict with interim continuity outside the tolerance rejects; with the fit not shown, or resting on an assumed or unknown duration, it warns. The full rule list with the sentence each rule rests on is in `tools/validate.py`.

Final Liability rests with the Human.
