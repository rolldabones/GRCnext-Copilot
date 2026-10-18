# GRCnext™ Advisory Tools Suite - Model-Agnostic Prompts

**Suite version:** 1.4 · **Repo:** GRCnext™ Copilot v2.6.0 · **Source design:** a MindStudio design brief (not published)

Amended 18 October 2026 (KST) in GRCnext™ Copilot v2.6.0: milestones against each service's own tolerance replace the former fixed window; one verdict scale (Demonstrated, Conditionally Demonstrated, Not Demonstrated); evidence state Not evidenced; Primitives in the suite table added; one interchange map; Custom GPT route and the unpublished design brief pointer dropped; draft tag dropped.

Six standalone system prompts implementing the Pipes, Switches, Exits methodology in any current assistant, with execution measured against each critical service's own impact tolerance from the onset of disruption. Each file is self-contained: paste one prompt as the system prompt or project instructions of any current assistant. No plugins, code execution, browsing, memory or vendor features are assumed.

| File | Tool | Function |
|---|---|---|
| [01-pipes-mapper.md](01-pipes-mapper.md) | Pipes Mapper | Dependency Registry: maps critical processes, data flows and dependency chains |
| [02-switch-registry.md](02-switch-registry.md) | Switch Registry | Registry and append-only log of switches; VIEW / FLIP / CONFIRM / NEW / ADVISE / EXPORT modes; desired state kept apart from verified actual state |
| [03-exit-prover.md](03-exit-prover.md) | Exit Prover | Tests exit readiness; Demonstrated / Conditionally Demonstrated / Not Demonstrated proof with gap analysis and milestones against tolerance |
| [04-treasury-reroute-planner.md](04-treasury-reroute-planner.md) | Treasury Reroute Planner | Plan B for financial pipes; masked identifiers; plans only, never executes |
| [05-data-switchboard-planner.md](05-data-switchboard-planner.md) | Data Switchboard Planner | Reroute, isolate or sever data flows; compliance checklist mapping |
| [06-clean-market-exit-kit.md](06-clean-market-exit-kit.md) | Clean Market Exit Kit | Orchestrator; merges all outputs into one master playbook from T0 (onset) to final exit |

## Translation from MindStudio

The suite was translated from a MindStudio design brief. That brief is not published; the prompts in this folder are the suite's only published form.

| MindStudio construct | Model-agnostic equivalent |
|---|---|
| Detect PII block | Confidentiality gate in each prompt: warn once, substitute neutral labels, redact in outputs, proceed |
| Checkpoint block | CHECKPOINT gates: stop and obtain explicit user confirmation before committing |
| Google Sheets persistence | Paste-in/paste-out registry protocol: user supplies current state, tool always re-emits the full updated registry with a version timestamp and change log |
| Create Google Doc | Board-ready markdown report section in every output |
| Run Workflow (sub-workflow reuse) | JSON interchange contract: each tool emits a `tool`-tagged JSON that downstream tools validate and consume |
| Run Function (custom code) | Explicit arithmetic shown in-line (limit checks, milestone arithmetic against the service's tolerance) using only user-supplied figures |
| Logic / Loop blocks | Numbered workflow steps in each prompt |

## Interchange contract

Every tool emits JSON with `"schema_version": "2.6"` as its first field, a `tool` field and an ISO 8601 version timestamp. Consumption map (the single map; each prompt's Interchange section states the same edges):

- pipes_mapper → Exit Prover, Data Switchboard Planner, Clean Market Exit Kit
- switch_registry → Exit Prover, Treasury Reroute Planner, Data Switchboard Planner, Clean Market Exit Kit
- exit_prover → Clean Market Exit Kit
- treasury_reroute_planner → Clean Market Exit Kit
- data_switchboard_planner → Clean Market Exit Kit
- service dossier (`tolerance_hours`) → Exit Prover, Treasury Reroute Planner, Data Switchboard Planner, Clean Market Exit Kit

Where money and data flows intersect, the Clean Market Exit Kit reconciles the treasury and data plans; neither planner feeds the other. The four tools that read `tolerance_hours` report three milestones against it in their JSON (`containment`, `interim_continuity`, `final_exit`), each with elapsed time from onset along the critical path, its basis (observed, estimated, assumed or unknown), its limit and whether it is within that limit. None of them sums against a fixed window.

Every tool runs in degraded standalone mode when upstream JSON is absent; findings gathered by interrogation are Provisional and verdicts are capped accordingly.

Before a payload is consumed by the next tool, run it through [`../tools/validate.py`](../tools/validate.py): it applies the schema and the policy rules the schema cannot carry, and exits non-zero on any reject. The validator is incomplete and its ACCEPT is not a readiness conclusion; a human reviews every readiness decision and every Demonstrated verdict. Both tools apply one evidence standard, `../methodology/evidence-standard.md`: an artifact is Verified when its content was supplied and reviewed in session, and a description of an artifact held elsewhere is a representation. Machine-enforceable definitions of the six payloads live in [`../schemas/`](../schemas/): `pipes-mapper-output`, `switch-registry-output`, `exit-prover-output`, `treasury-reroute-plan`, `data-switchboard-plan` and `clean-market-exit` (JSON Schema draft 2020-12).

## Primitives in the suite

The five primitives are defined in [`../methodology/glossary.md`](../methodology/glossary.md). The suite works on a narrower form of each. The narrowing is deliberate and is stated here so that no suite output is read as the full primitive.

| Primitive | Glossary definition (short) | How the suite narrows it |
|---|---|---|
| Services | A critical service: an outcome for a defined customer or stakeholder whose disruption beyond an approved level causes material harm | The suite's unit is the product, system or region in scope, mapped to the critical service it supports |
| Tolerances | The maximum tolerable disruption to a critical service, approved by an authority with standing to accept the risk | The tolerance is the service's own `tolerance_hours` from the service dossier, not a constant; when none is supplied, feasibility is Unknown |
| Pipes | A dependency through which a service is delivered: people, process, technology, data, facilities, providers, jurisdictions and their interconnections | Pipes Mapper registers source-to-destination dependency edges; people, facilities and jurisdictions enter as attributes of an edge, not as nodes |
| Switches | An authorized action that alters, pauses, isolates, reroutes, degrades, substitutes, recovers or stops service delivery | Switch Registry holds two-state switches (ON/OFF), while the Copilot's switches include actions without a stable two-state form (reroute, degrade, manual process); the two are linked by a shared `switch_id`, and the Copilot's switch catalog carries an optional `registry_switch_id` column |
| Exits | A predesigned path for leaving or replacing a dependency while keeping the service | Exit Prover tests an exit from a defined commitment; the Clean Market Exit Kit's exit is leaving a market, the narrowest case of the glossary's exit |

## Registry stewardship (read before first use)

The model-agnostic environment has no persistence. The audit trail survives only if the user saves every re-emitted registry, log and plan externally (repo, Sheet, document store) and pastes the current state back at the next session start. Each prompt enforces full-state re-emission and instructs the user to save; the discipline of doing so is the user's.

## Relationship to the Copilot

The Copilot assesses whether optionality exists. This suite operates the machinery the Copilot assesses. Both enforce the same evidence rules, house style and license (see repo root [`LICENSE`](../LICENSE)).

## Shared conventions

Evidence classification (Verified / Provisional / Not evidenced / Contradicted / Refuted / Not applicable). Unknown / Insufficient data for missing facts. Suite verdict scale for Exit Prover and Clean Market Exit Kit: Demonstrated / Conditionally Demonstrated / Not Demonstrated, the scale the Copilot's readiness decision uses. POTENTIAL HALLUCINATION for unsupported claims. GRCnext™ always one closed word with the trademark symbol. Governance, risk management and compliance always in full. No em dashes, no Oxford comma, US English. Status labels [↻ draft] / [⇥ pending review] / [✓ final]; end tags ✅ / ❌ / ❓; ⧉ single largest gap; ⚠ external counsel. All substantive outputs close with:

Final Liability rests with the Human.
