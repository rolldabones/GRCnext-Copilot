# SC2 provisional credit and the conversion action

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** df228af3f99ea6765767e1c80f457419181380308e0ec704ea22d0a828297372  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8960  **Output tokens:** 3041
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Classify the switch claim, state the credit it earns and the Switches level it supports, and name the action that would verify it.

- The switch action, trigger and intended operator are described in a draft runbook.
- An owner states in interview that decision authority is delegated and available out of hours.
- No execution record. No test. No signed delegation.
~~~~

## Assistant response

# GRCnext™ Evidence Review: Service B, Switches domain [⇥ pending review]

## Classification

**Provisional.** The switch claim rests on a draft artifact and an interview representation. Its executability component is **Not evidenced**.

| Ev. ID | Claim tested | Artifact | Evidence type | Status | Limitation |
|---|---|---|---|---|---|
| B-SW-01 | Action, trigger and operator are defined | Draft runbook | Document, uncontrolled draft | Provisional | Not approved or version-controlled. Date and owner Unknown. |
| B-SW-02 | Decision authority is delegated and available out of hours | Owner interview | Interview representation | Provisional | No signed delegation. Out-of-hours availability not shown. |
| B-SW-03 | The switch can be executed | None | None | Not evidenced | No execution record and no test. |

Nothing is Contradicted or Refuted. The absence of an execution record does not mean the switch cannot be executed. It means execution has not been shown.

## Credit earned

- **Verified credit:** none for execution or authority. The draft supports only the statement that a description exists.
- **Provisional credit:** labeled unverified, for design (B-SW-01) and delegation (B-SW-02). It converts to verified credit only through the actions below.

## Switches level supported

**L1 Described.** The switch is identified in preliminary documentation, but execution depends on an unsigned delegation and an interview statement.

- **L2 Designed is not awarded.** It needs documented responsibilities and procedures, and the runbook is a draft with no signed authority. It becomes available once B-SW-01 and B-SW-02 are converted to controlled documents.
- **L3 Exercised is unsupported.** No exercise has occurred, and an exercise below T2 could not earn it in any case.

## Effect on other results

- **Gate 4 (authority to invoke essential switches):** at most Provisional Pass, which caps the decision at Conditionally Demonstrated until the evidence-conversion action closes. This depends on the governing scenario, which was not supplied.
- **Gates 6 and 7:** Not evidenced, so the readiness decision is **Not Demonstrated** on the current record.
- **Tolerance result:** Not Tested. Tolerance, onset event and clock phases are Unknown.
- **Constraint Level:** Cannot be stated. The Pipes and Exits scores were not supplied, so only the Switches score (L1) is known.
- **Evidence confidence:** Low for this domain.

⧉ **Largest gap:** no execution record or test exists, so no timing exists to compare against the full clock from Detect through Stabilize.

## Verifying action

**Action:** a T2 controlled operational test of the switch.

1. The named operator invokes the switch and the named delegate authorizes it. The test runs outside normal hours or under realistic out-of-hours conditions, using the credentials and tools that would be used in practice.
2. The clock is recorded by phase with timestamps, and the evidence pack is preserved.

**Prerequisites (conversion of B-SW-01 and B-SW-02):**
- The runbook is approved and version-controlled, with a named owner.
- The delegation is signed and names the delegate, the scope, the trigger and an alternate for when the delegate is unreachable.

**Acceptance test:**
- The authorization is executed by the delegate on the signed instrument.
- The switch action completes and its effect is verified.
- Stabilization communications are issued.
- Elapsed time by phase is compared against the approved tolerance for Service B.

**Evidence required:** the approved runbook, the signed delegation, system logs, the authorization record, the timestamped timeline, the simulated-versus-performed statement and any findings with corrective actions.

**Owner:** the Service B owner who gave the interview (name not supplied). **Target period:** to be set by the Service B owner. **Residual risk:** a T2 test credits only the component tested, so end-to-end execution under tolerance needs a T3 rehearsal later.

## Decision required

Does management approve the runbook and sign the delegation, then authorize the T2 test and set its date?

[Purpose] Classify the Service B switch claim, state the credit and the supported Switches level, and name the verifying action.
[Decisions Made] Claim classified Provisional, with executability Not evidenced. Switches set at L1 Described, with no verified credit for execution or authority.
[Outstanding Items] Governing scenario and approved tolerance. Dates and owner of the draft runbook. Signed delegation. T2 test plan and date. Pipes and Exits evidence.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
