# SC5 the organization view is the minimum across services

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** cbe9e0b8fbb7ec08cc9f426d0410cb9a6c24250e537ed5fa08725322ceb77930  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8938  **Output tokens:** 1991
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

**Organization readiness position: Not Demonstrated.**

The organization view is the minimum of the service-level readiness positions, never an average. Service B is Conditionally Demonstrated, but it cannot lift the organization above the weakest service.

**Floor set by:** Service M and Service K jointly. Both are Not Demonstrated, so the readiness decision does not separate them.

⧉ Service M is the largest single gap. It has the lowest Constraint Level (1), meaning at least one of Pipes, Switches or Exits is at L1 Described, where execution still depends substantially on individuals, assumptions or incomplete arrangements. The table does not say which component.

## Service positions

| Service | Constraint Level | Readiness decision | Role in organization view |
| --- | --- | --- | --- |
| Service B | 2 | Conditionally Demonstrated | Above the floor |
| Service M | 1 | Not Demonstrated | Sets the floor (joint) |
| Service K | 2 | Not Demonstrated | Sets the floor (joint) |

Constraint Level is a maturity diagnostic, not a readiness decision. I have not combined or averaged it across services. For reference, the lowest value is 1 (Service M).

## Evidence status

- The table is a summary representation. I have not reviewed the underlying dossiers, gate results or evidence ledgers, so I treat these positions as **Provisional** and take them as given.
- **Evidence-conversion action:** confirm each decision against its dossier, with the eight core gate classifications and the tolerance result recorded.
- **Unknown / Insufficient data:** binding constraint, evidence confidence, tolerance result, gate results and domain scores for all three services. I cannot say why Services M and K are Not Demonstrated. The cause could be a core gate at Fail, a tolerance result of Not Met, or execution never shown within tolerance.
- **Scope limit:** this view covers only the three services assessed. It says nothing about any other critical service. If others exist and are unassessed, their position is Unknown, and the organization view should be labeled as covering assessed services only.

## Decisions required

1. **Accept or reject the organization position** of Not Demonstrated for the assessed scope. Owner: executive sponsor or the accountable senior management function.
2. **Confirm scope completeness.** Decide whether other critical services exist that should be assessed before this view is relied on externally.
3. **Direct remediation priority.** Start with Service M (lowest Constraint Level), then Service K. Prioritization needs the binding constraint and gate results for each, which were not supplied.

## Next assessment step

Supply, per service: the six domain scores, the eight core gate classifications, the tolerance result with the clock start and stop events, the binding constraint with its governing scenario and the evidence confidence. I can then identify what is actually holding Services M and K at Not Demonstrated and build a 90-day corrective-action backlog.

Do not paste secrets, credentials, protected personal data or unnecessary confidential content. Use neutral labels such as Service B and Vendor A.

[Purpose] Establish the GRCnext™ organization readiness position from three service-level results.
[Decisions Made] Organization position set at Not Demonstrated by the minimum rule, with Services M and K jointly setting the floor. No averaging applied.
[Outstanding Items] Verification of the inputs against dossiers, gate results, binding constraints, tolerance results, evidence confidence and scope completeness.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
