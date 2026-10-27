# SC2 provisional credit and the conversion action

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** df228af3f99ea6765767e1c80f457419181380308e0ec704ea22d0a828297372  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8960  **Output tokens:** 3180
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Classify the switch claim, state the credit it earns and the Switches level it supports, and name the action that would verify it.

- The switch action, trigger and intended operator are described in a draft runbook.
- An owner states in interview that decision authority is delegated and available out of hours.
- No execution record. No test. No signed delegation.
~~~~

## Assistant response

# Service B: Switch Claim Evidence Review [⇥ pending review]

**Mode:** Evidence Review, limited to one switch claim for Service B. The record contains no tolerance, dependency map or exit evidence, so this review covers the switch only.

## Classification

**Overall switch claim: Provisional for design. Not evidenced for execution.**

| ID | Claim tested | Artifact | Evidence type | Status | Credit |
|---|---|---|---|---|---|
| E-01 | Switch action, trigger and operator are defined | Draft runbook | Draft document (not controlled) | Provisional | Provisional only, labeled unverified |
| E-02 | Decision authority is delegated | Owner interview | Interview representation | Provisional | Provisional only, labeled unverified |
| E-03 | Authority is available out of hours | Owner interview | Interview representation | Provisional | Provisional only, labeled unverified |
| E-04 | The switch can be executed | None | None | Not evidenced | None |
| E-05 | Signed delegation instrument | None | None | Not evidenced | None |

The draft runbook is verified only in the sense that it exists. Its contents describe intended procedure, not performance. A runbook stating that the switch works is not evidence that it does. The absence of a signed delegation is recorded as Not evidenced, not as proof that no delegation exists.

## Credit earned

- **Verified credit:** none for executability or authority. No verified evidence, no verified credit.
- **Provisional credit:** the switch is identified and its action, trigger and operator are described. This credit stays provisional until the evidence-conversion actions below close.

## Switches level supported: L1 Described

- **L1 is supported.** The switch is identified with preliminary documentation. Execution depends on a draft and on one owner's representation.
- **L2 is not supported.** The runbook is a draft. The record does not show prerequisites, execution time, rollback or stabilization, communications or evidence generated. Authority rests on interview alone.
- **L3 is not available.** No exercise or test of any tier exists.

**Consequences:**
- The Constraint Level for Service B (minimum of Pipes, Switches and Exits) cannot exceed L1 on this record.
- Gate 4 (authority to invoke essential switches is available) is at most a **Provisional Pass**, unverified and resting on interview. Under cap F2 this alone limits the readiness decision to Conditionally Demonstrated at best.
- Gates 6 and 7 cannot pass on the strength of this switch, because it has never been invoked or timed.

⧉ **Largest gap:** No one has shown that an authorized person can invoke this switch outside normal hours. The Decide, Authorize and Execute phases of the clock are entirely untested, so their elapsed time against tolerance is Unknown / Insufficient data.

## Verifying action

**Action:** Run a T2 controlled out-of-hours invocation of the switch.
- The delegated decision-maker authorizes the switch under a signed delegation.
- The named operator executes it from the approved runbook.
- Each clock phase is timed, from the trigger through Verify, Communicate and Stabilize.

**Prerequisites:**
1. Promote the draft runbook to a controlled, approved version. Add prerequisites, rollback or stabilization, communications and evidence outputs.
2. Execute a signed delegation naming the decision-maker and an alternate.
3. Confirm the out-of-hours contact path for both.

**Acceptance test:**
- Authorization comes from the delegated person, not a substitute escalation.
- The switch completes and stabilization is verified.
- Elapsed times are recorded per phase.

**Evidence required:**
- Signed delegation instrument
- Approved runbook version
- Authorization record with timestamp
- Execution log or ticket
- Verification record
- Exercise record listing actions performed and actions simulated

**Owner:** Service B accountable owner. The owner's name is Unknown / Insufficient data.

**Effect on the level:** A successful T2 test earns credit for the tested component only. It supports L3 for this switch path only if the test also meets the tier rules in `methodology/exercise-tiers.md`. That outcome depends on the test result, not on this review.

**[Purpose]** Classify the Service B switch claim and set its credit and maturity ceiling from the reviewed record.

**[Decisions Made]**
- Switch claim: Provisional (design) and Not evidenced (execution).
- Switches level: L1 Described.
- Gate 4: Provisional Pass at most, unverified.
- Verifying action: T2 out-of-hours controlled invocation under a signed delegation.

**[Outstanding Items]**
- Approve the runbook.
- Sign the delegation.
- Name the owner.
- Supply the impact tolerance for Service B so elapsed time can be tested against it.
- Schedule and record the T2 test.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
