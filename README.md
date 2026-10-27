# GRCnext™ Copilot

**An evidence-led assistant for governance, risk management and compliance assessment and design.**

**Version 2.7.1 · 27 October 2026 · License: [CC BY-NC-SA 4.0](LICENSE) · Changes: [CHANGELOG.md](CHANGELOG.md)**

**Acceptance status ([ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), 27 October 2026, KST):** The main prompt ([`prompt/GRCnext-Copilot-v2.md`](prompt/GRCnext-Copilot-v2.md)) is accepted with residuals on claude-opus-5-5: run 20261027-R2 passed all twelve critical cases and 13 of the 14 others, with SC2 a residual ([run record](tests/prompt-evaluation-cases.md#suite-configuration-and-status)). It is not accepted on claude-sonnet-5-5, where critical case A6 failed in the same run, and the long-form and compact editions carry no acceptance. The advisory tools' run of 13 October 2026 (tests/evaluation-set/) is not yet read against ACCEPTANCE.md and carries no acceptance. The account's status table is in [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md#instrument-status).

GRCnext™ Copilot tests one thing: whether an organization holds **Global Optionality**. That is the capacity to preserve or create lawful, authorized and executable choices when a critical service, dependency, provider, jurisdiction, technology or operating assumption becomes unavailable or unacceptable.

The idea behind the method is the escapement. An escapement keeps a timepiece accurate over long periods without anyone touching it, by removing a dependence on something fragile. A governance control, done properly, works the same way. A control that holds only while someone is watching fails the moment attention lapses, and attention always lapses. GRCnext™ credits controls that are built into a system in advance and hold under stress, not controls that merely permit an action. The full reasoning is in [`methodology/method-and-logic.md`](methodology/method-and-logic.md).

The distinction the Copilot enforces is the one that matters in an audit:

> A policy that permits an action is not optionality. Optionality is an authorized person executing that action, within the impact tolerance, using tested procedures that produce recoverable evidence.

Or put in the operating principle the whole method turns on:

> **GRC owns the clock. Detect, decide, execute, within tolerance.**

---

## Start here

To run one assessment of one critical service, follow [`START-HERE.md`](START-HERE.md): paste the v2 prompt, fill the intake pack, send the first message, save the result as JSON and run the validator over it. The payment example walks the same route with its inputs, its assessment and its result file.

**What this instrument is, stated plainly.** This is a **structured self-assessment**. It is not a measurement, a benchmark, an audit, a certification or a rating. Its outputs are the organization's own answers, organized against a defined structure and disciplined by an evidence rule. That structure is what makes the answers comparable over time and arguable in front of a board. It does not make them independent. A score produced here evidences the organization's position; it does not attest to it, and it should never be presented externally as though a third party had.

How v2 differs from v1 is recorded in [`CHANGELOG.md`](CHANGELOG.md), in the entry for the first v2 release.

---

## The method in one page

**Unit of analysis.** The critical service: an outcome delivered to a defined customer whose disruption beyond an approved period or level creates material harm. Not an application, a department, a vendor, a process step or an org-chart entry.

**Six domains, each scored 0 to 4.** Services and tolerances; Pipes; Switches; Exits; Exercises; Evidence and improvement.

**Maturity.** L0 Unowned, L1 Described, L2 Designed, L3 Exercised, L4 Instrumented.

**Eight readiness gates.** Service and owner; approved measurable tolerance; mapped dependencies; switch authority; at least one executable exit for the top concentration dependency; at least one completed severe-but-plausible exercise; evidence that the tolerance was met; corrective actions with owners and dates. A fail or unknown on any core gate blocks an unqualified "demonstrated" conclusion.

**Four results plus the tolerance result.** Capability profile (all domain scores shown); Constraint Level = `min(Pipes, Switches, Exits)`, the ordinal maturity diagnostic, reported with the **binding constraint** (the clock phase or gate that actually limits execution in the governing scenario); Evidence confidence (High, Moderate, Low, Indeterminate); Readiness decision (Demonstrated, Conditionally Demonstrated, Not Demonstrated, the one verdict scale the advisory suite also uses; the suite's Demonstrated, in Exit Prover and the Clean Market Exit Kit, does not itself require a tolerance result of Met: the control is the validator's M4 check, which rejects a Demonstrated proof or Kit verdict whose interim continuity is outside the tolerance and warns when the fit is not shown); plus the Tolerance result (Met, Not Met, Not Tested, Cannot Determine), measured from the **onset of disruption**, not from detection.

Detail lives in [`methodology/`](methodology/).

---

## Repository map

```
GRCnext-Copilot/
├── README.md                     You are here
├── START-HERE.md                 One service, start to finish
├── LICENSE
├── CHANGELOG.md                  Version history, with the v1 to v2 diff
├── CITATION.cff
├── CONTRIBUTING.md
├── .github/workflows/
│   └── validate.yml              Runs the validator over fixtures, examples and samples on every push
├── prompt/
│   ├── GRCnext-Copilot-v2.md          Authoritative modular prompt
│   ├── GRCnext-Copilot-long-form.md   Self-contained edition with the reasoning inline
│   ├── GRCnext-Copilot-compact.md     Short edition of the v2 prompt
│   ├── model-configuration-notes.md   Deployment on any current assistant
│   └── v1-production-deployment.md    The v1 text the custom GPT ran, kept as the record
├── advisory-tools/                The operating suite
│   ├── README.md                  Suite overview, primitives in the suite, interchange map
│   ├── 01-pipes-mapper.md         Dependency Registry
│   ├── 02-switch-registry.md      Switch registry and append-only flip log
│   ├── 03-exit-prover.md          Exit proof with milestones against tolerance
│   ├── 04-treasury-reroute-planner.md  Plan B for financial pipes
│   ├── 05-data-switchboard-planner.md  Reroute, isolate or sever data flows
│   └── 06-clean-market-exit-kit.md     Orchestrator: T0 (onset) to final exit
├── methodology/
│   ├── method-and-logic.md   Conceptual foundation and the escapement logic
│   ├── capability-model.md
│   ├── scoring-method.md     Scoring, gates and the decision caps
│   ├── evidence-standard.md
│   ├── exercise-tiers.md
│   └── glossary.md
├── templates/                Blank: headers and fields only
│   ├── intake-pack.md        Keyed to the eight gates
│   ├── service-dossier.md
│   ├── evidence-ledger.csv
│   ├── switch-catalog.csv
│   ├── exit-playbook.md
│   ├── exercise-plan.md
│   └── capa-register.csv
├── schemas/                  Interchange contract 2.6; README carries the migration rules
├── examples/                 Each with input-pack.md, assessment.md and assessment-result.json
│   ├── payment-service/          Financial-services worked example
│   ├── manufacturing-service/    Physical, safety-critical worked example
│   └── agentic-ai-service/       Agentic AI worked example
├── tests/
│   ├── scoring-cases.md          Pins the rubric
│   ├── prompt-evaluation-cases.md Behavioral tests for the Copilot; the main prompt's suite, status and run record
│   ├── adversarial-inputs.md      Red-team prompts and expected behavior
│   ├── run_prompt_cases.py        Runs the 26-case suite against the API
│   ├── score_prompt_cases.py      Cross-model scorer, read under ACCEPTANCE.md
│   ├── prompt-fixtures/           Synthetic input for case A4
│   ├── prompt-runs/               Transcripts, manifests and scores of each logged run
│   ├── schema-policy-cases.md     Rules the schemas and validator enforce, with recorded runs
│   ├── advisory-suite-cases.md    Behavioral cases for Switch Registry and Exit Prover
│   └── evaluation-set/            Versioned run records, fixtures and emitted payloads
└── tools/
    ├── validate.py                Schema and policy validation of interchange payloads
    └── check_fixtures.py          Every fixture, example and sample against its expected verdict
```

---

## Advisory Tools Suite

The Copilot assesses optionality. The [`advisory-tools/`](advisory-tools/README.md) directory operates it: six standalone model-agnostic system prompts implementing Pipes, Switches and Exits against each critical service's own impact tolerance, reported as three milestones (containment, interim continuity, final exit). Pipes Mapper maintains the dependency registry, Switch Registry keeps the flip log, Exit Prover tests exit readiness, Treasury Reroute Planner and Data Switchboard Planner build the financial and data contingency plans and the Clean Market Exit Kit merges everything into one master playbook from T0 (onset) to final exit. Each prompt is self-contained, exchanges tool-tagged JSON validated by the suite schemas in [`schemas/`](schemas/) and by [`tools/validate.py`](tools/validate.py), which adds the policy checks a schema cannot express (incomplete by design: its acceptance is not a readiness conclusion and human review of every readiness decision is retained), enforces the same evidence rules as the Copilot and runs in a degraded standalone mode when upstream outputs are absent. Start with the suite README for the primitives as the suite narrows them, the interchange map and the registry stewardship rules. Behavioral validation is outstanding: run 2, which [`tests/advisory-suite-cases.md`](tests/advisory-suite-cases.md) requires before the suite prompts are relied on, has not been run; run 1 tested earlier versions of Switch Registry and Exit Prover only, and Pipes Mapper, Treasury Reroute Planner, Data Switchboard Planner and the Clean Market Exit Kit have no behavioral run.

---

## Deploy it

Full instructions with data-control and memory caveats are in [`prompt/model-configuration-notes.md`](prompt/model-configuration-notes.md). In brief:

**Claude (Project or Custom Instructions).** Paste [`prompt/GRCnext-Copilot-v2.md`](prompt/GRCnext-Copilot-v2.md) into the Project instructions. Project instruction limits are large enough for the full prompt, so no compaction is needed. Add the blank `templates/` and the `examples/` files as Project knowledge if you want the Copilot to reuse them; [`START-HERE.md`](START-HERE.md) is the first run.

**Short edition.** [`prompt/GRCnext-Copilot-compact.md`](prompt/GRCnext-Copilot-compact.md) is the v2 prompt in short form, for an assistant with a tight instruction limit; it carries the decision caps and points to the v2 prompt for the rest. Until the release of 18 October 2026 it was `compact-custom-gpt-version.md`, written for the 8,000-character field of a custom GPT; that route closed with the retirement (sources in [RETIREMENT.md](https://github.com/rolldabones/rolldabones/blob/main/RETIREMENT.md)), and the edition no longer fits that field.

**Former production instance.** The author's GRCnext™ Copilot custom GPT ran the **v1 single-prompt configuration** until 1 October 2026, documented in [`prompt/v1-production-deployment.md`](prompt/v1-production-deployment.md) as last verified on 15 July 2026, before the conversion: the v1 instruction in the Instruction field, no Knowledge files, no conversation starters; Web Search, Canvas, Image Generation and Code Interpreter & Data Analysis enabled. The v2 configuration this repository ships was never deployed to it.

> **Retired 1 October 2026 (KST).** The GRCnext™ Copilot custom GPT was retired on 1 October 2026 and converted to a private plug-in on the OpenAI platform. The instructions published in this repository are the text of record and suffice for anyone who wants to build their own. History and sources: [RETIREMENT.md](https://github.com/rolldabones/rolldabones/blob/main/RETIREMENT.md).

**Any strong model, standalone.** For a self-contained deployment that needs no attached files, paste [`prompt/GRCnext-Copilot-long-form.md`](prompt/GRCnext-Copilot-long-form.md) as the entire system prompt. It carries the methodology reasoning inline, so it suits stronger reasoning models with large context windows and platforms that cannot read attachments.

**Model.** Select the strongest available reasoning model on your platform. The method is model-neutral. Do not hardcode a model name into the prompt.

---

## What the Copilot will not do

It will not invent evidence, contractual language, legal authority, test results, owners, dates or scores. It will not assert legal or regulatory compliance without supporting evidence and authority. It treats "not supplied" as unknown, never as "does not exist." It warns against pasting secrets or personal data and redacts to neutral labels. For issues touching governing law, live disputes, sanctions, national security, regulated data, safety-critical services or criminal exposure it escalates and stops short of a jurisdiction-specific legal conclusion.

GRCnext™ Copilot is a decision-support and assurance-design tool. It is not legal advice and it is not a compliance certification.

---

## Origin

GRCnext™ received its first public exposition in the essay [*Made to Hold*](https://redcaps.substack.com/p/made-to-hold) (Substack, [redcaps](https://open.substack.com/pub/redcaps), 28 July 2026), which also introduced **Tiny Servants**. This repository states the framework and its scoring method fresh rather than excerpting the essay, so that the two artifacts can evolve independently: the essay as origin, the repository as canon.

## Part of the ecosystem

This repository is part of the [rolldabones governance ecosystem](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md), classified in Layer 2 (assessment and decision tools). Nearest neighbors:

- [grc](https://github.com/rolldabones/grc) - the OCEG-spine working method for governance, risk management and compliance; the five GRCnext™ primitives are defined here, not there
- [RedCap-00](https://github.com/rolldabones/RedCap-00) - the 72-hour operational-optionality self-check this method generalizes
- [RedCap-01](https://github.com/rolldabones/RedCap-01) - the objective-to-risk alignment diagnostic upstream of optionality design
- [Contract-Mechanism-Review-Assistant](https://github.com/rolldabones/Contract-Mechanism-Review-Assistant) - the contract reader that feeds the Contract Exit Review mode
- [AI-Impact-Assessment-Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool) - the pre-deployment gate whose kill-switch and decommission requirements are Switches and Exits here

---

## License and attribution

GRCnext™ and the associated doctrine vocabulary (Slow AI, Informed Intent, Final Liability) originate with the author. The three doctrines are used in this repository as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement; the glossary quotes them verbatim. See [`LICENSE`](LICENSE) for reuse terms.

## How to Cite

> Paik, Son-U Michael. *GRCnext™ Copilot*, v2.7.1. GRC Solutions Korea, 2026. https://github.com/rolldabones/GRCnext-Copilot

A machine-readable citation is in [CITATION.cff](CITATION.cff).

---

Final Liability rests with the Human.
