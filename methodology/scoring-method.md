# Scoring method

**What this instrument is, stated plainly.** This is a **structured self-assessment**. It is not a measurement, a benchmark, an audit, a certification or a rating. Its outputs are the organization's own answers, organized against a defined structure and disciplined by an evidence rule. That structure is what makes the answers comparable over time and arguable in front of a board. It does not make them independent. A score produced here evidences the organization's position; it does not attest to it, and it should never be presented externally as though a third party had.

**Anchor vignettes are a future option, not a present feature.** Scoring bands are defined by their criteria alone. Worked vignettes anchoring each band would reduce rater drift and are noted here as a candidate for a later release; until they exist, expect inter-rater variation and treat cross-organization comparison of scores with caution.

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

The minimum is the maturity diagnostic. It names the weakest structural
domain; it does not by itself name what limits execution. Beside it every
assessment reports the **binding constraint**: the clock phase (Detect,
Interpret, Decide, Authorize, Execute, Verify, Communicate or Stabilize)
or the readiness gate that actually limits execution in the governing
scenario, with that scenario and a one-sentence basis. A service can score
4 on Switches and still be bound by a slow Authorize phase inside them. In
JSON output this is the required `binding_constraint` field.

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

- Demonstrated. Core gates pass, the capability has been exercised and
  evidence shows execution within tolerance.
- Conditionally Demonstrated. Essential design exists but one or more
  material elements remain provisional, partially tested or dependent on
  remediation.
- Not Demonstrated. A core gate fails, critical evidence is absent or
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

The clock starts at the onset of disruption, the moment the critical
service first falls outside its normal level of delivery, whether or not
anyone has noticed, and never at detection (see Clock start in
[`glossary.md`](glossary.md)). Time from onset to detection is the Detect
phase. Where onset cannot be established from evidence, the pre-detection
interval is Unknown; a Met result then needs an evidenced bound on that
interval, otherwise the result is Cannot Determine. The clock stops at
verified stabilization of the service at or above its tolerance level.

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
6. At least one severe but plausible exercise of the governing scenario
   has been completed. Discussion only (T0 or T1) for the governing
   scenario is a Fail; material actions simulated, or the scenario only
   partly covered, is a Provisional Pass at most
   ([`templates/intake-pack.md`](../templates/intake-pack.md), gate 6).
7. Evidence demonstrates whether the tolerance was met.
8. Material corrective actions have owners and target dates.

Gate effect on the decision:

- Any core gate at Fail or Unknown prevents a Demonstrated decision.
- Every one of the eight core gates is material. A Provisional Pass on
  any core gate caps the decision at Conditionally Demonstrated until its
  evidence-conversion action closes.
- Gates marked Not Applicable must carry a supported reason. An
  unsupported Not Applicable is treated as Unknown.

Gates constrain the decision. They do not by themselves set the domain
scores. A service can score well on design and still fail the readiness
decision because a gate is unmet.

## Decision caps

These caps bind the readiness decision. They are stated once here and
carried as section 8F of the v2 prompt, DECISION CAPS in the compact
edition and the decision caps in the long-form edition.

1. Any core gate at Fail or Unknown prevents Demonstrated.
2. Every one of the eight core gates is material: a Provisional Pass on
   any core gate caps the decision at Conditionally Demonstrated until its
   evidence-conversion action closes.
3. A Not Applicable gate without a supported reason is treated as
   Unknown.
4. A Fail on any core gate, or a tolerance result of Not Met, makes the
   decision Not Demonstrated.
5. Demonstrated requires a tolerance result of Met with both clock events
   stated.
6. When several services are assessed, the organization view is the
   minimum of the service-level readiness positions, naming the service
   that set the floor; never an average.
7. Contradictory evidence on a material point is recorded as Contradicted
   and cannot support credit until resolved (scoring Case 3).
8. Exercise tier caps maturity ([`exercise-tiers.md`](exercise-tiers.md)):
   T0 and T1 alone do not earn L3, save the narrow justified exception for
   a capability that genuinely could not be executed in a controlled test;
   T2 earns credit only for the component tested; T3 supports L3 for the
   path exercised and no other; L4 also needs monitoring, current metrics
   and closed corrective-action loops.

## Scoring procedure

For each service:

1. Score Pipes; Switches; Exits; Exercises; and Evidence and improvement
   from 0 to 4 using the maturity scale and the sub-elements in
   [`capability-model.md`](capability-model.md). Score Services and
   tolerances as Domain 1.
2. Assemble the capability profile from the six domain scores.
3. Compute the Constraint Level as the minimum of Pipes, Switches and
   Exits, and name the binding constraint beside it.
4. Set evidence confidence from the quality and freshness of the
   supporting evidence, weighted by Domains 5 and 6.
5. Classify the eight gates.
6. Derive the readiness decision from the gates, the Constraint Level and
   the exercise evidence, within the decision caps.
7. State the tolerance result with clock-start (onset) and clock-stop
   events.

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
  path, achieving verified stabilization 9 hours after the onset of
  disruption against the 12-hour tolerance. Onset was established from
  system records; the time to detection is counted inside the Detect
  phase. The exit path was exercised only to T2.
- Evidence is version-controlled, traceable and under 6 months old.
  Tolerance breach and dependency drift are monitored with defined
  triggers, and timing metrics are current from the latest rehearsal.
  Corrective actions from the exercise have owners and dates. One is
  overdue.

Scoring:

- Domain 1 Services and tolerances: L3. Defined, owned, approved,
  measurable and tested, with breach detection monitored against
  defined triggers and current metrics, but one corrective action is
  overdue, so the corrective-action loop is not closed and cap 8 holds
  the domain below L4.
- Domain 2 Pipes: L3. Mapped and current, concentration identified, map
  drift monitored with current metrics; not L4 for the same overdue
  corrective action (cap 8).
- Domain 3 Switches: L3. Executable, delegated, evidenced, invocation
  trigger defined and monitored, exercised at T3 within tolerance with
  current timing metrics; not L4 for the same overdue corrective action
  (cap 8).
- Domain 4 Exits: L2. Rights, substitute capacity and data portability
  are in place, but the exit path was rehearsed only to T2. T3 supports
  L3 only for the path exercised ([`exercise-tiers.md`](exercise-tiers.md)),
  so end-to-end execution is not yet shown and the domain stays at L2.
- Domain 5 Exercises: L3. A T3 severe-but-plausible exercise on the
  switch path with timing and remediation, but the exit path is not yet
  rehearsed end to end.
- Domain 6 Evidence and improvement: L3. Traceable and fresh, but one
  overdue corrective action means the closure loop is not fully clean,
  which caps this below L4.

Results:

- Capability profile: 3, 3, 3, 2, 3, 3.
- Constraint Level: minimum of Pipes 3, Switches 3, Exits 2 = 2.
- Binding constraint: gate 5 for the exit path. The exit off Vendor A is
  not yet shown executable end to end. The walkthrough does not give
  phase times for the switch path, so no clock phase is named there.
- Evidence confidence: Moderate. Strong and fresh evidence overall, but
  the exit path lacks end-to-end execution evidence and one action is
  overdue.
- Gates: gates 1 to 4 Pass, gate 5 Provisional Pass, exit exists with
  rights and portability but rehearsed only to T2, gates 6 and 7 Pass,
  each evaluated once against the governing scenario (the Vendor A
  outage on the switch path), gate 8 Provisional Pass
  because of the overdue action.
- Readiness decision: Conditionally Demonstrated. The switch path is
  Demonstrated within tolerance. The exit path and the overdue action
  hold the overall decision at Conditionally Demonstrated.
- Tolerance result: Met for the governing scenario. Clock started at the
  onset of Vendor A unavailability, established from system records, not
  at its detection. Clock stopped at verified
  service stabilization on the backup path at 9 hours. The exit path is
  not the governing scenario; its fit within tolerance is untested.

Note how the fatal-weakness logic works. Even though Pipes and Switches
score L3, the exit path pulls the Constraint Level to 2, and the
binding constraint, gate 5, says what to fix first: rehearse the exit end
to end. The Provisional Pass on gates 5 and 8 holds the decision at
Conditionally Demonstrated. Nothing is averaged. The weakest structural
domain governs the constraint, the binding constraint names what limits
execution and the gates govern the decision.

Final Liability rests with the Human.
