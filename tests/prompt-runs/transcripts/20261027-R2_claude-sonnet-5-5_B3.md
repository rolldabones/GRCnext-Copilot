# B3 separates capability, confidence and constraint

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 99f7bff307d120fcd9aee186d6548f1afe9a3d5afe723ed3dbb7c92fefa9b1a7  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9056  **Output tokens:** 1959
**Truncated:** no

## User message

~~~~text
Service B scored 3, 2, 3, 1, 2 and 2 across the six domains, in the order of the capability model. Give me a single overall maturity number for this service.
~~~~

## Assistant response

# Service B: maturity position [↻ draft]

I will not give you an overall average. GRCnext™ requires that all domain scores be shown individually, because averaging hides the weakest part of the service. The closest single number the method supports is the **Constraint Level**, which is **1**.

## Capability profile (as supplied)

| Domain | Score |
|---|---|
| 1. Services and tolerances | 3 |
| 2. Pipes | 2 |
| 3. Switches | 3 |
| 4. Exits | **1** |
| 5. Exercises | 2 |
| 6. Evidence and improvement | 2 |

## Four results and the tolerance result

- **Constraint Level: 1.** This is the minimum of Pipes (2), Switches (3) and Exits (1). Exits is the weakest structural component. The score describes capability maturity only.
- **Binding constraint:** Unknown / Insufficient data. It depends on the governing scenario and clock-phase timings, and neither has been supplied. Exits at L1 is the likely candidate, but I cannot confirm it.
- **Evidence confidence:** Indeterminate. I have only the scores, with no artifacts, dates or evidence IDs, so I treat them as unverified representations. They earn provisional credit at most, until each is paired with an evidence-conversion action.
- **Readiness decision:** Not Demonstrated on current information. No gate results or tolerance evidence have been supplied, and no domain can be verified.
- **Tolerance result:** Cannot Determine. Neither the clock-start event (onset of disruption) nor the clock-stop event (verified stabilization) has been supplied.

## Gate implications

I have not been given gate results, so these are indicative only.

- **Gate 5 (executable exit):** An L1 Exits score means the exit is described but depends on individuals, assumptions or incomplete arrangements. A Pass is unlikely. I classify it Unknown pending evidence.
- **Gate 6 (severe but plausible exercise):** An L2 Exercises score means no L3 credit. A discussion-only exercise (T0 or T1) of the governing scenario is a Fail on this gate. Establish the exercise tier first.
- Under the decision caps, a Fail or Unknown on any core gate prevents Demonstrated.

⧉ **Largest gap:** Exits at L1. Service B has not shown a way to leave or replace its leading concentration dependency within tolerance.

## What I need to move this forward

1. The artifact behind each score, or confirmation that the scores are self-assessed.
2. The Service B outcome, accountable owner and approved impact tolerance.
3. The governing scenario and the leading concentration dependency.
4. The latest exercise tier, date and what was simulated versus performed.
5. The assessment date and evidence cut-off date.

Please use neutral labels such as Vendor A and Jurisdiction X, and do not paste credentials, personal data or unnecessary confidential material.

**[Purpose]** Respond to a request for a single maturity number while preserving the capability profile and the Constraint Level.

**[Decisions Made]** No overall average issued. Constraint Level recorded as 1. Scores treated as unverified representations.

**[Outstanding Items]** Evidence for each domain score, governing scenario, tolerance statement, clock events, gate results and exercise tier.

❓ needs input

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
