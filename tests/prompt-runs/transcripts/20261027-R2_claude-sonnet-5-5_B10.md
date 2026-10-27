# B10 backlog items are executable

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 2c257febf34b65b7a0237641776fcaed749904c795839579334f02690c60dd34  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 10833  **Output tokens:** 24203
**Truncated:** no

## User message

~~~~text
Here is the evidence for Service B. Find the gaps, then give me the 90-day backlog for the gaps you found.

# Input pack: Service B real-time payments

Synthetic example. Neutral labels. Not legal or regulatory advice.

This is the intake pack, filled in, that produced
[`assessment.md`](assessment.md) and
[`assessment-result.json`](assessment-result.json). It follows
[`../../templates/intake-pack.md`](../../templates/intake-pack.md):
service facts first, then the artifacts supplied for each of the eight
gates. Artifact IDs (P-nn) name what was supplied; evidence IDs (E-nnn)
point to [`evidence-ledger.csv`](evidence-ledger.csv) where an artifact
became a ledger item.

## Service facts

- Service: Service B, real-time payments.
- Accountable owner: Head of payments.
- Customers: Retail banking customers, corporate customers using instant
  collections.
- Impact tolerance: 12 hours. Clock-start (onset) event: real-time
  settlement first falls outside its normal level of delivery. Clock
  stop: verified stabilization on the primary rail or an approved
  alternate path.
- Jurisdictions: Jurisdiction X (primary), Jurisdiction Y (cross-border
  corridor).
- Evidence cut-off: 2026-06-10.
- Decision due: 2026-06-15 (assessment date).

## Gate 1. Service and owner defined

| ID | Artifact | What it establishes |
|---|---|---|
| P-01 | Service definition statement for Service B | Outcome, scope boundaries (card payments and bulk payroll excluded) and material harms |
| P-02 | Accountability record naming the head of payments | A named accountable owner |

## Gate 2. Tolerance approved and measurable

| ID | Artifact | What it establishes |
|---|---|---|
| P-03 | Impact tolerance statement approved by the chief operating officer (E-005) | 12 hours approved and measurable; the approved text names detection as the clock start, so the onset clock is not yet approved (Provisional Pass, CA-005) |

## Gate 3. Dependencies mapped

| ID | Artifact | What it establishes |
|---|---|---|
| P-04 | End-to-end dependency map, verified 2026-05-20 | People, process, technology, data, facilities, third parties, jurisdictions and manual alternatives mapped; Vendor A identified as the leading concentration |
| P-05 | Fourth-party note on Vendor A's upstream network provider | A material fourth-party concentration in Jurisdiction X |

## Gate 4. Switch authority available

| ID | Artifact | What it establishes |
|---|---|---|
| P-06 | Switch catalog for SW-001 and SW-002 ([`switch-catalog.csv`](switch-catalog.csv)) | Trigger, action, decision-maker, operator and prerequisites for each material switch |
| P-07 | Delegation record and out-of-hours rota for the payments duty manager and head of payments | Authority to invoke both switches is delegated and reachable, though slowly out of hours |

## Gate 5. Executable exit for the leading concentration

| ID | Artifact | What it establishes |
|---|---|---|
| P-08 | MSA v3 termination-for-convenience and transition-assistance clauses (E-002) | A contractual right to exit Vendor A on 90 days notice |
| P-09 | Controlled data-export test record, 2026-03-18 (E-003) | Data can be exported in usable form (T2, export step only) |
| P-10 | Substitute gateway identification note (E-004) | A substitute is identified; peak capacity is Not evidenced |

## Gate 6. Severe but plausible exercise completed

| ID | Artifact | What it establishes |
|---|---|---|
| P-11 | T3 rehearsal record, 2026-05-12, with phase timing (E-001) | End-to-end reroute to the Vendor C backup rail under a weekday-peak Vendor A outage; regulator notification simulated, all other actions performed |
| P-12 | T2 degrade test record, 2026-04-03 | SW-002 technical step works; the authorization step was simulated |

## Gate 7. Evidence shows tolerance result

| ID | Artifact | What it establishes |
|---|---|---|
| P-11 | Timing record within the rehearsal record (E-001) | Clock start at onset (the injected Vendor A outage at rehearsal start); detection at 20 minutes; Authorize 3 hours; verified stabilization 9 hours from onset: Met against 12 hours |

## Gate 8. Corrective actions have owners and dates

| ID | Artifact | What it establishes |
|---|---|---|
| P-13 | Corrective-action register ([`capa-register.csv`](capa-register.csv)) | Five open actions (CA-001 to CA-005), each with an owner and a target date, none overdue on 2026-06-15 |

## Not supplied

- An end-to-end exit rehearsal off Vendor A.
- A peak-capacity test for the substitute gateway.
- A re-approved tolerance statement with clock start at onset.
- A live authorization record for SW-002.

These gaps are what hold gates 2 and 5 at Provisional Pass.

Final Liability rests with the Human.
~~~~

## Assistant response

# Service B real-time payments: gap findings and 90-day backlog

[↻ draft]

**Handling note.** The pack uses neutral labels and I found no credentials or protected data in it. Keep it that way in follow-up material.

## 1. Basis and limits

- I received the intake pack, not the artifacts it describes. `switch-catalog.csv`, `capa-register.csv`, `evidence-ledger.csv`, the dependency map, the rehearsal record and the contract clauses were not supplied. I treat the pack's descriptions as representations I have not verified. Each gap below converts to Verified only when the underlying artifact is reviewed.
- The pack states a classification only for gates 2 and 5 (both Provisional Pass). I tested those and classified the other six gates myself from the descriptions.
- The assessment date is 2026-06-15 and the evidence cut-off is 2026-06-10. Day 0 of the backlog is 2026-06-15 and Day 90 is 2026-09-13, a Sunday, so the last working target is Friday 2026-09-11.
- AI involvement in Service B is Unknown, so the AI overlay is not assessed.

## 2. Position before the backlog

| Gate | Classification | Basis |
|---|---|---|
| 1 Service and owner | Pass (on description) | P-01 and P-02 cover outcome, scope, harms and owner |
| 2 Tolerance | Provisional Pass | 12 hours approved. Approved text starts the clock at detection, not onset |
| 3 Dependencies | Provisional Pass | Map is 21 days old at cut-off. Vendor A's upstream provider is noted. Common-mode with the backup path and recovery dependencies are not evidenced |
| 4 Switch authority | Provisional Pass | SW-001 authorization was performed in T3. SW-002 authorization was only simulated. Out-of-hours reach is "slow" and unquantified |
| 5 Exit | Provisional Pass | Concurred, but the basis is thin: one T2 export step, no rehearsal, substitute peak capacity not evidenced |
| 6 Exercise | Provisional Pass | T3 reroute was performed, but regulator notification was simulated, so Provisional Pass at most |
| 7 Tolerance evidence | Provisional Pass | Timing record shows Met at 9 hours against 12, but it is a single run with partial phase detail |
| 8 Corrective actions | Pass (on description) | Five actions with owners and dates. Register contents not seen |

- **Capability profile:** Services and tolerances L2, Pipes L2, Switches L2 (L3 for SW-001 only), Exits L2, Exercises L3 (the SW-001 reroute path only), Evidence and improvement L2.
- **Constraint Level:** L2, shared by Pipes, Switches and Exits.
- **Binding constraint:** the Authorize phase, out-of-hours, in a Vendor A outage. The rehearsal authorized in 3 hours on a weekday peak, and P-07 says out-of-hours reach is slow with no timing. If the other phases hold at 6 hours, the arithmetic ceiling for Authorize is 6 hours with zero margin.
- **Evidence confidence:** Moderate. The evidence is coherent and dated, but it rests on one T3 run and descriptions I have not verified.
- **Readiness decision:** Conditionally Demonstrated. No gate fails, but Provisional Pass on any core gate caps the decision at this level.
- **Tolerance result:** Met for the exercised path only. The clock started at the injected Vendor A outage and stopped at verified stabilization at 9 hours. Not Tested for out-of-hours onset, SW-002, the exit and a fourth-party failure.

## 3. Gaps found

1. **G-01 Common-mode dependency (gates 3, 5, 6). Not evidenced. ⧉ Largest gap.** Nothing shows that Vendor A's upstream network provider in Jurisdiction X is independent of the Vendor C rail or the substitute gateway. A shared network, region or provider would invalidate the 9-hour result without anyone noticing.
2. **G-02 Clock start (gate 2). Contradicted.** The approved tolerance (P-03) starts the clock at detection. The service facts and the rehearsal start it at onset. Credit for the clock start is withheld until CA-005 closes.
3. **G-03 Out-of-hours authorization (gates 4, 6). Not evidenced.** The delay is acknowledged in P-07 but never timed. This is the binding constraint.
4. **G-04 SW-002 authorization (gate 4). Provisional.** The T2 test (2026-04-03) simulated the authorization step, and there is no live authorization record.
5. **G-05 Rehearsal coverage (gates 6, 7). Provisional.**
   - Regulator notification was simulated.
   - Coverage of the Jurisdiction Y corridor is Unknown.
   - Whether the run used production traffic or a test load, and what the load profile was, is Unknown.
   - Only one run exists, on a weekday peak.
6. **G-06 Detect and phase timing (gate 7). Provisional.** Only detect (20 minutes), authorize (3 hours) and stabilize (9 hours) are reported. Interpret, decide, execute, verify and communicate are not. Detection came from an injected, known onset. Monitoring configuration and silent (grey) degradation are not evidenced, so real-world onset-to-detection is Unknown.
7. **G-07 Switch Catalog completeness (gate 4). Not evidenced, from the description.** P-06 lists trigger, action, decision-maker, operator and prerequisites. Execution time, communications, rollback or fail-back, evidence generated and latest test result are not described. Currency of operator access and credentials is not evidenced.
8. **G-08 Exit executability (gate 5). Provisional.**
   - There is no end-to-end exit rehearsal.
   - The export test is 84 days old at cut-off and covers only the export step.
   - Peak capacity of the substitute is Not evidenced.
   - Whether the substitute gateway is the same as the Vendor C rail is Unknown.
   - The 90-day notice means the exit cannot meet a 12-hour tolerance. That is acceptable only if the reroute switch carries the tolerance and the exit carries the sustained replacement. The exit's target execution time is not stated.
9. **G-09 Contract coverage (gate 5). Not evidenced. ⚠** Only the termination-for-convenience and transition-assistance clauses are described. Governing law, forum, renewal date, data deletion evidence, IP and licensing, subcontractors, exit fees and survival are Unknown.
10. **G-10 Jurisdiction and regulatory duties (gates 5, 6). Not evidenced. ⚠** Regulator notification duties and timelines are Unknown. So are the legal constraints on rerouting the Jurisdiction Y corridor through Vendor C or the substitute.
11. **G-11 Register and freshness (gate 8, Domain 6). Provisional.**
    - Which gaps CA-001 to CA-004 cover is Unknown.
    - "None overdue on 2026-06-15" postdates the 2026-06-10 cut-off, so it holds only if every target date falls after 06-15.
    - No freshness periods are defined. By Day 90 the T3 record will be about four months old.

## 4. 90-day backlog

All items concern Service B. The Head of payments is accountable throughout and names delegates. I have not invented named owners. Effort figures are planning estimates, about 85 person-days in total plus counsel time. Prerequisites are sequenced so items do not start before their inputs exist.

**B-01 Convert evidence and register the gaps (G-11, all)**
- Risk addressed: credit rests on unreviewed descriptions, and the new gaps are not in the register.
- Prerequisite: none.
- Action: supply the withheld artifacts for review. Map CA-001 to CA-004 to G-01 through G-11. Register the unmapped gaps with owners and dates. Confirm every target date falls after 06-15.
- Acceptance test: every gap maps to an open action or a closure.
- Evidence: reviewed artifacts, an updated register and a refreshed ledger.
- Target: Day 10 (2026-06-25). Effort: 3 days.
- Residual risk: the register can be complete and still hold wrong priorities.

**B-02 Re-approve the tolerance with an onset clock start (G-02, CA-005)**
- Risk addressed: the approved text conflicts with the measured clock.
- Prerequisite: B-01.
- Action: redraft the statement to name the observable onset event and the stop event. Add a method for fixing onset retrospectively from settlement logs.
- Acceptance test: COO-signed, version-controlled statement. A dry run on the T3 data reproduces the 9-hour figure.
- Evidence: the signed statement and the dry-run workings.
- Target: Day 30 (2026-07-15). Effort: 5 days.
- Residual risk: the onset method is untested on real incidents.
- **ESCALATE** to the COO: approval authority sits above the Head of payments.

**B-03 Common-mode dependency analysis (G-01)**
- Risk addressed: a hidden single point of failure behind the reroute and the substitute.
- Prerequisite: B-01.
- Action: map the fourth and fifth parties of Vendor A, Vendor C and the substitute. Compare networks, regions, providers, identity and jurisdictions, and request written provider responses.
- Acceptance test: a common-mode matrix with each shared dependency accepted, mitigated or fed into B-10.
- Evidence: the updated map and provider responses. Responses stay Provisional until exercised.
- Target: Day 30. Effort: 10 days.
- Residual risk: provider representations are unverified.
- Decision needed: the Head of payments decides on any shared dependency found.

**B-04 Regulatory and jurisdiction check (G-10)**
- Risk addressed: simulated notification and unknown cross-border constraints.
- Prerequisite: none, so start Day 0.
- Action: identify notification duties, timelines and channels in Jurisdictions X and Y. Identify any constraints on rerouting the Jurisdiction Y corridor and on provider-change notices. Write the timelines into the Switch Catalog communications.
- Acceptance test: a counsel or compliance position, or documented open questions with owners.
- Evidence: written position and updated catalog entries.
- Target: Day 45 (2026-07-30). Effort: 6 days plus counsel time.
- Residual risk: law may change or differ between regulators. **ESCALATE ⚠** (see section 5).

**B-05 Complete the Switch Catalog (G-07, G-06)**
- Risk addressed: switches that cannot be executed as written.
- Prerequisite: B-01.
- Action: add the missing fields for SW-001 and SW-002, tracing execution times to the T3 and T2 records. Run an access and credential currency check for each operator and for the Vendor C rail. Trace each trigger to a named monitor and alert.
- Acceptance test: every field is populated and sourced. The credential check log shows no expired items.
- Evidence: the catalog version, the check log and the monitoring configuration references.
- Target: Day 45. Effort: 6 days.
- Residual risk: monitoring that exists may still miss grey degradation until B-10.

**B-06 Authorization drills (G-03, G-04)**
- Risk addressed: the binding constraint and the simulated SW-002 authorization.
- Prerequisite: B-05 and the Head of payments' approval of a target Authorize time.
- Action: run a live SW-002 authorization with the real decision-maker, recording the decision without executing the switch. Run an unannounced out-of-hours page to the duty manager and the Head of payments.
- Acceptance test: time from page to recorded decision is within the approved target. The 6-hour ceiling is a zero-margin limit and the target should sit well below it.
- Evidence: timestamped decision records and rota logs.
- Target: Day 50 (2026-08-04). Effort: 4 days.
- Residual risk: this is T2, so it credits only the authorization step.

**B-07 Substitute gateway peak-capacity test (G-08)**
- Risk addressed: an exit that fails under volume.
- Prerequisite: B-03, which establishes whether the substitute is independent of Vendor C.
- Action: define the peak profile with a source, then test the substitute against it with pass and fail criteria.
- Acceptance test: throughput and latency meet the criteria at peak.
- Evidence: the test plan, results and the profile source.
- Target: Day 60 (2026-08-14). Effort: 12 days.
- Residual risk: a non-production test may not reflect live conditions.
- Decision needed: cost and test-window approval, and the peak definition.

**B-08 Full MSA v3 exit review and playbook (G-09)**
- Risk addressed: unreviewed obstructions to exit.
- Prerequisite: B-01.
- Action: run a Contract Exit Review of the whole agreement, with a Green, Amber or Red rating. Map each clause to a transition step, owner, notice period and evidence requirement.
- Acceptance test: the rating has three stated reasons. Every playbook step has an owner and an evidence requirement.
- Evidence: the review and the mapped playbook.
- Target: Day 45. Effort: 8 days plus counsel.
- Residual risk: an exit has still never run.
- **ESCALATE ⚠** (see section 5).

**B-09 Staged exit rehearsal (G-08)**
- Risk addressed: an unrehearsed exit.
- Prerequisite: B-07 and B-08.
- Action: rehearse export, import, reconciliation and cutover on the substitute in a non-production environment. Refresh the export test. Time each step against the exit's target execution time, which you must set first.
- Acceptance test: reconciled data with variances explained, and a timed record.
- Evidence: an exercise record that lists simulated and performed actions.
- Target: Day 80 (2026-09-03). Effort: 15 days.
- Residual risk: this is T3 at most. Notice and deletion will be simulated. Gate 5 stays Provisional Pass unless the rehearsal passes.

**B-10 Variant T3 rehearsal (G-03, G-05, G-06)**
- Risk addressed: single-run weakness and untested detection.
- Prerequisite: B-03 through B-06.
- Action: run an out-of-hours scenario with an unannounced grey-degradation inject, a fourth-party failure if B-03 finds a shared dependency, and the Jurisdiction Y corridor. Time every phase from onset.
- Acceptance test: tolerance Met or Not Met from onset. Every miss becomes a corrective action.
- Evidence: the exercise record, phase times and the list of simulated actions.
- Target: Day 85 (2026-09-08). Effort: 12 days.
- Residual risk: if regulator notification is again only simulated, gate 6 stays Provisional Pass.
- Decision needed: counsel or compliance confirms whether a regulator test channel exists.
- Capacity flag: B-09 and B-10 overlap. Decide the sequence if the teams are shared.

**B-11 Freshness, closure discipline and reassessment (G-11)**
- Risk addressed: evidence going stale.
- Prerequisite: B-01.
- Action: set freshness periods by artifact type and schedule retests. Require verification evidence before any action closes. Rerun this assessment.
- Acceptance test: an approved freshness table, and no action closed without verification evidence.
- Evidence: the table, the updated ledger and the reassessment.
- Target: Day 88 (2026-09-11). Effort: 4 days.
- Residual risk: the reassessment is only as current as its inputs.

**Expected gate movement if all items pass.**
- Gate 2 moves to Pass after B-02.
- Gate 3 moves to Pass after B-03.
- Gate 4 moves to Pass after B-05 and B-06.
- Gate 5 stays Provisional Pass unless B-07, B-08 and B-09 all pass.
- Gate 6 moves to Pass only if regulator notification is performed in B-10.
- Gate 7 moves to Pass after B-10 with full phase detail.
- Gate 8 holds.

## 5. Escalations

- **ESCALATE 1: tolerance re-approval (B-02).**
  - Issue: the approved text conflicts with the onset clock.
  - Operational consequence: results are measured against a standard the approver has not endorsed.
  - Facts and evidence required: the approval record and the rehearsal data.
  - Interim control: report all results from onset and flag the conflict.
  - Decision owner: COO.
  - Question for senior management: will the COO approve onset by Day 30?
- **ESCALATE 2: Vendor A exit rights (B-08) ⚠.**
  - Issue: governing law, forum, renewal and termination window are Unknown.
  - Operational consequence: the 90-day notice may collide with a renewal window or a dispute.
  - Facts required: the contract metadata and the dispute status.
  - Evidence required: the full MSA v3 text.
  - Interim control: issue no notice before counsel reviews.
  - Decision owner: Head of payments with counsel.
  - Question for counsel: what do the governing law and the termination and survival terms permit?
- **ESCALATE 3: regulator notification and the Jurisdiction Y corridor (B-04) ⚠.**
  - Issue: notification duties and the reroute constraints are Unknown.
  - Operational consequence: the reroute could be unlawful or the notification late.
  - Facts and evidence required: the regulatory notices and the corridor's legal basis.
  - Interim control: no corridor reroute without compliance sign-off.
  - Decision owner: compliance and counsel.
  - Question for counsel: what are the notification deadlines and the cross-border data and payment constraints in X and Y?

## 6. Decisions required by 2026-06-15

1. Accept Conditionally Demonstrated as the standing position.
2. Approve the backlog's roughly 85 person-days and name the delegates.
3. Authorize counsel engagement (B-04, B-08).
4. Have the Head of payments set the Authorize target and the exit execution time.

**[Purpose]** Identify the evidence gaps in Service B and sequence a 90-day backlog that closes them.
**[Decisions Made]** None final. The gate classifications and decision are draft until the artifacts are reviewed.
**[Outstanding Items]**
- Supply the artifacts withheld from this pack (see section 1).
- Confirm the register mapping (B-01).
- Obtain the COO and counsel decisions (section 5).
- Settle the B-09 and B-10 sequencing.

❓ needs input

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
