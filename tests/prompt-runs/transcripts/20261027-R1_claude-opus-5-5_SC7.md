# SC7 the clock starts at onset, not at detection

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** f420fcae72bddb1bd0b89c61a7d6b3cd4b8106f81819ee9e119c78f026fe4f78  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8952  **Output tokens:** 2795
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the clock start, the clock stop, the elapsed time, the tolerance result and the readiness decision.

- Approved impact tolerance: four hours.
- Disruption begins at 02:00. Nobody notices until 04:00. The service is verified stable on an alternate path at 07:00.
~~~~

## Assistant response

# Service B: Tolerance and Readiness Determination [⇥ pending review]

**Mode:** Assessment (limited to the tolerance result and the readiness decision)

## Result

| Item | Determination |
|---|---|
| Clock start | **02:00**, at the onset of disruption |
| Clock stop | **07:00**, when the service was verified stable on the alternate path |
| Elapsed time | **5 hours** |
| Approved impact tolerance | 4 hours (tolerance limit reached at 06:00) |
| Tolerance result | **Not Met** (exceeded by 1 hour) |
| Readiness decision | **Not Demonstrated** |

## Basis

**Clock start.** The clock starts when the service first falls outside its normal level of delivery, whether or not anyone has noticed. Disruption began at 02:00. Detection at 04:00 is not the clock start. It ends the Detect phase.

**Clock stop.** The clock stops at verified stabilization of the service at or above its tolerance level. The record states the service was verified stable on an alternate path at 07:00.

**Elapsed time by phase.**

| Phase | Interval | Duration |
|---|---|---|
| Detect | 02:00 to 04:00 | 2 hours |
| Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize | 04:00 to 07:00 | 3 hours combined |
| **Total** | 02:00 to 07:00 | **5 hours** |

The record does not split the 3-hour post-detection interval into individual phases. That breakdown is Unknown / Insufficient data.

**Readiness decision.** Under decision cap F4, a tolerance result of Not Met makes the decision Not Demonstrated. This is true regardless of how the other seven core gates would score. Gate 7 (evidence demonstrates whether the tolerance was met) is a **Pass**: the evidence answers the question, and the answer is no.

## The measurement trap this avoids

If the clock were started at detection, the elapsed time would be 3 hours and the result would appear to be Met. That would be a false pass. The two undetected hours were real service harm to Service B's customers. They count.

## Binding constraint

⧉ **Binding constraint: the Detect phase**, in the governing scenario of an unnoticed disruption beginning outside staffed hours.

Two hours of undetected disruption consumed half the four-hour tolerance. That left 2 hours for a response that took 3. With the response performance actually observed, cutting detection to under 1 hour would have kept the service within tolerance. The response window still deserves scrutiny, because its phase breakdown is not evidenced.

## Evidence classification

| Claim | Status | Limitation |
|---|---|---|
| Tolerance approved at 4 hours | Verified (per the user's designation of this record as reviewed evidence) | The approving authority and approval record are not identified |
| Onset at 02:00 | Verified (as above) | The observable onset event and its source (monitoring record, log, customer report) are not named |
| Detection at 04:00 | Verified (as above) | The detection mechanism is not stated |
| Verified stable at 07:00 | Verified (as above) | The verification method and the stabilization criterion are not stated |

The record also does not say whether this was an actual event (T4) or an exercise. The exercise tier is therefore Unknown. This does not change the tolerance result or the decision.

## What cannot be concluded from this record

- **Domain scores and Constraint Level.** These are Unknown / Insufficient data. No evidence on Pipes, Switches or Exits was supplied.
- **Evidence confidence.** This is Moderate at best, pending the source artifacts behind each timestamp.
- **Gates 1 to 6 and gate 8.** These are Unknown. They do not affect the outcome, because the Not Met result already fixes the decision at Not Demonstrated.

## Priority actions

1. **Close the detection gap.** Define the observable onset event for Service B, then instrument monitoring and out-of-hours alerting so detection falls well inside 1 hour. *Acceptance test:* a controlled T2 test in which injected degradation is detected and alerted within the target time. *Evidence:* alert logs with timestamps.
2. **Decompose the 04:00 to 07:00 window.** Reconstruct timestamps for Interpret, Decide, Authorize, Execute, Verify, Communicate and Stabilize from tickets, logs and decision records. *Acceptance test:* every phase has a sourced timestamp. *Evidence:* a timeline with artifact references.
3. **Open a corrective-action record and schedule a retest.** Assign a named owner and target date, then retest the end-to-end path (T3) against the 4-hour tolerance measured from onset.

**[Purpose]** Determine the clock events, elapsed time, tolerance result and readiness decision for Service B from the supplied record.

**[Decisions Made]** Clock start 02:00 at onset. Clock stop 07:00 at verified stabilization. Elapsed time 5 hours. Tolerance Not Met. Readiness Not Demonstrated. Binding constraint is the Detect phase.

**[Outstanding Items]** Source artifacts for each timestamp. Event type and exercise tier. Phase breakdown of the 3-hour response window. Domain evidence needed to score the capability profile and Constraint Level. Owners for the corrective actions.

**Decision required now:** The accountable owner of Service B must accept the breach on record and approve the detection remediation as the first corrective action.

> Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
