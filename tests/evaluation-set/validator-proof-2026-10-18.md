# Validator proof 3, 18 October 2026

`tools/validate.py` as shipped in GRCnext™ Copilot v2.6.0, proved on the
maintainer's machine (Python 3.10.12, jsonschema 3.2.0, Draft 7) in session
T6 of the whole-account review of 15 October 2026. Method as in proofs 1
and 2: each rule is quiet on its clean base, fires on a constructed defect,
and the exit code matches the finding level. From v2.6.0 the same fixtures
run in GitHub Actions on every push (`.github/workflows/validate.yml`).

## Status

**INCOMPLETE.** The validator is a control on the interchange layer. ACCEPT
means the record follows the repository's written rules as far as they are
stated mechanically. It is not a readiness conclusion. Human review of every
readiness decision and every Demonstrated proof is retained.

## The R6 defect and its repair (review report 08, item A6)

The v2.5.0 derivation of "the newest evidenced execution event" counted
drill rows, so a registry whose production status was correctly unchanged
after a drill was rejected, against `advisory-tools/02-switch-registry.md`
section 4 (drill events never change the production status). The 44 proofs
of proof 2 never probed a drill row.

| Fixture | Defect probed | v2.5.2 validator | v2.6.0 validator | Exit |
|---|---|---|---|---|
| `fixtures/v2.6.0/D1-...` | drill-only completed event with evidence, status unchanged | REJECT (R6, the defect firing) | ACCEPT (quiet) | 0 |
| `fixtures/v2.6.0/D2-...` | the same event as production | REJECT (R6) | REJECT (R6, the guard still fires) | 1 |
| run 1 payload S7b | drill row log[3] | REJECT, 3 findings (two S0, one R6) | not re-run: pre-2.6 record | n.a. |

The run record `run-2026-10-13-01.json` said 2 findings for S7b; it now
carries the count of 3 with a dated correction naming the false R6.

## New rule proofs

| Rule | Level | Base | Defect constructed | Fired | Exit |
|---|---|---|---|---|---|
| S1 | REJECT | v2.5.2 exit-prover clean base | no `schema_version` (fixture S1) | yes, with S0 | 1 |
| A5 | REJECT (was WARN) | assessment-result | Demonstrated with gate 5 Provisional Pass (fixture A1) | yes | 1 |
| M1 | REJECT | exit-prover 52 h against 48 h | `within_limit` true (fixture M2) | yes | 1 |
| M1 | REJECT | exit-prover | containment basis unknown with elapsed 1 h (constructed in session) | yes | 1 |
| M2 | REJECT | exit-prover | interim limit 72 h against tolerance 12 h (fixture M4) | yes | 1 |
| M2 | REJECT | treasury plan, tolerance null | interim limit 72 h (fixture M8) | yes | 1 |
| M3 | REJECT | exit-prover | milestones out of order (fixture M6) | yes | 1 |
| M4 | REJECT | exit-prover | Demonstrated, interim 14 h against 12 h (fixture M5) | yes | 1 |
| M4 | WARN | exit-prover | Demonstrated, interim basis assumed (constructed in session) | yes | 0 |

Quiet on every clean base (assessment result, exit prover, switch
registry: ACCEPT, 0 findings, exit 0) and on the accepting cases D1, M1,
M3 and M7.

## Regression over the migrated fixtures

The eighteen fixtures of `clean-bases/`, `policy-cases/` and
`eval-2026-10-13-02/` were migrated to schema 2.6 and run under v2.5.2
(before) and v2.6.0 (after). Every verdict is unchanged and every finding
is the same rule at the same path; the only differences are message
wording (PASS read as Demonstrated in E4, "production" added in R6).
Rule E7 (PASS with `feasible_72h` false) is retired with the field; M4
replaces it.

## Not re-validated

The run 1 payloads and the run 1 input registries under
`fixtures/run-inputs/` are records of what was emitted and supplied on 13
October 2026 under schema 2.5. They carry no `schema_version` and are not
migrated, re-validated or run in Actions. `E4-pipes.json` and
`E4-switch-registry.json`, the fixtures run 2 needs, were migrated and
ACCEPT.

Final Liability rests with the Human.
