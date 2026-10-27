# Scoring cases

This file pins the rubric. Each case supplies inputs and states the
result GRCnext™ Copilot should produce. If a change to the method or the
prompt alters any expected result below, that change is a regression
until it is justified and this file is updated to match.

The mechanics under test are the ones most easily broken:

- the Constraint Level minimum rule
- the readiness gates and their caps
- provisional credit and the evidence-conversion action
- contradictory evidence blocking a Demonstrated decision
- exercise tiers gating the maturity level
- the organization view as the minimum across services
- the clock starting at onset of disruption, not at detection

Vocabulary follows `methodology/scoring-method.md`,
`methodology/evidence-standard.md` and `methodology/exercise-tiers.md`.
Read those first. These cases do not restate the definitions. They only
fix the outputs.

These cases are part of the main prompt's suite as SC1 to SC7; its
configuration, status and run record are in
[`prompt-evaluation-cases.md`](prompt-evaluation-cases.md#suite-configuration-and-status).
Each case carries a run input and a run pass condition naming the
mechanics a run is scored on. The cases were numbered 1 to 7 before
27 October 2026 (KST).

**Critical cases:** none.

---

## Case SC1: the minimum rule and the exit gate both bite

A single service. Switches and Pipes are strong and tested. The exit for
the leading concentration dependency exists on paper only.

Inputs.

- Service and owner defined. Tolerance approved and measurable.
- Pipes: end-to-end map current, concentrations identified. Strong.
- Switches: reroute switch delegated, tested at T3, executed within
  tolerance in the rehearsal. Strong.
- Exits: a written exit plan for the leading concentration dependency
  exists. No transition assistance secured, no substitute qualified, no
  rehearsal. Described only.
- Exercises: the reroute rehearsal was T3. Evidence current.

Run input, sent verbatim.

```text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the developed assessment: the capability profile, the Constraint Level and binding constraint, the evidence confidence, the gate results, the tolerance result and the readiness decision.

- Service and owner defined. Impact tolerance approved and measurable.
- Pipes: end-to-end dependency map current, concentrations identified. Strong.
- Switches: reroute switch delegated, tested at T3, executed within tolerance in the rehearsal. Strong.
- Exits: a written exit plan for the leading concentration dependency exists. No transition assistance secured, no substitute qualified, no rehearsal. Described only.
- Exercises: the reroute rehearsal was T3. Evidence current.
```

Run pass condition. PASS when the response shows the six domain scores
individually with Exits at 1 or below, sets the Constraint Level at the
Exits score, classifies the executable-exit gate (gate 5) as Fail,
reaches Not Demonstrated and averages nothing. The other domain scores
and the confidence rating are judgment within the method and are not
pinned by the run. The expected results below remain the rubric; the run
pins only what this condition names.

Expected capability profile.

| Domain | Score |
| --- | --- |
| Services and tolerances | 4 |
| Pipes | 4 |
| Switches | 4 |
| Exits | 1 |
| Exercises | 3 |
| Evidence and improvement | 3 |

Expected results.

- Constraint Level: minimum of Pipes, Switches and Exits is minimum of
  4, 4 and 1, which is 1.
- Evidence confidence: Moderate. The tested elements are strong, but the
  exit is untested and unsupported.
- Readiness decision: Not Demonstrated.
- Tolerance result: Not Tested for the exit path. The governing
  concentration-loss scenario has never been run.

Key gates.

| Gate | Status |
| --- | --- |
| Executable exit for leading concentration | Fail |
| Severe but plausible exercise completed | Pass |

What this pins. A top score on Switches and a T3 rehearsal cannot rescue
a missing exit. The minimum rule pulls the Constraint Level to 1 and the
failed exit gate holds the decision at Not Demonstrated. Nothing is
averaged up.

---

## Case SC2: provisional credit and the conversion action

A single switch is claimed. The support is a draft runbook and an
interview statement that authority is delegated. Nothing has been tested.

Inputs.

- Switch action, trigger and intended operator are described in a draft
  runbook.
- An owner states in interview that decision authority is delegated and
  available out of hours.
- No execution record. No test. No signed delegation.

Run input, sent verbatim.

```text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Classify the switch claim, state the credit it earns and the Switches level it supports, and name the action that would verify it.

- The switch action, trigger and intended operator are described in a draft runbook.
- An owner states in interview that decision authority is delegated and available out of hours.
- No execution record. No test. No signed delegation.
```

Run pass condition. PASS when the response classifies the switch claim
as Provisional, labels any credit as unverified, pairs it with an
evidence-conversion action that includes a controlled test of the switch
and a signed delegation, names an owner and target date for that action
or flags that they are missing, keeps Switches below L3 Exercised and
does not treat the absence of a test as the absence of the switch. The
expected results below remain the rubric; the run pins only what this
condition names.

Expected treatment.

- Verification status for the switch claim: Provisional.
- Credit: provisional only, and clearly labeled as unverified.
- Required evidence-conversion action: run a T2 controlled test of the
  switch and produce the signed delegation. The action has an owner and
  a target date, or it is flagged that these are missing.
- Switches domain: capped. A described switch supported only by a draft
  and a representation does not reach the Exercised level.
- Evidence confidence contribution: Low for this element.

What this pins. A representation earns provisional credit, never
verified credit, and only when it is labeled and paired with a
conversion action. Absence of a test is not treated as absence of the
switch. It is treated as an untested switch with a named path to
verification.

---

## Case SC3: contradictory evidence blocks Demonstrated

An exit rehearsal is presented as a success within tolerance. The
underlying records conflict with that claim.

Inputs.

- A summary report states the exit was rehearsed end-to-end and
  completed within the approved tolerance.
- The exercise record for the same event shows a T1 facilitated
  tabletop. No system actions were performed. The stated completion time
  is an estimate produced in discussion, not a measured elapsed time.

Run input, sent verbatim.

```text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Can the exit be marked Demonstrated?

- A summary report states the exit was rehearsed end-to-end and completed within the approved tolerance.
- The exercise record for the same event shows a T1 facilitated tabletop. No system actions were performed. The stated completion time is an estimate produced in discussion, not a measured elapsed time.
```

Run pass condition. PASS when the response classifies the
within-tolerance claim as Contradicted, or as Refuted on the reading that
the exercise record affirmatively disproves it (the prompt's own state for
a disproved claim), does not mark the exit or the service Demonstrated,
requires the conflict to be resolved, whether by reconciling the two
records or by correcting the summary against the primary record, and
requires a controlled test or end-to-end rehearsal (T2 or T3) with a
measured elapsed time before Demonstrated is considered, and does not
treat the tabletop estimate as a measured result. The expected results
below remain the rubric; the run pins only what this condition names.
Condition widened 27 October 2026 (KST) to admit Refuted, case defect
found in run 20261027-R1.

Expected treatment.

- Verification status for the claim that the exit executes within
  tolerance: Contradicted. The summary and the exercise record cannot
  both be true.
- Evidence confidence for the exit element: Indeterminate.
- Readiness decision: cannot be Demonstrated. Contradicted evidence on a
  core claim prevents an unqualified conclusion.
- Resolution required: reconcile the two records, then run a T2 or T3
  test that produces a measured elapsed time before any Demonstrated
  decision is considered.

What this pins. Conflicting evidence on a core claim is surfaced and
resolved, not silently averaged or resolved in favor of the more
flattering document. A tabletop estimate is not a measured result.

---

## Case SC4: exercise tier gates the maturity level

The governing severe but plausible scenario has been examined only in a
facilitated tabletop.

Inputs.

- A T1 facilitated tabletop was run for the governing scenario.
- Participants included the accountable owner and the relevant
  authority.
- Findings and notional decisions were recorded. No switch or exit was
  invoked. No timing was measured against tolerance.

Run input, sent verbatim.

```text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Score the Exercises domain, classify the exercise gate and give the tolerance result.

- A T1 facilitated tabletop was run for the governing severe but plausible scenario.
- Participants included the accountable owner and the relevant authority.
- Findings and notional decisions were recorded. No switch or exit was invoked. No timing was measured against tolerance.
- The capability could be put to a controlled test; nothing prevents one.
```

Run pass condition. PASS when the response scores Exercises at L2 or
below (not L3), classifies the severe-but-plausible-exercise gate (gate
6) as Fail and gives the tolerance result as Not Tested. The expected
results below remain the rubric; the run pins only what this condition
names.

Expected treatment.

- Exercises domain: caps at L2 Designed. It does not reach L3 Exercised.
  A discussion-based tabletop does not establish that the capability
  could be executed under stress, and the capability here could
  reasonably be put to a controlled test.
- Gate: severe but plausible exercise completed is Fail, because a
  discussion-only tabletop of the governing scenario is not an exercise
  of it (`templates/intake-pack.md`, gate 6: "Fail: no exercise, or
  discussion only for the governing scenario").
- Tolerance result: Not Tested.

What this pins. The tier of the exercise gates the maturity level. T0
and T1 do not earn L3. Only a controlled test, an end-to-end rehearsal
or a live event supports the Exercised level, and then only with
measured evidence. A T1 tabletop of the governing scenario is a Fail on
the exercise gate, as the intake pack and the manufacturing example read.

Expected result amended 20 October 2026 (KST): the exercise gate moved
from "Provisional Pass at most" to Fail, to match the intake pack.

---

## Case SC5: the organization view is the minimum across services

Three critical services have been assessed. Their individual results
differ. The portfolio result is required.

Inputs.

| Service | Constraint Level | Readiness decision |
| --- | --- | --- |
| Service B | 2 | Conditionally Demonstrated |
| Service M | 1 | Not Demonstrated |
| Service K | 2 | Not Demonstrated |

Run input, sent verbatim.

```text
Three critical services have been assessed. Give the organization view.

| Service | Constraint Level | Readiness decision |
| --- | --- | --- |
| Service B | 2 | Conditionally Demonstrated |
| Service M | 1 | Not Demonstrated |
| Service K | 2 | Not Demonstrated |
```

Run pass condition. PASS when the response gives an organization
readiness view of Not Demonstrated as the minimum of the three service
positions, not an average and not the strongest, names the service or
services that set the floor (Service M, or Service M and Service K
jointly, since both are Not Demonstrated) and keeps the three service
results shown beside the organization view. The expected results below
remain the rubric; the run pins only what this condition names.
Condition amended 27 October 2026 (KST): it no longer pins an
organization Constraint Level, which neither the prompt nor
`methodology/scoring-method.md` defines (case defect found in run
20261027-R1).

Expected results.

- Organization Constraint Level: not defined by the method, which takes
  the organization view as the minimum of the readiness positions
  (`methodology/scoring-method.md`, cap 6). The lowest service value, 1
  at Service M, may be reported for reference. Amended 27 October 2026
  (KST); until then this line read "minimum of 2, 1 and 2, which is 1,
  governed by Service M".
- Organization readiness view: Not Demonstrated. The portfolio inherits
  the weakest service, not the average and not the strongest.
- Reporting: the individual service results are still shown in full. The
  organization view does not replace them. It sits above them.

What this pins. The organization level is the minimum across the
services assessed. One weak service governs the portfolio view. A strong
service does not lift the organization result, and the individual
profiles are never collapsed into the single organization number.

---

## Case SC6: the full profile is reported, never collapsed

This case confirms the worked walkthrough in
`methodology/scoring-method.md`.

Inputs.

- A single service scoring 3, 3, 3, 2, 3, 3 across the six domains in
  order.
- One corrective action is overdue. The priority exit is designed but
  untested.

Run input, sent verbatim.

```text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the capability profile, the Constraint Level and binding constraint, the evidence confidence, the tolerance result and the readiness decision.

- Domain scores, in the order of the capability model: Services and tolerances 3, Pipes 3, Switches 3, Exits 2, Exercises 3, Evidence and improvement 3.
- The governing scenario (loss of the primary provider, handled by the reroute switch) was rehearsed end-to-end at T3: onset at 09:00, verified stabilization at 17:00, against an approved twelve-hour tolerance. Timing records are current.
- The priority exit is designed: exit rights, transition assistance and a substitute are secured in writing. The exit has not been rehearsed.
- One corrective action is overdue.
```

Run pass condition. PASS when the response shows all six scores
individually as 3, 3, 3, 2, 3, 3 without averaging them or reducing them
to one grade, sets the Constraint Level at 2, names the executable exit
(gate 5) as the binding constraint, gives the tolerance result as Met
for the governing scenario and reaches Conditionally Demonstrated held
by the overdue action and the unrehearsed exit. The expected results
below remain the rubric; the run pins only what this condition names.

Expected results.

- Capability profile: all six domain scores are shown individually. The
  profile is 3, 3, 3, 2, 3, 3. It is not reduced to an average or to a
  single grade.
- Constraint Level: minimum of Pipes, Switches and Exits is 2.
- Binding constraint: gate 5, the executable exit, for the exit
  scenario.
- Evidence confidence: Moderate.
- Readiness decision: Conditionally Demonstrated, held there by the
  overdue action and the untested exit.
- Tolerance result: Met for the governing scenario; the exit path's fit
  within tolerance is untested.

What this pins. Capability, confidence and constraint stay separate. The
Constraint Level does not by itself produce the readiness decision. The
gates govern the decision, and a strong profile still
carries its open items on its face.

Expected result amended 18 October 2026 (KST) in v2.6.0: the
walkthrough's Exits score moved from L3 to L2 under the tier rule
(`methodology/exercise-tiers.md`: T3 supports L3 only for the path
exercised, and the exit path reached T2), so the profile and the
Constraint Level follow; the binding constraint line is new with the
binding-constraint finding.

Amended 20 October 2026 (KST): the walkthrough's Services and
tolerances, Pipes and Switches scores moved from L4 to L3 under cap 8
(L4 needs closed corrective-action loops, and one action is overdue), so
the profile follows; the Constraint Level stays 2.

---

## Case SC7: the clock starts at onset, not at detection

The acceptance case for finding F04 of the evaluation brief.

Inputs.

- A critical service with an approved impact tolerance of four hours.
- Disruption begins at 02:00. Nobody notices until 04:00. The service is
  verified stable on an alternate path at 07:00.

Run input, sent verbatim.

```text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the clock start, the clock stop, the elapsed time, the tolerance result and the readiness decision.

- Approved impact tolerance: four hours.
- Disruption begins at 02:00. Nobody notices until 04:00. The service is verified stable on an alternate path at 07:00.
```

Run pass condition. PASS when the response starts the clock at onset
(02:00), not at detection (04:00), stops it at verified stabilization
(07:00), gives five hours elapsed against four, a tolerance result of
Not Met and a readiness decision of Not Demonstrated, and does not call
the tolerance Met on a three-hour reading. The expected results below
remain the rubric; the run pins only what this condition names.

Expected results.

- Clock start: onset of disruption at 02:00. Detection at 04:00 ends the
  Detect phase (two hours); it does not start the clock.
- Clock stop: verified stabilization at 07:00.
- Elapsed: five hours against a four-hour tolerance.
- Tolerance result: Not Met.
- Readiness decision: Not Demonstrated (decision caps rule 4).
- Binding constraint: the Detect phase, which alone consumes half the
  tolerance.

What this pins. A clock started at detection would read three hours and
call the tolerance Met. The organization's failure to notice is part of
the disruption its customers suffered, so it is on the clock. Where the
onset time cannot be established, the pre-detection interval is Unknown
and the result is Cannot Determine unless an evidenced bound on that
interval still fits the tolerance.

---

Final Liability rests with the Human.
