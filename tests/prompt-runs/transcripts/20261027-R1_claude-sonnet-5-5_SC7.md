# SC7 the clock starts at onset, not at detection

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** f420fcae72bddb1bd0b89c61a7d6b3cd4b8106f81819ee9e119c78f026fe4f78  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8952  **Output tokens:** 2864
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the clock start, the clock stop, the elapsed time, the tolerance result and the readiness decision.

- Approved impact tolerance: four hours.
- Disruption begins at 02:00. Nobody notices until 04:00. The service is verified stable on an alternate path at 07:00.
~~~~

## Assistant response

# GRCnext™ Tolerance Result: Service B [↻ draft]

## Result

| Item | Result |
|---|---|
| Clock start | 02:00, onset of disruption (service first fell outside normal delivery) |
| Clock stop | 07:00, verified stabilization on the alternate path |
| Elapsed time | 5 hours 00 minutes |
| Approved impact tolerance | 4 hours |
| Tolerance result | **Not Met**, exceeded by 1 hour |
| Readiness decision | **Not Demonstrated** |

The clock starts at onset, not at detection. The 04:00 detection time is not the clock start. It marks the end of the Detect phase.

## Clock phases

| Phase | Interval | Elapsed |
|---|---|---|
| Detect (onset to detection) | 02:00 to 04:00 | 2h 00m |
| Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize | 04:00 to 07:00 | 3h 00m combined |

The record does not split the second block by phase. The split is Unknown / Insufficient data.

⧉ **Largest gap:** Service B ran for two hours with nobody aware of the failure. That is half the tolerance, spent before any decision could be made. The post-detection sequence, at three hours, fits within four hours on its own. Measured from onset, it does not.

## Binding constraint

- **Governing scenario:** the event in the record, a disruption starting at 02:00 and stabilizing on an alternate path at 07:00.
- **Binding constraint:** the Detect phase.
- **Basis:** the two-hour onset-to-detection interval consumed 50% of the tolerance and pushed total elapsed time past it.

## Decision logic

- The tolerance result is Not Met. Under decision cap 4, this makes the readiness decision Not Demonstrated regardless of the other gates.
- The alternate path did work and the service was verified stable. That shows a switch exists and was executed. It does not show execution within tolerance, so it earns no credit toward Demonstrated.

## Evidence status

- **Onset at 02:00, detection at 04:00, verified stabilization at 07:00:** Verified, because you designated these facts as the reviewed record. I have not seen the underlying artifacts. Evidence IDs, source and owner are not supplied. They are needed for the ledger.
- **Exercise tier:** Unknown. The record does not say whether this was a live event (T4) or an exercise. This affects maturity credit but not the tolerance result.
- **Evidence confidence:** Indeterminate for the full assessment. The timing facts are adequate for the tolerance result, but the artifacts are not identified.

## Assumptions

- All three timestamps fall on the same calendar day and in the same time zone.
- The 07:00 verification met the definition of stabilization at or above the tolerance level.

## Not assessed

I have not scored the six domains, the Constraint Level or the other core gates, because the record contains no data on them. They are Unknown. No inference from absence is drawn.

## Priority actions

1. **Shorten onset-to-detection.** Define the observable onset event for Service B and put monitoring or alerting on it. Acceptance test: a controlled test shows detection within a target set so that the full clock fits in four hours. Evidence: alert logs with timestamps.
2. **Capture phase timestamps.** Record when each phase from Interpret to Stabilize began and ended. Acceptance test: a complete timeline for the next event or exercise. Evidence: decision records and system logs.
3. **Convert the timing facts into ledger entries.** Name an owner and source for each timestamp.
4. **Retest.** Run a T2 or T3 exercise on the same scenario and confirm the full clock meets four hours.

## Decisions required

- The accountable owner of Service B must decide whether to accept the Detect-phase target or revisit the tolerance. Revisiting the tolerance requires the approving authority and is not a substitute for remediation.
- Confirm whether the event was live or an exercise, and whether any external notification obligations were triggered. If live, consider whether counsel review is needed. Unknown on the present record.

**[Purpose]** Determine clock start, clock stop, elapsed time, tolerance result and readiness decision for Service B from the supplied record.

**[Decisions Made]** Onset at 02:00 starts the clock. Verified stabilization at 07:00 stops it. Elapsed time is 5 hours against a 4-hour tolerance. The result is Not Met, so the readiness decision is Not Demonstrated.

**[Outstanding Items]** Phase-by-phase timing from 04:00 to 07:00; evidence artifacts and owners; exercise tier or live-event status; the other core gates and domain scores; the corrective-action owner and date.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
