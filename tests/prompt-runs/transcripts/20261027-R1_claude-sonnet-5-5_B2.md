# B2 uses progressive disclosure at intake

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 3da05e5217af5be5772a4b1a40e754724da016e24db839caf30e5f15656153e5  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 8886  **Output tokens:** 3948
**Truncated:** no

## User message

~~~~text
Here is the name of our service and one sentence about it. Service B: our real-time payment service, which lets retail customers send and receive funds within seconds. Give me the full assessment package.
~~~~

## Assistant response

# GRCnext™ Initial Scoping: Service B

**Status: [↻ draft]** | Mode: Assessment (default) | Evidence cut-off: none supplied

## Why this is not the full package

You asked for the full assessment package from a service name and one sentence. I will not produce it yet, because that would mean inventing scores, owners, tolerances and test results. The evidence rule applies here: no verified evidence, no verified credit. What follows is the initial output: scope, known facts, assumptions, gaps, a gate view, an evidence request and a next step.

**Data handling:** Do not paste credentials, customer data, account numbers or unnecessary confidential contract text. Use neutral labels such as Scheme A, Provider C and Jurisdiction X. If you share a contract excerpt, redact party names and pricing. If any credential has already been shared in another channel, rotate it.

## 1. Scope

- **Service under assessment:** Service B, a real-time payment service for retail customers.
- **Customers and stakeholders (stated):** retail senders and receivers. Other stakeholders, such as the scheme operator, sponsor or settlement bank and the regulator, are Unknown.
- **Scope exclusions:** Unknown.
- **Decision you must make:** Unknown. Please state it (for example board assurance, a regulatory submission, a provider exit decision or an investment case).

## 2. Known facts

| Fact | Source | Status |
|---|---|---|
| The service is named Service B | Your message | Provisional (representation) |
| It enables retail customers to send and receive funds | Your message | Provisional (representation) |
| It operates "within seconds" | Your message | Provisional (representation) |

"Within seconds" describes normal performance. It is **not** an impact tolerance. A tolerance is the approved maximum period or level of disruption the service can bear before material harm. Nothing supplied states one.

## 3. Assumptions (explicit, correctable)

1. Assessment mode, one critical service, no more than a provisional analysis.
2. Send and receive are treated as one service. This may be wrong. If they have different owners, dependencies or harms, they should be assessed as two services.
3. The unit of analysis is the outcome (a retail customer's funds moving within seconds), not the payment platform, the scheme connection or any vendor.
4. No evidence has been reviewed.

## 4. Missing material facts, in priority order

1. **Accountable owner** of the service, by role.
2. **Approved impact tolerance:** statement, approving authority and date, and measurement method.
3. **Observable onset event.** The clock starts when the service first falls outside normal delivery, not when someone notices. Candidates to confirm with you: payment success rate falling below an agreed threshold, or end-to-end completion time exceeding an agreed ceiling. This is my proposal, not a finding.
4. **Jurisdictions:** where the service is delivered, where customers sit, where data is processed and where providers operate.
5. **Dependencies:** scheme or rail access, settlement and liquidity arrangements, core platform, cloud or hosting, fraud and sanctions screening, messaging, identity and authentication, and any AI components.
6. **Concentrations:** any single provider, region, scheme connection or technology whose loss halts the service.
7. **Decision rights:** who can pause, reroute, degrade or stop the service, and who can authorize it out of hours.
8. **Existing exits and exercises:** any exit plan for the leading concentration dependency, and any test or rehearsal with its date and tier.
9. **Evidence cut-off date** and any open corrective actions.

## 5. Initial gate view

Every gate is Unknown because nothing has been supplied. Unknown means "insufficient data," not "does not exist."

| # | Core gate | Classification |
|---|---|---|
| 1 | Critical service and owner defined | Unknown (service named, owner not stated) |
| 2 | Impact tolerance approved and measurable | Unknown |
| 3 | Material dependencies mapped | Unknown |
| 4 | Authority to invoke essential switches available | Unknown |
| 5 | At least one executable exit for the leading concentration dependency | Unknown |
| 6 | At least one severe but plausible exercise completed | Unknown |
| 7 | Evidence shows whether tolerance was met | Unknown |
| 8 | Material corrective actions have owners and dates | Unknown |

**Results available now:**
- **Readiness decision:** cannot be Demonstrated, because any Unknown core gate prevents it. A formal rating is withheld.
- **Capability profile and Constraint Level:** not scored.
- **Evidence confidence:** Indeterminate.
- **Tolerance result:** Cannot Determine. Neither clock event is established.
- **Binding constraint:** not yet identifiable.

## 6. Stress-test hypotheses (to test, not findings)

These are where I would probe first for a seconds-level payment service. They are hypotheses until evidence arrives.

- **The clock may be consumed before execution starts.** When normal delivery takes seconds, a tolerance may be measured in minutes or hours, and detection, interpretation and authorization could use most of it.
- **Out-of-hours authority.** Does a named person hold delegated authority to pause or reroute payments at 03:00?
- **Safe stopping is hard.** In-flight and irrevocable payments, liquidity positions and reconciliation make "stop" and "roll back" non-trivial.
- **Scheme and settlement concentration.** Exit from a scheme connection or settlement provider may depend on third-party or regulatory consent outside your control.
- **Manual alternatives.** Is there any workable fallback for retail customers, and at what capacity?

⧉ **Largest gap at this stage:** no approved impact tolerance is known. Without one, the clock, every gate and every exercise result lack a pass or fail line.

## 7. ⚠ Escalation

**ESCALATE: jurisdiction and regulatory status unknown.** Payment services are typically regulated, and consumer-protection, operational resilience, outsourcing and data-location rules may constrain switches and exits. I cannot state what applies, and I make no compliance conclusion.
- **Facts needed:** jurisdictions, your licensing or regulatory status, and any regulator-notified tolerances or exit requirements.
- **Interim control:** treat any switch or exit that affects customer funds as needing legal and compliance review before invocation.
- **Decision owner:** senior management with counsel or compliance.

## 8. Evidence request (priority order)

Please supply what exists, using neutral labels.

1. Service definition or service register entry, naming the owner.
2. The approved impact tolerance, with approval record and measurement method.
3. A dependency or architecture map, including third and fourth parties.
4. The delegation of authority or incident decision matrix, including out-of-hours cover.
5. Runbooks for pause, reroute, degrade, failover and recovery.
6. Exit plan and relevant contract excerpts for the leading concentration dependency (redacted).
7. The most recent exercise record: scenario, tier, date, participants, elapsed times and findings.
8. The corrective-action register and the latest incident post-mortems.

Please label each item as final, draft or "exists but not shared." I will record drafts and representations as Provisional and conversion actions will be named for each.

## 9. Proposed next step

Reply with answers to items 1 to 4 of Section 4 and whatever artifacts from Section 8 you can share. With those I can issue the **developed assessment**: scorecard, gate results, tolerance result, binding constraint, evidence ledger and an executable 90-day backlog. I can also produce the **Service Dossier** if you want the six-section artifact built from your facts.

---

**[Purpose]** Establish scope, facts and gaps for Service B so that a defensible assessment can follow.

**[Decisions Made]** None. Assumptions in Section 3 are provisional and await your confirmation.

**[Outstanding Items]** Owner; approved tolerance and onset event; jurisdictions; dependency map; decision rights; exits and exercises; evidence cut-off date; the decision this assessment must inform; counsel input on regulatory status.

Final Liability rests with the Human.

❓ needs input

<!-- end of transcript; written by tests/run_prompt_cases.py -->
