# SC4 exercise tier gates the maturity level

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 8ae2878ad749f1baf0f85cdfcc7da03625202c56594331bd2401ef6a4ed73fb1  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9168  **Output tokens:** 2600
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Score the Exercises domain, classify the exercise gate and give the tolerance result.

- A T1 facilitated tabletop was run for the governing severe but plausible scenario.
- Participants included the accountable owner and the relevant authority.
- Findings and notional decisions were recorded. No switch or exit was invoked. No timing was measured against tolerance.
- The capability could be put to a controlled test; nothing prevents one.
~~~~

## Assistant response

# GRCnext™ Exercises Assessment: Service B [↻ draft]

## Result summary

| Item | Result |
|---|---|
| Exercises domain score | **L2 Designed** |
| Gate 6 (severe but plausible exercise of the governing scenario) | **Fail** |
| Tolerance result | **Not Tested** |

## Exercise classification

- **Tier:** T1 facilitated tabletop.
- **Performed:** facilitated discussion with the accountable owner and the relevant authority. Findings and notional decisions were recorded.
- **Simulated or not done:** every operational action. No switch or exit was invoked, and no timing was measured against tolerance.
- **Evidence status:** Verified for what occurred, per the reviewed record. Evidence of execution is Not evidenced.

## Basis for each result

**Exercises domain, L2.**
- Credit: the governing scenario was exercised, the right owner and authority took part, and findings were recorded. This supports a designed capability with identified responsibilities and intended decisions.
- Cap: a T1 alone cannot earn L3. The narrow exception applies only where a capability genuinely could not be executed in a controlled test. Here a controlled test is feasible, so the exception is unavailable.
- Missing for L3: no action was performed, no elapsed times were captured by clock phase, and no tolerance-linked result exists.
- Unknown / Insufficient data: whether pass and fail criteria were tied to tolerance, whether corrective actions were assigned and whether a retest is scheduled. If the scenario was run without documented criteria, L1 is the more defensible score. The record supplied does not say, so I have not assumed it.

**Gate 6, Fail.** The gate requires a severe but plausible exercise of the governing scenario. A discussion-only T0 or T1 of that scenario is a Fail. Because no material action was performed, this is not a Provisional Pass. The gate is classified once, against the governing scenario.

**Tolerance result, Not Tested.** No timing was measured, so no evidence shows whether the tolerance was met.
- Clock start: onset of disruption, when Service B first falls outside its normal level of delivery. The record does not name an observable onset event, so the pre-detection interval is Unknown.
- Clock stop: verified stabilization of Service B at or above tolerance level. This did not occur in the exercise.
- Not Tested is the right label because no execution was attempted. Cannot Determine would apply if a test had run without usable timing.

## Readiness consequence

A Fail on a core gate and a tolerance result other than Met mean Service B cannot be Demonstrated. Under the decision caps, the Fail on Gate 6 makes the service-level readiness decision **Not Demonstrated** until the exercise evidence changes. Gate 7 follows the same logic, since no evidence shows whether tolerance was met. I leave its formal classification to the full assessment.

⧉ **Largest gap:** the record shows no executed switch or exit and no clock measurement from onset. Everything else about Service B's optionality remains asserted rather than shown.

## Evidence-conversion actions

1. **Name the onset event.** The accountable owner defines the observable event that starts the clock for Service B's governing scenario.
   - Acceptance test: the event is documented, approved and measurable from system records.
2. **Run a T2 controlled test of the primary switch.** Timing is captured per phase from onset: Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize.
   - Acceptance test: a timed execution record exists and is compared against the approved tolerance.
3. **Run a T3 end-to-end rehearsal of the governing scenario.** The rehearsal includes the relevant authority making and recording real authorization decisions.
   - Acceptance test: verified stabilization is reached and timed, and the evidence pack is preserved.
   - Credit: T3 supports L3 for the path exercised and no other.
4. **Record the corrective actions** from the existing tabletop with owners and target dates, and schedule the retest.
   - Acceptance test: each action has an owner, a date and verification-based closure.

Decision for management: approve and resource the T2 test, then the T3 rehearsal, with target dates.

## [Purpose]
Score the Exercises domain for Service B, classify the exercise gate and state the tolerance result from the supplied evidence record.

## [Decisions Made]
- Exercises domain: L2, with L1 possible if the missing criteria and corrective-action facts prove absent.
- Gate 6: Fail.
- Tolerance result: Not Tested.

## [Outstanding Items]
- Onset event for Service B: Unknown.
- Pass and fail criteria, corrective actions and retest status from the tabletop: Unknown.
- Scores for the other five domains, and the remaining gates, are not assessed here.

✅ complete

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
