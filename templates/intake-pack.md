# Intake Pack: [service name]

Status: [↻ draft] / [⇥ pending review] / [✓ final]
Prepared by: [name or role]
Date: [YYYY-MM-DD, Asia/Seoul]

Fill this pack for one critical service and supply it to GRCnext™
Copilot with the artifacts it lists. It is keyed to the eight core
readiness gates in
[`../methodology/scoring-method.md`](../methodology/scoring-method.md).
Give every artifact a stable ID and say what it establishes. Prefer
evidence of actual execution over statements of intended procedure. Use
neutral labels such as Vendor A and Jurisdiction X. Do not paste
secrets, credentials or protected personal data. A filled example is
[`../examples/payment-service/input-pack.md`](../examples/payment-service/input-pack.md).

Every gate can also be classified Unknown (the evidence does not settle
it) or Not Applicable (only with a supported reason; an unsupported Not
Applicable is treated as Unknown). A Fail or Unknown on any gate
prevents Demonstrated; a Provisional Pass on any gate caps the decision
at Conditionally Demonstrated until its evidence-conversion action
closes.

The Pass, Provisional Pass and Fail lines under each gate are guidance
for filling the pack, read from the gate text; they are not additional
rules. The Copilot classifies each gate, and where a line here differs
from `methodology/scoring-method.md`, the method governs.

## Service facts

- Service (the outcome a customer receives, not an asset):
- Accountable owner (named role):
- Customers and stakeholders:
- Impact tolerance (hours):
- Clock-start (onset) event (the observable moment the service first
  falls outside its normal level of delivery, whether or not anyone has
  noticed; not detection):
- Clock-stop event (verified stabilization at or above tolerance level):
- Material jurisdictions:
- Evidence cut-off date:
- Decision due (date and decision owner):

## Gate 1. Service and owner defined

- Question: Is the critical service defined by its outcome, scope and
  harms, with a named accountable owner?
- Artifacts to supply: service definition statement; accountability
  record or RACI naming the owner.
- Pass: both artifacts exist, are current and agree.
- Provisional Pass: the service is defined but ownership rests on a
  representation or a draft record.
- Fail: no defined service or no accountable owner.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Gate 2. Tolerance approved and measurable

- Question: Is there an approved impact tolerance in hours, with the
  onset clock-start event and the clock-stop event stated?
- Artifacts to supply: approved tolerance statement; approval record of
  the authority with standing to accept the risk; measurement method.
- Pass: approved on record, measured from onset to verified
  stabilization, with both clock events stated.
- Provisional Pass: approved but not measurable as stated (for example
  the approved text starts the clock at detection), or approval pending.
- Fail: no tolerance, or no approval.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Gate 3. Dependencies mapped

- Question: Are material dependencies mapped end to end, with
  concentrations flagged and the map's verification date known?
- Artifacts to supply: dependency map across people, process, technology,
  data, facilities, third and material fourth parties, jurisdictions and
  manual alternatives; date of last verification.
- Pass: map current and verified, concentrations identified.
- Provisional Pass: map exists but is unverified, partial or past its
  re-verification date.
- Fail: no map, or the leading concentration is not identified.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Gate 4. Switch authority available

- Question: Can the authority to invoke each essential switch be
  exercised when needed, including out of hours?
- Artifacts to supply: switch catalog
  ([`switch-catalog.csv`](switch-catalog.csv)); delegation records;
  out-of-hours rota.
- Pass: authority delegated, reachable and shown in an exercise or event.
- Provisional Pass: authority delegated on paper but not shown, or shown
  only in simulation.
- Fail: no one with authority, or authority outside existing delegation.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Gate 5. Executable exit for the leading concentration

- Question: Can the service leave or replace its leading concentration
  dependency while keeping the service?
- Artifacts to supply: contractual exit and transition rights; data
  portability test; substitute arrangement and capacity evidence; exit
  rehearsal record.
- Pass: exit rehearsed for the path relied on, substitute capacity
  confirmed, data proven portable.
- Provisional Pass: rights and partial tests exist (for example a T2 data
  export) but no end-to-end rehearsal or confirmed capacity.
- Fail: exit described only, or no substitute.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Gate 6. Severe but plausible exercise completed

- Question: Has at least one severe but plausible scenario been exercised,
  with the simulated-versus-performed split recorded?
- Artifacts to supply: exercise plan and record with tier (T0 to T4),
  participants, actions simulated and actions performed.
- Pass: an exercise of the governing scenario at a tier that supports the
  credit claimed.
- Provisional Pass: exercised, but material actions simulated or the
  scenario only partly covered.
- Fail: no exercise, or discussion only for the governing scenario.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Gate 7. Evidence shows tolerance result

- Question: Does evidence show whether the tolerance was met, measured
  from onset?
- Artifacts to supply: timing record across Detect, Interpret, Decide,
  Authorize, Execute, Verify, Communicate and Stabilize, with the onset
  and stop events.
- Pass: a timed record states both clock events and supports Met or Not
  Met.
- Provisional Pass: a record exists but a clock event or phase rests on
  estimate.
- Fail: no timing evidence. Where onset cannot be established the
  pre-detection interval is Unknown, and a Met result needs an evidenced
  bound on it.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Gate 8. Corrective actions have owners and dates

- Question: Does every material corrective action have an owner and a
  target date, and is none overdue?
- Artifacts to supply: corrective-action register
  ([`capa-register.csv`](capa-register.csv)).
- Pass: every material action owned and dated, none overdue.
- Provisional Pass: actions owned but some without firm dates, or an
  action overdue with a recorded escalation.
- Fail: actions identified but not owned or not dated.

| ID | Artifact | What it establishes |
|---|---|---|
| | | |

## Not supplied

List what the pack does not contain and why. Absence is a finding, not a
blank.

-

Final Liability rests with the Human.
