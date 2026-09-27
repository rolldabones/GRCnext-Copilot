# Changelog

All notable changes to GRCnext™ Copilot are recorded here. Dates use the
Asia/Seoul time zone (UTC+9).

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
