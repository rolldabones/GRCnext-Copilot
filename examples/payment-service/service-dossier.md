# Service Dossier: Service B real-time payments

Status: [✓ final]
Assessment date: 2026-06-15 (Asia/Seoul)
Evidence cut-off date: 2026-06-10
Prepared by: Assessment lead (synthetic example)

Synthetic example. Neutral labels throughout.

---

## 1. Service definition

- Service name: Service B, real-time payments.
- Service outcome: A customer can send or receive funds and see them
  settle within seconds, at any hour.
- Accountable owner: Head of payments.
- Customers and stakeholders: Retail banking customers, corporate
  customers using instant collections, the treasury function, the
  regulator liaison.
- Material jurisdictions: Jurisdiction X (primary), Jurisdiction Y
  (cross-border corridor).
- Material harms: Customers cannot pay bills or receive time-critical
  funds, reputational damage, potential regulatory breach if disruption
  exceeds tolerance.
- Scope boundaries: Covers the real-time rail. Excludes card payments and
  scheduled bulk payroll, which are separate services.

## 2. Impact tolerance

- Tolerance statement: No more than 12 hours of disruption to real-time
  settlement in a severe but plausible scenario.
- Measurement method: Elapsed time from detection to verified
  stabilization on any acceptable settlement path.
- Clock start: Detection of a material disruption to real-time
  settlement.
- Clock stop: Verified stabilization on the primary rail or an approved
  alternate path.
- Approving authority: Chief operating officer, on record.
- Underlying assumptions: Backup rail capacity is sufficient for peak
  volume, and delayed batch settlement is acceptable to customers for a
  bounded period.
- Latest result: Met for the reroute scenario. Not Tested end to end for
  the exit scenario.

## 3. End-to-end dependency map

Last verified: 2026-05-20.

- People: Payments duty manager, payments operations engineers,
  settlement operations lead, treasury on-call.
- Process: Real-time authorization, settlement, reconciliation, exception
  handling.
- Technology: Core payments platform, Vendor A gateway, backup rail
  console, reconciliation engine.
- Data: Transaction records, settlement instructions, customer account
  data.
- Facilities: Two data centers, one operations center.
- Third parties: Vendor A (primary gateway), Vendor C (backup rail).
- Fourth parties (material): Vendor A relies on a single upstream network
  provider in Jurisdiction X.
- Jurisdictions: Jurisdiction X, Jurisdiction Y.
- Recovery dependencies: Backup rail console access, current credentials,
  reconciliation controls.
- Concentrations: Vendor A is the leading concentration dependency. The
  upstream network provider behind Vendor A is a fourth-party
  concentration.
- Manual alternatives: Delayed batch settlement, capacity limited to
  roughly half of peak real-time volume.

## 4. Switch Catalog

See [`../../templates/switch-catalog.csv`](../../templates/switch-catalog.csv)
for the tabular form. Two material switches.

Switch SW-001

- Trigger: Vendor A gateway unavailable beyond 30 minutes.
- Action: Reroute payment flow to the Vendor C backup rail.
- Authorized decision-maker: Payments duty manager.
- Operator: Payments operations engineer.
- Prerequisites: Standing access to the backup rail console, current
  credentials, runbook RB-07.
- Execution time: Target under 4 hours across the full clock; pass
  criterion is the 12-hour impact tolerance. Rehearsed at 9 hours end to
  end, within tolerance, target missed.
- Communications: Treasury, customer comms, regulator liaison per plan.
- Rollback or stabilization: Fail back to Vendor A once restored and
  verified.
- Evidence generated: Rerouting log, timing record, comms log.
- Latest test result: T3 rehearsal 2026-05-12, stabilized in 9 hours,
  passed against the 12-hour tolerance; 4-hour internal target missed.

Switch SW-002

- Trigger: Suspected data-integrity fault in settlement.
- Action: Degrade to delayed batch settlement.
- Authorized decision-maker: Head of payments.
- Operator: Settlement operations lead.
- Prerequisites: Batch settlement mode enabled, reconciliation controls
  active.
- Execution time: Target under 2 hours to a safe degraded state.
- Communications: Customers notified of delayed settlement, regulator if
  threshold met.
- Rollback or stabilization: Resume real-time settlement after integrity
  confirmed.
- Evidence generated: Mode-change record, reconciliation report.
- Latest test result: T2 test 2026-04-03, passed for the technical step.
  The authorization step was simulated, not performed.

## 5. Priority exit plan

For Vendor A, the leading concentration dependency. See
[`../../templates/exit-playbook.md`](../../templates/exit-playbook.md).

- Dependency being exited: Vendor A gateway.
- Exit triggers: Sustained Vendor A instability, material price change, or
  loss of confidence in Vendor A resilience.
- Legal and contractual rights: Termination for convenience on 90 days
  notice under MSA v3. Transition assistance clause present.
- Notice requirements: 90 days to Vendor A, customer notice if service
  characteristics change, regulator notification per applicable rules.
- Data actions: Retrieve transaction and configuration data in a
  documented format. Deletion at Vendor A evidenced by certificate.
- Transition steps: Qualify substitute gateway, integrate, run parallel,
  cut over, decommission Vendor A.
- Substitute arrangement: Substitute gateway identified. Capacity not yet
  confirmed under peak load.
- Resource and cost assumptions: One-time integration cost estimated.
  Ongoing cost broadly comparable.
- Residual risks: The upstream network provider behind Vendor A may also
  sit behind the substitute. Not yet confirmed.
- Target execution time: 90 to 120 days.
- Evidence requirements: Rehearsal record, data portability proof,
  deletion certificate.
- Latest rehearsal result: T2 controlled technical test of data export on
  2026-03-18. Not rehearsed end to end.

## 6. Exercise and evidence record

- Latest scenario: Vendor A gateway unavailable during a weekday peak.
- Exercise tier: T3 end-to-end rehearsal for the reroute path.
- Date: 2026-05-12.
- Participants: Payments duty manager, operations engineers, treasury
  on-call, customer comms, regulator liaison.
- Actions simulated: Regulator notification.
- Actions performed: Detection, decision, authorization, reroute
  execution, verification, customer communication, stabilization.
- Elapsed times: Detect 20 minutes, interpret 25 minutes, decide 40
  minutes, authorize 3 hours, execute 1 hour, verify 40 minutes,
  communicate 30 minutes, stabilize to 9 hours total.
- Tolerance met or not met: Met against the 12-hour tolerance.
- Evidence pack: See
  [`../../templates/evidence-pack-index.md`](../../templates/evidence-pack-index.md)
  applied to this service.
- Findings: Authorization was the slowest phase at 3 hours because the
  authorized decision-maker was hard to reach out of hours. The exit path
  is not rehearsed end to end. The dependency map is aging.
- Corrective actions: See
  [`../../templates/capa-register.csv`](../../templates/capa-register.csv).
- Retest status: Reroute path retest scheduled. Exit path first end-to-end
  rehearsal not yet scheduled.

---

## Appendices

- A. Evidence ledger extract: see
  [`assessment.md`](assessment.md).
- B. Legal and jurisdictional issue list: Vendor A termination mechanics
  reserved for counsel review before invocation.

Final Liability rests with the Human.
