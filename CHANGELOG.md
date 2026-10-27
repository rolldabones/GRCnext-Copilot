# Changelog

All notable changes to GRCnext™ Copilot are recorded here. Dates use the
Asia/Seoul time zone (UTC+9).

## v2.7.0 (2026-10-27)

Minor release. The main prompt has its first logged runs and an acceptance under `ACCEPTANCE.md` in the `rolldabones` repository: accepted with residuals on claude-opus-5-5 (run 20261027-R2: all twelve critical cases and 13 of the 14 others, SC2 a residual); not accepted on claude-sonnet-5-5 (critical case A6 failed). Prepared with Claude, approved by Michael Paik, who ruled the suite, the configuration and the critical cases and concurred per case with both runs on 27 October 2026 (KST).

- **Prompt rules (all three editions, kept consistent).** Section 2 makes the ESCALATE label a fixed element that holds when a user asks to drop the escalation language; section 18 adds a request for a definitive jurisdiction-specific legal conclusion, or a prediction that a dispute will be won, to the escalation triggers (run 20261027-R1, case A3). Gate 6 in section 7 now reads Fail for a discussion-only exercise (T0 or T1) of the governing scenario and Provisional Pass at most for partial or simulated coverage, as `templates/intake-pack.md` gate 6 already did; `methodology/scoring-method.md` carries the same text (run 20261027-R1, case SC4). The prompt proper's SHA-256 moves from `288c5800…71186f` to `bea208c3…7b11f7b`.
- **Suite.** `tests/prompt-evaluation-cases.md` states the main prompt's suite (26 cases: B1 to B10; A1 to A9 in `adversarial-inputs.md`; SC1 to SC7 in `scoring-cases.md`, renumbered from 1 to 7), the configuration (the v2 prompt proper as the system prompt alone), the **Critical cases** line (B1, B5, B6, A1 to A9), the status and the run record. Every case carries a literal run input; B8 to B10 include `examples/payment-service/input-pack.md` and A4 a synthetic contract in `tests/prompt-fixtures/`; each SC case carries a run pass condition. After run 20261027-R1, case A8's expected behavior was reworded (the closing line ends substantive deliverables only), SC3's condition admits Refuted, SC5's no longer pins an organization Constraint Level the method does not define, and B4's run input names the actions; each amendment is dated in place.
- **Harness.** New `tests/run_prompt_cases.py` and `tests/score_prompt_cases.py`, ported from master-prompt-for-in-house-legal-and-compliance: the prompt hash and run-input hash in every transcript, cross-model scoring with self-scoring refused, the run read against ACCEPTANCE.md (a) to (c), and a review sheet for (d) and (e). Requests are streamed with `max_tokens` 32,000. The user message in each transcript sits inside a fence, so the invented address in case A1 stays out of the external link check. `.gitignore` added.
- **Evidence.** `tests/prompt-runs/` holds both runs: 104 transcripts, four manifests and eight score files. Run 20261027-R1 tested the v2.6.3 text and is kept as its record (not accepted on either model).
- **Front door.** README status line and repository tree; this file; `CITATION.cff`.
- **Erratum.** The v2.6.3 entry below says the tests file "names its critical cases"; it did not, and the line first appears in this release. The entry stays as cut.

## v2.6.3 (2026-10-26)

Patch release. Acceptance restated as a tolerance: the tests file is now read under the account rule, `ACCEPTANCE.md` in the `rolldabones` repository, names its critical cases and records the instrument's status under that rule (not accepted: no logged run of the main prompt); the README carries the same status below its masthead. No rule in the instrument changed and no run was made; the edits are to the test record and the front door. Train A of the whole-account review of 24 October 2026 (KST); prepared with Claude, approved by Michael Paik.

## v2.6.2 (2026-10-20)

Patch. Independent review of 20 October 2026; changes made with Claude, approved by Michael Paik. Corrections to examples, methodology prose, tests, tool notes and two advisory prompts' wording. No schema rule, field or schema_version changed; no scoring rule or gate changed.

- **Examples.** Manufacturing gate count and dossier tolerance result conformed to the JSON (GNC-06, GNC-07); manufacturing Switches L3 basis stated under cap 8 (GNC-31). Payment CA-003 risk restated against the 2026-08-20 due date (GNC-15); E-002 holds the exit right Verified and a new E-006 holds the execution capability Provisional (GNC-19); gate 7 and the tolerance result stated once for the governing scenario (GNC-08); the binding-constraint basis is the weekday-peak rehearsal finding (GNC-09). Agentic phase times sum to 90 minutes and the detection share is about 40 percent (GNC-16, GNC-17). Evidence type `none`, which the evidence-item enum does not carry, replaced by `interview representation` in the four Not evidenced rows (GNC-18).
- **Methodology.** Scoring walkthrough: Services and tolerances, Pipes and Switches L4 to L3 under cap 8, one corrective action being overdue (GNC-11); gates 6 and 7 one state each (GNC-08). The remaining "gives way" and "tooth that will not catch" claims withdrawn in v2.6.0 removed from method-and-logic and the long-form edition (GNC-12). Glossary: the United Kingdom term (important business service) and the DORA term (critical or important function, Article 3, point (22)) named, the hybrid term stated as this method's own (GNC-20); SS1/21 link moved to the March 2022 version and the comparison caveat closed (GNC-32). Evidence standard: an unsupported Not Applicable is recorded as Unknown / Insufficient data, not a seventh state; long-form "five different questions" (GNC-27).
- **Prompts.** Switch Registry 1.5: MODE: CONFIRM states that an open drill request reads Unknown and that a drill event does not set production status (GNC-05). Clean Market Exit Kit 1.2: the degraded-mode cap is advisory, matched in `schemas/clean-market-exit.schema.json` description (GNC-03). Both not accepted pending a logged run. Compact edition and configuration notes no longer say the compact edition holds on its own (GNC-13). Suite 1.5.
- **Statements of what is checked.** README: the suite's Demonstrated does not itself require a tolerance result of Met; validator M4 is the control (GNC-01). START-HERE: ACCEPT narrowed to the checks the validator makes (GNC-04). Exit Prover schema description narrowed to what its conditional checks (GNC-02). README and suite README: run 2 not yet run, four tools with no behavioral run (GNC-14). Suite README names Switch Registry and Exit Prover as the two tools sharing the evidence standard (GNC-29).
- **Tests and tools.** Scoring Case 5 Service B at Constraint Level 2 and Case 6 restated (GNC-23); Case 4 exercise gate pinned to Fail as the intake pack reads (GNC-10); Case E2 "Not evidenced" (GNC-21); personal names in case text and the S4 evidence fixture replaced by roles (GNC-25); clean-base and fixtures A1, X3, X4 clock start at onset (GNC-24); adversarial case A7 sentence repaired (GNC-26). `tools/check_fixtures.py` also compares the indexed rule of each REJECT fixture and removes its temporary directory (GNC-30).
- **Style and pins.** README serial comma removed (GNC-26); suite README and evaluation-set README pins moved with the repository version (GNC-22).
- **Errata to earlier entries (left as cut).** v2.6.0, "One verdict scale": the suite's Demonstrated was said to keep its definition "unchanged in substance"; it does not itself require a tolerance result of Met, as the Copilot's does (GNC-01).
- **Reading earlier entries (GNC-28).** Earlier entries refer to the maintainer's account-maintenance records: a session (Session C, T3, T4, T6) is one scheduled review or maintenance pass over the account; a reviewer report, a determination (D1, D5) and a ruling (7, 9) are findings and decisions recorded in those passes; register row 17 is this repository's row in the maintainer's improvement register; the C1 version check is the account check that the README, changelog and tag versions agree. The License metadata sweep paragraph at the foot of the v2.2.2 entry has no heading of its own. Shipped entries stay as cut.
- README masthead, How to Cite, `CITATION.cff`, `tests/schema-policy-cases.md` and `tests/evaluation-set/README.md` mastheads and the suite README pin to v2.6.2.

## v2.6.1 (2026-10-20)

- LICENSE: two defects against the Creative Commons legal code corrected (the space in 'ShareAlike. In'; the CC0 sentence of the closing notice). Operative terms unchanged.
- **README, Short edition:** "Until v2.6.0 it was" now reads "Until the release of 18 October 2026 it was". Wording only; the sentence is history, and the C1 version check read its version as a masthead disagreement once the masthead moved (weekly sweep of 20 October 2026, on Michael Paik's ruling the same day).
- README masthead, How to Cite, `tests/schema-policy-cases.md` masthead and `CITATION.cff` to v2.6.1. Schemas, fixtures and the advisory suite are unchanged.

## v2.6.0 (2026-10-18)

Minor. Session T6 of the whole-account review of 15 October 2026 (doc section 6; reviewer report 08), under determination D1: one clock, one tolerance, one verdict scale, interchange contract 2.6, a first-run route and continuous integration. The method's rules change in the places listed; every changed instrument re-versions with a dated amendment note. Schema payloads written under 2.5 must be migrated (`schemas/README.md`).

**Instruments amended (dated amendment notes in each file).**

- **One clock (F04).** The tolerance clock starts at the **onset of disruption**, not at detection; the interval from onset to detection is the Detect phase. Defined once in `methodology/glossary.md` (Clock start) and stated the same way in capability-model, exercise-tiers (which read "usually detection"), method-and-logic, scoring-method, the v2, long-form and compact prompts and the service-dossier and exercise-plan templates. Where onset cannot be established the pre-detection interval is Unknown and the result is Cannot Determine without an evidenced bound. The PRA SS1/21 alignment is stated as what the source supports (para 3.1 definition; paras 3.7 and 4.11 count from the disruption; no detection trigger named; read 18 October 2026), not as a requirement. Scoring Case 7 (onset 02:00, detection 04:00, stable 07:00, four-hour tolerance: Not Met) pins it.
- **One tolerance (F06).** No suite tool sums against 72 hours. Exit Prover 1.3, Treasury Reroute Planner 1.1, Data Switchboard Planner 1.1 and Clean Market Exit Kit 1.1 take `tolerance_hours` from the service dossier and report three milestones (containment, interim continuity, final exit), each with elapsed time from onset along the critical path, a basis (observed, estimated, assumed, unknown), its limit and whether it is within it. Interim continuity is measured against the tolerance; final exit against the supplied authority (a 30- or 90-day notice period is now a limit, not a false `feasible_72h`). Pipes Mapper 1.1 and Switch Registry 1.4 drop the 72-hour model from their identity sentences.
- **Binding constraint (F05).** The Constraint Level `min(Pipes, Switches, Exits)` stays as the ordinal maturity diagnostic; beside it every assessment reports the clock phase or gate that actually limits execution. The minimum no longer claims to name "the tooth that will not catch".
- **Decision caps.** Section 8F of `prompt/GRCnext-Copilot-v2.md`, the compact edition's DECISION CAPS, long-form IX-F and scoring-method's Decision caps state the eight caps once, including the three the tests enforced and the authoritative prompt did not carry (Provisional Pass cap, unsupported Not Applicable as Unknown, organization view as the minimum). Rule change: **every core gate is material**, so a Provisional Pass on any gate caps the decision; until v2.6.0 "material gate" was undefined and the validator only warned.
- **One verdict scale.** Exit Prover PASS / PROVISIONAL PASS / FAIL and the Kit's READY / PROVISIONAL / NOT READY become Demonstrated / Conditionally Demonstrated / Not Demonstrated, the Copilot's readiness scale; definitions unchanged in substance. Gate statuses (Pass, Provisional Pass, Fail, Unknown, Not Applicable) are classifications and stay. The evidence state "Not demonstrated" is renamed **"Not evidenced"**, so it no longer differs from the decision by case alone.
- **Primitives in the suite.** `advisory-tools/README.md` (suite 1.4) gains a table naming how each tool narrows each primitive; one interchange map, with the prompts conformed (report 08 A11); the Custom GPT route (A8) and the unpublished MindStudio brief pointer (A12) dropped; the switch catalog gains an optional `registry_switch_id` (B8).
- **Modes.** The thirteen v2 modes that were names only get one line each (inputs, output), in v2 section 13 and long-form Part XV.
- **Scoring walkthrough.** `methodology/scoring-method.md`: Exits L3 to L2 for an exit rehearsed only to T2 (the tier rule), Constraint Level 3 to 2; clock at onset. Scoring Case 6 follows with its reason stated.

**Interchange contract 2.6 and the validator.**

- All nine schemas: `schema_version` "2.6" (required on the eight top-level payloads); `tolerance_hours` and `milestones` replace `feasible_72h` and `72h_feasible`; the verdict scale; `binding_constraint` required in the assessment result. Migration rules in the new `schemas/README.md`.
- `tools/validate.py`: R6 excludes drill rows (report 08 A6; the v2.5.0 derivation rejected a registry whose production status was correctly unchanged after a drill, proved on S7b); A5 rejects; S1 names a pre-2.6 payload; M1 to M4 check the milestones; E7 retires with its field; "GRCnext(TM)" now GRCnext™. Proof: `tests/evaluation-set/validator-proof-2026-10-18.md`, with the R6 defect shown firing under v2.5.2 and quiet under v2.6.0 (fixture D1) and the guard still firing on production rows (D2).
- `tools/check_fixtures.py` (new) and `.github/workflows/validate.yml` (new): every fixture, every example's `assessment-result.json`, the run 2 inputs and the six prompt samples against their expected verdicts, on every push and pull request, under the current `jsonschema` 4.x (Draft 2020-12). 41 items, 0 mismatches under jsonschema 3.2.0 and 4.26.0 on 18 October 2026.
- Fixtures: the eighteen in `clean-bases/`, `policy-cases/` and `eval-2026-10-13-02/` migrated with every verdict and rule unchanged; twelve new in `fixtures/v2.6.0/` (D1, D2, M1 to M8, A1, S1), M1 and M3 rebuilding the evaluation brief's 52-hour and 92-hour cases to their totals (the brief's step data is not in the repository). `run-2026-10-13-01.json` S7b corrected from 2 to 3 findings with a dated note. Run 1 payloads and input registries are schema 2.5 records and are not migrated.
- `tests/schema-policy-cases.md` 2.6.0: the "no runner ships" sentence struck; the 2020-12 run closed by the review's run under jsonschema 4.26; the new cases tabled. `tests/advisory-suite-cases.md` verdict terms with a dated note; run 1 left as run.

**First run and examples (F07, F08).**

- `START-HERE.md` (new): one service from an empty assistant to a validated result and a dossier.
- `templates/intake-pack.md` (new), keyed to the eight gates. The three template CSVs are header-only; their Service B rows moved to `examples/payment-service/`. `templates/evidence-pack-index.md` removed (its five-state list lacked Refuted and its columns differed from the ledger; the ledger is the evidence item's one shape).
- Each example gains `input-pack.md` and `assessment-result.json`.
- **Payment example rescored.** CA-003 was "Overdue" with a 31 July target on a 15 June assessment and a map verified 20 May: now due 2026-08-20, Open. Switches 4 to 3 (authorization simulated, loops open); Exits 3 to 2 (tier rule); Services and tolerances 4 to 3 and gate 2 Provisional Pass, because the approved tolerance named detection as the clock start (new CA-005 re-approves it at onset). Profile 3, 3, 3, 2, 3, 3; Constraint Level 2; binding constraint Authorize (3 hours of 9) for the reroute and gate 5 for the exit; Conditionally Demonstrated, Moderate. Counts aligned: two switches (failback is SW-001's rollback), five open actions.

**Retirement residue and naming.**

- `prompt/compact-custom-gpt-version.md` renamed `prompt/GRCnext-Copilot-compact.md`, the short edition for any assistant (10,055 characters, measured 18 October 2026; it no longer fits the closed 8,000-character field). `prompt/v1-production-deployment.md` status recast as the record of what ran until 1 October 2026; the v1 block unchanged. `prompt/model-configuration-notes.md` Custom GPT section marked history.
- README: "What changed in v2" cut to a pointer (changelog material); a Start here section; the repository tree redrawn (START-HERE, CITATION.cff, tools/ inside the tree); "four results plus the tolerance result" settled; the grc neighbor line corrected (grc is the OCEG-spine method; the primitives are defined here, report 08 A7).
- Draft tags dropped from the six prompts, the suite README and two test files; serial commas removed (report 08 C1); prose arrows "ON->OFF" as the enum writes them; personal names in fixtures and the Switch Registry sample replaced by roles.
- Masthead, How to Cite and `CITATION.cff` to 2.6.0 in lockstep; `tests/schema-policy-cases.md` version line with them (pin `grcnext-tests-version`).

**Not changed, with reasons.** Report 08 C4 schema file names (`*-output` against `*-plan`) and C6 (runs out of `tests/` into `evaluation-set/`) left: renames break inbound paths for no rule gain. CHANGELOG history (the headingless "License metadata sweep" entry, two "licence" spellings, untagged v2.0.0 to v2.1.0) left as shipped history (ruling 7). The two serial commas inside the archived v1 configuration left as record.

## v2.5.2 (2026-10-18)

Patch. Session T4 of the whole-account review of 15 October 2026 (doc section 4, items 4 and 6; reviewer report 08, items 8 and 9), under determination D5: the GRCnext™ Copilot custom GPT was retired on 1 October 2026 and converted to a private plug-in on the OpenAI platform; the instructions published here are the text of record. Notice lines only; the GRCnext™ v2.6.0 train is session T6. No schema, scoring rule, gate, fixture, prompt body or advisory-tool prompt text changed.

- **`README.md` Deploy it.** ~~"**Deployed production instance (as of 15 July 2026).** The author's deployed custom GPT is at https://chatgpt.com/g/g-69831f7f8df48191a3808c37306ec918-grcnexttm-copilot and currently runs the **v1 single-prompt configuration** ... has not yet been deployed to that instance. When production changes, this paragraph and that file change and the repository version bumps."~~ **STRUCK.** Now "Former production instance": the v1 configuration as last verified on 15 July 2026, before the conversion; v2 never deployed to it. The live link is removed.
- **`README.md` retirement notice.** ~~"> **Retirement notice, 28 September 2026 (KST), corrected 5 October 2026 (KST).** OpenAI is retiring custom GPTs. ... The link above was verified resolving on 5 October 2026 and stops working on 11 December 2026, and the ChatGPT Custom GPT route above closes with it."~~ and its second paragraph ~~"Everything needed to build your own stays published here: ... test before you rely on the output."~~ **STRUCK.** Replaced by the account's one dated line, which points to RETIREMENT.md in the profile repository for the long form.
- **`README.md` ChatGPT Custom GPT route** marked closed and pointed at the Claude and standalone routes.
- **`prompt/v1-production-deployment.md`.** ~~"(current)"~~ and ~~"**Status: CURRENT PRODUCTION as of 15 July 2026.** This file is the system of record for the configuration the deployed custom GPT actually runs at <link>. ... On redeployment to v2, this file is re-marked superseded and the repository re-versions."~~ **STRUCK.** Now "(retired)", with a status line that states the configuration as last verified on 15 July 2026, before the conversion. The mirrored configuration below the line is unchanged.
- **`prompt/model-configuration-notes.md`.** One dated line at the head of the ChatGPT Custom GPT section marks the route closed; the steps stay as record.
- **`prompt/GRCnext-Copilot-v2.md` header note** (the blockquote above the prompt, not the prompt body): ~~"or attached to a Custom GPT as a Knowledge file. For the ChatGPT instructions field (8,000-character limit), use `prompt/compact-custom-gpt-version.md` and attach this file as Knowledge."~~ **STRUCK**; the note now names any current assistant and records the custom GPT route as closed. The compact edition keeps its file name until T6, which renames it in the v2.6.0 naming pass.
- **`advisory-tools/README.md`.** ~~"a Custom GPT's instructions field,"~~ **STRUCK** from the deployment sentence: four of the six prompts exceed the 8,000-character field (02: 13,554; 03: 11,133; 05: 8,100; 06: 8,957 characters, whole file, measured 18 October 2026), and the route is retiring. The suite header's repository version reads v2.5.2 (it read v2.5.0).
- `tests/schema-policy-cases.md` version line to 2.5.2, the repository version (pin `grcnext-tests-version`); its cases and recorded run are unchanged.
- README masthead, How to Cite and `CITATION.cff` to 2.5.2 in lockstep.

## v2.5.1 (2026-10-17)

Patch. Session T3 of the whole-account review of 15 October 2026 (doc sections 1 and 8; reviewer report 08, items C1 and B/C glossary). No schema, scoring rule, gate, fixture or advisory-tool text changed.

- **`methodology/glossary.md` Doctrine terms:** the three entries restated the doctrines into different rules: Slow AI as "governance owns the clock", Informed Intent as a decision "traceable to a human who understood it" (no purpose, authority, boundaries or exit), Final Liability without decision rights, oversight or the power to intervene. Each now quotes the canonical statement of rolldabones DOCTRINE.md v1.2.0 verbatim with a section link, under the doctrine citation line. "GRC owns the clock" stays GRCnext™'s operating principle and is now said to be that, not Slow AI.
- **`README.md`:** the first link to DOCTRINE.md in the repository, in License and attribution.
- **`tests/schema-policy-cases.md`:** version line 2.3.2 corrected to 2.5.1, the repository version; the file's cases and recorded run are unchanged.
- **Serial commas** removed from the Not Demonstrated definition in `prompt/GRCnext-Copilot-v2.md` (the prompt that forbids them), `prompt/GRCnext-Copilot-long-form.md` and `methodology/scoring-method.md`, and from three domain lines of the v2 prompt. Wording otherwise unchanged. The same fault in the six advisory tools and `templates/service-dossier.md` waits for v2.6.0 (session T6), which re-versions each tool; the deployed configurations are Locked (ruling 9 of 15 October 2026) and session T4's.
- Masthead, How to Cite and `CITATION.cff` to 2.5.1 in lockstep.

## v2.5.0 (2026-10-13)

Second external evaluation of v2.4.0 (run by the maintainer with another model, same day) and the session's own audit, answered. Minor release: Switch Registry's evidence standard changes (1.3); the validator gains six reject rules and two warnings and no longer crashes on malformed input; it is marked INCOMPLETE and human review of readiness conclusions is stated as retained everywhere the validator is described.

- **Ruling of 13 October 2026 (maintainer):** keep the validator marked incomplete; retain human review of readiness conclusions; fix the false acceptances and the crash before relying on automated validation; broader calibration, documentation and onboarding refinements wait.
- **`advisory-tools/02-switch-registry.md`, version 1.3.** MODE: CONFIRM applies the evidence standard Exit Prover applies: an evidence item is Verified only when its content was supplied and reviewed in session or an observation is recorded; a description of an artifact held elsewhere, however specific, is a representation and leaves status Unknown. `evidence_ref` records what was reviewed, not what was reported. §7 names `methodology/evidence-standard.md` as the sole definition. Closes the S4 loophole the evaluation found: the v2.4.0 positive case let a described export and log move status to ON.
- **`tools/validate.py`.** Crash closed: a malformed payload (null or non-object entries in `gates`, `evidence_items`, `switches`, `obligations`, `gaps`, `log`; non-object `tolerance_result` or `capability_profile`) now reports "S0 malformed, policy rules not applied" and exits 1. False acceptances closed: R6 (status against the newest evidenced execution event in the log; the evaluation's first case), E4 widened (any open request under PASS, with or without recorded history; the evaluation's second case), A9 (Conditionally Demonstrated with a failed gate; the evaluation's third case), A10 (Conditionally Demonstrated with tolerance Not Met), R5 (status against a recorded `last_verified_state`), E5 (PASS with an unowned or undated obligation), E6 (PASS with a missing switch). Warnings added: A11, E7. Docstring carries STATUS: INCOMPLETE and KNOWN GAPS. Forty-four proofs, forty-four passed: `tests/evaluation-set/validator-proof-2026-10-13-02.md`.
- **`tests/advisory-suite-cases.md`.** S4 input now carries synthetic export and log contents; expected behavior and fail condition require review of supplied content and name a described artifact as a fail; run 1's S4 re-adjudicated FAIL against the new text, PARTIAL against the old, both recorded. Run 2 requirements stated: current prompts, true system prompt, valid fixtures, behavioral dispositions recorded apart from validator acceptance, E4 completed.
- **`tests/evaluation-set/`.** `fixtures/eval-2026-10-13-02/` (the four counterexamples with the v2.4.0 result and the catching rule); `fixtures/run-inputs/S4-evidence.txt`, `E4-artifact-pack.md`, `E4-pipes.json`, `E4-switch-registry.json` (valid fixtures for run 2; the first E4 Pipes Mapper draft failed its own schema and was corrected by the validator before it shipped); run record annotated; README marks the validator incomplete.
- **Open, by the maintainer's ruling.** Run 2 under the intended deployment configuration; scoring-boundary anchor vignettes and assessor calibration; the remaining brief findings F04, F05, F06, F08; a schema version field; a CI workflow.
- **`advisory-tools/README.md`** suite 1.3, pin, evidence standard and incompleteness stated. **`README.md`** suite paragraph, version line and How to Cite; **`CITATION.cff`** in lockstep.

## v2.4.0 (2026-10-13)

Two new instruments on the maintainer's ruling of 13 October 2026, made after run 1 of the advisory suite cases: a validator that applies the schemas and the policy rules the schemas cannot express, and a versioned evaluation set that records what was run, against what, with what result. Minor release: new instruments, no methodology change. Closes the evaluation brief's F03 remedy and the mechanical half of F07.

- **`tools/validate.py`, new.** Python 3.8+, `jsonschema` 3.2 or 4.x, files only, no network. Detects the payload kind (the `tool` field, or the field set for an assessment result, evidence item or service dossier), validates against the schema, then applies policy rules, each quoting the governing sentence of the methodology beside it: evidence items in evidence-item form (E1); no PASS on a representation (E2) or on an open switch request (E4); execution events need `evidence_ref` (R1); an open request means status Unknown (R2); eight gates each once (A1); constraint level is the minimum (A2); Fail, Unknown or unsupported Not Applicable blocks Demonstrated (A3, A4); Demonstrated needs tolerance Met (A6); Met or Not Met needs clock events (A8). Rules the text does not pin mechanically are WARN, never REJECT: unowned gaps under PASS (E3), declared states (R3), version 1.0 rows (R4), Provisional Pass under Demonstrated (A5), low confidence under Demonstrated (A7). Exit 0 clean, 1 on any REJECT, 2 on an unreadable or unrecognized payload. Twenty proofs, twenty passed, recorded in the evaluation set.
- **`tests/evaluation-set/`, new.** `README.md` (what a run records); `run-2026-10-13-01.json` (run 1: twelve dispositions, the validator's verdict on all eight emitted payloads and the four inputs); `payloads/run-2026-10-13-01/` (the eight payloads as emitted); `fixtures/run-inputs/` (the inputs as used, one of them faulty and recorded as such); `fixtures/policy-cases/` (the eleven schema policy cases as JSON with an index of expected verdicts); `fixtures/clean-bases/` (one valid payload per validated kind); `validator-proof-2026-10-13.md`.
- **Under the v2.4.0 schemas** 7 of 8 run 1 payloads still reject; S5 accepts, its only defects having been nulls on two optional fields.
- **`schemas/switch-registry-output.schema.json`.** `description` and `evidence_ref` accept null, as `owner` and `clause_ref` already did; every model run wrote null for an absent optional value. Nothing else changes.
- **`advisory-tools/02-switch-registry.md`.** Sample log gains the `verified` row that evidences SW-001's OFF, so the sample passes the validator without a declared-state warning. Prompt text otherwise unchanged; version stays 1.2.
- **`tests/schema-policy-cases.md`.** C7's fixture enriched to a full Provisional evidence item in evidence-item form, which rule E1 requires; disposition unchanged.
- **`tests/advisory-suite-cases.md`** points at the evaluation set. **`README.md`** tree, suite paragraph and **`CONTRIBUTING.md`** name the validator and the set; **`advisory-tools/README.md`** places the validator between emission and consumption. **`CITATION.cff`**, version line and How to Cite in lockstep.
- **Not in this release.** Anchor vignettes at scoring boundaries (F07's second half); a CI workflow to run the validator; a second-model run. All carried in the maintenance register.

## v2.3.2 (2026-10-13)

First recorded run of the advisory suite cases, and the corrections it forced. Twelve cases run against Claude (Fable 5.1) on 13 October 2026: eleven behavioral passes, one partial (S4), one not run on a fixture fault (E4). The behavioral rules of v2.3.0 held under pressure. Every JSON payload the tools emitted failed the v2.3.1 schemas. Patch: prompt wording, optional schema fields, tests.

- **`tests/advisory-suite-cases.md`.** Run 1 recorded with model, harness deviation, adjudicator, dispositions, the interchange finding and the adjudicator's own fixture faults. S4's fail condition now names appending supersession wording into an earlier log row as an edit. E4 gains its fixture requirement (artifact text present, suite JSON supplied).
- **`advisory-tools/03-exit-prover.md`, version 1.2.** §5: `feasible_72h` is boolean only, missing durations go to `assumptions`; interim phase results are prose and the Proof JSON is emitted once at Validation with an enum verdict. §6: evidence items take the form of `evidence-item.schema.json`, field list stated, `verification_status` never `status`; the sample now shows one; switch entries may carry `id`, `owner`, `requested_state`, `last_verified` and `last_verified_state` from the registry, and an open request is a gap. §7: no undefined field, no value outside an enum, no null for a required string or boolean. Corrects a v2.3.0 defect: the schema required `verification_status` on evidence items and the prompt never named the field, so all four Exit Prover runs wrote `status`.
- **`advisory-tools/02-switch-registry.md`, version 1.2.** §3: a timestamp the user has not supplied is asked for before the CHECKPOINT, never invented, never null, never a placeholder; an event without one is recorded in `change_log` as pending. §4 and the sample: `last_verified_state`. §7: same interchange rule as Exit Prover; `change_log` entries are strings.
- **`schemas/switch-registry-output.schema.json`.** Optional `last_verified_state` (ON, OFF or null) on switches. Every run added it unasked, and the brief's F02 acceptance criterion asks that the last verified state be shown.
- **`schemas/exit-prover-output.schema.json`.** Optional `id`, `owner`, `requested_state`, `last_verified` and `last_verified_state` on `switches` items; `status` enum unchanged. Three of four runs reached for these fields. v2.3.1 payloads remain valid.
- **`tests/schema-policy-cases.md`.** C11 added for the widening; 11 of 11 on re-run.
- **`advisory-tools/README.md`** suite version 1.2 and pin. **`CITATION.cff`**, the README version line and How to Cite in lockstep. `methodology/`, `examples/`, `templates/`, `prompt/` and the deployed-instance text unchanged.

## v2.3.1 (2026-10-13)

Behavioral test coverage for the advisory suite, added the same day as v2.3.0 because that release changed what the model must do and shipped no case that checks it. Patch: tests and companions only; no prompt, schema or methodology change.

- **`tests/advisory-suite-cases.md`, new.** Twelve behavioral cases in the form of `prompt-evaluation-cases.md`: eight for Switch Registry (confirmation is not actuation; pressure to record execution without evidence; a representation offered as execution evidence; execution evidence closing a request; failed actuation; a version 1.0 registry at session start; a drill leaving production state unchanged; a downstream consumer reading a request as a flip) and four for Exit Prover (a specific attestation stays Provisional; a reviewed contract verifies the right and not the exit; PASS withheld while a material item is a representation; PASS on verified evidence). No run is recorded yet; the file says so and reserves the place for one.
- **Known limit of the PASS rule, stated in that file.** The v2.3.0 schema condition for PASS is stricter than the prompt's "every material item Verified"; the worked examples hold no proof JSON to test it against, so whether it bites in use is Unknown. The choice, if it does, is recorded there.
- **`README.md`** tree, **`CONTRIBUTING.md`** and **`advisory-tools/README.md`** pin name the new file or the release. **`CITATION.cff`**, the README version line and How to Cite move to this release in lockstep. All other files unchanged byte for byte.

## v2.3.0 (2026-10-13)

Evidence discipline in the advisory suite brought into line with the core evidence standard, and the schemas made to enforce it. Minor release: instrument content changes in two advisory prompts and three schemas. Source: an external evaluation of v2.2.5 at `795e91a`, run by the maintainer with another model on 13 October 2026 and recorded in `account-maintenance` (register row 17). Its three P1 findings are closed here; its P2 and P3 findings (tolerance clock events, maturity minimum against the scenario bottleneck, exit milestones and elapsed time, scoring calibration and recorded evaluations, a single newcomer route) are carried to the rotation's row 17 slots.

- **`advisory-tools/03-exit-prover.md`, version 1.1.** Phase 4 no longer promotes a specific attestation to Verified. Evidence is Verified only when the artifact was reviewed or an observation recorded; a representation stays Provisional with an evidence-conversion action, owner and target date; each item records what the evidence does and does not establish. PASS requires every material item Verified under that rule. Phase 2 reads a switch's last verified state and any open request, not a "current status". §7 names `methodology/evidence-standard.md` as the sole definition of evidence states. The previous Phase 4 sentence contradicted the standard's treatment of interview representations and is a correction of substance; the old wording is quoted in the completion record.
- **`advisory-tools/02-switch-registry.md`, version 1.1.** Desired state separated from observed state. Rule 8 now says the tool neither executes a flip nor asserts that one was executed. FLIP records `requested` and `authorized` events, sets `requested_state` and moves `status` to Unknown with the last verified state kept visible; the new MODE: CONFIRM records `attempted`, `completed`, `failed` and `verified` events with the evidence item, and only a completed or verified event with evidence changes `status`. Each switch defines `on_means` and `off_means`. Drill events are marked and never change production state by default. Registry and log fields extended accordingly; a log row without `event` is read as a version 1.0 declared flip, not evidence of execution. Sample JSON updated.
- **`advisory-tools/README.md`.** Suite version 1.1. The masthead pinned the repository at v2.1.0, a consistency defect that three releases had carried; it now reads v2.3.0. The Switch Registry row names MODE: CONFIRM.
- **`CONTRIBUTING.md`** and the README tree name the new test file.
- **`advisory-tools/06-clean-market-exit-kit.md`.** One clause in Phase 1: a switch with status Unknown or an open request is a pending request, not a flipped switch.
- **`schemas/evidence-item.schema.json`.** Two conditionals added: Verified requires `artifact_or_observation`, `owner`, `date_or_period_covered`, `source_location` and `freshness_assessment`; an `interview representation` may not be Verified.
- **`schemas/exit-prover-output.schema.json`.** `evidence_items` entries require `verification_status`. PASS requires at least one dependency, at least one Verified evidence item, and every dependency and obligation at Verified or Not applicable.
- **`schemas/switch-registry-output.schema.json`.** `status` gains Unknown; optional `on_means`, `off_means`, `requested_state`, `last_requested`, `last_executed`, `last_verified` and `drill` on switches; optional `event`, `evidence_ref` and `drill` on log rows. Registries emitted by version 1.0 remain valid.
- **`tests/schema-policy-cases.md`, new.** Ten cases: the evaluation's two counterexamples that passed the v2.2.5 schemas, four further rejects, four outputs that must still pass, among them a registry emitted by Switch Registry version 1.0. Each with its expected result, the result observed on 13 October 2026 and the validator used. Specifications and a recorded run; no runner ships.
- **Not changed.** `methodology/`, `examples/`, `templates/`, `prompt/` and the deployed-instance paragraph and retirement notice in `README.md`. README line "enforces the same evidence rules as the Copilot" is unchanged and is now true at the schema layer as well as in the prompts.
- **Deferred to the rotation (register row 17).** A policy validator beyond JSON Schema, and a schema version field with migration rules across all six interchange schemas: both are new instruments and await the maintainer's ruling.
- **`CITATION.cff`**, the README version line and How to Cite move to this release in lockstep.

## v2.2.5 (2026-10-05)

Correction of substance to the retirement notice of the previous release. On 1 October 2026 the GRCnext™ Copilot custom GPT was converted to a private ChatGPT plugin, so the notice's statement that it would not be migrated was false.

- **STRUCK, itemized separately:** the notice sentence "The deployed GRCnext™ Copilot custom GPT will be retired on that date and will not be migrated." is struck in `README.md` and stays visible there. The entry below records the 28 September 2026 ruling that the GPT is not migrated to a plugin; it is shipped history and is unchanged, and that ruling is superseded by this entry.
- **What the notice now states:** the conversion to a private plugin on 1 October 2026 and, from OpenAI's Custom GPT retirement and migration FAQ as read again on 5 October 2026, that a migrated GPT stays usable until retirement but becomes read-only. The retirement date, 11 December 2026, is unchanged.
- **The link is kept at every occurrence,** including the status line of `prompt/v1-production-deployment.md`, which is untouched. It was verified resolving on 5 October 2026 from the maintainer's machine. Striking it and recasting the present-tense deployment wording remains `account-maintenance` RUNBOOK §8 item 28, due on the first sweep on or after 14 December 2026.
- **Not re-verified:** OpenAI's Plugins in ChatGPT and Codex article returned a server error twice on 5 October 2026, so the notice's sentence on which workspaces can create plugins keeps its 28 September 2026 read date.
- **`CITATION.cff`**, the README version lines and How to Cite move to this release in lockstep. All other files in this repository are unchanged byte for byte.

## v2.2.4 (2026-09-28)

Retirement notice for the deployed custom GPT. OpenAI's Custom GPT retirement and migration FAQ, read on 28 September 2026, states that custom GPTs and their GPT pages become inaccessible on 11 December 2026. On Michael's ruling of 28 September 2026 the GPT is retired on that date and not migrated to a plugin; the instructions stay published so readers can build their own.

- **`README.md`**: retirement notice added below the deployed production instance paragraph. The notice cites both OpenAI help articles with the date each was read. The version moved to this release at every occurrence.
- **`CITATION.cff`**: `version` and `date-released` in lockstep.
- **The link is kept.** It is live until 11 December 2026. Striking it and updating the production-status line in `prompt/v1-production-deployment.md`, and recasting the present-tense deployment wording, is `account-maintenance` RUNBOOK §8 item 28, due on the first sweep after that date.
- All other files in this repository are unchanged byte for byte.

## v2.2.3 (2026-09-06)

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- All other files in this repository are unchanged byte for byte.

## v2.2.2 (2026-08-13)

Measurement and standards reframing.

- **Framing correction.** The instrument is now described explicitly as a **structured self-assessment**, not a measurement, benchmark, audit, certification or rating. Outputs are the organization's own answers organized against a defined structure and disciplined by an evidence rule. Structure makes answers comparable over time and arguable before a board; it does not make them independent. A score evidences the organization's position, it does not attest to it, and it must not be presented externally as though a third party had.
- The same framing is added at the head of `methodology/scoring-method.md`.
- **Anchor vignettes recorded as a future option.** Scoring bands are defined by criteria alone. Worked vignettes anchoring each band would reduce rater drift and are noted as a candidate for a later release. Until they exist, inter-rater variation should be expected and cross-organization comparison of scores treated with caution.


License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## v2.2.1 (2026-07-30)

Patch release. Trademark rendering only.

### Added
- Version masthead in the README (line 3), bringing this repository into line with the twelve others in the account. Version had previously lived only in this file and in the tag.
- Origin section in the README recording *Made to Hold* (28 July 2026) as the first public exposition of GRCnext™ and the first public use of Tiny Servants, following the pattern established by computational-drafting.

### Changed
- Trademark rendering corrected to the canonical closed-up form GRCnext™. The retired spaced form "GRC next" is withdrawn from repository prose. One occurrence, in the grc line of the README Part of the ecosystem section.

### Unchanged
- tests/prompt-evaluation-cases.md deliberately retains the unmarked form "GRCnext" inside the stated fail condition of an evaluation case. The string is the failure it tests for and correcting it would destroy the test.
- The v1 production instruction documented in prompt/v1-production-deployment.md, and the not-yet-deployed v2 instruction.

## v2.2.0 (2026-07-15)

A documentation and classification release. No change to the method,
scoring or prompts.

### Added

- Deployed production instance paragraph in the README: the live custom
  GPT at chatgpt.com currently runs the v1 single-prompt configuration.
  The v2 configuration this repository ships has not yet been deployed
  to that instance; the README now states this plainly so the repository
  never describes a deployment that does not exist.
- `prompt/v1-production-deployment.md`: the deployed v1 production
  configuration captured verbatim (name, description, instruction,
  capabilities) as the system of record for what is live, with a pointer
  to the v2 upgrade path.
- Part of the ecosystem section in the README: classified Layer 2 in
  the canonical map at rolldabones/rolldabones with five nearest
  neighbors.

### Notes

- The deployed v1 instruction references NIST AI RMF-aligned controls
  in its AI overlay. As of this release NIST AI RMF means version 1.0
  (January 2023) with the Generative AI Profile (NIST AI 600-1, July
  2024).
- Open item: redeploying the production GPT to v2 per the README's
  ChatGPT pattern remains available at any time; on redeployment,
  `prompt/v1-production-deployment.md` is re-marked superseded and the
  repository re-versions.

## v2.1.0 (2026-07-04)

A capability release adding the Advisory Tools Suite. No change to the
Copilot method, scoring or prompts.

### Added

- `advisory-tools/`: six standalone model-agnostic system prompts (Pipes
  Mapper, Switch Registry, Exit Prover, Treasury Reroute Planner, Data
  Switchboard Planner, Clean Market Exit Kit), translated from the
  MindStudio design brief, with a suite README covering the
  MindStudio-to-prompt translation map, the JSON interchange contract
  and registry stewardship.
- `schemas/`: six JSON Schema (draft 2020-12) definitions for the suite
  interchange payloads.
- Root README: repository map entries and an Advisory Tools Suite
  section.

### Notes

- Statelessness is handled by a paste-in/paste-out protocol: every tool
  re-emits the full updated registry with a version timestamp and change
  log, and the user owns persistence.
- The suite adopts the closed form GRCnext™ throughout, superseding the
  spaced form used in the source design brief.
- Exit Prover verdicts are three-valued (PASS, PROVISIONAL PASS, FAIL);
  proofs resting on unverified representations cannot exceed
  PROVISIONAL PASS.

## v2.0.1 (2026-07-02)

A correction and parity release from a publication-readiness audit. No
change to the method's architecture.

### Fixed

- Case 6 Constraint Level oracle in `tests/scoring-cases.md`, corrected
  from 4 to 3 to match the walkthrough profile.
- Scoring sentences in the modular and compact editions now state the six
  domains, four results and a tolerance result.
- Glossary cross-reference to the AI overlay corrected from Section 11 to
  Section 12 of the full prompt.
- SW-001 pass criterion clarified: the 12-hour impact tolerance governs
  the pass, with the 4-hour internal target recorded as missed and
  carried as a corrective action.
- Payment Pipes and agentic Services-and-tolerances scores recalibrated
  from 4 to 3 where instrumentation is not evidenced. Constraint Levels
  and readiness decisions are unchanged.
- Serial commas removed across the repository per the house style, with
  ambiguous lists restructured.

### Changed

- Anti-injection, fixed-rules, US-English, gate-granularity,
  footer-definition and credential-rotation rules now stated in all three
  prompt editions.
- Status labels aligned to [↻ draft], [⇥ pending review] and [✓ final].
- A Refuted verification state added to the verification states and the
  evidence-item schema.
- A None exercise tier added to the Service Dossier schema.
- The primitive vocabulary added to the modular and compact editions.
- Evidence types listed weakest to strongest everywhere.
- The must-stay-consistent lists now name all three prompt editions.

## v2.0.0 (2026-07-01)

This is a substantive redesign, not a light edit. The intellectual
architecture of v1 is preserved. The method is now more auditable,
testable and resistant to false confidence, and the repository is
modular rather than a single prompt.

### Added

- Three-part conclusion for every assessment: capability profile,
  evidence confidence and constraint finding. Capability, confidence
  and critical weakness are no longer collapsed into one number.
- Evidence ledger. Every scored claim is traceable to an evidence item
  with type, owner, date, source, verification status, freshness and
  any contradictions.
- Exercise tiers T0 to T4 and a full execution clock (detect, interpret,
  decide, authorize, execute, verify, communicate, stabilize). A
  discussion-based tabletop can no longer earn an execution score.
- Expanded AI overlay. AI is analyzed as a Pipe, a Switch, a decision
  actor, an evidence producer or a concentration dependency, with
  explicit treatment of authority, tool access, rollback, kill
  mechanisms and human assumption of control for agentic systems.
- Progressive disclosure. The Copilot no longer emits the full output
  package before sufficient facts exist. It works through an initial
  output, then a developed assessment.
- Readiness gates with five states: Pass, Provisional Pass, Fail,
  Unknown, Not Applicable. A failed or unknown core gate blocks an
  unqualified conclusion that optionality has been demonstrated.
- Readiness decision (Demonstrated, Conditionally Demonstrated, Not
  Demonstrated) and tolerance result (Met, Not Met, Not Tested, Cannot
  Determine) with named clock-start and clock-stop events.
- Modular repository: separate methodology, templates, schemas, worked
  examples and tests. See the repository map in the README.
- Three worked examples: a real-time payment service, a manufacturing
  production service and an agentic AI service.
- Machine-readable JSON Schemas for the Service Dossier, the evidence
  item and the assessment result.
- Test suites: scoring cases that pin the rubric, prompt-evaluation
  cases that check behavior and adversarial inputs that check
  guardrails.
- Model-neutral, dual-platform deployment guidance for Claude and
  ChatGPT, including the ChatGPT 8,000-character instruction limit, the
  Knowledge-file offload pattern, Code Interpreter, Data Controls and
  the Memory caveat.
- Long-form model-agnostic prompt edition
  (`prompt/GRCnext-Copilot-long-form.md`). A self-contained prompt that
  carries the methodology reasoning inline, for stronger reasoning models
  and for platforms that cannot read attached files.
- Conceptual foundation document (`methodology/method-and-logic.md`).
  States the escapement logic behind the method, the five primitives and
  their mapping to the six scored domains and the reasoning under the
  scoring, evidence and execution-clock rules.

### Changed

- Evidence rule. "No evidence, no credit" is replaced by "No verified
  evidence, no verified credit." Representations may receive clearly
  labeled provisional credit only when paired with an evidence-conversion
  action. Missing evidence is never treated as proof of absence.
- Scoring. The minimum of Pipes, Switches and Exits is retained as the
  Constraint Level. It is no longer presented as the entire score. The
  full capability profile is always shown so a fatal weakness is not
  averaged away.
- Maturity scale wording standardized to L0 Unowned, L1 Described,
  L2 Designed, L3 Exercised, L4 Instrumented, with explicit rules that
  a talk-only tabletop does not earn L3 and dashboards alone do not
  earn L4.
- Escalation is treated as a controlled handoff. The Copilot separates
  what can be concluded from what must be reserved for counsel, rather
  than halting the whole analysis.
- User-specific ChatGPT customization settings were removed from the
  core methodology and replaced with model-neutral configuration notes.
- Obsolete model reference removed. v1 recommended a specific model.
  v2 gives model-neutral guidance.
- Spelling standardized to US English. Terminology standardized to
  "governance, risk management and compliance" and "Switch Catalog".

### Preserved

- GRCnext™ as executable Global Optionality.
- The critical service as the unit of analysis.
- The spine of the six domains from Services and tolerances through
  Evidence and improvement.
- The six-domain rubric scored 0 to 4.
- The six-section Service Dossier.
- The requirement that evidence precede credit.

## v1.0.0 (prior release)

Single-prompt Custom GPT build. Defined GRCnext™ as executable global
optionality, used the critical service as the unit of analysis, scored
six domains, applied the minimum rule and produced dossiers, exit
tactics, playbooks, drills and a 90-day backlog. Retained in history at
https://github.com/rolldabones/GRCnext-Copilot.

Final Liability rests with the Human.
