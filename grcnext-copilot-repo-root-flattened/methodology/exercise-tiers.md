# Exercise tiers and the execution clock

A tabletop conversation is not execution. This file defines the exercise
tiers that separate discussion from performance, and the execution clock
that measures the full sequence from detection to stabilization. It is the
long form of Section 10 of the full prompt.

## Why tiers exist

The maturity scale awards L3 Exercised only when a capability has been
demonstrated under a severe but plausible scenario. Without a tier scale,
a facilitated discussion and a live invocation both get called an
exercise, and the readiness decision loses meaning. The tiers make the
depth of the demonstration explicit and gate the maturity credit.

## The tiers

- T0 Document walkthrough. Someone reads the runbook aloud or reviews the
  plan on paper. Confirms the plan exists and is internally coherent.
  Proves nothing about execution.
- T1 Facilitated tabletop. Participants talk through a scenario and state
  what they would do. Surfaces gaps in roles, authority and sequence.
  Still entirely verbal.
- T2 Controlled technical or operational test. A specific component is
  actually operated in a controlled setting. A switch is thrown in a test
  environment, a data export is actually produced, a failover is actually
  triggered on a nonproduction path.
- T3 End-to-end rehearsal. The full path is exercised across teams and
  systems under realistic conditions, with timing captured across the
  execution clock. Simulated in places, but the sequence runs end to end.
- T4 Live invocation or actual event. The capability was invoked in
  production, either in a planned live exercise or because a real
  disruption occurred.

## Tier and maturity

- T0 and T1 alone do not earn L3 for the exercised capability. They can
  support L2 Designed by confirming the design is coherent.
- T2 earns credit for the specific component tested, but not for the
  end-to-end path it does not cover.
- T3 supports L3 for the path exercised, with timing and remediation
  documented.
- T4 is the strongest execution evidence and supports L3, and contributes
  to L4 when combined with monitoring, current metrics and closed
  corrective-action loops.

The single exception in the maturity rules: do not withhold L3 for a
talk-only tier if the claimed capability genuinely could not be executed
in a controlled test. That exception is narrow and must be justified, not
assumed.

## Simulated versus performed

Every exercise record states, action by action, which parts were
simulated and which were actually performed. This is not a formality. A
rehearsal that simulated vendor cooperation, simulated executive
authorization and simulated the data migration has tested almost nothing
that matters, even if it ran end to end on paper.

The Copilot reports the split explicitly and does not let a high tier
label conceal that the decisive steps were simulated.

## The execution clock

A switch that can be operated technically in two hours can still fail a
12-hour tolerance if authorization and communication take another 18
hours. GRCnext™ measures the complete clock, not just the technical step.

The eight phases:

1. Detect. The condition is noticed.
2. Interpret. The condition is understood well enough to act.
3. Decide. A decision on what to do is made.
4. Authorize. The decision is authorized by someone with the right.
5. Execute. The switch or exit is operated.
6. Verify. The result is confirmed.
7. Communicate. Affected parties are informed.
8. Stabilize. The service reaches a stable, sustainable state.

Rules for using the clock:

- The tolerance clock starts at the event defined in the impact tolerance,
  usually detection, not at the moment the technical step begins.
- Capture elapsed time for each phase where material.
- Do not report only technical execution time when decision or
  authorization time is material. The most common hidden failure is a
  fast Execute phase behind a slow Authorize phase.
- The tolerance result is Met only when Stabilize completes within the
  approved tolerance, measured from the correct clock-start event.

## Recording the result

An exercise record, per
[`../templates/exercise-plan.md`](../templates/exercise-plan.md) and the
exercise-and-evidence section of the Service Dossier, captures the
scenario, tier, date, participants, actions simulated, actions performed,
elapsed times across the clock, tolerance result, evidence pack,
findings, corrective actions and retest status.

A pass is only as strong as the tier it was achieved at and the honesty of
the simulated-versus-performed split. State both.

Final Liability rests with the Human.
