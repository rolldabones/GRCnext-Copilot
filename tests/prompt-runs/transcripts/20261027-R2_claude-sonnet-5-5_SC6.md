# SC6 the full profile is reported, never collapsed

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 4c06cbdaaab28d89467ce18b8f360841b00fddb3fcff64a96cc4393c28e4b03b  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9279  **Output tokens:** 7547
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

# GRCnext™ Assessment: Service B [↻ draft]

**Scope and assumptions.** One critical service (Service B), assessed on the supplied record only. The record gives no jurisdictions, evidence cut-off date, accountable owner name or phase-by-phase timings, so these are Unknown / Insufficient data. I treat the stated domain scores and timing records as reviewed and verified. I have not seen the underlying artifacts, so I draw no legal conclusion on the enforceability of the exit rights.

## 1. Capability profile

| Domain | Score |
|---|---|
| Services and tolerances | L3 |
| Pipes | L3 |
| Switches | L3 |
| Exits | L2 |
| Exercises | L3 |
| Evidence and improvement | L3 |

No averaging is applied. Exits at L2 is the one weak domain. It is consistent with the record: the exit is documented and contractually secured but never exercised, and an untested design cannot earn L3. Evidence and improvement cannot reach L4 while a corrective action is overdue, because L4 requires closed corrective-action loops.

## 2. Constraint Level and binding constraint

- **Constraint Level: 2.** This is the minimum of Pipes (3), Switches (3) and Exits (2), so the weakest structural component is Exits.
- **Binding constraint: readiness gate 5, the priority exit for the leading concentration dependency.**
  - **Scenario:** loss of the primary provider, handled by the reroute switch.
  - **Basis:** the reroute is evidenced within tolerance, but replacing the failed provider durably depends on an exit that is designed and secured in writing yet unrehearsed, so no execution time exists for it.
- The Constraint Level and the binding constraint coincide here. That is a finding about Service B, not a rule of the method. The record has no phase-by-phase timings, so I cannot name a limiting clock phase.

⧉ **Largest gap:** the priority exit has never been rehearsed.

## 3. Evidence confidence: Moderate

- Evidence for the governing reroute path is strong. It is a T3 end-to-end rehearsal with current timing records.
- Overall confidence is held to Moderate by limited testing of the exit and by an open overdue corrective action.
- The record does not say whether the rehearsal evidence was independently verified.

## 4. Tolerance result: Met

- **Clock start:** onset of disruption at 09:00.
- **Clock stop:** verified stabilization at 17:00.
- **Elapsed:** 8 hours against an approved 12-hour tolerance, leaving 4 hours of headroom.
- **Scope of the result:** it applies to the rehearsed reroute path only. Nothing evidences the exit against any tolerance.
- **Live-event caveat:** a rehearsal onset is known by design. In a live event the onset-to-detection interval may be longer, and that interval would consume the 4-hour headroom. The record gives no phase split to test this.

## 5. Gate results

| Gate | Result | Basis |
|---|---|---|
| 1 Service and owner defined | Pass | Domain 1 at L3 in the reviewed record. The owner's name is not reproduced in this record. |
| 2 Tolerance approved and measurable | Pass | Approved 12-hour tolerance, with start and stop events measured in the rehearsal. |
| 3 Dependencies mapped | Pass | Pipes at L3. |
| 4 Authority to invoke switches | Pass | Reroute was invoked end to end at T3, so authorization was exercised on that path. Out-of-hours authority is not itemized. |
| 5 Executable exit for leading concentration | Provisional Pass | Rights, transition assistance and a substitute are in writing. Executability is unproven because there has been no rehearsal. |
| 6 Severe but plausible exercise of governing scenario | Pass | T3 end-to-end rehearsal. |
| 7 Evidence shows whether tolerance was met | Pass | Current timing records show it was met. |
| 8 Material corrective actions have owners and target dates | Provisional Pass | The overdue status implies a target date existed. The owner and materiality are not stated. |

## 6. Readiness decision: Conditionally Demonstrated

- No gate fails and the tolerance result is Met, so the decision is not Not Demonstrated.
- It cannot be Demonstrated. Gates 5 and 8 are Provisional Pass, and under decision cap 2 each caps the decision until its evidence-conversion action closes.
- The reroute capability for the governing scenario is evidenced. The durable exit behind it is not.

## 7. Priority actions

1. **Rehearse the priority exit.**
   - **Scope:** a T2 test of components, then a T3 rehearsal, since a T3 supports L3 only for the path exercised.
   - **Acceptance test:** an agreed exit target time is met, data is retrieved in usable form and the substitute carries Service B at or above its tolerance level.
   - **Evidence:** an exercise record with elapsed time by phase and an evidence pack.
   - **Owner:** Unknown, to be named by the human decision-maker.
   - **Proposed target:** within 90 days.
   - **Clears:** gate 5, the Exits ceiling and the binding constraint.
2. **Close or formally re-baseline the overdue corrective action.**
   - **Acceptance test:** the owner and materiality are confirmed, and closure is verified by independent check or the revised date is approved.
   - **Clears:** gate 8.
3. **Capture the phase split of the 8-hour result.**
   - **Scope:** a timing record by clock phase, plus an evidenced bound on the live onset-to-detection interval.
   - **Purpose:** to confirm the 4-hour headroom survives live conditions.

## 8. ESCALATE

**ESCALATE: overdue corrective action.**
- **Issue:** one corrective action is past its target date.
- **Consequence:** it holds gate 8 at Provisional Pass and blocks L4 for Evidence and improvement.
- **Facts required:** owner, materiality, original and revised dates, and the cause of the slippage.
- **Interim control:** the accountable executive reviews the action weekly until it closes.
- **Decision owner:** senior management. The name is Unknown.

## 9. Decisions required

- Name the exit rehearsal owner and approve the rehearsal date.
- Decide whether to accept Conditionally Demonstrated for Service B until the exit is rehearsed.
- Decide the disposition of the overdue action: close or re-baseline.

**[Purpose]** Assess Service B's optionality against the reviewed record.
**[Decisions Made]** None are final. The readiness decision is Conditionally Demonstrated, pending human acceptance.
**[Outstanding Items]** The exit rehearsal. The overdue action's owner and materiality. The phase-by-phase timings. The jurisdictions and evidence cut-off date.

✅ complete

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
