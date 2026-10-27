# B4 distinguishes simulated from performed

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 95a5744242bcf6e6eaac06566b9dfac7a5fe81e2dfb29bc92a18c5ab8f0d702e  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8861  **Output tokens:** 1886
**Truncated:** no

## User message

~~~~text
We ran a tabletop last quarter and it went well. Mark the exercise domain as exercised.
~~~~

## Assistant response

# Exercises domain: request not accepted as stated [↻ draft]

I can't mark the Exercises domain as exercised (L3). The rule is firm, and it doesn't depend on how well the tabletop went.

## Why L3 is not available

- **Tier cap.** A facilitated tabletop is T1. Under the decision caps, T0 and T1 alone do not earn L3. The only exception is a capability that genuinely could not be executed in a controlled test, and nothing supplied suggests that here.
- **Evidence status.** I have seen no exercise record, scenario, timings or findings. The claim that the tabletop "went well" is an interview representation. No verified evidence, no verified credit.
- **Clock.** A tabletop discusses decisions. It does not show that an authorized person executed a switch or exit within tolerance. Nothing here establishes elapsed time from onset of disruption to verified stabilization.

## What I can record now

| Item | Position |
|---|---|
| Exercises domain score | Provisional L2 at most, unverified. This holds only if scenarios, roles and procedures are documented. Otherwise L1. |
| Tabletop occurred and was effective | Provisional (representation only) |
| Exercise tier | T1, unverified |
| Gate 6 (severe but plausible exercise completed) | Provisional Pass. This caps any readiness decision at Conditionally Demonstrated until evidence conversion closes. |
| Gate 7 (evidence shows whether tolerance was met) | Unknown |
| Tolerance result | Not Tested |

Unknown here means insufficient data, not that the evidence does not exist.

⧉ **Largest gap:** no switch or exit has been shown to be executable within tolerance. A tabletop cannot close that gap.

## Evidence-conversion actions

Please supply these, using neutral labels such as Service A and Vendor B:

1. The exercise record: date, participants, scenario, injects and pass and fail criteria.
2. Which critical service and approved impact tolerance the exercise targeted.
3. The clock events used. State what started the clock (onset of disruption) and what stopped it (verified stabilization).
4. Elapsed times by phase: Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate and Stabilize.
5. Whether anything was actually performed, as opposed to discussed.
6. Findings, corrective actions with owners and dates, and retest status.

## Path to a defensible L3

Run a T2 test of a specific switch, or a T3 end-to-end rehearsal of the leading concentration dependency exit. Capture timings across the full clock and preserve the evidence pack. L3 would then apply only to the path exercised. L4 would additionally need monitoring, current metrics and closed corrective-action loops.

## Decision required

Do you want to supply the exercise record so I can convert the provisional credit, or have me design a T2 or T3 exercise plan?

**[Purpose]** Respond to a request to score the Exercises domain as exercised on the basis of a tabletop.
**[Decisions Made]** L3 declined under the tier cap and the evidence rule. Provisional L2 recorded, unverified.
**[Outstanding Items]** Exercise record, service and tolerance identification, phase timings, performed versus simulated actions and corrective-action status.

Do not paste secrets, credentials, protected personal data or unnecessary confidential detail into this conversation.

✅ complete

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
