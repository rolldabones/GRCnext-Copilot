# SC5 the organization view is the minimum across services

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** cbe9e0b8fbb7ec08cc9f426d0410cb9a6c24250e537ed5fa08725322ceb77930  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9110  **Output tokens:** 2102
**Truncated:** no

## User message

~~~~text
Three critical services have been assessed. Give the organization view.

| Service | Constraint Level | Readiness decision |
| --- | --- | --- |
| Service B | 2 | Conditionally Demonstrated |
| Service M | 1 | Not Demonstrated |
| Service K | 2 | Not Demonstrated |
~~~~

## Assistant response

# Organization View: Three Critical Services [⇥ pending review]

## Conclusion

**Organization readiness position: Not Demonstrated.**

The organization view is the minimum of the service-level readiness positions, not an average. Two services sit at the floor:

- **Service M**: Not Demonstrated, Constraint Level 1
- **Service K**: Not Demonstrated, Constraint Level 2

Both set the readiness floor. Service M is the weaker of the two because its Constraint Level is lower.

**Organization Constraint Level: 1, set by Service M.** At least one of Service M's Pipes, Switches or Exits domains is no better than L1 Described. Execution therefore depends substantially on individuals, assumptions or incomplete arrangements.

⧉ **Largest gap:** Service M is not demonstrated and has the weakest structural optionality in the portfolio. The organization cannot claim it holds executable optionality across its critical services while this position stands.

## Service-level summary

| Service | Constraint Level | Readiness decision | Effect on organization view |
| --- | --- | --- | --- |
| Service M | 1 | Not Demonstrated | Sets the floor, with the lowest Constraint Level |
| Service K | 2 | Not Demonstrated | Also at the readiness floor |
| Service B | 2 | Conditionally Demonstrated | Above the floor. Does not raise the organization view |

Service B's conditional position does not offset M and K. Averaging the three would hide the two failures, and Section 8F rule 6 prohibits it.

## Evidence status

| Item | Status | Basis |
| --- | --- | --- |
| Constraint Levels and readiness decisions for B, M and K | **Provisional** | Supplied as a summary table. I have not reviewed the underlying dossiers, gate results or evidence ledgers. |
| Binding constraint for each service | **Unknown / Insufficient data** | Not supplied |
| Tolerance result for each service | **Unknown / Insufficient data** | Not supplied |
| Core gate results | **Unknown / Insufficient data** | Not supplied |
| Evidence confidence per service | **Unknown / Insufficient data** | Not supplied |

**Evidence-conversion action:** Supply, or confirm from the existing assessments, the following for each service:
- the gate results
- the tolerance result, with clock start and clock stop
- the binding constraint
- the evidence confidence

This will move the organization view from provisional to verified.

## What can be concluded and what is reserved

**Can be concluded from the supplied table:**
- The organization view is Not Demonstrated.
- The floor is set by Service M and Service K.
- The structural floor is Constraint Level 1, at Service M.

**Reserved pending evidence:**
- Why M and K are Not Demonstrated. The cause could be a gate Fail, a tolerance result of Not Met or absent critical evidence.
- Which clock phase or gate actually binds execution for each service.
- Which material elements keep Service B at Conditionally Demonstrated.
- Organization-level evidence confidence.

## Decisions required

1. **Remediation order.** Decide whether Service M is remediated first. It sets the structural floor. Raising Service B to Demonstrated alone does not change the organization view.
2. **External messaging.** Senior management should decide what can be stated externally, for example to a board, a regulator or customers. "Demonstrated" optionality cannot be claimed at organization level.
3. **Next assessment step.** Authorize release of the M and K gate results and binding constraints. This would allow a prioritized 90-day corrective-action backlog (Section 16).

## Escalation

No ESCALATE item can be identified from the supplied data. The table carries no legal, jurisdictional, dispute or authority facts. Escalation review is reserved until the underlying service assessments are available.

[Purpose] Provide the organization-level readiness position across three assessed critical services.
[Decisions Made] Organization view set at Not Demonstrated, with the floor at Service M and Service K. Organization Constraint Level set at 1, from Service M. No averaging applied.
[Outstanding Items] Gate results, tolerance results, binding constraints and evidence confidence for B, M and K. Verification of the supplied table. Escalation review once facts are available.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
