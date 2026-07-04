# GRCnext™ Advisory Tools Suite - Model-Agnostic Prompts

**Suite version:** 1.0 [↻ draft] · **Repo:** GRCnext™ Copilot v2.1.0 · **Source design:** MindStudio design brief (rolldabones/wip)

Six standalone system prompts implementing the Pipes, Switches, Exits methodology and the 72-hour execution model in any frontier chat model. Each file is self-contained: paste one prompt into a Claude Project's custom instructions, a Custom GPT's instructions field, a Gemini Gem or any comparable system-prompt slot. No plugins, code execution, browsing, memory or vendor features are assumed.

| File | Tool | Function |
|---|---|---|
| [01-pipes-mapper.md](01-pipes-mapper.md) | Pipes Mapper | Dependency Registry: maps critical processes, data flows and dependency chains |
| [02-switch-registry.md](02-switch-registry.md) | Switch Registry | Registry and append-only log of switches; VIEW / FLIP / NEW / ADVISE / EXPORT modes |
| [03-exit-prover.md](03-exit-prover.md) | Exit Prover | Tests exit readiness; PASS / PROVISIONAL PASS / FAIL proof with gap analysis |
| [04-treasury-reroute-planner.md](04-treasury-reroute-planner.md) | Treasury Reroute Planner | Plan B for financial pipes; masked identifiers; plans only, never executes |
| [05-data-switchboard-planner.md](05-data-switchboard-planner.md) | Data Switchboard Planner | Reroute, isolate or sever data flows; compliance checklist mapping |
| [06-clean-market-exit-kit.md](06-clean-market-exit-kit.md) | Clean Market Exit Kit | Orchestrator; merges all outputs into one T0 to T+72h master playbook |

## Translation from MindStudio

| MindStudio construct | Model-agnostic equivalent |
|---|---|
| Detect PII block | Confidentiality gate in each prompt: warn once, substitute neutral labels, redact in outputs, proceed |
| Checkpoint block | CHECKPOINT gates: stop and obtain explicit user confirmation before committing |
| Google Sheets persistence | Paste-in/paste-out registry protocol: user supplies current state, tool always re-emits the full updated registry with a version timestamp and change log |
| Create Google Doc | Board-ready markdown report section in every output |
| Run Workflow (sub-workflow reuse) | JSON interchange contract: each tool emits a `tool`-tagged JSON that downstream tools validate and consume |
| Run Function (custom code) | Explicit arithmetic shown in-line (limit checks, 72h summation) using only user-supplied figures |
| Logic / Loop blocks | Numbered workflow steps in each prompt |

## Interchange contract

Every tool emits JSON with a `tool` field and an ISO 8601 version timestamp. Consumption map:

- pipes_mapper → Exit Prover, Data Switchboard Planner, Clean Market Exit Kit
- switch_registry → Exit Prover, Treasury Reroute Planner, Data Switchboard Planner, Clean Market Exit Kit
- exit_prover → Clean Market Exit Kit
- treasury_reroute_planner → Clean Market Exit Kit
- data_switchboard_planner → Exit Prover, Clean Market Exit Kit

Every tool runs in degraded standalone mode when upstream JSON is absent; findings gathered by interrogation are Provisional and verdicts are capped accordingly.

Machine-enforceable definitions of the six payloads live in [`../schemas/`](../schemas/): `pipes-mapper-output`, `switch-registry-output`, `exit-prover-output`, `treasury-reroute-plan`, `data-switchboard-plan` and `clean-market-exit` (JSON Schema draft 2020-12).

## Registry stewardship (read before first use)

The model-agnostic environment has no persistence. The audit trail survives only if the user saves every re-emitted registry, log and plan externally (repo, Sheet, document store) and pastes the current state back at the next session start. Each prompt enforces full-state re-emission and instructs the user to save; the discipline of doing so is the user's.

## Relationship to the Copilot

The Copilot assesses whether optionality exists. This suite operates the machinery the Copilot assesses. Both enforce the same evidence rules, house style and license (see repo root [`LICENSE`](../LICENSE)).

## Shared conventions

Evidence classification (Verified / Provisional / Not demonstrated / Contradicted / Refuted / Not applicable). Unknown / Insufficient data for missing facts. POTENTIAL HALLUCINATION for unsupported claims. GRCnext™ always one closed word with the trademark symbol. Governance, risk management and compliance always in full. No em dashes, no Oxford comma, US English. Status labels [↻ draft] / [⇥ pending review] / [✓ final]; end tags ✅ / ❌ / ❓; ⧉ single largest gap; ⚠ external counsel. All substantive outputs close with:

**Final Liability rests with the Human.**
