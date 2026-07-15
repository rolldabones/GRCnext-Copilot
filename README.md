# GRCnext™ Copilot

**An evidence-led assistant for governance, risk management and compliance assessment and design.**

GRCnext™ Copilot tests one thing: whether an organization holds **Global Optionality**. That is the capacity to preserve or create lawful, authorized and executable choices when a critical service, dependency, provider, jurisdiction, technology or operating assumption becomes unavailable or unacceptable.

The idea behind the method is the escapement. An escapement keeps a timepiece accurate over long periods without anyone touching it, by removing a dependence on something fragile. A governance control, done properly, works the same way. A control that holds only while someone is watching fails the moment attention lapses, and attention always lapses. GRCnext™ credits controls that are built into a system in advance and hold under stress, not controls that merely permit an action. The full reasoning is in [`methodology/method-and-logic.md`](methodology/method-and-logic.md).

The distinction the Copilot enforces is the one that matters in an audit:

> A policy that permits an action is not optionality. Optionality is an authorized person executing that action, within the impact tolerance, using tested procedures that produce recoverable evidence.

Or put in the operating principle the whole method turns on:

> **GRC owns the clock. Detect, decide, execute, within tolerance.**

---

## What changed in v2

v1 was a single dense instruction block that did the work of a constitution, a methodology, a scoring engine, a legal triage protocol, a report template and one user's ChatGPT settings all at once. It worked, but it invited the model to satisfy an output checklist mechanically and it flattened materially different risk profiles into a single minimum score.

v2 keeps the intellectual spine and repairs the failure modes:

1. **Three separate conclusions, not one.** Every assessment now reports **capability** (what the organization appears able to do), **evidence confidence** (how strongly that is supported) and the **constraint finding** (the weakest condition that could defeat execution under stress). A polished but stale document no longer scores like a recently executed drill.
2. **A verifiable evidence rule.** "No evidence, no credit" became "no *verified* evidence, no *verified* credit." Representations can take provisional credit while labeled unverified and tied to a named evidence-conversion action, so the Copilot stays useful during discovery without silently treating absence as proof of absence.
3. **The minimum rule is preserved but demoted.** `min(Pipes, Switches, Exits)` is retained as the **Constraint Level**, not the whole score. It sits alongside the full capability profile, an evidence-confidence rating and a readiness decision.
4. **Time is first-class.** The method measures the full execution clock: Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize. A switch that runs in two hours can still fail a twelve-hour tolerance if authorization and communication add eighteen more.
5. **Exercises are tiered.** T0 walkthrough through T4 live invocation. The Copilot must state which actions were simulated and which were performed, and it will not award "Exercised" maturity for a conversation.
6. **The AI overlay is real.** AI is analyzed as a Pipe, a Switch, a decision actor, an evidence producer or a concentration dependency. For agentic AI the method governs the verb, the boundary and the consequence, and it refuses to assume a human-in-the-loop control is effective without testing the human's information, authority, time and practical ability to intervene.
7. **Progressive disclosure.** The Copilot no longer emits a full assessment package before the facts exist. It scopes, states assumptions, requests evidence and proposes the next step.
8. **Worked examples and tests ship with the method.** Without them, different models interpret the rubric differently. See `examples/` and `tests/`.

A full v1 to v2 diff is in [`CHANGELOG.md`](CHANGELOG.md).

---

## The method in one page

**Unit of analysis.** The critical service: an outcome delivered to a defined customer whose disruption beyond an approved period or level creates material harm. Not an application, a department, a vendor, a process step or an org-chart entry.

**Six domains, each scored 0 to 4.** Services and tolerances; Pipes; Switches; Exits; Exercises; Evidence and improvement.

**Maturity.** L0 Unowned, L1 Described, L2 Designed, L3 Exercised, L4 Instrumented.

**Eight readiness gates.** Service and owner; approved measurable tolerance; mapped dependencies; switch authority; at least one executable exit for the top concentration dependency; at least one completed severe-but-plausible exercise; evidence that the tolerance was met; corrective actions with owners and dates. A fail or unknown on any core gate blocks an unqualified "demonstrated" conclusion.

**Four scoring results.** Capability profile (all domain scores shown); Constraint Level = `min(Pipes, Switches, Exits)`; Evidence confidence (High, Moderate, Low, Indeterminate); Readiness decision (Demonstrated, Conditionally Demonstrated, Not Demonstrated); plus a Tolerance result (Met, Not Met, Not Tested, Cannot Determine).

Detail lives in [`methodology/`](methodology/).

---

## Repository map

```
GRCnext-Copilot/
├── README.md                     You are here
├── LICENSE
├── CHANGELOG.md                  v1 to v2 diff and version history
├── CONTRIBUTING.md
├── prompt/
│   ├── GRCnext-Copilot-v2.md          Authoritative modular prompt
│   ├── GRCnext-Copilot-long-form.md   Self-contained model-agnostic prompt
│   ├── compact-custom-gpt-version.md  Fits the ChatGPT 8,000-char field
│   └── model-configuration-notes.md   Deployment on Claude, ChatGPT and elsewhere
├── advisory-tools/                New in v2.1: the operating suite
│   ├── README.md                  Suite overview, translation map, interchange contract
│   ├── 01-pipes-mapper.md         Dependency Registry
│   ├── 02-switch-registry.md      Switch registry and append-only flip log
│   ├── 03-exit-prover.md          Exit readiness proof: PASS / PROVISIONAL PASS / FAIL
│   ├── 04-treasury-reroute-planner.md  Plan B for financial pipes
│   ├── 05-data-switchboard-planner.md  Reroute, isolate or sever data flows
│   └── 06-clean-market-exit-kit.md     Orchestrator: T0 to T+72h master playbook
├── methodology/
│   ├── method-and-logic.md   Conceptual foundation and the escapement logic
│   ├── capability-model.md
│   ├── scoring-method.md
│   ├── evidence-standard.md
│   ├── exercise-tiers.md
│   └── glossary.md
├── templates/
│   ├── service-dossier.md
│   ├── evidence-ledger.csv
│   ├── switch-catalog.csv
│   ├── exit-playbook.md
│   ├── exercise-plan.md
│   ├── evidence-pack-index.md
│   └── capa-register.csv
├── schemas/
│   ├── service-dossier.schema.json
│   ├── evidence-item.schema.json
│   ├── assessment-result.schema.json
│   ├── pipes-mapper-output.schema.json     Advisory Tools interchange
│   ├── switch-registry-output.schema.json
│   ├── exit-prover-output.schema.json
│   ├── treasury-reroute-plan.schema.json
│   ├── data-switchboard-plan.schema.json
│   └── clean-market-exit.schema.json
├── examples/
│   ├── payment-service/          Financial-services worked example
│   ├── manufacturing-service/    Physical, safety-critical worked example
│   └── agentic-ai-service/       Agentic AI worked example
└── tests/
    ├── scoring-cases.md          Pins the rubric
    ├── prompt-evaluation-cases.md Behavioral tests for the Copilot
    └── adversarial-inputs.md      Red-team prompts and expected behavior
```

---

## Advisory Tools Suite (new in v2.1)

The Copilot assesses optionality. The [`advisory-tools/`](advisory-tools/README.md) directory operates it: six standalone model-agnostic system prompts implementing Pipes, Switches and Exits under the 72-hour execution model. Pipes Mapper maintains the dependency registry, Switch Registry keeps the flip log, Exit Prover tests exit readiness, Treasury Reroute Planner and Data Switchboard Planner build the financial and data contingency plans, and the Clean Market Exit Kit merges everything into one T0 to T+72h master playbook. Each prompt is self-contained, exchanges tool-tagged JSON validated by the suite schemas in [`schemas/`](schemas/), enforces the same evidence rules as the Copilot and runs in a degraded standalone mode when upstream outputs are absent. Start with the suite README for the MindStudio-to-prompt translation map, the interchange contract and the registry stewardship rules.

---

## Deploy it

Full instructions with data-control and memory caveats are in [`prompt/model-configuration-notes.md`](prompt/model-configuration-notes.md). In brief:

**Claude (Project or Custom Instructions).** Paste [`prompt/GRCnext-Copilot-v2.md`](prompt/GRCnext-Copilot-v2.md) into the Project instructions. Project instruction limits are large enough for the full prompt, so no compaction is needed. Add the `templates/` and `examples/` files as Project knowledge if you want the Copilot to reuse them.

**ChatGPT Custom GPT.** The instructions field caps at 8,000 characters, so paste [`prompt/compact-custom-gpt-version.md`](prompt/compact-custom-gpt-version.md) there and attach [`prompt/GRCnext-Copilot-v2.md`](prompt/GRCnext-Copilot-v2.md) as a Knowledge file. Enable Code Interpreter so the GPT can read the Knowledge and the templates. Turn training off in Data Controls. Note that enabling Memory changes outputs.

**Deployed production instance (as of 15 July 2026).** The author's deployed custom GPT is at https://chatgpt.com/g/g-69831f7f8df48191a3808c37306ec918-grcnexttm-copilot and currently runs the **v1 single-prompt configuration**, documented verbatim in [`prompt/v1-production-deployment.md`](prompt/v1-production-deployment.md): the v1 instruction in the Instruction field, no Knowledge files, no conversation starters, and Web Search, Canvas, Image Generation and Code Interpreter & Data Analysis enabled. The v2 configuration this repository ships (compact edition as Instruction plus the modular v2 prompt as Knowledge, per the pattern above) has not yet been deployed to that instance. When production changes, this paragraph and that file change and the repository version bumps.

**Any strong model, standalone.** For a self-contained deployment that needs no attached files, paste [`prompt/GRCnext-Copilot-long-form.md`](prompt/GRCnext-Copilot-long-form.md) as the entire system prompt. It carries the methodology reasoning inline, so it suits stronger reasoning models with large context windows and platforms that cannot read attachments.

**Model.** Select the strongest available reasoning model on your platform. The method is model-neutral. Do not hardcode a model name into the prompt.

---

## What the Copilot will not do

It will not invent evidence, contractual language, legal authority, test results, owners, dates or scores. It will not assert legal or regulatory compliance without supporting evidence and authority. It treats "not supplied" as unknown, never as "does not exist." It warns against pasting secrets or personal data and redacts to neutral labels. For issues touching governing law, live disputes, sanctions, national security, regulated data, safety-critical services or criminal exposure it escalates and stops short of a jurisdiction-specific legal conclusion.

GRCnext™ Copilot is a decision-support and assurance-design tool. It is not legal advice and it is not a compliance certification.

---

## Part of the ecosystem

This repository is part of the [rolldabones governance ecosystem](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md), classified in Layer 2 (assessment and decision tools). Nearest neighbors:

- [grc](https://github.com/rolldabones/grc) - the GRC next framework whose five primitives this Copilot runs as a scoring engine
- [RedCap-00](https://github.com/rolldabones/RedCap-00) - the 72-hour operational-optionality self-check this method generalizes
- [RedCap-01](https://github.com/rolldabones/RedCap-01) - the objective-to-risk alignment diagnostic upstream of optionality design
- [Contract-Mechanism-Review-Assistant](https://github.com/rolldabones/Contract-Mechanism-Review-Assistant) - the contract reader that feeds the Contract Exit Review mode
- [AI-Impact-Assessment-Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool) - the pre-deployment gate whose kill-switch and decommission requirements are Switches and Exits here

---

## License and attribution

GRCnext™ and the associated doctrine vocabulary (Slow AI, Informed Intent, Final Liability) originate with the author. See [`LICENSE`](LICENSE) for reuse terms.

---

Final Liability rests with the Human.
