# Input pack: Service K agentic resolution

Synthetic example. Neutral labels. Not legal or regulatory advice.

This is the intake pack, filled in, that produced
[`assessment.md`](assessment.md) and
[`assessment-result.json`](assessment-result.json). It follows
[`../../templates/intake-pack.md`](../../templates/intake-pack.md). The
AI overlay applies. Artifact IDs (K-nn) name what was supplied; evidence
IDs (E-Kn) point to the ledger extract in the assessment.

## Service facts

- Service: Service K, automated resolution of a high-volume operational
  queue by Agent A.
- Accountable owner: Head of operations. Named human principal for Agent
  A: the operations automation manager.
- Customers: End customers whose requests are in the queue.
- Impact tolerance: 1 hour. Clock-start (onset) event: the first
  materially incorrect or stalled automated action. Clock stop: verified
  human control of the queue.
- Jurisdictions: Jurisdiction X.
- Evidence cut-off: 2026-06-20.
- Decision due: 2026-06-25 (assessment date).

## Gate 1. Service and owner defined

| ID | Artifact | What it establishes |
|---|---|---|
| K-01 | Service definition and intended-use statement for Agent A | Outcome, scope (specialist-team items excluded) and material harms |
| K-02 | Accountability record | Head of operations accountable; operations automation manager named as human principal |

## Gate 2. Tolerance approved and measurable

| ID | Artifact | What it establishes |
|---|---|---|
| K-03 | Impact tolerance statement approved by the head of operations, endorsed by the risk function | 1 hour from the first materially incorrect or stalled action (onset) to verified human control |

## Gate 3. Dependencies mapped

| ID | Artifact | What it establishes |
|---|---|---|
| K-04 | End-to-end dependency map, verified 2026-06-05 | Vendor M as the leading concentration, the shared cloud provider as fourth party, Agent A as a single point |

## Gate 4. Switch authority available

| ID | Artifact | What it establishes |
|---|---|---|
| K-05 | Switch catalog for SW-K1 to SW-K4 | Trigger, action, decision-maker and operator for kill, tool-access revocation, rollback and degrade |
| K-06 | Delegation record for the kill switch | Kill authority is immediate; the risk function can trigger it unilaterally |

## Gate 5. Executable exit for the leading concentration

| ID | Artifact | What it establishes |
|---|---|---|
| K-07 | Vendor M terms and portability note | Termination is permitted; prompts, configuration and logs are exportable |
| K-08 | Alternate-model integration note (E-K4) | An alternate is integrable but decision quality is Not evidenced; substitution is described, not built (Fail) |

## Gate 6. Severe but plausible exercise completed

| ID | Artifact | What it establishes |
|---|---|---|
| K-09 | T3 stop-and-rollback test record, 2026-06-12, with phase timing (E-K1, E-K2) | Kill switch halted Agent A in under 5 minutes; rollback to human handling performed; customer communication simulated |
| K-10 | T2 tool-access revocation test record, 2026-05-28 | Revocation works for the technical step |
| K-11 | T1 tabletop notes for the human-in-the-loop degrade mode | Degrade mode discussed only; reviewer capacity at volume unproven |

## Gate 7. Evidence shows tolerance result

| ID | Artifact | What it establishes |
|---|---|---|
| K-09 | Timing record within the T3 test record (E-K2, E-K3) | Clock start at onset (first materially incorrect automated action); detection at 25 minutes; verified human control at about 90 minutes: Not Met against 1 hour |
| K-12 | Monitoring alerts and disable event log | Corroborates the detection time and the kill-switch time |

## Gate 8. Corrective actions have owners and dates

| ID | Artifact | What it establishes |
|---|---|---|
| K-13 | Corrective-action list from the hotwash | Actions identified with owners; some lack firm target dates (Provisional Pass) |

## AI overlay inputs

| ID | Artifact | What it establishes |
|---|---|---|
| K-14 | Tool-access and permission configuration for Agent A | Agent A can act directly on downstream systems at volume |
| K-15 | Decision and action logs | Logging and traceability retained |

## Not supplied

- A validation run for the alternate model.
- A timed test of human control within 1 hour.
- A volume test of the human-in-the-loop degrade mode.

Final Liability rests with the Human.
