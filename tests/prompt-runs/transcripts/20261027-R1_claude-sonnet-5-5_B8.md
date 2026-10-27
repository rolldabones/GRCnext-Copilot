# B8 house style holds

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 692bec40732fec23541f9afbdee67660bc8c1f52aac83338fe026d7775bf9969  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 10646  **Output tokens:** 2365
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

The evidence supports a Conditionally Demonstrated position for Service B, not Demonstrated. On switches, the T3 rehearsal of 2026-05-12 (E-001) is the strongest item. It performed an end-to-end reroute to the Vendor C backup rail under a weekday-peak Vendor A outage, with only regulator notification simulated. Elapsed time was 20 minutes to detect, 3 hours to authorize and 9 hours from onset to verified stabilization, so the tolerance result is Met against 12 hours. That credit covers only the path exercised, and the pack does not say which switch ID (SW-001 or SW-002) that rehearsal exercised, so the mapping should be confirmed. SW-002 is Provisional: the T2 degrade test shows the technical step works, but authorization was simulated and no live authorization record exists. Delegation exists and is reachable, but slowly out of hours. The rehearsal ran at weekday peak, so out-of-hours authorization time is Unknown. That matters because the 3 hours of margin could erode if authorization runs long (inference, not evidenced). On exits, per the pack, the Vendor A contract gives a termination-for-convenience right on 90 days notice (E-002), and the T2 export test (E-003) shows data can be exported in usable form. The notice period cannot meet a 12-hour tolerance, so the reroute, not the contractual exit, is the within-tolerance mechanism. A substitute gateway is identified, but peak capacity is Not evidenced (E-004) and no end-to-end exit rehearsal off Vendor A exists, so gate 5 stays at Provisional Pass. ⧉ The largest gap is this untested exit for the leading concentration. Whether the Vendor C path avoids the fourth-party upstream network concentration in Jurisdiction X is also Unknown. On evidence, the tolerance statement approved by the chief operating officer names detection as the clock start, so the onset clock used in the rehearsal is not yet approved (CA-005) and gate 2 is a Provisional Pass. The Met result was measured on the stricter onset basis, but the onset was injected, so the real pre-detection interval in a live event remains unproven. Five corrective actions (CA-001 to CA-005) have owners and target dates, none overdue on 2026-06-15. Provisional Passes on gates 2 and 5 cap the decision at Conditionally Demonstrated until their evidence-conversion actions close. Evidence confidence is Moderate: the evidence is recent and includes an executed T3, but it is limited to one scenario and depends on partially tested components. These conclusions rest on the intake pack descriptions and not on direct review of the underlying artifacts.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
