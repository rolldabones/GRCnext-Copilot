# SC6 the full profile is reported, never collapsed

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 4c06cbdaaab28d89467ce18b8f360841b00fddb3fcff64a96cc4393c28e4b03b  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9279  **Output tokens:** 5214
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

**Mode:** Assessment. **Scope:** Service B only. **Evidence basis:** The facts you supplied, treated as the reviewed evidence record. No other artifacts were examined.

## 1. Capability profile

| Domain | Score | Basis |
|---|---|---|
| Services and tolerances | L3 Exercised | Approved twelve-hour tolerance, exercised in the governing scenario |
| Pipes | L3 Exercised | Provider dependency exercised through the T3 rehearsal |
| Switches | L3 Exercised | Reroute switch performed end-to-end at T3 |
| Exits | L2 Designed | Rights, transition assistance and substitute secured in writing, not rehearsed |
| Exercises | L3 Exercised | T3 rehearsal of the governing scenario. Under the T3 tier cap, this credit covers only the reroute path. |
| Evidence and improvement | L3 Exercised | Current timing records. One overdue corrective action keeps this domain below L4. |

No averaging is applied. The Exits score is the visible weakness.

## 2. Constraint Level and binding constraint

**Constraint Level: L2.** This is the minimum of Pipes 3, Switches 3 and Exits 2. Exits sets it.

**Binding constraint:** Gate 5, the executable exit for the leading concentration dependency.
- **Governing scenario:** Loss of the primary provider, handled by the reroute switch.
- **Basis:** The reroute path met tolerance with a four-hour margin, so no clock phase binds on this evidence. The priority exit is the only remaining path if provider loss becomes permanent or the reroute is unavailable, and its executability has not been shown.

**Clock phases:** The record gives only total elapsed time. Phase durations are Unknown / Insufficient data. This does not change the binding constraint, but it hides how much of the margin each phase consumes.

## 3. Evidence confidence: Moderate

- **Reroute path: High.** Executed T3 performance and current timing records support it.
- **Priority exit: Moderate at best.** Written rights are verified design evidence, but there is no executed evidence that the exit works.
- **Corrective-action record: Incomplete.** The owner of the overdue action is not in the record.

## 4. Readiness gates

| # | Gate | Result | Note |
|---|---|---|---|
| 1 | Service and owner defined | Pass | Supported by the Services and tolerances score of L3 |
| 2 | Tolerance approved and measurable | Pass | Twelve hours, approved, measured from onset to stabilization |
| 3 | Dependencies mapped | Pass | Pipes L3, exercised |
| 4 | Authority to invoke essential switches | Pass | Reroute invoked in an end-to-end T3 rehearsal |
| 5 | Executable exit for leading concentration | **Provisional Pass** | Designed and contractually secured, never exercised |
| 6 | Severe but plausible exercise completed | Pass | T3 rehearsal of the governing scenario |
| 7 | Evidence shows whether tolerance met | Pass | Current timing records |
| 8 | Corrective actions have owners and target dates | **Unknown** | The overdue status implies a target date existed. Owner and materiality are not in the record. |

## 5. Tolerance result: Met (rehearsal)

| Element | Value |
|---|---|
| Clock start | 09:00, onset of primary provider loss (rehearsal inject) |
| Clock stop | 17:00, verified stabilization via reroute |
| Elapsed time | 8 hours against a 12-hour tolerance |
| Margin | 4 hours |

This result applies to the rehearsed reroute path at T3. It is not a live T4 result, and it says nothing about the exit path.

## 6. Readiness decision: Conditionally Demonstrated

- **Positive case:** The governing scenario was executed end-to-end within tolerance, and no core gate fails.
- **Cap from Gate 5:** Its Provisional Pass caps the decision at Conditionally Demonstrated until the exit is exercised (cap F2).
- **Cap from Gate 8:** Its Unknown status independently prevents Demonstrated (cap F1).

`⧉` **Largest gap:** The priority exit has never been exercised. Written rights and a contracted substitute are design evidence, not executability. If primary provider loss becomes permanent, Service B depends on a path with no timing evidence against tolerance.

## 7. Evidence-conversion actions

| # | Action | Acceptance test | Evidence required |
|---|---|---|---|
| 1 | Run at least a T2 exit test covering data retrieval in usable form and substitute onboarding, then a T3 exit rehearsal | Exit steps executed and timed against the exit target time. Data verified usable at the substitute. | Exercise record, timing log, data integrity check, signed hotwash |
| 2 | Confirm owner, target date and materiality of the overdue corrective action, then reset the date with approval | Named owner and approved revised date recorded in the corrective-action register | Register entry and approval record |
| 3 | Extract phase-level timings (Detect through Stabilize) from the T3 records | All eight phases timed from 09:00 onset | Annotated timing record |

**ESCALATE: Overdue corrective action.**
- **Operational consequence:** An unclosed finding may erode the four-hour margin. If the action is material, Gate 8 cannot pass.
- **Facts required:** The action's content, owner, original date and reason for slippage.
- **Interim control:** Senior management acknowledgment and a dated recovery plan.
- **Decision owner:** The Service B accountable owner.
- **Question for senior management:** Accept the slippage with a revised date, or reallocate resources to close it now?

**[Purpose]** Assess Service B readiness from the supplied evidence record.
**[Decisions Made]** Constraint Level L2. Binding constraint Gate 5. Tolerance Met (rehearsal). Confidence Moderate. Decision Conditionally Demonstrated.
**[Outstanding Items]** Exit rehearsal, overdue action owner and materiality, and phase-level timings.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
