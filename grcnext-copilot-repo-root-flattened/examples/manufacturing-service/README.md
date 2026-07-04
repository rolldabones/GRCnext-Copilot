# Worked example: manufacturing production service

This example shows GRCnext™ applied to a physical, safety-critical
critical service. It is synthetic. All names are neutral labels. Nothing
here describes a real organization, and nothing here is legal, safety or
regulatory advice.

## Scenario

A manufacturer operates Service M, continuous production on a primary
line that converts a single raw material into finished product. Two
concentrations dominate. First, a single raw-material supplier, Vendor R.
Second, the line control system supplied and maintained by a single
automation vendor, Vendor S, covering the SCADA and MES layer.

If Vendor R cannot deliver, or if the Vendor S control system fails,
production stops. A stopped line has a safety dimension as well as a
commercial one, because an uncontrolled stop can damage equipment or
create hazards.

The manufacturer has an approved impact tolerance of 24 hours of
production stoppage for Service M before contractual penalties and
downstream customer harm become material.

## What this example demonstrates

- A completed Service Dossier for a physical service where a switch may be
  to stop safely rather than to keep running. See
  [`service-dossier.md`](service-dossier.md).
- A scored assessment that lands at Not Demonstrated because a core gate
  fails. See [`assessment.md`](assessment.md).
- The difference between a safety stop, which is well rehearsed, and an
  exit, which does not exist because no second raw-material supplier is
  qualified.
- How a T1 tabletop does not earn L3 for the exercised capability.

## The switches in play

- Stop the line safely under control (the priority safety switch).
- Switch to manual or degraded control if the automation layer is
  impaired.
- Draw down buffer stock of raw material to extend runway during a
  supplier disruption.

## The exit in play

- Qualify and switch to a second raw-material supplier. This exit is
  described but not built. No second supplier is qualified, so there is no
  executable exit for the leading concentration.

## How to read the result

The safety switch is strong, but optionality requires Pipes, Switches and
Exits together. A missing exit for the leading concentration is a core
gate failure, and the readiness decision reflects it regardless of how
good the safety stop is.

Final Liability rests with the Human.
