# Evaluation set

**Version 2.6.2 · 20 October 2026**

**The validator is INCOMPLETE and its ACCEPT is not a readiness conclusion.** Human review of every readiness decision and every Demonstrated proof is retained; the tool checks a record against the repository's own written rules and nothing else. Its known gaps are in its docstring and in `validator-proof-2026-10-13-02.md`.

The versioned record of what the GRCnext™ Copilot instruments were tested
against, what came back and who judged it. Added on the maintainer's ruling
of 13 October 2026 after run 1 of `../advisory-suite-cases.md` showed that
behavior and interchange can pass and fail independently: the prompts held
their evidence rules under pressure while every payload they emitted broke
the schema contract. One file per run; nothing here is deleted, and an
expected result changes only with a reason stated in the run file and a
changelog entry.

## What is here

- `fixtures/policy-cases/` · the eleven cases of `../schema-policy-cases.md`
  as JSON, with `index.json` carrying each case's expected verdict. Run
  them through `tools/validate.py`; C01 to C06 reject, C07 to C11 accept.
- `fixtures/clean-bases/` · one valid payload per validated kind
  (assessment result, Exit Prover proof, Switch Registry snapshot). Every
  policy rule in `tools/validate.py` was proved against these: the rule is
  quiet on the clean base, fires on a constructed defect, and the exit code
  matches the finding level. The proofs are in `validator-proof-2026-10-13.md` (v2.4.0, twenty),
  `validator-proof-2026-10-13-02.md` (v2.5.0, forty-four) and
  `validator-proof-2026-10-18.md` (v2.6.0: the R6 drill repair and the
  milestone, A5 and S1 rules).
- `fixtures/run-inputs/` · the registries and dependency file handed to the
  models in run 1, as used, faults included; and, from v2.5.0, the valid
  fixtures run 2 needs: `S4-evidence.txt` (synthetic export and log line
  contents), `E4-artifact-pack.md`, `E4-pipes.json`, `E4-switch-registry.json`.
- `fixtures/v2.6.0/` · the twelve cases added with interchange contract
  2.6 (drill rows, milestones against tolerance, A5, pre-2.6 payloads),
  with `index.json` carrying each expected verdict and rule.
- `fixtures/eval-2026-10-13-02/` · the four counterexamples from the second
  external evaluation of v2.4.0, with `index.json` carrying the v2.4.0
  result and the rule that now catches each.
- `payloads/<run>/` · what the models emitted, transcribed from their
  output. These are evidence of model behavior, not examples to follow;
  most of them fail the schemas, which is the point of keeping them.
  Run 1's payloads and input registries are schema 2.5 records: not
  migrated, not re-validated and not run in Actions.
- `run-<date>-<n>.json` · the run record: method and prompt versions with
  digests, model and configuration, adjudicator, one disposition per case
  with the observation that supports it, and the validator's verdict on
  every payload and every input.

## What a run records

Method version (repository tag and commit), tool prompt versions and their
digests, the model and its configuration including how the prompt was
supplied, the date in Asia/Seoul, the fixture files used, each case's
disposition (PASS, PARTIAL, FAIL, NOT RUN) with the observation that
supports it, the validator's result on each emitted payload, any
adjudication and who adjudicated. A disposition the adjudicator is unsure
of is PARTIAL with the doubt stated, never rounded to PASS.

## Continuous integration

From v2.6.0, `.github/workflows/validate.yml` runs `tools/check_fixtures.py`
on every push and pull request: every fixture under `clean-bases/`,
`policy-cases/`, `eval-2026-10-13-02/` and `v2.6.0/` against the verdict its
index expects (and, for a REJECT whose index names a rule, against that rule), every example's `assessment-result.json`, and the JSON
sample in each of the six advisory prompts. A mismatch fails the build.

## What this set is not

It is not a benchmark and it does not score models. One run of one model
says what that model did once. A pass is weak evidence; a fail is strong
evidence; a validator REJECT is mechanical and needs no adjudication.
Anchor vignettes at scoring boundaries, the evaluation brief's F07 second
half, are not here yet; they need the maintainer's judgment on the rubric
and are carried in the maintenance register.

Final Liability rests with the Human.
