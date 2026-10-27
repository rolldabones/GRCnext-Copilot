# SC3 contradictory evidence blocks Demonstrated

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 031db8d348aaeeac5dd9fffdd01540ba609908c3029f26dc9712336773ecf952  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8967  **Output tokens:** 4218
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Can the exit be marked Demonstrated?

- A summary report states the exit was rehearsed end-to-end and completed within the approved tolerance.
- The exercise record for the same event shows a T1 facilitated tabletop. No system actions were performed. The stated completion time is an estimate produced in discussion, not a measured elapsed time.
~~~~

## Assistant response

# Service B: Exit Readiness Determination [⇥ pending review]

## Answer

**No. The exit cannot be marked Demonstrated.** The readiness decision for the Service B exit is **Not Demonstrated** and the tolerance result is **Not Tested**.

The summary report says the exit was rehearsed end-to-end and completed within tolerance. The exercise record for the same event disproves that: it was a T1 facilitated tabletop, no system actions were performed and the completion time was an estimate made in discussion, not a measured elapsed time. A discussion estimate cannot show that anyone can execute the exit within tolerance.

⧉ **Largest gap:** Management reporting overstates exit capability. The summary report gives a T1 tabletop the credit of a T3 rehearsal with a measured tolerance result. Any decision, attestation or report that relied on it is resting on a refuted claim.

## Evidence ledger

| ID | Claim tested | Artifact | Evidence type | Status | Credit | Evidence-conversion action |
|---|---|---|---|---|---|---|
| E-01 | Exit was rehearsed end-to-end | Summary report | Controlled document (secondary) | **Refuted** by E-02 | None | Withdraw or correct the claim; reissue the report citing E-02 |
| E-02 | Nature of the exercise | Exercise record, same event | Exercise record (primary) | **Verified** as a T1 tabletop with no system actions | Credit for a T1 tabletop only | None for classification; see backlog |
| E-03 | Exit completed within approved tolerance | Summary report, with estimate in E-02 | Representation (discussion estimate) | **Refuted** as a measured result; the estimate itself is **Provisional** | None toward tolerance | Measure elapsed time from onset to verified stabilization in a T2 or T3 exercise |

**POTENTIAL HALLUCINATION:** The summary report's statement "rehearsed end-to-end and completed within the approved tolerance" is not supported by the primary record. Treat it as unsupported until the report author points to execution evidence. None has been supplied.

Owner, date, freshness and source location: Unknown / Insufficient data for E-01 to E-03.

## Why the claim is refuted, not just contradicted

- **End-to-end:** A T3 rehearsal performs the exit actions across the full path. The primary record says no system actions were performed. That affirmatively disproves the end-to-end claim.
- **Within tolerance:** A tolerance result needs a measured interval from the onset of disruption to verified stabilization. The primary record says the time was an estimate produced in discussion. No clock start or clock stop was observed, so no tolerance result was measured.

## Tolerance result: Not Tested

- **Clock start:** No onset event was simulated or observed. Unknown.
- **Clock stop:** No verified stabilization occurred, because no system actions were performed. Unknown.
- **Basis:** A T1 estimate does not test execution. Decision cap 5 bars Demonstrated without a Met result with both clock events stated.

## Gate view (exit-relevant gates, against the exercised scenario)

| Gate | Classification | Basis |
|---|---|---|
| 5. Executable exit for the leading concentration dependency | **Unknown** | Executability was not tested. No exit plan, contract or substitute capacity was supplied. |
| 6. Severe but plausible exercise completed | **Unknown** | A T1 tabletop occurred. Scenario content and severity were not supplied. |
| 7. Evidence demonstrates whether tolerance was met | **Fail** | The only timing evidence is a discussion estimate. The record shows no measurement was taken. |
| 1 to 4 and 8 | **Unknown / Insufficient data** | Not supplied. |

Gate 7 at Fail makes the decision Not Demonstrated under cap 4. Gates 5 and 6 at Unknown would independently bar Demonstrated under cap 1.

## Capability and constraint

- **Exits domain:** At most **L2**, and only if a documented exit design exists. None was supplied, so the score is Unknown / Insufficient data. Cap 8 means a T1 alone cannot earn L3.
- **Exercises domain:** At most **L2**. A tabletop was held, but no switch or exit was invoked and no timing was captured.
- **Evidence and improvement:** There is a material finding. The organization's reporting converted a T1 discussion into a claimed T3 result without challenge. This weakens confidence in other summary claims for Service B until they are traced to primary records.
- **Pipes and Switches:** Unknown / Insufficient data.
- **Constraint Level:** Cannot be fully computed. Exits caps it at **2 or lower**.
- **Binding constraint:** **Gate 7, at the Execute and Verify phases.** The governing scenario was not supplied, so this is evaluated against the exercised T1 scenario. Basis: no exit action has been performed, so the time to execute and verify the exit is unmeasured and may exceed tolerance.
- **Evidence confidence:** **Indeterminate.** The only execution claim is refuted, and the surviving evidence is a discussion estimate.

## Prioritized actions

Owners and target dates are not supplied. I have not assigned them.

| # | Action | Acceptance test | Evidence required | Decision or escalation |
|---|---|---|---|---|
| 1 | Correct the summary report. Reclassify the event as T1 with tolerance result Not Tested. | The revised report matches E-02 and cites it. | The corrected report with version history. | **ESCALATE** if the original report reached the board, auditors, customers or a regulator (see below). |
| 2 | Identify every decision, attestation or report that relied on E-01. | A complete list with a disposition for each item. | A reliance register. | Senior management decision on restatement. |
| 3 | Supply the exit plan, the contract exit provisions and the substitute arrangement for the dependency. | Gate 5 can be classified from documents. | The priority exit plan and relevant contract clauses. | None. |
| 4 | Design a T2 controlled test of the critical exit components, especially data retrieval in usable form and substitute activation. | Measured elapsed time per clock phase. | Logs, system records and a timestamped exercise record. | Approve test scope and safety constraints. |
| 5 | Run a T3 end-to-end rehearsal measured from a defined onset event to verified stabilization. | Tolerance result is Met or Not Met, with both clock events stated. | An exercise record with observed timings and an evidence pack. | Approve the rehearsal window. |
| 6 | Add a control requiring that exercise summaries state the tier and the simulated-versus-performed split, with traceability to the primary record. | The next summary passes an independent check. | Procedure update and a review record. | None. |

**ESCALATE: reporting integrity.**
- **Issue:** The summary report misstated the exercise tier and the tolerance result.
- **Operational consequence:** Decision-makers may believe an exit is available that has never been executed.
- **Facts required:** Who prepared and approved the report, who received it and whether any party relied on it.
- **Interim control:** Treat Service B exit capability as Not Demonstrated in all reporting.
- **Decision owner:** Unknown. The accountable owner of Service B must be identified.

⚠ If the report was submitted to a regulator, supervisor or customer as evidence of operational resilience or exit capability, obtain external counsel's view on correction and notification obligations.

---

**[Purpose]** Determine whether the Service B exit can be marked Demonstrated, based on the two supplied facts.

**[Decisions Made]** The readiness decision is Not Demonstrated. The tolerance result is Not Tested. The summary report claims are Refuted. The exercise is classified T1. Gate 7 is Fail.

**[Outstanding Items]** Service B owner and approved tolerance; governing scenario; exit plan and contract terms; scores for Pipes and Switches; reliance on the original report; owners and dates for the actions.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
