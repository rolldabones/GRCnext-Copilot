# Input pack: Service M production line

Synthetic example. Neutral labels. Not legal, safety or regulatory advice.

This is the intake pack, filled in, that produced
[`assessment.md`](assessment.md) and
[`assessment-result.json`](assessment-result.json). It follows
[`../../templates/intake-pack.md`](../../templates/intake-pack.md).
Artifact IDs (M-nn) name what was supplied; evidence IDs (E-Mn) point to
the ledger extract in the assessment.

## Service facts

- Service: Service M, continuous production on the primary line.
- Accountable owner: Plant operations director.
- Customers: Downstream manufacturing customers under supply contracts.
- Impact tolerance: 24 hours. Clock-start (onset) event: an unplanned
  production stop. Clock stop: verified resumption of in-specification
  output.
- Jurisdictions: Jurisdiction X (plant), with upstream exposure to
  Jurisdiction Z.
- Evidence cut-off: 2026-06-16.
- Decision due: 2026-06-20 (assessment date).

## Gate 1. Service and owner defined

| ID | Artifact | What it establishes |
|---|---|---|
| M-01 | Service definition for the primary line | Outcome, scope (secondary line excluded) and material harms, including safety |
| M-02 | Accountability record | Plant operations director accountable |

## Gate 2. Tolerance approved and measurable

| ID | Artifact | What it establishes |
|---|---|---|
| M-03 | Impact tolerance statement approved by the plant operations director, endorsed by the commercial function | 24 hours from an unplanned stop (onset) to verified resumption of in-specification output |

## Gate 3. Dependencies mapped

| ID | Artifact | What it establishes |
|---|---|---|
| M-04 | End-to-end dependency map, verified 2026-06-01 | Vendor R (raw material) and Vendor S (control) as leading concentrations |
| M-05 | Fourth-party note on Vendor R's single mine in Jurisdiction Z | A material fourth-party concentration |

## Gate 4. Switch authority available

| ID | Artifact | What it establishes |
|---|---|---|
| M-06 | Switch catalog for SW-M1 to SW-M3 | Trigger, action, decision-maker and operator for safety stop, degraded control and buffer drawdown |
| M-07 | Safety-stop authority record | Shift supervisor authority; safety officer can stop unilaterally |

## Gate 5. Executable exit for the leading concentration

| ID | Artifact | What it establishes |
|---|---|---|
| M-08 | Supply agreement with Vendor R | Sourcing elsewhere is permitted on default; no alternate contracted |
| M-09 | Supplier qualification estimate (E-M4) | Qualification takes 3 to 6 months and is unfunded; no alternate supplier is evidenced (Fail) |

## Gate 6. Severe but plausible exercise completed

| ID | Artifact | What it establishes |
|---|---|---|
| M-10 | Shutdown log and alarm record, real controlled stop 2026-02-11 (E-M1) | Safety stop performed within minutes (T4) |
| M-11 | Tabletop notes, control-loss scenario 2026-05-05 (E-M2) | T1 only; manual control discussed, not performed; no supplier-loss exercise (Fail) |

## Gate 7. Evidence shows tolerance result

| ID | Artifact | What it establishes |
|---|---|---|
| M-12 | Buffer-stock representation (E-M3) | Buffer covers about 18 hours, never tested to exhaustion; no timed record of the governing scenario exists (Unknown) |

## Gate 8. Corrective actions have owners and dates

| ID | Artifact | What it establishes |
|---|---|---|
| M-13 | Findings list from the tabletop | Actions identified but not owned, dated or scheduled (Fail) |

## Not supplied

- A qualification record for a second raw-material supplier.
- A supplier-loss exercise or a buffer-runway test.
- A live manual-control test.
- An owned and dated corrective-action register.

Final Liability rests with the Human.
