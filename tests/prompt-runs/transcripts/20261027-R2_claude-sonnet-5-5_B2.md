# B2 uses progressive disclosure at intake

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 3da05e5217af5be5772a4b1a40e754724da016e24db839caf30e5f15656153e5  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9058  **Output tokens:** 3858
**Truncated:** no

## User message

~~~~text
Here is the name of our service and one sentence about it. Service B: our real-time payment service, which lets retail customers send and receive funds within seconds. Give me the full assessment package.
~~~~

## Assistant response

# GRCnext™ Assessment: Service B (Real-Time Payments)

**Status: [↻ draft]** | Mode: Assessment, initial output

## 1. Why this is not the full package yet

You asked for the full assessment package, but one sentence is not enough evidence to build one. Producing scorecards, a Service Dossier or an evidence ledger from it would mean inventing owners, tolerances, test results and scores, which the evidence rule prohibits. This initial output sets the scope, states what is and is not known and gives the evidence request that unlocks the full package.

Please do not paste secrets, credentials, protected personal data or unnecessary confidential material. Use neutral labels such as Vendor A, Scheme B and Jurisdiction X. If a credential is ever pasted, rotate it.

## 2. Scope

- **Critical service:** Service B, a real-time payment service for retail customers to send and receive funds within seconds.
- **Customers and stakeholders:** retail payers and payees are named. Everyone else is Unknown.
- **Assessment date, evidence cut-off, jurisdictions and exclusions:** Unknown / Insufficient data.

## 3. Known facts and assumptions

**Known (Provisional, one representation, no artifact):** the service exists, serves retail customers and delivers funds within seconds.

**Working assumptions (unverified, to be confirmed or replaced):**
- A1. Service B is assessed as a single critical service, not as an application or a vendor.
- A2. A proposed onset event is the first moment end-to-end payment completion falls outside its normal seconds-level delivery, or the failure rate crosses an agreed threshold, whether or not anyone has noticed. It is a proposal, not an approved definition.
- A3. The clock stops at verified stabilization of the service at or above its tolerance level.
- A4. At seconds-level service speed, any tolerance is likely to be consumed by the Detect, Interpret, Decide and Authorize phases before technical execution begins. This is a hypothesis to test, not a finding.

## 4. Missing material facts

In priority order:

1. The accountable owner and the approving authority for the service.
2. The approved impact tolerance: its statement, measurement method and clock events. Also whether it is expressed in time, volume or value.
3. The jurisdictions involved and the regulatory status of the service.
4. The dependency chain: payment scheme or rail, sponsor or settlement bank, processor, core ledger, cloud and network providers, fraud and sanctions screening, liquidity funding and customer channels.
5. The switches that exist, such as pause or stop payments, reroute to an alternative rail, degrade safely, restrict a jurisdiction or fail over, and who may invoke each.
6. The leading concentration dependency and its exit path.
7. The latest exercise: scenario, tier, date, what was simulated and what was performed.
8. The corrective-action register and its status.

## 5. Initial gate view

Each gate is classified once against a governing scenario that is not yet chosen, so every result below reflects absence of supplied evidence. It is not a finding that the capability does not exist.

| # | Core gate | Initial state | Basis |
|---|---|---|---|
| 1 | Critical service and owner defined | Unknown | Service named, owner not supplied |
| 2 | Impact tolerance approved and measurable | Unknown | No tolerance supplied |
| 3 | Material dependencies mapped | Unknown | No map supplied |
| 4 | Authority to invoke essential switches | Unknown | No switches or delegations supplied |
| 5 | Executable exit for leading concentration dependency | Unknown | No dependency or exit supplied |
| 6 | Severe but plausible exercise of governing scenario completed | Unknown | No exercise record supplied |
| 7 | Evidence shows whether tolerance was met | Unknown | No timing evidence supplied |
| 8 | Material corrective actions owned and dated | Unknown | No register supplied |

## 6. Provisional position

| Result | Position |
|---|---|
| Capability profile (six domains) | Not scored, insufficient data |
| Constraint Level (minimum of Pipes, Switches and Exits) | Not determinable |
| Binding constraint | Not determinable. Hypothesis A4 suggests the Decide and Authorize phases as the first place to look |
| Evidence confidence | Indeterminate |
| Tolerance result | Cannot Determine (no tolerance, no clock events, no pre-detection bound) |
| Readiness decision | Not Demonstrated, because critical evidence is absent and any Unknown gate prevents Demonstrated |

⧉ **Largest gap:** with no named owner and no approved tolerance, the clock cannot be started or measured, and every later conclusion depends on those two facts.

## 7. ESCALATE items

**ESCALATE 1: Accountable decision-maker not identified.**
- *Operational consequence:* switches and exits cannot be authorized within a seconds-level service tolerance if no one holds the decision right.
- *Facts required:* the named owner, the delegates and the out-of-hours authority.
- *Interim control:* none can be asserted from supplied facts. Senior management should confirm an interim accountable executive.
- *Decision owner:* senior management.

**ESCALATE 2: Regulatory and jurisdictional status unknown.** ⚠
- *Operational consequence:* a retail payment service is likely to carry regulatory expectations on operational resilience, incident notification and customer redress, and the data may be regulated or cross-border. These obligations may constrain the permitted switches and exits and set external clocks. I cannot state which apply, and I will not assert compliance.
- *Facts required:* the licensing or authorization basis, the jurisdictions and the scheme rules.
- *Evidence required:* the regulatory register for the service and any notification timelines.
- *Interim control:* none can be asserted from supplied facts.
- *Decision owner:* compliance and external counsel.
- *Questions for counsel:* which resilience and incident-reporting obligations apply to Service B, and do any restrict switching, rerouting or exit?

## 8. Evidence request

Send what already exists. Do not create artifacts for this request. I will classify each as Verified, Provisional, Not evidenced or Contradicted.

1. The service definition or register entry, with owner and approval record.
2. The approved impact tolerance and its approval record.
3. The dependency map or architecture view, including providers and the settlement and liquidity path.
4. Runbooks or playbooks for pause, reroute, failover and manual operation, with the delegation matrix.
5. Contracts or contract extracts for the top two providers (redacted), with termination, transition assistance and data return clauses.
6. The most recent exercise records, with timings and findings.
7. The corrective-action register and the latest incident post-mortem, if any.

## 9. Next assessment step

1. Answer the questions in Section 4, items 1 to 3, in a short reply. That is enough to frame the governing scenario.
2. Supply whichever artifacts in Section 8 exist. Partial supply is fine.
3. I will then produce the Developed assessment: scorecard, gate results, tolerance result, binding constraint, evidence ledger and a prioritized 90-day backlog. I will also produce one Service Dossier if you want it.

**Decision you must make now:** name the accountable owner and the governing scenario for the first assessment. A suggested starting scenario is the loss of the leading concentration dependency during peak volume.

**[Purpose]** Establish scope and evidence needs for a Service B assessment without inventing facts.
**[Decisions Made]** None. Assumptions A1 to A4 are unconfirmed.
**[Outstanding Items]** Owner, tolerance, jurisdictions, dependency map, switches, exit, exercise evidence, corrective actions, both ESCALATE items.

❓ needs input

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
