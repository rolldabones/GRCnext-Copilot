# SC1 the minimum rule and the exit gate both bite

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** a8d2b014da6b287f91602fe69c3fe89ffcf3cebdcf586b047a40c99cbda306b8  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9257  **Output tokens:** 8237
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the developed assessment: the capability profile, the Constraint Level and binding constraint, the evidence confidence, the gate results, the tolerance result and the readiness decision.

- Service and owner defined. Impact tolerance approved and measurable.
- Pipes: end-to-end dependency map current, concentrations identified. Strong.
- Switches: reroute switch delegated, tested at T3, executed within tolerance in the rehearsal. Strong.
- Exits: a written exit plan for the leading concentration dependency exists. No transition assistance secured, no substitute qualified, no rehearsal. Described only.
- Exercises: the reroute rehearsal was T3. Evidence current.
~~~~

## Assistant response

# GRCnext™ Developed Assessment: Service B [↻ draft]

Do not paste secrets, credentials, protected personal data or unnecessary confidential detail into this engagement. Keep neutral labels such as Vendor A and Jurisdiction X.

## 1. Scope and assumptions

- **Service:** Service B. Owner and approved, measurable impact tolerance are recorded as defined.
- **Evidence basis:** the facts you supplied, treated as the reviewed record. No artifact IDs, dates, source locations or tolerance values were supplied. Those fields are Unknown / Insufficient data.
- **Assumption 1:** the governing severe but plausible scenario is loss of, or an unacceptable condition in, the leading concentration dependency. The record does not name the scenario. If it is narrower, gates 5 and 6 should be re-run.
- **Assumption 2:** the reroute switch is the near-term response to that scenario. The exit is the longer-term response.

## 2. Executive scorecard

| Result | Finding |
|---|---|
| Readiness decision | **Not Demonstrated** |
| Constraint Level | **1** (Exits) |
| Binding constraint | Gate 5 in the Execute-to-Stabilize phases. Basis: the leading concentration dependency has a written exit plan but no transition assistance, no qualified substitute and no rehearsal, so the exit cannot be shown to run within tolerance. |
| Evidence confidence | **Moderate** |
| Tolerance result | **Cannot Determine** |

⧉ Largest risk: Service B has a strong, exercised short-term switch but no executable exit for its leading concentration dependency. If the dependency stays unacceptable beyond what the reroute can bridge, the organization has no demonstrated way out.

## 3. Capability profile

| Domain | Score | Basis |
|---|---|---|
| 1. Services and tolerances | L2 Designed (provisional) | Owner defined and tolerance approved and measurable. The record does not confirm that the clock starts at onset or that assumptions are documented. L3 is available once those are verified. |
| 2. Pipes | L3 Exercised | Map is current and concentrations are identified. The mapped path was exercised through the T3 rehearsal. No monitoring or metrics evidence supports L4. |
| 3. Switches | L3 Exercised | Reroute is delegated, tested at T3 and executed within tolerance. T3 supports L3 for the path exercised only. L4 needs monitoring, current metrics and closed corrective-action loops, which are not evidenced. |
| 4. Exits | L1 Described | Written plan only. No transition assistance, no qualified substitute, no rehearsal. |
| 5. Exercises | L2 Designed | One current T3 rehearsal covers the reroute path. The exit path is untested, and the record does not show documented remediation or retest. The reroute path alone would support L3. |
| 6. Evidence and improvement | Unknown / Insufficient data | Only exercise evidence freshness is stated. Artifact ownership, decision records, corrective actions and closure verification are not in the record. Unscored, not scored zero. |

The weakness in Exits is shown separately and not averaged into the other scores.

## 4. Constraint Level and binding constraint

- **Constraint Level:** minimum of Pipes (3), Switches (3) and Exits (1) is **1**. Exits is the weakest structural component.
- **Binding constraint:** Gate 5, which limits the Execute and Stabilize phases for the exit in the governing scenario. Here the structural and operational constraints point to the same place. They are separate findings, and the binding constraint should be re-evaluated as Exits improves.

**Stress-test question that could change the picture:** what does the reroute route to? If the reroute target depends on the substitute that has not been qualified, or on the same concentration dependency, the Switches score is overstated for this scenario. Please confirm.

## 5. Evidence confidence: Moderate

Moderate fits because the evidence is current and coherent, and the reroute was executed in a T3 rehearsal. Three things keep it from High:

- Independent verification is not stated.
- The clock events and phase timings behind "within tolerance" are not stated.
- The Evidence and improvement domain is empty in the record.

For the exit path, confidence would be Low, since it rests on a written plan alone.

## 6. Gate results

| # | Gate | Result | Basis |
|---|---|---|---|
| 1 | Critical service and owner defined | Pass | Recorded as defined. |
| 2 | Impact tolerance approved and measurable | Pass | Recorded as approved and measurable. |
| 3 | Material dependencies mapped | Pass | Current map, concentrations identified. Fourth-party and recovery dependency coverage is not stated. |
| 4 | Authority to invoke essential switches | Pass | Reroute is delegated and was executed in the T3 rehearsal. Out-of-hours availability and decision authority for the exit are not in the record. |
| 5 | Executable exit for leading concentration dependency | **Fail** | Written plan only. No transition assistance, no qualified substitute, no rehearsal. Not executable. |
| 6 | Severe but plausible exercise of governing scenario | Provisional Pass | The T3 rehearsal covered the reroute part of the scenario only. The exit was not exercised, which is partial coverage under the gate definition. Conversion action: exercise the exit path. |
| 7 | Evidence shows whether tolerance was met | Provisional Pass | Evidence shows the reroute met tolerance in rehearsal. The clock start and stop events are not stated, and the exit path has no timing evidence. Conversion action: obtain the rehearsal timeline from onset to verified stabilization. |
| 8 | Material corrective actions have owners and target dates | Unknown | No corrective-action record was supplied. The exit gaps above are material findings and need entries. |

## 7. Tolerance result: Cannot Determine

- **Clock start:** not stated. Service B needs a named, observable onset event, meaning the moment delivery first falls outside its normal level, not the moment of detection.
- **Clock stop:** not stated. It should be verified stabilization of Service B at or above its tolerance level.
- **Pre-detection interval:** Unknown. A rehearsal with an injected event cannot bound it, so a Met result needs an evidenced bound.
- **Reroute path:** executed within tolerance in rehearsal. This is promising but not a Met result until both clock events and the full-clock phases (Detect through Stabilize, including Authorize and Communicate) are confirmed.
- **Exit path:** Not Tested.

## 8. Readiness decision: Not Demonstrated

- A Fail on gate 5 makes the decision Not Demonstrated (cap F4).
- Gate 8 is Unknown, which independently prevents Demonstrated (cap F1).
- Gates 6 and 7 are Provisional Passes, which would cap the decision at Conditionally Demonstrated at best (cap F2).
- A tolerance result of Met with both clock events stated is required for Demonstrated and is absent (cap F5).

**What can be concluded:** Service B has demonstrated, executable optionality for the reroute switch in the rehearsed path. **What cannot be concluded:** that Service B can leave its leading concentration dependency.

## 9. Prioritized actions (proposed 90-day sequence)

Owners are not in the record and should be named by the accountable service owner. Target periods are proposals.

| Priority | Action | Acceptance test | Evidence required | Proposed period |
|---|---|---|---|---|
| 1 | Open a corrective-action register covering the exit gaps, with owners and dates (gate 8). | Every material gap has a named owner and target date. | Register extract with version and approver. | Days 0 to 15 |
| 2 | Convert gate 7 evidence: reconstruct the rehearsal timeline against the clock phases, naming the onset and stop events. | Elapsed time per phase from onset to verified stabilization is documented and compared to tolerance. | Rehearsal log, decision records and timestamps. | Days 0 to 30 |
| 3 | Secure transition assistance for the leading concentration dependency, including data return in usable form. | Terms are executed or confirmed in writing and their timing fits the exit target. | Executed amendment or provider confirmation. | Days 0 to 60 |
| 4 | Qualify a substitute for the dependency. | Substitute passes defined qualification criteria and a capacity test at required volume. | Qualification record and test results. | Days 15 to 90 |
| 5 | Run a T2 component test of the exit steps, then plan a T3 exit rehearsal against tolerance. | Exit steps execute within the target time. Full clock is captured, with simulated and performed actions stated. | Exercise record, timings and findings with retest status. | T2 by day 90, T3 after substitute qualification |
| 6 | Confirm what the reroute routes to, and confirm out-of-hours availability of delegates. | Written confirmation that the reroute target is independent of the leading concentration dependency. | Dependency map extract and delegation roster. | Days 0 to 30 |

## 10. Decisions required

1. The Service B owner must accept or reject the Not Demonstrated position and fund actions 3 and 4.
2. The owner must name the governing scenario so that gates 5 and 6 can be fixed against it.
3. The owner must name the clock onset and stop events for the exit and for the reroute.

## 11. Escalation

**ESCALATE: contractual rights and transition assistance** ⚠
- **Issue:** transition assistance is not secured. The contractual exit rights, governing law and forum are not in the record.
- **Operational consequence:** if the provider has no obligation to assist, exit timing cannot be assumed.
- **Facts and evidence required:** the contract, governing law, termination windows, notice terms and any dispute status.
- **Interim control:** treat the exit as non-executable and rely on the reroute only.
- **Decision owner:** Service B owner with procurement and legal.
- **Questions for counsel:** what assistance and data-return obligations apply, and what notice is required to trigger them?

**ESCALATE: exit decision authority**
- **Issue:** no named decision-maker for invoking the exit appears in the record.
- **Operational consequence:** the Authorize phase of the exit clock is unbounded.
- **Interim control:** the service owner holds the decision until a delegation is documented.
- **Decision owner:** senior management.

## 12. Outstanding information

- The impact tolerance value and the observable onset event.
- The governing scenario, and what the reroute routes to.
- Corrective-action records, evidence owners and version control.
- Evidence IDs, dates and source locations, so a full evidence ledger can be built.

[Purpose] Developed assessment of Service B against the GRCnext™ gates, domains and decision caps.
[Decisions Made] Readiness decision Not Demonstrated. Constraint Level 1 (Exits). Evidence confidence Moderate. Tolerance result Cannot Determine.
[Outstanding Items] Confirm scenario, clock events and reroute target. Open the corrective-action register. Secure transition assistance and qualify a substitute. Rehearse the exit. Resolve both ESCALATE items.

Final Liability rests with the Human.

❓ needs input

<!-- end of transcript; written by tests/run_prompt_cases.py -->
