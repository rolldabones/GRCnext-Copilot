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

Vocabulary follows `methodology/scoring-method.md`,
`methodology/evidence-standard.md` and `methodology/exercise-tiers.md`.
Read those first. These cases do not restate the definitions. They only
fix the outputs.

---

## Case 1: the minimum rule and the exit gate both bite

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

## Case 2: provisional credit and the conversion action

A single switch is claimed. The support is a draft runbook and an
interview statement that authority is delegated. Nothing has been tested.

Inputs.

- Switch action, trigger and intended operator are described in a draft
  runbook.
- An owner states in interview that decision authority is delegated and
  available out of hours.
- No execution record. No test. No signed delegation.

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

## Case 3: contradictory evidence blocks Demonstrated

An exit rehearsal is presented as a success within tolerance. The
underlying records conflict with that claim.

Inputs.

- A summary report states the exit was rehearsed end-to-end and
  completed within the approved tolerance.
- The exercise record for the same event shows a T1 facilitated
  tabletop. No system actions were performed. The stated completion time
  is an estimate produced in discussion, not a measured elapsed time.

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

## Case 4: exercise tier gates the maturity level

The governing severe but plausible scenario has been examined only in a
facilitated tabletop.

Inputs.

- A T1 facilitated tabletop was run for the governing scenario.
- Participants included the accountable owner and the relevant
  authority.
- Findings and notional decisions were recorded. No switch or exit was
  invoked. No timing was measured against tolerance.

Expected treatment.

- Exercises domain: caps at L2 Designed. It does not reach L3 Exercised.
  A discussion-based tabletop does not establish that the capability
  could be executed under stress, and the capability here could
  reasonably be put to a controlled test.
- Gate: severe but plausible exercise completed is Provisional Pass at
  most, not a full Pass, because nothing was executed or measured.
- Tolerance result: Not Tested.

What this pins. The tier of the exercise gates the maturity level. T0
and T1 do not earn L3. Only a controlled test, an end-to-end rehearsal
or a live event supports the Exercised level, and then only with
measured evidence. A T1 tabletop yields at most Provisional Pass on the
exercise gate, and an assessor marks Fail where the governing scenario
remains untested.

---

## Case 5: the organization view is the minimum across services

Three critical services have been assessed. Their individual results
differ. The portfolio result is required.

Inputs.

| Service | Constraint Level | Readiness decision |
| --- | --- | --- |
| Service B | 3 | Conditionally Demonstrated |
| Service M | 1 | Not Demonstrated |
| Service K | 2 | Not Demonstrated |

Expected results.

- Organization Constraint Level: minimum of 3, 1 and 2, which is 1,
  governed by Service M.
- Organization readiness view: Not Demonstrated. The portfolio inherits
  the weakest service, not the average and not the strongest.
- Reporting: the individual service results are still shown in full. The
  organization view does not replace them. It sits above them.

What this pins. The organization level is the minimum across the
services assessed. One weak service governs the portfolio view. A strong
service does not lift the organization result, and the individual
profiles are never collapsed into the single organization number.

---

## Case 6: the full profile is reported, never collapsed

This case confirms the worked walkthrough in
`methodology/scoring-method.md`.

Inputs.

- A single service scoring 4, 4, 4, 3, 3, 3 across the six domains in
  order.
- One corrective action is overdue. The priority exit is designed but
  untested.

Expected results.

- Capability profile: all six domain scores are shown individually. The
  profile is 4, 4, 4, 3, 3, 3. It is not reduced to an average or to a
  single grade.
- Constraint Level: minimum of Pipes, Switches and Exits is 3.
- Evidence confidence: Moderate.
- Readiness decision: Conditionally Demonstrated, held there by the
  overdue action and the untested exit.
- Tolerance result: Met for the tested paths, Not Tested for the exit.

What this pins. Capability, confidence and constraint stay separate. A
high Constraint Level does not by itself produce a Demonstrated
decision. The gates govern the decision, and a strong profile still
carries its open items on its face.

---

Final Liability rests with the Human.
