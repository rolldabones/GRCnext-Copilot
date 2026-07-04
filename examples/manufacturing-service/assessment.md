# Assessment: Service M production line

Status: [✓ final]
Assessment date: 2026-06-20 (Asia/Seoul)
Evidence cut-off date: 2026-06-16

Synthetic example. Neutral labels. Not legal, safety or regulatory advice.

## TL;DR

- Service M has a strong, real-event-tested safety stop, but a safety stop
  is not optionality on its own.
- ⧉ There is no executable exit for the leading raw-material
  concentration, Vendor R. No second supplier is qualified. This is a core
  gate failure.
- The Constraint Level is 1, set by Exits.
- Readiness decision is Not Demonstrated. Evidence confidence is Low for
  the elements that matter under a supplier-loss scenario.
- The 24-hour tolerance has never been tested to buffer exhaustion or to a
  supplier switch.

## A. Capability profile

| Domain | Score | Basis |
|---|---|---|
| Services and tolerances | 3 | Defined, owned, tolerance approved, but never tested against the governing supplier-loss scenario |
| Pipes | 3 | Mapped, both concentrations and a fourth-party mine dependency identified, map current |
| Switches | 3 | Safety stop is T4 and strong, but manual control is only T1 and buffer runway is untested to exhaustion |
| Exits | 1 | Exit is described only. No second supplier qualified, no substitute capacity today |
| Exercises | 2 | A real safety-stop event exists, but the control-loss and supplier-loss scenarios reached only T1 |
| Evidence and improvement | 2 | Some strong evidence, but key scenarios are untested and no retest is scheduled |

## B. Constraint level

Constraint Level = minimum of Pipes (3), Switches (3), Exits (1) = 1.

The exit is the fatal weakness. The plant can stop safely and can limp on
degraded control for a while, but it cannot leave Vendor R within
tolerance, and buffer stock only postpones the problem.

## C. Evidence confidence

Low for the governing scenario.

The safety stop has High-confidence real-event evidence. But the question
that sets the tolerance, can Service M survive a Vendor R loss within 24
hours, rests on an untested buffer assumption and a non-existent exit.
Confidence for that scenario is Low.

## D. Readiness decision

Not Demonstrated.

Core gate 5 fails: there is no executable exit for the leading
concentration dependency. Core gate 6 is not met for the governing
scenario, because no severe-but-plausible supplier-loss exercise has been
completed beyond a tabletop. Either failure alone blocks a Demonstrated
decision.

## E. Tolerance result

Cannot Determine.

- Clock start would be an unplanned production stop.
- Clock stop would be verified resumption of in-specification output.
- The 24-hour tolerance has not been tested to buffer exhaustion or to a
  supplier switch, so no result can be stated.

## Gate results

| Gate | Status | Note |
|---|---|---|
| Service and owner defined | Pass | Plant operations director accountable |
| Tolerance approved and measurable | Pass | 24 hours, approved |
| Dependencies mapped | Pass | Both concentrations and the mine dependency identified |
| Switch authority available | Pass | Safety stop authority is clear and immediate |
| Executable exit for leading concentration | Fail | No second raw-material supplier qualified |
| Severe but plausible exercise completed | Fail | Only T1 tabletop for control loss, no supplier-loss test |
| Evidence shows tolerance result | Unknown | Tolerance never tested for the governing scenario |
| Corrective actions have owners and dates | Fail | Actions identified but not owned, dated or scheduled |

Four gates are not passed. Two are hard Fails on core gates.

## Top breakpoints

1. No executable exit for Vendor R. Qualification takes 3 to 6 months and
   is unfunded.
2. Fourth-party concentration: a candidate second supplier may depend on
   the same mine in Jurisdiction Z.
3. Manual control is unproven on the line. A T1 tabletop is not execution.
4. Buffer runway is assumed at 18 hours but never tested to exhaustion.

## Evidence ledger extract

| Evidence ID | Claim | Type | Status | Freshness | Limitation |
|---|---|---|---|---|---|
| E-M1 | Safe controlled stop achievable in minutes | production event | Verified | Current | Covers stop, not resumption within tolerance |
| E-M2 | Manual control can sustain production | none | Not demonstrated | n.a. | Tabletop only, never run on line |
| E-M3 | Buffer covers about 18 hours | interview representation | Provisional | Uncertain | Never tested to exhaustion |
| E-M4 | Alternate raw-material supplier available | none | Not demonstrated | n.a. | No supplier qualified |

## Prioritized backlog

| Action | Risk addressed | Owner | Acceptance test | Target |
|---|---|---|---|---|
| Fund and start qualification of a second raw-material supplier | No exit for the leading concentration | Procurement director | Qualification record and trial production pass | Start within 30 days |
| Confirm whether candidate suppliers depend on the Jurisdiction Z mine | Hidden fourth-party concentration | Supply risk lead | Documented upstream map | 60 days |
| Run a controlled live manual-control test with safety fallback | Manual control unproven | Plant operations director | Timed test record within safety limits | 60 days |
| Test buffer runway to a controlled threshold | Buffer assumption unverified | Materials lead | Measured runway record | 90 days |

## Decisions required

- Fund the second-supplier qualification, or formally accept the residual
  risk of a single raw-material source with only buffer stock as
  mitigation.
- Assign owners and dates to the corrective actions, which currently have
  neither.

## Escalation items

⚠ The single-source raw-material exposure with no qualified alternate is a
board-level risk-acceptance decision, not an operational one. It should be
recorded as an explicit accepted risk with a named owner if qualification
is not funded. Any live test near buffer exhaustion or manual control
requires sign-off from the safety function.

[Purpose] Score Service M optionality and identify what blocks
demonstration under the governing supplier-loss scenario.
[Decisions Made] Recorded Not Demonstrated. Safety stop credited as strong
but insufficient on its own.
[Outstanding Items] Second-supplier qualification, fourth-party map,
live manual-control test, buffer-runway test, ownership of corrective
actions.

❓ needs input: funding decision on second-supplier qualification.

Final Liability rests with the Human.
