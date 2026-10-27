# SC6 the full profile is reported, never collapsed

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 4c06cbdaaab28d89467ce18b8f360841b00fddb3fcff64a96cc4393c28e4b03b  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 9107  **Output tokens:** 6858
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the capability profile, the Constraint Level and binding constraint, the evidence confidence, the tolerance result and the readiness decision.

- Domain scores, in the order of the capability model: Services and tolerances 3, Pipes 3, Switches 3, Exits 2, Exercises 3, Evidence and improvement 3.
- The governing scenario (loss of the primary provider, handled by the reroute switch) was rehearsed end-to-end at T3: onset at 09:00, verified stabilization at 17:00, against an approved twelve-hour tolerance. Timing records are current.
- The priority exit is designed: exit rights, transition assistance and a substitute are secured in writing. The exit has not been rehearsed.
- One corrective action is overdue.
~~~~

## Assistant response

# GRCnext™ Assessment: Service B [⇥ pending review]

**Basis:** The supplied facts are treated as the reviewed evidence record. Governing scenario: loss of the primary provider, handled by the reroute switch. Assessment date, evidence cut-off date and jurisdictions were not supplied (Unknown / Insufficient data).

## 1. Results

| Result | Finding |
|---|---|
| **Capability profile** | Services and tolerances 3 (L3), Pipes 3 (L3), Switches 3 (L3), Exits 2 (L2), Exercises 3 (L3), Evidence and improvement 3 (L3) |
| **Constraint Level** | **2**, set by Exits (minimum of Pipes 3, Switches 3, Exits 2) |
| **Binding constraint** | Gate 5, an executable exit for the leading concentration dependency. In the loss-of-primary-provider scenario the reroute switch held the tolerance, but the exit that would replace the provider is written and unrehearsed, so its executability is not shown. |
| **Evidence confidence** | **Moderate** |
| **Tolerance result** | **Met** |
| **Readiness decision** | **Conditionally Demonstrated** |

The Constraint Level and the binding constraint coincide here, but they are different findings. The Constraint Level is the maturity diagnostic. The binding constraint names the gate that limits the decision.

## 2. Basis for each result

**Capability profile.** No domain is scored L4, and nothing in the record shows monitoring, current metrics or closed corrective-action loops. The L3 scores for Switches and Exercises apply to the reroute path exercised and to no other path (cap F8). Exits at L2 Designed fits the record. The arrangements are documented and secured, but none has been exercised. A T3 rehearsal of the reroute cannot lift the exit score.

**Tolerance result.**
- Clock start: onset of disruption at 09:00.
- Clock stop: verified stabilization at 17:00.
- Elapsed time: 8 hours against an approved 12-hour tolerance, a 4-hour margin.
- Result: Met, with both clock events stated and current timing records.

Three limits apply:
- The result covers a T3 rehearsal, not a live event.
- It covers the reroute path only, not the exit.
- Phase timings (Detect through Stabilize) were not supplied, so I cannot say which phase consumed the most of the 8 hours. The margin is therefore not yet decomposable (Unknown).

**Evidence confidence.** Evidence for the reroute path is strong: executed T3 performance with current timing records. Confidence is held at Moderate for three reasons:
- The exit is documented but untested.
- One corrective action is overdue, and its details are not in the record.
- The record does not say whether the rehearsal evidence was independently observed.

**Readiness decision.** Two caps hold the decision below Demonstrated:
- Gate 5 is a Provisional Pass. Cap F2 limits the decision to Conditionally Demonstrated until the evidence-conversion action closes.
- Gate 8 is Unknown. Cap F1 prevents Demonstrated.

Not Demonstrated would require a Fail on a core gate or a tolerance result of Not Met, and neither is present. The record does not support that outcome.

## 3. Readiness gates

| Gate | Classification | Basis |
|---|---|---|
| 1. Service and owner defined | Pass | Services and tolerances at L3. The record does not itemize the named owner. |
| 2. Tolerance approved and measurable | Pass | Twelve-hour tolerance approved; timing records current. |
| 3. Dependencies mapped | Pass | Pipes at L3. The record treats the primary provider as the leading concentration dependency. |
| 4. Authority to invoke essential switches | Pass | Reroute was invoked end to end in the T3 rehearsal. |
| 5. Executable exit for leading concentration dependency | **Provisional Pass** | Exit rights, transition assistance and a substitute are secured in writing (Verified as documents). Executability is Not evidenced because the exit has not been rehearsed. |
| 6. At least one severe but plausible exercise | Pass | T3 end-to-end rehearsal of the governing scenario. |
| 7. Evidence shows whether tolerance was met | Pass | 8 hours against 12, current timing records. |
| 8. Corrective actions have owners and target dates | **Unknown** | One action is overdue. Its owner, target date, materiality and escalation status are not in the record. |

Gate 8 is the most consequential unknown. If the overdue action lacks an owner or target date, the gate becomes a Fail and the decision becomes Not Demonstrated under cap F4. If the action bears on the reroute path or the exit, it also weakens the Moderate confidence rating.

**Finding classification:**
- Reroute performance within tolerance: **Verified**.
- Written exit arrangements: **Verified** as documents.
- Enforceability of those arrangements: **Not evidenced**. The governing law was not supplied, so no legal conclusion is drawn.
- Exit executability: **Not evidenced**.
- Overdue action: **Unknown / Insufficient data**.

⧉ **Single largest gap:** The priority exit has never been executed, so there is no evidence it can be completed within any tolerance, including data retrieval in usable form and substitute capacity at the required service level.

## 4. Prioritized actions

| # | Action | Acceptance test | Evidence required | Proposed target period |
|---|---|---|---|---|
| 1 | Rehearse the priority exit. Test components at T2 first (data retrieval, substitute onboarding), then run the full path at T3. | Exit completed with the full clock captured; substitute stabilizes the service at or above tolerance level; data retrieved in usable form. | Exercise record, timing by phase, simulated-versus-performed split, findings. | Within 90 days (proposal, subject to owner confirmation) |
| 2 | Resolve the overdue corrective action. Confirm owner, original and revised target date and materiality. Escalate if it touches the reroute or exit path. | Action closed with verification, or re-baselined with a named owner and approved date. | Action register entry, closure verification, escalation record. | Immediate confirmation of facts; closure date set by the owner |
| 3 | Obtain the phase-by-phase timing of the T3 rehearsal. | Elapsed time documented for Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate and Stabilize. | Timing log. | Within 30 days |

Owners are not named in the record and I have not invented any.

## 5. Decisions required

1. Whether senior management accepts a Conditionally Demonstrated position for Service B pending exit rehearsal.
2. Who authorizes and resources the exit rehearsal, and who is the accountable decision-maker for it.
3. Whether the overdue action needs escalation.

No ESCALATE item arises on the supplied facts. Counsel review of exit-right enforceability becomes necessary if the governing law or any live dispute is later identified.

## 6. Closing blocks

**[Purpose]** Assess Service B against the GRCnext™ readiness model from the supplied evidence record.

**[Decisions Made]**
- Constraint Level set at 2 (Exits).
- Binding constraint set as Gate 5.
- Evidence confidence rated Moderate.
- Tolerance result Met (8 hours against 12).
- Readiness decision Conditionally Demonstrated.

**[Outstanding Items]**
- Owner, target date and materiality of the overdue corrective action (Gate 8).
- Exit rehearsal (Gate 5 evidence conversion).
- Phase timings of the T3 rehearsal.
- Independent observation status of the rehearsal.
- Assessment date, evidence cut-off date and governing law.

Final Liability rests with the Human.

❓ needs input

<!-- end of transcript; written by tests/run_prompt_cases.py -->
