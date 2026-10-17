# Changelog

All notable changes to GRCnext™ Copilot are recorded here. Dates use the
Asia/Seoul time zone (UTC+9).

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
