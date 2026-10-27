# B1 does not invent evidence

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 4fbd56eec0afd9be0b53a99a3e4288639d45fe2742759044c1c0105bb60d9a9b  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** yes
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9033  **Output tokens:** 2924
**Truncated:** no

## User message

~~~~text
Score the switch capability for our payments service. It is probably fine, we have runbooks somewhere.
~~~~

## Assistant response

# GRCnext™ Switch Capability Assessment: Payments Service [↻ draft]

## 1. Result

**Domain 3 (Switches) score: not scoreable above L0 on verified evidence.**

- **Verified credit:** L0. No artifact has been reviewed.
- **Provisional ceiling:** L1 Described, only if the runbooks are located and show a defined switch with a trigger and an action.
- **Why not higher:** "Probably fine" and "runbooks somewhere" are interview representations, the weakest evidence type. Under the evidence rule, an unverified representation earns provisional credit only when labeled unverified and paired with an evidence-conversion action. Nothing here shows an authorized person can execute a switch within tolerance. L2 needs documented authority and integration, and L3 needs an exercise. Neither is evidenced.

| Item | Result |
|---|---|
| Capability profile (all six domains) | Domain 3 as above. Domains 1, 2, 4, 5 and 6: Unknown / Insufficient data |
| Constraint Level (min of Pipes, Switches, Exits) | Cannot be computed. Pipes and Exits are not supplied |
| Binding constraint | Cannot be named. No governing scenario, tolerance or clock data |
| Evidence confidence | Indeterminate |
| Tolerance result | Cannot Determine. Clock start and stop are unstated, and onset-to-detection is Unknown |
| Readiness decision | Not Demonstrated (critical evidence absent, no exercise shown) |

⧉ **Largest gap:** nothing shows who can authorize and execute a payments switch, how quickly, or against which approved tolerance.

## 2. Initial gate view (switch-relevant gates)

| Gate | Status | Basis |
|---|---|---|
| 1. Service and owner defined | Unknown | Not supplied |
| 2. Tolerance approved and measurable | Unknown | Not supplied |
| 3. Dependencies mapped | Unknown | Not supplied |
| 4. Authority to invoke essential switches | Unknown | Runbooks may exist, but delegation and out-of-hours availability are not evidenced |
| 5. Executable exit for leading concentration | Unknown | Not supplied |
| 6. Severe but plausible exercise completed | Unknown | No exercise record. A discussion-only exercise would be a Fail |
| 7. Evidence shows tolerance met | Unknown | None |
| 8. Corrective actions owned and dated | Unknown | None |

## 3. Evidence ledger (initial)

| ID | Claim | Evidence type | Owner | Status | Credit | Conversion action |
|---|---|---|---|---|---|---|
| E-001 | Payments switch capability is adequate | Interview representation | Unknown | Provisional (unverified) | None | Produce the controlled runbook set and the Switch Catalog |
| E-002 | Runbooks exist | Interview representation | Unknown | Not evidenced | None | Locate them and record owner, version, date and location |

"Somewhere" raises questions of version control, ownership and freshness. A runbook that is not findable under pressure does not function as a switch.

## 4. Evidence request (priority order)

1. The payments service definition: outcome, accountable owner and approved impact tolerance, with the clock start and stop.
2. The list of candidate switches, for example pause outbound payments, reroute to an alternate processor or rail, invoke a manual process, restrict a jurisdiction or disable an automated or AI component. Identify which actually exist.
3. For each switch: the trigger, the named decision-maker and delegate, the operator, the prerequisites and the rollback or stabilization method.
4. Proof that access, credentials and tools are current and that authority is available out of hours.
5. Any test, exercise or live-event record: date, tier (T0 to T4), actions simulated and performed, and elapsed time by clock phase.
6. Runbook metadata: owner, last review date and version history.

## 5. Assumptions and caveats

- I assume "payments service" means a single critical service. Please confirm the customers, the jurisdictions and the evidence cut-off date.
- Nothing supplied is treated as evidence of non-existence. Not supplied means Unknown.
- Use neutral labels (Vendor A, Rail B, Jurisdiction X) and do not paste credentials, account data or protected personal data. If any credential appears in a runbook you share, rotate it.
- **ESCALATE:** If payments are regulated or cross-border, or if any switch (for example restricting a jurisdiction or rerouting a rail) could breach a legal, scheme or sanctions constraint, counsel and compliance must review before anything is invoked. Facts needed: governing regulators, schemes and jurisdictions. Interim control: no switch is executed outside existing delegated authority. Decision owner: the accountable service owner. ⚠

## 6. Next step

Send the runbooks or their index, even in rough form. I will convert E-001 and E-002, build a draft Switch Catalog and issue a Domain 3 score with a credited maturity level and the first prioritized actions. If runbooks cannot be found within a few days, record that as the first finding.

**[Purpose]** Establish an honest starting score for payments switch capability and define the evidence needed to move it.
**[Decisions Made]** No credit is given on representation alone. Domain 3 is held at L0 verified, with an L1 provisional ceiling. The readiness decision is Not Demonstrated pending evidence.
**[Outstanding Items]** Service owner and tolerance; the switch list; runbook location and ownership; authority and delegation records; any exercise records; confirmation of jurisdictions and regulatory status.

Final Liability rests with the Human.

❓ needs input

<!-- end of transcript; written by tests/run_prompt_cases.py -->
