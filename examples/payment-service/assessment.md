# Assessment: Service B real-time payments

Status: [✓ final]
Assessment date: 2026-06-15 (Asia/Seoul)
Evidence cut-off date: 2026-06-10

Synthetic example. Neutral labels. Not legal or regulatory advice.

## TL;DR

- Service B holds a demonstrated reroute switch within its 12-hour
  tolerance, stabilized at 9 hours in a T3 rehearsal.
- ⧉ The exit from Vendor A is the single biggest gap. It is not rehearsed
  end to end and substitute capacity is not confirmed under peak load.
- The Constraint Level is 3, set by Pipes and Exits, not by the stronger
  Switches score.
- Readiness decision is Conditionally Demonstrated. Evidence confidence is
  Moderate.
- Two material corrective actions are open and one dependency-map action
  is overdue.

## A. Capability profile

Six domain scores, each 0 to 4, reported individually.

| Domain | Score | Basis |
|---|---|---|
| Services and tolerances | 4 | Defined and owned, tolerance approved and measurable with explicit clock events, gateway-availability trigger monitored, timing metrics current from the 2026-05-12 rehearsal |
| Pipes | 3 | Mapped end to end, Vendor A and fourth-party concentrations identified, but the map re-verification is overdue (CA-003), so currency is not instrumented |
| Switches | 4 | Reroute switch executable and delegated, invocation trigger defined and monitored, rehearsed at T3 within tolerance with verified timing evidence |
| Exits | 3 | Rights and data portability in place, but exit not rehearsed end to end and substitute capacity unconfirmed |
| Exercises | 3 | Strong T3 on the reroute path, but the exit path only reached T2 |
| Evidence and improvement | 3 | Traceable and fresh, but one corrective action is overdue, so the closure loop is not clean |

## B. Constraint level

Constraint Level = minimum of Pipes (3), Switches (4), Exits (3) = 3.

The weakest structural components of optionality are the pipes and the
exit. The organization can switch around a Vendor A outage but cannot
yet show it can leave Vendor A within tolerance.

## C. Evidence confidence

Moderate.

The reroute evidence is current, execution-based and independently
reviewable. The exit evidence relies on a data-export test and
contractual rights without an end-to-end rehearsal, and one corrective
action is overdue. That mix supports Moderate, not High.

## D. Readiness decision

Conditionally Demonstrated.

The reroute path is Demonstrated within tolerance. The exit path is not
demonstrated end to end, substitute capacity is unconfirmed, and an
overdue action remains. Those hold the overall decision at Conditionally
Demonstrated rather than Demonstrated.

## E. Tolerance result

Met for the reroute scenario.

- Clock start: detection of Vendor A unavailability.
- Clock stop: verified stabilization on the Vendor C backup rail at 9
  hours.
- Not Tested end to end for the exit scenario.

## Gate results

| Gate | Status | Note |
|---|---|---|
| Service and owner defined | Pass | Head of payments accountable |
| Tolerance approved and measurable | Pass | 12 hours, approved by COO |
| Dependencies mapped | Provisional Pass | Map verified 2026-05-20 but a re-verification action is overdue |
| Switch authority available | Pass | Delegated, though out-of-hours reachability was slow in rehearsal |
| Executable exit for leading concentration | Provisional Pass | Exit exists on paper and in a T2 data-export test, not end to end |
| Severe but plausible exercise completed | Pass | T3 reroute rehearsal 2026-05-12 |
| Evidence shows tolerance result | Pass | For the reroute path |
| Corrective actions have owners and dates | Provisional Pass | One action overdue |

No gate is a hard Fail. The Provisional Passes on material gates cap the
decision at Conditionally Demonstrated.

## Top breakpoints

1. Exit from Vendor A not rehearsed end to end, and substitute capacity
   unconfirmed under peak load.
2. Fourth-party concentration: the upstream network provider behind
   Vendor A may also sit behind the substitute gateway.
3. Authorization latency: 3 hours in rehearsal because the decision-maker
   was hard to reach out of hours.
4. Aging dependency map, re-verification overdue.

## Evidence ledger extract

| Evidence ID | Claim | Type | Status | Freshness | Limitation |
|---|---|---|---|---|---|
| E-001 | Backup rail activates within tolerance | exercise record | Verified | Current | None |
| E-002 | Vendor A exit rights permit termination for convenience | contract | Provisional | Rights current | No end-to-end rehearsal |
| E-003 | Data can be exported from Vendor A in usable form | observed test | Verified | Current | Export only, not full cutover |
| E-004 | Substitute gateway can carry peak volume | none | Not demonstrated | n.a. | No capacity test |

## Prioritized backlog

| Action | Risk addressed | Owner | Acceptance test | Target |
|---|---|---|---|---|
| Run a T3 end-to-end exit rehearsal off Vendor A | Cannot leave the leading concentration within tolerance | Vendor management lead | Exercise record shows cutover within tolerance | 2026-09-30 |
| Confirm substitute gateway peak capacity and upstream provider | Hidden fourth-party concentration survives the exit | Payments architect | Capacity test and provider map | 2026-08-31 |
| Re-verify end-to-end dependency map | Decisions made on stale map | Service owner | Dated verified map | 2026-07-31 (overdue) |
| Re-run degrade switch test with live authorization | Authorization step never actually performed | Payments resilience lead | Evidence of live authorization within clock | 2026-08-15 |

## Decisions required

- Accept or reject the current Conditionally Demonstrated position for
  Service B pending the exit rehearsal.
- Fund the substitute-gateway capacity test.

## Escalation items

None require external counsel at this stage. ⚠ Before any live Vendor A
exit, the termination mechanics and cross-border notification duties in
Jurisdiction Y should be reviewed by qualified counsel.

[Purpose] Score Service B optionality against the GRCnext™ method and
identify what blocks an unqualified demonstration.
[Decisions Made] Reroute path accepted as Demonstrated within tolerance.
Overall service held at Conditionally Demonstrated.
[Outstanding Items] Exit rehearsal, substitute capacity confirmation,
dependency-map re-verification, live-authorization retest.

✅ complete

Final Liability rests with the Human.
