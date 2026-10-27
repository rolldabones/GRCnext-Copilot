# SC2 provisional credit and the conversion action

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** df228af3f99ea6765767e1c80f457419181380308e0ec704ea22d0a828297372  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9132  **Output tokens:** 2966
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Classify the switch claim, state the credit it earns and the Switches level it supports, and name the action that would verify it.

- The switch action, trigger and intended operator are described in a draft runbook.
- An owner states in interview that decision authority is delegated and available out of hours.
- No execution record. No test. No signed delegation.
~~~~

## Assistant response

# Service B: Switch claim classification [↻ draft]

## Classification: Provisional

The claim is that an authorized person can execute the switch out of hours. The record supports it only by a draft artifact and an interview representation. Nothing shows it has been executed or tested.

| Element of the claim | Evidence | State |
|---|---|---|
| Action, trigger and intended operator | Draft runbook (not a controlled document) | Provisional |
| Decision authority delegated and available out of hours | Owner's interview statement only. No signed delegation. | Provisional (representation only) |
| Executability and timing | No execution record. No test. | Not evidenced |

Weakest-link rule: the claim as a whole cannot be rated above its least-supported element that is material to execution. Authority and executability are both material, so the claim stays Provisional and does not reach Verified.

## Credit earned

- **Verified credit: none.** No verified evidence, no verified credit.
- **Provisional credit only, labeled unverified.** The credit rests on the draft runbook and the interview statement. It converts to verified credit only through the action below.
- **Execution time contribution to the clock: Unknown / Insufficient data.** Tolerance result for this switch: Not Tested.

## Switches level supported: L1 Described

- The draft runbook identifies the action, trigger and intended operator. That fits L1: preliminary documentation, with execution depending on individuals and assumptions.
- L2 Designed is not supported. It needs documented and controlled responsibilities, procedures, dependencies and intended actions. Here the runbook is a draft, the delegation is unsigned and the record is silent on prerequisites, communications, rollback or stabilization and downstream effects.
- L3 Exercised is not supported. No test has been performed at any tier.

Because the Constraint Level is the minimum of Pipes, Switches and Exits, Switches at L1 caps it at L1 for Service B, whatever the other two domains score.

## Action that would verify it

**Evidence-conversion action: a controlled out-of-hours invocation (T2) of the switch, run by the delegated operator under an approved runbook, with the signed delegation in place beforehand.**

1. **Prerequisite A.** Obtain a signed, dated delegation. It must name the role or person, the scope of the switch, the out-of-hours coverage arrangement and any conditions on use.
2. **Prerequisite B.** Approve and version-control the runbook. It must add prerequisites, expected execution time, communications, rollback or stabilization and evidence generated.
3. **Test.** Invoke the switch in a controlled environment or window outside normal hours. Capture timestamps for decide, authorize, execute and verify.
4. **Acceptance test.**
   - The named delegate authorizes without escalating to anyone outside the delegation.
   - The operator completes the action from the approved runbook.
   - The result is verified.
   - Elapsed time is recorded against the Service B tolerance.
5. **Evidence required.** The signed delegation, the approved runbook version, the test record with time stamps, the system logs of the action and the ticket or decision record.
6. **Owner.** The Service B owner who made the representation. No individual is named in the record, so the owner assignment and target date are for the decision owner to set.

A T2 test earns credit only for the component tested, so L3 for the full path would still need a T3 rehearsal. Completing the action above would support L2 on approval and a tested-component credit on execution.

## Escalation

ESCALATE (conditional): the record does not identify who holds the delegated authority. If the owner cannot name the delegate and produce the signed delegation, the organization has no identifiable accountable decision-maker for this switch. In that case senior management must decide who holds the authority and whether any interim manual control is needed. Until then, the delegation claim should not be relied on in any readiness decision.

⧉ Largest gap: the authority to invoke the switch rests on an unsigned, interview-only representation.

[Purpose] Classify the Service B switch claim, state its credit and level, and name the verifying action.
[Decisions Made] Claim classified Provisional. No verified credit. Switches supports L1 only.
[Outstanding Items] Signed delegation. Approved runbook. T2 out-of-hours test record. Named owner and target date.

✅ complete

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
