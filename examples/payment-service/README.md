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
measured from detection of a material disruption to verified
stabilization.

## What this example demonstrates

- A completed Service Dossier with all six core sections. See
  [`service-dossier.md`](service-dossier.md).
- A scored assessment with the four results, the eight gates, an evidence
  ledger and the three-part conclusion. See
  [`assessment.md`](assessment.md).
- How a capability that scores well on switches can still land at
  Conditionally Demonstrated because the exit path is not rehearsed end
  to end and a corrective action is overdue.
- How the execution clock catches a fast technical step sitting behind a
  slower authorization step.

## The switches in play

- Reroute payment flow to a backup rail.
- Degrade to delayed batch settlement.
- Fail back to the primary rail once Vendor A is restored and verified.

## The exit in play

- Migrate Service B off Vendor A to a substitute gateway. Contractual
  rights exist and data portability was tested, but the full exit has
  only been exercised to a controlled technical test, not end to end.

## How to read the result

Read the assessment top to bottom. The capability profile shows the
individual domain scores. The Constraint Level is the minimum of Pipes,
Switches and Exits. The evidence confidence and readiness decision tell
you how far the demonstration actually went, and the tolerance result
states the clock-start and clock-stop events. Nothing is averaged.

Final Liability rests with the Human.
