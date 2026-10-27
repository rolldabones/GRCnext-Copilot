# SC5 the organization view is the minimum across services

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** cbe9e0b8fbb7ec08cc9f426d0410cb9a6c24250e537ed5fa08725322ceb77930  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9110  **Output tokens:** 2138
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

# GRCnext™ Organization View [↻ draft]

## Result

**Organization readiness decision: Not Demonstrated.**

**Floor set by:** Service M and Service K jointly. Both are at Not Demonstrated, the lowest position in the set, so neither can be named as the sole floor. Service B (Conditionally Demonstrated) sits above the floor and does not lift it.

**Method:** The organization view is the minimum of the service-level readiness positions (decision cap F6). Averaging is not permitted. Two of three services at Not Demonstrated therefore determine the result, whatever Service B shows.

| Service | Readiness position | Rank (lowest = 1) | Role in organization view |
| --- | --- | --- | --- |
| Service M | Not Demonstrated | 1 (tied) | Sets the floor |
| Service K | Not Demonstrated | 1 (tied) | Sets the floor |
| Service B | Conditionally Demonstrated | 2 | Above the floor, no effect |

## Reading the Constraint Levels

Constraint Level (minimum of Pipes, Switches and Exits) is a structural maturity diagnostic. It is not an input to the readiness minimum and cannot break the tie above.

- Service M has the weakest structure (Constraint Level 1, the lowest in the set). One or more of its Pipes, Switches or Exits is only Described. ⧉ This is the single largest gap in the portfolio: the weakest structural position coincides with a Not Demonstrated decision.
- Service K has a Constraint Level of 2 but is still Not Demonstrated. That is consistent with the framework: a designed structure does not make optionality demonstrated. The cause lies elsewhere, such as a failed or Unknown core gate, a tolerance result of Not Met, or missing evidence.
- Service B has a Constraint Level of 2 and is Conditionally Demonstrated. This implies no core gate is at Fail or Unknown, but at least one material element is provisional or only partly tested.
- Reporting "organization Constraint Level 1" would be a different statement from the readiness decision. If the organization view includes it, label it as the lowest service-level diagnostic (Service M) and keep it separate.

## What the table does not tell us

The following are **Unknown / Insufficient data**:

- The binding constraint for each service and its governing scenario.
- Which core gates failed or are Unknown for Service M and Service K.
- Tolerance results, and the clock start and stop events.
- Evidence confidence for each service.
- Assessment date, evidence cut-off date and the approved impact tolerances.

I cannot say why Service M and Service K are Not Demonstrated, or what would move them. Do not infer causes from the Constraint Level alone.

## Decisions required

1. **Accept or challenge the position.** Confirm that management will report the organization as Not Demonstrated, with Service M and Service K as the floor.
2. **Sequence remediation.** Service M and Service K must each reach at least Conditionally Demonstrated before the organization position can rise. Service B improving does not change the organization view.
3. **Supply the missing facts** listed above so each dossier can state its binding constraint and gate results.

## Next step

Send, for Service M first and then Service K, the gate results, tolerance result, binding constraint and evidence confidence. I can then build a prioritized corrective-action backlog with acceptance tests. Use neutral labels and do not paste secrets, credentials or protected personal data.

**[Purpose]** State the organization-level readiness position from three service-level results.

**[Decisions Made]** None final. Provisional finding: organization view is Not Demonstrated, floor set jointly by Service M and Service K.

**[Outstanding Items]** Gate results, tolerance results, binding constraints, evidence confidence and evidence cut-off date for all three services. Management acceptance of the position.

✅ complete

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
