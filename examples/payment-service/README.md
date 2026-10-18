# Worked example: real-time payment service

This example shows GRCnext™ applied to a financial-services critical
service. It is synthetic. All names are neutral labels. Nothing here
describes a real organization, and nothing here is legal or regulatory
advice.

## Scenario

A retail bank operates Service B, a real-time payment service that lets
customers send and receive funds within seconds. The service depends on a
single external payment gateway, Vendor A, which is the leading
concentration dependency. If Vendor A becomes unavailable, customers
cannot move money in real time, which causes rapid consumer harm and
reputational damage.

The bank has an approved impact tolerance of 12 hours for Service B,
measured from onset of disruption (the moment real-time settlement first
falls outside its normal level of delivery) to verified stabilization.
The statement on record named detection as the clock start, so the onset
clock awaits re-approval (corrective action CA-005).

## What this example demonstrates

- A completed Service Dossier with all six core sections. See
  [`service-dossier.md`](service-dossier.md).
- The synthetic evidence inputs that produced the assessment, keyed to
  the eight gates. See [`input-pack.md`](input-pack.md).
- A scored assessment with the four results plus the tolerance result,
  the eight gates, the binding constraint and an evidence ledger extract.
  See [`assessment.md`](assessment.md), and the same assessment as an
  `assessment_result` payload in
  [`assessment-result.json`](assessment-result.json).
- The working registers: [`capa-register.csv`](capa-register.csv),
  [`evidence-ledger.csv`](evidence-ledger.csv) and
  [`switch-catalog.csv`](switch-catalog.csv).
- How a reroute switch that met tolerance in rehearsal still leaves the
  service at Conditionally Demonstrated: the exit path is rehearsed only
  to T2 and the onset clock awaits re-approval.
- How the execution clock catches a fast technical step sitting behind a
  slower authorization step.

## The switches in play

Two material switches:

- SW-001: reroute payment flow to the Vendor C backup rail. Failing back
  to the primary rail once Vendor A is restored and verified is SW-001's
  rollback, not a separate switch.
- SW-002: degrade to delayed batch settlement.

## The exit in play

- Migrate Service B off Vendor A to a substitute gateway. Contractual
  rights exist and data portability was tested, but the full exit has
  only been exercised to a controlled technical test, not end to end.

## How to read the result

Read the assessment top to bottom. The capability profile shows the
individual domain scores (3, 3, 3, 2, 3, 3). The Constraint Level is the
minimum of Pipes, Switches and Exits: 2, set by Exits. Beside it the
binding constraint names what actually limits execution: the Authorize
phase (3 hours of 9) for the reroute scenario and gate 5 (executable
exit) for the exit scenario. The evidence confidence (Moderate) and the
readiness decision (Conditionally Demonstrated, capped by Provisional
Passes on gates 2 and 5) tell you how far the demonstration actually
went, and the tolerance result states the clock-start and clock-stop
events. Five corrective actions are open (CA-001 to CA-005), none
overdue. Nothing is averaged.

Final Liability rests with the Human.
