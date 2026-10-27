# SC7 the clock starts at onset, not at detection

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** f420fcae72bddb1bd0b89c61a7d6b3cd4b8106f81819ee9e119c78f026fe4f78  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9124  **Output tokens:** 2710
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the clock start, the clock stop, the elapsed time, the tolerance result and the readiness decision.

- Approved impact tolerance: four hours.
- Disruption begins at 02:00. Nobody notices until 04:00. The service is verified stable on an alternate path at 07:00.
~~~~

## Assistant response

# Service B: Tolerance and Readiness Result [⇥ pending review]

## Result

| Element | Result |
|---|---|
| Clock start | 02:00, onset of disruption |
| Clock stop | 07:00, verified stabilization on the alternate path |
| Elapsed time | 5 hours |
| Approved impact tolerance | 4 hours |
| Tolerance result | **Not Met** (exceeded by 1 hour) |
| Readiness decision | **Not Demonstrated** |

## Basis

**Clock start.** The clock starts when the service first falls outside its normal level of delivery, whether or not anyone has noticed. Under GRCnext™, detection at 04:00 is not the clock start. The interval from 02:00 to 04:00 is the Detect phase, the first phase of the execution clock.

**Clock stop.** The clock stops at verified stabilization of the service at or above its tolerance level. The record states verified stability at 07:00.

**Elapsed time by phase.**

| Phase | Window | Duration |
|---|---|---|
| Detect | 02:00 to 04:00 | 2 hours |
| Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize | 04:00 to 07:00 | 3 hours combined. The split across phases is Unknown / Insufficient data. |
| **Total** | 02:00 to 07:00 | **5 hours** |

**Common miscount.** Starting the clock at detection would produce 3 hours and a false Met result. That calculation hides the 2-hour detection gap, and that gap is the cause of the breach.

**Readiness decision.** Decision cap F4 applies. A tolerance result of Not Met makes the decision Not Demonstrated. No other evidence can lift it.

## Binding constraint

**Detect phase, governing scenario: Service B primary-path disruption with switch to the alternate path.**

Basis: Detection used 2 of the 4 tolerance hours. The response after detection took 3 hours, which is fast but could not recover the time lost before anyone noticed.

⧉ **Largest gap:** pre-detection latency. To meet tolerance at the current post-detection speed, detection must occur within 1 hour of onset.

## What cannot be determined from this record

- **Constraint Level.** Unknown. Pipes, Switches and Exits cannot be scored from timing facts alone. The capability profile has not been scored.
- **Exercise tier.** Unknown. The record does not state whether this was a live event (T4) or a rehearsal (T2 or T3). It also does not state which actions were performed and which were simulated.
- **Gates.** Gate 2 (approved, measurable tolerance) and gate 7 (evidence shows whether tolerance was met) are Pass on this record. Gates 1, 3, 4, 5, 6 and 8 are Unknown.

## Evidence ledger (summary)

| ID | Claim | Status | Evidence-conversion action |
|---|---|---|---|
| E1 | Tolerance is 4 hours, approved | Verified, per your designation of the reviewed record | Attach the approval record and name the approving authority |
| E2 | Onset at 02:00 | Verified, per designation | Attach monitoring or system log showing first deviation |
| E3 | Detection at 04:00 | Verified, per designation | Attach the alert or incident ticket timestamp |
| E4 | Verified stable at 07:00 | Verified, per designation | Attach the stabilization verification record |

Evidence confidence: **Moderate** for the four timing points, since source artifacts are not cited. **Indeterminate** for the domain scores.

## Prioritized actions

1. **Detection latency.**
   - Action: set monitoring thresholds and alert routing so detection occurs within 1 hour of onset.
   - Acceptance test: in a T2 test, an induced disruption is alerted within 60 minutes.
   - Evidence: alert log with onset and alert timestamps.
2. **Post-detection phase timing.**
   - Action: break the 3-hour window into the phases from Interpret through Stabilize.
   - Acceptance test: each phase has a recorded start and stop.
   - Evidence: incident timeline or exercise record.
3. **Corrective action and retest.**
   - Action: open a corrective action with a named owner and target date, then retest end to end.
   - Acceptance test: a T3 rehearsal stabilizes within 4 hours of onset.
   - Evidence: exercise record with clock events stated.

## Decision required

The Service B owner must accept the 1-hour tolerance breach and approve the corrective action for detection latency. The owner is Unknown / Insufficient data.

**[Purpose]** Determine the clock events, elapsed time, tolerance result and readiness decision for Service B.
**[Decisions Made]** The clock runs from onset at 02:00 to verified stabilization at 07:00. Elapsed time is 5 hours. Tolerance is Not Met. Readiness is Not Demonstrated. The binding constraint is the Detect phase.
**[Outstanding Items]** Source artifacts for E1 to E4, the exercise tier, a phase split for 04:00 to 07:00, classification of six Unknown gates, the domain scores and the accountable owner.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
