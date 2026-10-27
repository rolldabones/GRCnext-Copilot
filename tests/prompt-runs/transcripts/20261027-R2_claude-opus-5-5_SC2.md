# SC2 provisional credit and the conversion action

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** df228af3f99ea6765767e1c80f457419181380308e0ec704ea22d0a828297372  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9132  **Output tokens:** 3188
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Classify the switch claim, state the credit it earns and the Switches level it supports, and name the action that would verify it.

- The switch action, trigger and intended operator are described in a draft runbook.
- An owner states in interview that decision authority is delegated and available out of hours.
- No execution record. No test. No signed delegation.
~~~~

## Assistant response

# GRCnext™ Evidence Review: Service B Switch Claim [⇥ pending review]

## Classification

| Component of the switch claim | Evidence | Status |
|---|---|---|
| Design (action, trigger, intended operator) | Draft runbook | **Provisional** |
| Decision authority delegated and available out of hours | Owner interview only; no signed delegation | **Provisional** |
| Executability (the switch works when invoked) | No execution record, no test | **Not evidenced** |

**Overall switch claim: Provisional.** Nothing is Verified. Nothing is Contradicted or Refuted: the record lacks evidence but does not disprove the claim. The absence of a test or signed delegation is recorded as Not evidenced, not as proof that the capability does not exist.

## Credit Earned

- **Verified credit: none.** No verified evidence, no verified credit.
- **Provisional credit:** limited to the existence of a described switch and a stated authority arrangement. Each is labeled unverified and tied to an evidence-conversion action below.

## Switches Level Supported

- **Verified: L0 Unowned.** Without verified evidence, neither ownership nor arrangements are demonstrated.
- **Provisional: L1 Described.** The switch is identified in preliminary documentation, but execution depends on a draft and an unconfirmed representation.
- **L2 Designed is not supported.** L2 requires documented responsibilities and procedures. Here the runbook is a draft and decision rights exist only in an interview statement.
- **L3 is not reachable on this record.** There has been no exercise of any tier.

**Downstream effect:**
- The Constraint Level for Service B (the minimum of Pipes, Switches and Exits) cannot exceed L1 provisional, or L0 verified.
- Gate 4 (authority to invoke essential switches) is at most a Provisional Pass, which caps the readiness decision at Conditionally Demonstrated.
- The tolerance result for this switch is **Not Tested**. Other gates were outside this review and remain Unknown / Insufficient data.

## Evidence Ledger

| ID | Claim tested | Artifact | Type | Status | Resulting credit | Evidence-conversion action |
|---|---|---|---|---|---|---|
| SB-E01 | Switch action, trigger and operator are defined | Draft runbook | Controlled document (draft) | Provisional | Provisional L1 | Approve and version-control the runbook under a named owner |
| SB-E02 | Authority is delegated and available out of hours | Owner interview | Interview representation | Provisional | Provisional, Gate 4 | Obtain a signed delegation naming the primary and alternate decision-makers and their out-of-hours availability |
| SB-E03 | Switch is executable within tolerance | None supplied | None | Not evidenced | None | Conduct a timed, out-of-hours T2 controlled test (see below) |

## Action That Would Verify the Claim

⧉ **Largest gap:** the switch has never been executed. Decision authority out of hours rests on one interview statement.

**Named evidence-conversion action:** run an out-of-hours T2 controlled test of the Service B switch with the following elements.

1. Hold the test only after the signed delegation (SB-E02) and the approved runbook (SB-E01) are in place.
2. Have the delegated decision-maker, or the named alternate, actually authorize the switch. Do not let a facilitator assume that step.
3. Have the intended operator perform the action using current access and tools.
4. Timestamp each clock phase: Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate and Stabilize. Measure from a defined simulated onset, not from detection.
5. Preserve system logs, the authorization record and the communications record as the evidence pack.

**Acceptance test:**
- The switch is invoked by the delegated authority.
- It executes and is verified within the Service B impact tolerance.
- Each clock phase is evidenced.

**Credit outcome:** a passing T2 test, together with the signed delegation and approved runbook, supports **verified L2** for the tested component only. **L3** requires a T3 end-to-end rehearsal of the governing severe but plausible scenario.

**ESCALATE: Out-of-hours decision authority.**
- **Issue:** Delegation is asserted but unsigned.
- **Consequence:** If the stated authority is not valid at 02:00, the Authorize phase may stall and consume the tolerance.
- **Facts and evidence required:** the signed delegation instrument, the identity of the delegator and the alternate coverage roster.
- **Interim control:** Senior management confirms in writing who may invoke the switch until the delegation is executed.
- **Decision owner:** Service B accountable executive.
- **Question for senior management:** Does the delegating authority hold the power to delegate this switch, and who acts if the delegate is unreachable?

[Purpose] Classify the Service B switch claim and state its credit, level and verification path.
[Decisions Made] Claim classified Provisional. No verified credit. Switches level is verified L0 and provisional L1. Gate 4 is at most a Provisional Pass.
[Outstanding Items] SB-E01 runbook approval; SB-E02 signed delegation; SB-E03 timed T2 test; tolerance figure for Service B; other gates not assessed.

✅ complete

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
