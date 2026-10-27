# SC5 the organization view is the minimum across services

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** cbe9e0b8fbb7ec08cc9f426d0410cb9a6c24250e537ed5fa08725322ceb77930  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8938  **Output tokens:** 2216
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

# Organization View: Optionality Readiness Across Three Critical Services [⇥ pending review]

## Conclusion

**The organization has not demonstrated optionality.** The organization view takes the weakest service result, not an average. Two of three services are Not Demonstrated, so that is the organization's position.

| Organization result | Position | Set by |
| --- | --- | --- |
| Readiness decision | **Not Demonstrated** | Service M and Service K (tied) |
| Constraint Level | **1** | Service M |
| Evidence confidence | Unknown / Insufficient data | Not supplied for any service |
| Tolerance result | Unknown / Insufficient data | Not supplied for any service |
| Binding constraint | Unknown / Insufficient data | Not supplied for any service |

⧉ **Single largest gap: Service M.** It holds the lowest Constraint Level (1) and is Not Demonstrated. At least one of its Pipes, Switches or Exits domains is only at L1 Described. That means execution depends heavily on individuals, assumptions or incomplete arrangements. The table does not say which domain sets the 1.

## Service-Level Positions

| Service | Constraint Level | Readiness decision | Reading |
| --- | --- | --- | --- |
| Service M | 1 | Not Demonstrated | Sets both floors. Structural optionality is at L1 in at least one component. |
| Service K | 2 | Not Demonstrated | Shares the readiness floor. A Constraint Level of 2 alongside Not Demonstrated suggests a failed core gate or a tolerance result of Not Met. The cause is Unknown from the supplied data. |
| Service B | 2 | Conditionally Demonstrated | Strongest position. One or more core gates likely sit at Provisional Pass pending evidence conversion. |

Readiness decision and Constraint Level are separate measures. Service K shows why: its Constraint Level matches Service B's, yet its readiness decision is lower. A Constraint Level of 2 does not protect a service from a gate failure or a missed tolerance.

## Basis and Evidence Status

- **Provisional.** The three service results are representations supplied in this request. I have not reviewed the underlying gate results, domain scores, evidence ledgers or exercise records. The organization view inherits their reliability and nothing more.
- **Evidence-conversion action.** Supply the scorecard or Service Dossier for each service, covering:
  - all six domain scores;
  - the eight gate classifications;
  - the tolerance result with clock start and stop events;
  - the binding constraint;
  - evidence confidence.
- **No contradictions detected.** The supplied positions are internally consistent with the decision caps. Service K's lower readiness despite a Constraint Level of 2 is permissible, not contradictory.
- **No averaging applied.** An average would hide that two services cannot show executable optionality, so none is reported.

## What Changes the Organization View

The organization reaches Conditionally Demonstrated only when **both** Service M and Service K reach at least Conditionally Demonstrated. Fixing one leaves the other as the floor. Service M also needs its weakest structural domain raised before the organization Constraint Level can move above 1.

## Decisions Required

1. Accept Not Demonstrated as the reportable organization position to the governing body. This is a decision for the senior accountable owner.
2. Direct remediation priority to Service M first, then Service K. Base the order on the binding constraints once they are supplied, not on Constraint Level alone.
3. Confirm the evidence cut-off date for these three results, so the organization view can be dated.

---

**[Purpose]** State the organization-level readiness position from three service-level assessments, using the minimum rule.

**[Decisions Made]**
- The organization readiness is Not Demonstrated, with the floor set by Service M and Service K.
- The organization Constraint Level is 1, set by Service M.
- No averaging was applied.

**[Outstanding Items]**
- Domain scores, gate results, tolerance results, binding constraints and evidence confidence for all three services.
- The cause of Not Demonstrated for Service M and Service K.
- Evidence cut-off and assessment dates.
- The remediation backlog, which cannot be built responsibly until the above is supplied.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
