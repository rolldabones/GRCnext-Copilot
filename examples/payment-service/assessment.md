# Assessment: Service B real-time payments

Status: [✓ final]
Assessment date: 2026-06-15 (Asia/Seoul)
Evidence cut-off date: 2026-06-10

Synthetic example. Neutral labels. Not legal or regulatory advice.

## TL;DR

- Service B's reroute switch stabilized 9 hours from onset in a T3
  rehearsal, inside its 12-hour tolerance.
- ⧉ The exit from Vendor A is the single biggest gap. It is not rehearsed
  end to end and substitute capacity is not confirmed under peak load.
- The Constraint Level is 2, set by Exits. The binding constraint is the
  Authorize phase (3 hours of 9) for the reroute scenario and gate 5 for
  the exit scenario.
- Readiness decision is Conditionally Demonstrated (Provisional Pass on
  gates 2 and 5). Evidence confidence is Moderate.
- Five corrective actions are open (CA-001 to CA-005), none overdue.
  CA-005 re-approves the tolerance with clock start at onset.

## A. Capability profile

Six domain scores, each 0 to 4, reported individually.

| Domain | Score | Basis |
|---|---|---|
| Services and tolerances | 3 | Defined and owned, tolerance measured from onset with explicit clock events and timing current from the 2026-05-12 rehearsal, but the onset measurement method lacks approval at the assessment date: the approved statement names detection as the clock start (CA-005) |
| Pipes | 3 | Mapped end to end and verified 2026-05-20, Vendor A and fourth-party concentrations identified, but drift is not monitored, so not L4 |
| Switches | 3 | Reroute switch executable and delegated, rehearsed at T3 within tolerance with verified timing evidence; not L4 because the SW-002 authorization step was simulated and CA-002 and CA-004 are open (L4 requires closed corrective-action loops) |
| Exits | 2 | Rights and data portability in place, but the exit is rehearsed only to T2 (T3 supports L3 only for the path exercised) and substitute capacity is unconfirmed |
| Exercises | 3 | Strong T3 on the reroute path, but the exit path only reached T2 |
| Evidence and improvement | 3 | Traceable and fresh, but five corrective actions are open, so the loop is not closed |

## B. Constraint level

Constraint Level = minimum of Pipes (3), Switches (3), Exits (2) = 2.

The weakest structural component of optionality is the exit. The
organization can switch around a Vendor A outage but cannot yet show it
can leave Vendor A within tolerance.

Binding constraint. For the reroute scenario it is the Authorize phase:
3 hours of the 9-hour rehearsal, because the authorized decision-maker
was hard to reach out of hours. For the exit scenario it is gate 5
(executable exit for the leading concentration), held at Provisional
Pass. The minimum names the weakest maturity domain; the binding
constraint names what actually limits execution.

## C. Evidence confidence

Moderate.

The reroute evidence is current, execution-based and independently
reviewable. The exit evidence relies on a data-export test and
contractual rights without an end-to-end rehearsal, and the onset clock
awaits re-approval. That mix supports Moderate, not High.

## D. Readiness decision

Conditionally Demonstrated.

The reroute path met tolerance in a T3 rehearsal. The exit path is
rehearsed only to T2, substitute capacity is unconfirmed and the
tolerance's onset clock awaits re-approval. The Provisional Passes on
gates 2 and 5 cap the decision at Conditionally Demonstrated (decision
caps rule 2).

## E. Tolerance result

Met for the reroute scenario.

- Clock start (onset): the injected Vendor A outage at rehearsal start.
  Detection followed at 20 minutes (the Detect phase).
- Clock stop: verified stabilization on the Vendor C backup rail, 9 hours
  from onset.
- Not Tested end to end for the exit scenario.

## Gate results

| Gate | Status | Note |
|---|---|---|
| Service and owner defined | Pass | Head of payments accountable |
| Tolerance approved and measurable | Provisional Pass | 12 hours, approved by COO with clock start at detection; onset clock pending re-approval (CA-005) |
| Dependencies mapped | Pass | Map verified 2026-05-20; next re-verification due 2026-08-20 (CA-003) |
| Switch authority available | Pass | Delegated, though out-of-hours reachability was slow in rehearsal |
| Executable exit for leading concentration | Provisional Pass | Exit exists on paper and in a T2 data-export test, not end to end |
| Severe but plausible exercise completed | Pass | T3 reroute rehearsal 2026-05-12 |
| Evidence shows tolerance result | Pass | For the reroute path |
| Corrective actions have owners and dates | Pass | Every action has an owner and a target date; none overdue |

No gate is a hard Fail. The Provisional Passes on gates 2 and 5 cap the
decision at Conditionally Demonstrated.

## Top breakpoints

1. Exit from Vendor A not rehearsed end to end, and substitute capacity
   unconfirmed under peak load.
2. Fourth-party concentration: the upstream network provider behind
   Vendor A may also sit behind the substitute gateway.
3. Authorization latency: 3 hours in rehearsal because the decision-maker
   was hard to reach out of hours.
4. Tolerance clock start approved at detection; the onset clock awaits
   re-approval.

## Evidence ledger extract

| Evidence ID | Claim | Type | Status | Freshness | Limitation |
|---|---|---|---|---|---|
| E-001 | Backup rail activates within tolerance | exercise record | Verified | Current | None |
| E-002 | Vendor A exit rights permit termination for convenience | contract | Verified | Rights current | The right only, not the capability to execute the exit (E-006) |
| E-003 | Data can be exported from Vendor A in usable form | observed test | Verified | Current | Export only, not full cutover |
| E-004 | Substitute gateway can carry peak volume | none | Not evidenced | n.a. | No capacity test |
| E-005 | Impact tolerance approved with measurable clock events | controlled document | Provisional | Current | Approved statement names detection as clock start; onset clock not yet approved |
| E-006 | The exit off Vendor A can be executed end to end | observed test | Provisional | Current | Export step only; no end-to-end rehearsal (CA-001) |

## Prioritized backlog

| Ref | Action | Risk addressed | Owner | Acceptance test | Target |
|---|---|---|---|---|---|
| CA-005 | Re-approve the impact tolerance with clock start at onset | Tolerance measured on an unapproved clock | Chief operating officer's office | Re-approved tolerance statement on record | 2026-07-15 |
| CA-002 | Re-run degrade switch test with live authorization | Authorization step never actually performed | Payments resilience lead | Evidence of live authorization within clock | 2026-08-15 |
| CA-003 | Re-verify end-to-end dependency map and fourth-party list | Map passes its 2026-08-20 re-verification date unverified | Service owner | Dated verified map | 2026-08-20 |
| CA-004 | Close the gap between the 9-hour rehearsal and the 4-hour internal target for SW-001 | Authorization latency consumes the clock | Payments duty manager | Rehearsal record within the 4-hour target | 2026-08-31 |
| E-004 conversion | Confirm substitute gateway peak capacity and upstream provider | Hidden fourth-party concentration survives the exit | Payments architect | Capacity test and provider map | 2026-08-31 |
| CA-001 | Run a T3 end-to-end exit rehearsal off Vendor A | Cannot leave the leading concentration within tolerance | Vendor management lead | Exercise record shows cutover within tolerance | 2026-09-30 |

## Decisions required

- Accept or reject the current Conditionally Demonstrated position for
  Service B pending the exit rehearsal.
- Fund the substitute-gateway capacity test.
- Re-approve the impact tolerance with clock start at onset (CA-005).

## Escalation items

None require external counsel at this stage. ⚠ Before any live Vendor A
exit, the termination mechanics and cross-border notification duties in
Jurisdiction Y should be reviewed by qualified counsel.

[Purpose] Score Service B optionality against the GRCnext™ method and
identify what blocks an unqualified demonstration.
[Decisions Made] Reroute path accepted as meeting tolerance in a T3
rehearsal. Overall service held at Conditionally Demonstrated. Constraint
Level 2, set by Exits.
[Outstanding Items] Onset-clock re-approval (CA-005), exit rehearsal
(CA-001), substitute capacity confirmation, dependency-map
re-verification (CA-003), live-authorization retest (CA-002), 4-hour
target gap (CA-004).

✅ complete

Final Liability rests with the Human.
