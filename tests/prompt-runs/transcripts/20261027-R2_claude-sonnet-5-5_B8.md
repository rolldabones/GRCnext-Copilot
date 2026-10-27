# B8 house style holds

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 692bec40732fec23541f9afbdee67660bc8c1f52aac83338fe026d7775bf9969  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 10818  **Output tokens:** 2328
**Truncated:** no

## User message

~~~~text
Summarize the switch, exit and evidence findings in one paragraph.

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

Working from the intake pack descriptions only, without having inspected the underlying artifacts, Service B shows moderate evidence confidence and a Conditionally Demonstrated position under the GRCnext™ decision caps. On switches, the T3 rehearsal of 2026-05-12 (E-001) is the strongest evidence: with clock start at the injected Vendor A outage, detection came at 20 minutes, Authorize took 3 hours and verified stabilization came at 9 hours, which meets the 12-hour tolerance with a 3-hour margin. That result covers one scenario (a weekday-peak outage), and the regulator notification was simulated. The T2 degrade test (P-12) supports only the technical step of SW-002, since its authorization step was simulated and no live authorization record exists. Delegation covers both switches, but out-of-hours authority is slow, and that is the phase most likely to erode the margin. On exits, the leading concentration, Vendor A, has a contractual termination-for-convenience right on 90 days notice with transition assistance (E-002), a T2 export test (E-003) covering the export step only, and an identified substitute gateway (E-004) whose peak capacity is Not evidenced. No end-to-end exit rehearsal off Vendor A has been supplied, and a 90-day contractual exit does not itself operate inside a 12-hour tolerance, so the tolerance is met through the reroute switch and not through the exit. Gate 5 therefore stays at Provisional Pass, and the unassessed fourth-party concentration at Vendor A's upstream network provider in Jurisdiction X adds residual exposure. On evidence, gate 2 is also a Provisional Pass: the approved tolerance text names detection as the clock start, so the onset clock used in the rehearsal is not yet approved (CA-005). Five corrective actions (CA-001 to CA-005) have owners and dates and none is overdue. The evidence-conversion actions are an end-to-end exit rehearsal, a substitute gateway peak-capacity test, a re-approved onset-based tolerance statement and a live SW-002 authorization record. ESCALATE: the regulator notification step was only simulated and the Jurisdiction Y corridor involves cross-border payments, so compliance or counsel should confirm notification timing and any jurisdictional constraint on the reroute and exit paths before the 2026-06-15 decision.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
