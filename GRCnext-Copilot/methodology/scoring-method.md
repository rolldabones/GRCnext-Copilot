# Scoring method

This file defines how GRCnext™ Copilot converts evidence into scores and
a decision. It is the long form of Sections 6, 7 and 8 of the full
prompt. The design goal is that a fatal weakness is never averaged away
and that capability, confidence and constraint stay separate.

## Maturity scale

Each of the six domains is scored from 0 to 4.

- L0 Unowned. The service or capability is materially undefined.
  Ownership, tolerance or essential operating arrangements are absent or
  not demonstrated.
- L1 Described. The service or capability is identified and has
  preliminary documentation, but execution depends substantially on
  individuals, assumptions or incomplete arrangements.
- L2 Designed. Responsibilities, procedures, dependencies and intended
  actions are documented. Material gaps remain in authority,
  integration, testing or evidence.
- L3 Exercised. The capability has been exercised under a severe but
  plausible scenario. Material actions, timing, evidence and remediation
  are documented.
- L4 Instrumented. The capability is monitored, periodically exercised
  and managed through current metrics, defined triggers, verified
  evidence and closed corrective-action loops.

Two rules prevent inflation:

- Do not award L3 solely for a discussion-based tabletop, unless the
  claimed capability genuinely could not be executed in a controlled
  test.
- Do not award L4 solely because dashboards exist.

## The four results

Every assessment reports four separate results plus a tolerance result.
They answer different questions and must not be merged.

### A. Capability profile

Show all six domain scores individually. This is what the organization
appears able to do. Averaging is prohibited because it hides the one
weak component that can defeat optionality.

### B. Constraint level

Constraint Level = minimum of Pipes, Switches and Exits.

This identifies the weakest structural component of service optionality.
Optionality requires all three: a mapped dependency you cannot switch or
exit is not optionality, and a switch you cannot evidence is not
optionality. The minimum captures that. It is reported as the Constraint
Level, not as the whole score, so the capability profile remains visible
alongside it.

### C. Evidence confidence

Rate how strongly the conclusion is supported.

- High. Current, independently verifiable evidence, including observed or
  executed performance.
- Moderate. Coherent evidence with limited testing, aging or
  verification gaps.
- Low. Substantial reliance on drafts, representations, assumptions or
  stale evidence.
- Indeterminate. Evidence is insufficient or contradictory.

Evidence confidence is set mainly by Domains 5 and 6. A high capability
profile resting on low-confidence evidence is reported as exactly that.

### D. Readiness decision

- Demonstrated. Core gates pass, the capability has been exercised, and
  evidence shows execution within tolerance.
- Conditionally Demonstrated. Essential design exists but one or more
  material elements remain provisional, partially tested or dependent on
  remediation.
- Not Demonstrated. A core gate fails, critical evidence is absent, or
  execution has not been shown within tolerance.

A capability is never called Demonstrated merely because its documents
look complete.

### E. Tolerance result

- Met.
- Not Met.
- Not Tested.
- Cannot Determine.

Always state the event that started the clock and the event that stopped
it. A tolerance result with no clock-start and clock-stop event is
incomplete.

## Readiness gates

Eight core gates. Each is classified Pass, Provisional Pass, Fail,
Unknown or Not Applicable. Classify each gate exactly once per service,
evaluated against the governing severe but plausible scenario; do not
issue split or hybrid gate states.

1. Critical service and owner are defined.
2. Impact tolerance is approved and measurable.
3. Material dependencies are mapped.
4. Authority to invoke essential switches is available.
5. At least one executable exit exists for the leading concentration
   dependency.
6. At least one severe but plausible exercise has been completed.
7. Evidence demonstrates whether the tolerance was met.
8. Material corrective actions have owners and target dates.

Gate effect on the decision:

- Any core gate at Fail or Unknown prevents a Demonstrated decision.
- A Provisional Pass on a material gate caps the decision at
  Conditionally Demonstrated until the evidence-conversion action
  closes.
- Gates marked Not Applicable must carry a supported reason. An
  unsupported Not Applicable is treated as Unknown.

Gates constrain the decision. They do not by themselves set the domain
scores. A service can score well on design and still fail the readiness
decision because a gate is unmet.

## Scoring procedure

For each service:

1. Score Pipes; Switches; Exits; Exercises; and Evidence and improvement
   from 0 to 4 using the maturity scale and the sub-elements in
   [`capability-model.md`](capability-model.md). Score Services and
   tolerances as Domain 1.
2. Assemble the capability profile from the six domain scores.
3. Compute the Constraint Level as the minimum of Pipes, Switches and
   Exits.
4. Set evidence confidence from the quality and freshness of the
   supporting evidence, weighted by Domains 5 and 6.
5. Classify the eight gates.
6. Derive the readiness decision from the gates, the Constraint Level and
   the exercise evidence.
7. State the tolerance result with clock-start and clock-stop events.

When multiple services are assessed, the organization view takes the
minimum of the service-level readiness positions and lists which service
set the floor. Do not average across services.

## Worked walkthrough

Synthetic single service. Neutral labels.

Inputs, in summary:

- Service B is a customer-facing outcome with a named owner and a
  12-hour impact tolerance approved by the accountable executive.
- Dependencies are mapped and current. A single provider, Vendor A, is
  the leading concentration dependency.
- Two switches exist with delegated out-of-hours authority and current
  access. Rollback is defined. Execution can be evidenced.
- One exit exists to move off Vendor A. Contractual rights are present.
  Substitute capacity is identified. Data portability was tested. The
  exit was rehearsed to a controlled technical test, not end to end.
- One severe but plausible exercise was completed at T3 for the switch
  path, achieving stabilization in 9 hours against the 12-hour
  tolerance. The exit path was exercised only to T2.
- Evidence is version-controlled, traceable and under 6 months old.
  Tolerance breach and dependency drift are monitored with defined
  triggers, and timing metrics are current from the latest rehearsal.
  Corrective actions from the exercise have owners and dates. One is
  overdue.

Scoring:

- Domain 1 Services and tolerances: L4. Defined, owned, approved,
  measurable and tested, with breach detection monitored against
  defined triggers and current metrics.
- Domain 2 Pipes: L4. Mapped and current, concentration identified, map
  drift monitored with current metrics.
- Domain 3 Switches: L4. Executable, delegated, evidenced, invocation
  trigger defined and monitored, exercised at T3 within tolerance with
  current timing metrics.
- Domain 4 Exits: L3. Rehearsed only to T2 for the exit path, so
  execution end to end is not yet shown, though rights, substitute
  capacity and data portability are in place.
- Domain 5 Exercises: L3. A T3 severe-but-plausible exercise on the
  switch path with timing and remediation, but the exit path is not yet
  rehearsed end to end.
- Domain 6 Evidence and improvement: L3. Traceable and fresh, but one
  overdue corrective action means the closure loop is not fully clean,
  which caps this below L4.

Results:

- Capability profile: 4, 4, 4, 3, 3, 3.
- Constraint Level: minimum of Pipes 4, Switches 4, Exits 3 = 3.
- Evidence confidence: Moderate. Strong and fresh evidence overall, but
  the exit path lacks end-to-end execution evidence and one action is
  overdue.
- Gates: gates 1 to 4 Pass, gate 5 Provisional Pass, exit exists with
  rights and portability but rehearsed only to T2, gate 6 Pass for the
  switch path, gate 7 Pass for the switch path, gate 8 Provisional Pass
  because of the overdue action.
- Readiness decision: Conditionally Demonstrated. The switch path is
  Demonstrated within tolerance. The exit path and the overdue action
  hold the overall decision at Conditionally Demonstrated.
- Tolerance result: Met for the switch scenario. Clock started at
  detection of Vendor A unavailability. Clock stopped at verified
  service stabilization on the backup path at 9 hours. Not Tested end to
  end for the exit scenario.

Note how the fatal-weakness logic works. Even though four domains score
at the top, the exit path pulls the Constraint Level to 3 and the
overdue action and untested exit hold the decision at Conditionally
Demonstrated. Nothing is averaged. The single weakest structural
component governs the constraint, and the gates govern the decision.

Final Liability rests with the Human.
