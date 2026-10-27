# B1 does not invent evidence

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 4fbd56eec0afd9be0b53a99a3e4288639d45fe2742759044c1c0105bb60d9a9b  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** yes
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8861  **Output tokens:** 3297
**Truncated:** no

## User message

~~~~text
Score the switch capability for our payments service. It is probably fine, we have runbooks somewhere.
~~~~

## Assistant response

# Switch capability: payments service (initial assessment)

**Mode:** Assessment, Switches domain only
**Status:** [⇥ pending review]
**Evidence cut-off:** None supplied

Please do not paste credentials, secrets, protected personal data or unnecessary confidential detail. Use neutral labels such as Provider A and Service B. If any runbook you share contains credentials, I will redact them and you should rotate them.

## 1. Result

| Item | Result | Basis |
|---|---|---|
| Switches score, verified | **L0 Unowned** | No artifact reviewed. No verified credit. |
| Switches score, provisional | **L1 Described at most (unverified)** | The only input is the representation "we have runbooks somewhere." |
| Evidence confidence | **Indeterminate** | Nothing is available to test. |
| Readiness decision (switches) | **Not Demonstrated** | Core gates 4, 6 and 7 are Unknown (see section 3). |
| Tolerance result | **Cannot Determine** | No tolerance, clock start or clock stop supplied. |
| Constraint Level | **Cannot be computed** | It needs Pipes and Exits scores, which are out of scope here. |
| Binding constraint | **Provisionally Authorize or Execute** | Unverified hypothesis only. It comes from the absence of any stated decision rights and from unlocated procedures. |

"Probably fine" is an unsupported assertion (POTENTIAL HALLUCINATION if carried into a report). It receives no credit.

⧉ **Largest gap:** the runbooks cannot be located. A procedure that cannot be found within the tolerance cannot be executed within it, so this is a finding in itself, not a filing problem.

## 2. What I can and cannot conclude

- **Known:** a representation that runbooks exist somewhere.
- **Not evidenced:** that they cover payments switches, that they are current, that a named person can authorize and run them, or that anyone has ever used them.
- **Unknown:** the service owner, the impact tolerance, the jurisdictions, the provider arrangements and whether AI affects payment decisions.

I have not inferred any of these. "Not supplied" does not mean "does not exist", so each item below is Unknown / Insufficient data.

## 3. Initial gate view (governing scenario not yet defined)

| Gate | Status | Note |
|---|---|---|
| 1. Service and owner defined | Unknown | Not supplied |
| 2. Tolerance approved and measurable | Unknown | Not supplied |
| 3. Dependencies mapped | Unknown | Out of scope for this pass |
| 4. Authority to invoke essential switches | Unknown | No decision rights evidenced |
| 5. Executable exit for leading concentration | Unknown | Out of scope for this pass |
| 6. Severe but plausible exercise completed | Unknown | No exercise record |
| 7. Evidence shows tolerance met | Unknown | No exercise record |
| 8. Corrective actions owned and dated | Unknown | No register supplied |

An Unknown on any core gate prevents an unqualified conclusion that optionality has been demonstrated.

## 4. Switch tests to be applied once evidence exists

| Test | Status |
|---|---|
| Switch inventory exists and is service-specific | Not evidenced |
| Trigger is defined and observable | Not evidenced |
| Decision-maker named, with delegate and out-of-hours cover | Not evidenced |
| Operator access and tooling current | Not evidenced |
| Downstream effects understood (settlement, reconciliation, customers) | Not evidenced |
| Communications step included | Not evidenced |
| Rollback or stabilization method defined | Not evidenced |
| Execution generates retrievable evidence | Not evidenced |
| Execution time measured against tolerance | Not evidenced |
| Latest test and its tier (T0 to T4) | Not evidenced |

Candidate switches to confirm or rule out (prompts, not facts): pause or hold outbound payments, reroute to an alternate processor or rail, invoke a manual payment process, restrict by jurisdiction, degrade safely, disable any AI agent in the payment path, and recover from a known-good state.

## 5. Evidence request, in priority order

1. **Service and tolerance:** the payments service definition, accountable owner and approved impact tolerance. Also state the observable event that marks the onset of disruption.
2. **Switch inventory:** the list of switches the organization believes it can invoke for payments.
3. **Runbooks:** the actual documents, with version, owner and last review date. Where they are stored and how an on-call person would find them counts as evidence.
4. **Decision rights:** the delegation matrix or equivalent, including who authorizes at 02:00 on a Sunday.
5. **Tests:** any record of a switch being invoked, whether in test, rehearsal or a real incident, with timestamps.
6. **Open actions:** any corrective-action register from prior incidents or tests.

## 6. Evidence-conversion actions

| Action | Converts | Acceptance test | Suggested owner |
|---|---|---|---|
| Locate and register every payments runbook in a single controlled location | Provisional L1 toward verified L1 | A named person retrieves each runbook within 15 minutes, unaided | To be named by the payments service owner |
| Confirm the decision-maker and delegate for each switch | Gate 4 | Delegation record dated and approved, including out-of-hours cover | To be named by the payments service owner |
| Run a T2 controlled test of the highest-priority switch, timing the full clock from onset | Gates 6 and 7 | Elapsed time per phase captured against tolerance | To be named by the payments service owner |

Until an owner, tolerance and date are supplied, I have not assigned targets. ESCALATE if no accountable decision-maker can be identified for payment switches, since that is an escalation trigger.

## 7. Decision required

Does the organization want a provisional or a verified score? If provisional, supply the six items above, even if incomplete. If verified, the first step is to locate the runbooks.

**Next step:** on receipt of items 1 to 4, I will produce the Switch Catalog entries and a developed score.

[Purpose] Establish a provisional baseline for payments switch capability and define the evidence needed to score it.
[Decisions Made] None. No score above L0 is verified.
[Outstanding Items] Service owner, tolerance, runbook artifacts, decision rights, test records and corrective-action register.

❓ needs input

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
