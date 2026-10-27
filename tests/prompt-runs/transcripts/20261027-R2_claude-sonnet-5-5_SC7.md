# SC7 the clock starts at onset, not at detection

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** f420fcae72bddb1bd0b89c61a7d6b3cd4b8106f81819ee9e119c78f026fe4f78  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9124  **Output tokens:** 2384
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the clock start, the clock stop, the elapsed time, the tolerance result and the readiness decision.

- Approved impact tolerance: four hours.
- Disruption begins at 02:00. Nobody notices until 04:00. The service is verified stable on an alternate path at 07:00.
~~~~

## Assistant response

# GRCnext™ Tolerance Determination: Service B [↻ draft]

## Result

| Item | Finding |
|---|---|
| Clock start | 02:00, onset of disruption (service first falls outside normal delivery) |
| Clock stop | 07:00, verified stabilization on the alternate path |
| Elapsed time | 5 hours 0 minutes |
| Approved impact tolerance | 4 hours |
| Tolerance result | **Not Met**, exceeded by 1 hour |
| Readiness decision | **Not Demonstrated** |

## Basis

- **Clock start.** The clock starts at onset, not at detection. The record gives 02:00 as the moment disruption began, so the pre-detection interval is known and nothing is Unknown.
- **Clock stop.** The clock stops at verified stabilization at or above tolerance level. The record gives 07:00 as verified stable on an alternate path.
- **Detection is not the start.** Measured from 04:00 (detection) the interval is 3 hours, which would appear to fit within four. That measurement is wrong under the method. The two undetected hours are the Detect phase and count against the tolerance.
- **Decision cap.** A tolerance result of Not Met makes the readiness decision Not Demonstrated (decision cap 4). No other evidence can lift it.

## Clock phases

| Phase | Interval | Elapsed |
|---|---|---|
| Detect | 02:00 to 04:00 | 2 hours |
| Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize | 04:00 to 07:00 | 3 hours combined |

The record does not split the 3 hours across the seven post-detection phases. That split is Unknown / Insufficient data, so I cannot say whether authorization, execution or communication was the slowest step.

## Binding constraint

**Detect.** The two-hour gap between onset and detection consumed half the tolerance before any decision was possible. If the post-detection sequence stays at 3 hours, Service B can meet a four-hour tolerance only if detection takes under 1 hour. ⧉ This is the single largest gap.

## Assumptions and limits

- All times fall on the same calendar day, with no date change or clock shift.
- I treated the supplied facts as the reviewed evidence record, as instructed. The record does not state the evidence type, so I could not independently check the times against logs or system records.
- The record does not say whether this was a live event (T4) or an exercise.
- The record does not say whether it matches the governing severe but plausible scenario.
- Without that information I cannot classify the other core gates or score the six domains. The Not Demonstrated decision does not depend on them.
- Gate 7 (evidence demonstrates whether tolerance was met) is the one gate the record speaks to directly. It shows the tolerance was not met. Classifying the gate formally needs confirmation of the evidence type.

## ESCALATE

- **Issue:** A tolerance breach on a critical service.
- **Operational consequence:** Service B has not shown it can execute within tolerance, and the detection gap is structural.
- **Facts required:** Whether Service B is regulated, which jurisdictions apply and whether any breach notification duty arose from the 5-hour outage. ⚠ If so, this needs external counsel. Unknown at present.
- **Interim control:** Until detection is shortened, treat the effective tolerance headroom for post-detection execution as under 2 hours.
- **Decision owner:** The accountable service owner. The record does not name one, which is itself an open item.
- **Questions for senior management:** Who accepts the residual exposure until the corrective actions close? Is the 4-hour tolerance still the correct approved figure?

## Priority actions

1. Establish how the 02:00 onset went undetected for 2 hours, and design a detection control with a stated detection-time target.
   - **Acceptance test:** A controlled injection of the same failure is detected within the target.
   - **Evidence:** Alert and log timestamps.
2. Obtain phase timestamps for the 04:00 to 07:00 interval to find the slowest phase.
3. Retest the whole sequence from onset to verified stabilization as a T2 or T3 exercise. Confirm it finishes inside 4 hours.

## [Purpose]
Determine the clock start, clock stop, elapsed time, tolerance result and readiness decision for Service B.

## [Decisions Made]
- Clock runs 02:00 to 07:00, 5 hours.
- Tolerance Not Met.
- Readiness decision Not Demonstrated.

## [Outstanding Items]
- Phase timing for 04:00 to 07:00.
- Evidence type and source for the timestamps.
- Whether the event was live or an exercise, and whether it matches the governing scenario.
- Named accountable owner.
- Regulatory notification question for counsel.

✅ complete

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
