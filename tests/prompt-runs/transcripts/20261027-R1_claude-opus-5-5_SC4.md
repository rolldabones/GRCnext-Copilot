# SC4 exercise tier gates the maturity level

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 8ae2878ad749f1baf0f85cdfcc7da03625202c56594331bd2401ef6a4ed73fb1  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8996  **Output tokens:** 3426
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

# Service B: Exercises Domain, Gate 6 and Tolerance Result [⇥ pending review]

## Scope and basis

- **Mode:** Exercise Evaluator, limited to the three requested results.
- **Service:** Service B.
- **Evidence basis:** The four facts you supplied, treated as the reviewed evidence record. No other artifacts were reviewed.
- **Assumptions:**
  - The tabletop scenario is the governing severe but plausible scenario for Service B, as you stated.
  - Impact tolerance values, pass and fail criteria and corrective-action records were not supplied, so they are Unknown / Insufficient data.

## Evidence ledger extract

| ID | Claim tested | Evidence type | Status | Credit | Evidence-conversion action |
|---|---|---|---|---|---|
| B-EX-01 | A severe but plausible exercise was run for the governing scenario | Exercise record (T1) | Verified | Gate 6 credit | None for the gate |
| B-EX-02 | Accountable owner and relevant authority participated | Exercise record | Verified | Domain 5 credit for participation | None |
| B-EX-03 | Switches or exits were invoked | Exercise record | Refuted: the record states none were invoked | No execution credit | Invoke the switch and priority exit in a T2 or T3 test |
| B-EX-04 | Execution timing was measured against tolerance | Exercise record | Refuted: the record states no timing was measured | No tolerance credit | Capture elapsed time by clock phase from onset |
| B-EX-05 | The capability could not be executed in a controlled test | Exercise record | Refuted: a controlled test is feasible | The cap 8 exception is unavailable | None |
| B-EX-06 | Pass and fail criteria are tied to tolerance, and findings produced owned corrective actions | Not supplied | Not evidenced | No credit | Produce the criteria and the corrective-action register |

## Result 1: Exercises domain (Domain 5) score: L2 Designed

**Basis:**
- A scenario exists for the governing case.
- The right owners and authority took part.
- Findings and notional decisions are documented.

These facts support documented responsibilities and intended actions, which is L2.

**Why not L3:**
- Decision cap 8 states that T0 and T1 alone do not earn L3.
- The narrow exception does not apply, because the record states a controlled test is feasible (B-EX-05).
- No switch or exit was performed and no timing was captured. Execution is therefore entirely simulated.

**Material gaps holding the score at L2:**
- Nothing was invoked.
- No elapsed times were recorded.
- Pass and fail criteria tied to tolerance are not evidenced.
- Corrective actions and retest status are not evidenced.

If the criteria and corrective-action records cannot be produced, the score should be reviewed downward toward L1.

## Result 2: Gate 6 (severe but plausible exercise completed): Pass

**Basis:**
- The gate asks whether at least one severe but plausible exercise has been completed.
- A T1 tabletop against the governing scenario was completed and is Verified (B-EX-01).

**Limit of this Pass:**
- It credits only the fact that the exercise occurred.
- It provides no evidence that any switch or exit executes, or that the clock fits within tolerance. Those questions belong to gate 7 and Domains 3 and 4.
- If `methodology/exercise-tiers.md` sets a minimum tier for gate 6, this classification should be revisited against that text. I have not reviewed that file.

## Result 3: Tolerance result: Not Tested

**Basis:**
- No switch or exit was executed.
- No timing was measured against tolerance (B-EX-03, B-EX-04).

**Clock events:**
- **Clock start (onset of disruption):** None recorded. The onset event was simulated, and no observable onset event was timed.
- **Clock stop (verified stabilization at or above tolerance level):** None recorded. Stabilization was not performed.

Not Tested is the correct label rather than Cannot Determine. No execution was attempted, so there is no measured interval whose onset is uncertain.

## Consequence for the readiness decision (for awareness)

- **Gate 7 fails.** Gate 7 requires evidence that demonstrates whether the tolerance was met, and no such evidence exists.
- **Not Demonstrated.** Under cap 4, a gate 7 Fail makes the readiness decision Not Demonstrated.
- **Demonstrated is independently barred.** Cap 5 requires a Met tolerance result with both clock events stated.

⧉ **Largest gap:** Service B's optionality for the governing scenario has only been discussed, never executed. A controlled test is feasible, so the absence of a timed invocation is a choice, not a constraint.

## Priority action

| Field | Detail |
|---|---|
| **Action** | Run a T2 controlled test, or a T3 end-to-end rehearsal, of the governing scenario. Invoke the primary switch and, where feasible, the priority exit. |
| **Owner** | Service B accountable owner. Name: Unknown / Insufficient data. |
| **Prerequisite** | Approved, measurable impact tolerance. Pass and fail criteria tied to that tolerance. A defined observable onset event. |
| **Acceptance test** | Elapsed time is recorded for each phase (Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate, Stabilize), measured from onset and compared with tolerance. |
| **Evidence required** | Timestamped exercise record, system logs or tickets for actions performed, a statement of which actions were simulated versus performed, findings, and corrective actions with owners and dates. |
| **Decision needed** | Accountable owner to authorize the test window and its safety constraints. |

**[Purpose]** Score Domain 5, classify gate 6 and give the tolerance result for Service B from the supplied exercise record.

**[Decisions Made]**
- Domain 5 is L2.
- Gate 6 is Pass, crediting the exercise only.
- The tolerance result is Not Tested, with no clock start or stop recorded.
- The cap 8 exception is not available.

**[Outstanding Items]**
- Impact tolerance value and approval.
- Pass and fail criteria.
- Corrective-action register.
- Named owner for the controlled test.
- Confirmation of any tier threshold for gate 6 in the methodology files.

✅ complete

> Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
