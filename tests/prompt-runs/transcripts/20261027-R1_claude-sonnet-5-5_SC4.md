# SC4 exercise tier gates the maturity level

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 8ae2878ad749f1baf0f85cdfcc7da03625202c56594331bd2401ef6a4ed73fb1  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8996  **Output tokens:** 3973
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

**Mode:** Exercise Evaluator, scoped to Domain 5 (Exercises), gate 6 and the tolerance result.
**Evidence basis:** The four facts supplied are treated as the reviewed record, so they are Verified for what they state. Nothing outside them is credited.

## 1. Exercise classification

| Element | Finding |
|---|---|
| Tier | **T1 facilitated tabletop** |
| Scenario | Governing severe but plausible scenario (Verified) |
| Participants | Accountable owner and relevant authority (Verified) |
| Performed | Discussion, notional decisions, recording of findings |
| Simulated | All decisions, and any authorization, execution, verification, communication and stabilization |
| Switch or exit invoked | None |
| Timing against tolerance | None measured |

## 2. Domain 5 score: Exercises = L2 (Designed)

**Basis for L2.** The scenario is the governing one, the right decision-makers took part, and findings were recorded. That is more than L1 (Described). The exercise shows that decisions can be reasoned about. It does not show they can be executed.

**Why not L3.** Decision cap F8 applies. T0 and T1 alone do not earn L3 except where a capability genuinely could not be executed in a controlled test. The record states that a controlled test is feasible, so the exception is unavailable. Separately, L3 requires documented actions, timing and evidence of material execution. Actions were notional and no timing exists, so L3 is not met on the facts either.

**Items not evidenced.** These are Unknown / Insufficient data, not absent:
- pass and fail criteria tied to tolerance
- recorded assumptions and injects
- an evidence pack preserved to a retrievable standard
- corrective actions raised from the findings, with owners and dates
- a retest requirement

Any of these could lift confidence in the L2 score. None can lift the score above L2 without a T2 or higher test.

## 3. Gate classification

**Gate 6 (at least one severe but plausible exercise completed): Pass.**

The record verifies that an exercise was completed against the governing scenario. The gate's wording sets no tier floor, so I classify it as written. The Pass confers no credit for execution. The tier shortfall is carried by the L2 score and by gate 7.

**Consequence for gate 7 (evidence demonstrates whether tolerance was met): Fail.** With no invocation and no timing, the record cannot show whether tolerance was met. Under decision cap F1 and F4 this prevents a Demonstrated readiness decision for Service B. Its ceiling on this evidence is Not Demonstrated. This is a consequence flagged for your review, not a full gate review.

## 4. Tolerance result: **Not Tested**

- **Clock start (onset event):** Not supplied. Unknown / Insufficient data.
- **Clock stop (verified stabilization at or above tolerance level):** Not reached, because nothing was executed.
- **Elapsed time by phase** (Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize): none measured. Notional decisions are not elapsed times.

This is not a Not Met result. The record neither shows a breach nor supports a claim of compliance. Cap F5 bars Demonstrated without a Met result and both clock events stated.

## 5. Single largest gap

⧉ No switch or exit was invoked and no clock was run. The Authorize and Execute phases, where tolerance is most often lost, are entirely unevidenced for Service B.

## 6. Priority actions

| # | Action | Owner | Acceptance test | Evidence required |
|---|---|---|---|---|
| 1 | Define the onset event, clock start and clock stop for Service B and approve pass and fail criteria tied to tolerance | Accountable service owner (name to be confirmed) | Criteria approved in writing before the next test | Controlled, versioned criteria document |
| 2 | Run a T2 controlled test invoking the principal switch for the governing scenario, with phase timestamps from injected onset | Service owner with the relevant authority | Every clock phase timed; tolerance result stated as Met or Not Met | Time-stamped logs, exercise record, simulated-versus-performed statement |
| 3 | Convert the tabletop findings into corrective actions with owners and target dates | Service owner | Each finding has an owner, date and acceptance test | Corrective-action register entries |
| 4 | Plan a T3 end-to-end rehearsal after T2 remediation | Service owner | Full clock run from onset to verified stabilization | Exercise evidence pack and retest record |

Order of execution: 1, then 2 and 3 in parallel, then 4. Credit above L2 for the exercised path arrives only after action 2 or 4 produces timed evidence.

## 7. Decision required

The service owner must approve a T2 controlled test with a named date. Until that test runs, Service B should be reported as Exercises L2, gate 6 Pass, gate 7 Fail and tolerance Not Tested.

**[Purpose]** Score the Exercises domain, classify the exercise gate and state the tolerance result for Service B.
**[Decisions Made]** Exercises L2. Gate 6 Pass. Gate 7 Fail as a flagged consequence. Tolerance result Not Tested.
**[Outstanding Items]** Onset and stop events; pass and fail criteria; corrective-action status; evidence pack location; T2 test date.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
