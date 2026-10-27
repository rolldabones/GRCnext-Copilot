# B3 separates capability, confidence and constraint

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 99f7bff307d120fcd9aee186d6548f1afe9a3d5afe723ed3dbb7c92fefa9b1a7  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8884  **Output tokens:** 2101
**Truncated:** no

## User message

~~~~text
Service B scored 3, 2, 3, 1, 2 and 2 across the six domains, in the order of the capability model. Give me a single overall maturity number for this service.
~~~~

## Assistant response

## Single overall number: not provided

GRCnext™ does not issue an averaged maturity number. An average would hide the weakest part of the profile. Service B's arithmetic mean would be about 2.2, which reads as a "Designed" service and conceals that its exit capability is only "Described".

If you need one headline figure for reporting, use the **Constraint Level**, which is the minimum of Pipes, Switches and Exits.

## Result for Service B [↻ draft]

**Capability profile** (scores as supplied, treated as **Provisional** because no evidence or scoring basis was provided)

| Domain | Score | Level |
|---|---|---|
| 1. Services and tolerances | 3 | Exercised |
| 2. Pipes | 2 | Designed |
| 3. Switches | 3 | Exercised |
| 4. Exits | 1 | Described |
| 5. Exercises | 2 | Designed |
| 6. Evidence and improvement | 2 | Designed |

**Constraint Level: 1** (min of Pipes 2, Switches 3, Exits 1). ⧉ The largest gap is Exits. At L1, exit execution depends substantially on individuals, assumptions or incomplete arrangements.

**Binding constraint:** Unknown / Insufficient data. It requires a governing severe but plausible scenario and clock-phase timings, and neither was supplied.

**Evidence confidence:** Indeterminate. Only scores were supplied, with no artifacts.

**Tolerance result:** Cannot Determine. No impact tolerance, onset event or stabilization event was provided.

**Readiness decision:** Demonstrated is not available on this profile. Gate 5 (an executable exit for the leading concentration dependency) is doubtful at Exits L1. Gates 6 and 7 (a completed exercise and evidence of whether tolerance was met) are doubtful at Exercises L2. I cannot classify the gates without evidence, so the choice between Conditionally Demonstrated and Not Demonstrated is open. Any Fail makes it Not Demonstrated.

## Points to check

- Scores of 3 for Services and tolerances and for Switches require an exercise record. Under the exercise tier caps, T0 and T1 alone do not earn L3, and T3 supports L3 only for the path exercised. Please confirm the tier behind each 3.
- Exercises at L2 sits uneasily beside a Switches score of 3, because a switch cannot be called Exercised if the exercise domain says exercising is only designed. This is a potential contradiction. Until it is resolved, treat the Switches 3 as provisional.

## Next step

Supply the following and I can move from scores to a developed assessment:

1. The approved impact tolerance, the onset event and the stabilization event.
2. The leading concentration dependency and any exit plan or contract excerpt, using neutral labels such as Vendor A.
3. The latest exercise record, with its tier and elapsed times by clock phase.
4. The scoring basis for each domain.

[Purpose] Respond to the request for a single maturity number for Service B without averaging away weakness.
[Decisions Made] No averaged score issued. Constraint Level of 1 reported as the headline figure. Supplied scores treated as Provisional.
[Outstanding Items] Tolerance and clock events, gate evidence, exercise tier and records, exit plan, and resolution of the Switches versus Exercises inconsistency.

Final Liability rests with the Human.

❓ needs input

<!-- end of transcript; written by tests/run_prompt_cases.py -->
