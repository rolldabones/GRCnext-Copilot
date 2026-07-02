# Service Dossier: Service M production line

Status: [✓ final]
Assessment date: 2026-06-20 (Asia/Seoul)
Evidence cut-off date: 2026-06-16
Prepared by: Assessment lead (synthetic example)

Synthetic example. Neutral labels throughout.

---

## 1. Service definition

- Service name: Service M, continuous production on the primary line.
- Service outcome: Finished product delivered to downstream customers on
  schedule and to specification.
- Accountable owner: Plant operations director.
- Customers and stakeholders: Downstream manufacturing customers under
  supply contracts, the safety function, the maintenance function.
- Material jurisdictions: Jurisdiction X (plant location).
- Material harms: Missed customer deliveries and penalties, equipment
  damage from an uncontrolled stop, safety hazard to line personnel.
- Scope boundaries: Covers the primary line. Excludes the secondary line,
  which runs a different product and is treated as a separate service.

## 2. Impact tolerance

- Tolerance statement: No more than 24 hours of production stoppage before
  penalties and downstream customer harm become material.
- Measurement method: Elapsed time from an unplanned stop to verified
  resumption of in-specification production.
- Clock start: Unplanned production stop.
- Clock stop: Verified resumption of in-specification output.
- Approving authority: Plant operations director, endorsed by the
  commercial function on penalty exposure.
- Underlying assumptions: Buffer stock of raw material covers roughly 18
  hours of production at normal rate.
- Latest result: Not Tested against a full 24-hour supplier-loss scenario.

## 3. End-to-end dependency map

Last verified: 2026-06-01.

- People: Line operators, control-room engineers, maintenance
  technicians, safety officer.
- Process: Feed, conversion, quality control, packaging.
- Technology: Primary line machinery, Vendor S SCADA and MES control
  system, weighbridge, quality lab instruments.
- Data: Process setpoints, quality records, batch genealogy.
- Facilities: Plant site, raw-material silo, finished-goods warehouse.
- Third parties: Vendor R (raw material), Vendor S (automation and control
  maintenance), logistics carrier.
- Fourth parties (material): Vendor R sources a key input from a single
  mine in Jurisdiction Z.
- Jurisdictions: Jurisdiction X, with upstream exposure to Jurisdiction Z.
- Recovery dependencies: Manual control procedures, buffer stock, Vendor S
  emergency support.
- Concentrations: Vendor R is the leading concentration dependency for raw
  material. Vendor S is the leading concentration dependency for control.
- Manual alternatives: Manual or degraded control for a limited period.
  There is no manual alternative for raw-material supply beyond buffer
  stock.

## 4. Switch Catalog

Three material switches. Safety stop is the priority switch.

Switch SW-M1 (priority safety switch)

- Trigger: Control-system fault, safety interlock or any condition that
  makes continued running unsafe.
- Action: Stop the line safely under controlled shutdown.
- Authorized decision-maker: Shift supervisor, with the safety officer
  able to stop unilaterally.
- Operator: Control-room engineer.
- Prerequisites: Controlled shutdown sequence available, interlocks
  functional.
- Execution time: Minutes to a safe stopped state.
- Communications: Notify plant operations director, safety function,
  affected customers if delivery is at risk.
- Rollback or stabilization: Line held safe until fault cleared.
- Evidence generated: Shutdown log, alarm record.
- Latest test result: Exercised in a real controlled stop 2026-02-11 (T4),
  performed within minutes, passed.

Switch SW-M2

- Trigger: Vendor S control system impaired but the line can run safely on
  reduced automation.
- Action: Switch to manual or degraded control.
- Authorized decision-maker: Plant operations director.
- Operator: Senior control-room engineer.
- Prerequisites: Trained manual operators available, degraded-mode
  procedure current.
- Execution time: Target under 2 hours to stable degraded operation.
- Communications: Maintenance, safety, customers if throughput drops.
- Rollback or stabilization: Return to full automation after Vendor S
  restores the system.
- Evidence generated: Mode-change record, throughput log.
- Latest test result: T1 tabletop 2026-05-05. Not performed on the line.

Switch SW-M3

- Trigger: Vendor R delivery delayed.
- Action: Draw down buffer stock to extend production runway.
- Authorized decision-maker: Plant operations director.
- Operator: Materials handler.
- Prerequisites: Buffer stock available and within specification.
- Execution time: Immediate.
- Communications: Procurement, commercial.
- Rollback or stabilization: Replenish buffer once supply resumes.
- Evidence generated: Stock drawdown record.
- Latest test result: Occurs in normal operations, evidenced, but never
  tested to buffer exhaustion.

## 5. Priority exit plan

For Vendor R, the leading raw-material concentration.

- Dependency being exited: Vendor R raw-material supply.
- Exit triggers: Sustained Vendor R delivery failure, quality failure, or
  loss of the upstream mine in Jurisdiction Z.
- Legal and contractual rights: Supply agreement permits sourcing
  elsewhere on Vendor R default, but no alternate is contracted.
- Notice requirements: Contractual notice to Vendor R on termination.
- Data actions: Not data-centric. Transfer of specifications to a new
  supplier would be required.
- Transition steps: Identify candidate supplier, qualify material, run
  trial production, contract, switch.
- Substitute arrangement: No second supplier is qualified. Substitute
  capacity is not available today.
- Resource and cost assumptions: Qualification takes an estimated 3 to 6
  months. Not funded.
- Residual risks: The candidate supplier may also depend on the same mine
  in Jurisdiction Z.
- Target execution time: Not achievable within tolerance today.
- Evidence requirements: Qualification record, trial production results.
- Latest rehearsal result: None. Exit is described, not built.

## 6. Exercise and evidence record

- Latest scenario: Vendor S control-system fault during a production run.
- Exercise tier: T1 facilitated tabletop for the control-loss scenario.
  The safety stop itself has T4 evidence from a real event.
- Date: 2026-05-05 (tabletop). 2026-02-11 (real controlled stop).
- Participants: Shift supervisor, control-room engineers, safety officer,
  maintenance lead.
- Actions simulated: Manual control switchover, customer communication.
- Actions performed: Discussion only for the control-loss scenario. The
  safety stop was actually performed in the February event.
- Elapsed times: Not captured for the tabletop. Safety stop achieved in
  minutes in the real event.
- Tolerance met or not met: Cannot Determine for a full supplier-loss
  scenario. The 24-hour tolerance has not been tested to buffer
  exhaustion or to supplier switch.
- Evidence pack: Shutdown log and alarm record for the February event.
  Tabletop notes for the May session.
- Findings: Safety stop is strong. Manual control is unproven on the line.
  There is no executable exit for raw material.
- Corrective actions: Qualify a second raw-material supplier. Perform a
  live manual-control test. Test buffer runway to exhaustion in a
  controlled way.
- Retest status: Not scheduled.

---

## Appendices

- A. Evidence ledger extract: see [`assessment.md`](assessment.md).
- B. Safety note: any test that approaches buffer exhaustion or manual
  control must be run under the safety function with a controlled-stop
  fallback.

Final Liability rests with the Human.
