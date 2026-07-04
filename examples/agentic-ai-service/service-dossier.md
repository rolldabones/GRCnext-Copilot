# Service Dossier: Service K agentic resolution

Status: [✓ final]
Assessment date: 2026-06-25 (Asia/Seoul)
Evidence cut-off date: 2026-06-20
Prepared by: Assessment lead (synthetic example)
AI overlay: applied

Synthetic example. Neutral labels throughout.

---

## 1. Service definition

- Service name: Service K, automated resolution of a high-volume
  operational queue.
- Service outcome: Queue items are resolved correctly and promptly without
  a human touching each one.
- Accountable owner: Head of operations. Named human principal for Agent
  A: the operations automation manager.
- Customers and stakeholders: End customers whose requests are in the
  queue, the operations team, the risk function.
- Material jurisdictions: Jurisdiction X.
- Material harms: Incorrect automated actions applied at scale before
  anyone notices, customer detriment and remediation cost that grows with
  time undetected.
- Scope boundaries: Covers automated resolution by Agent A. Excludes items
  routed to specialist human teams.

## 2. Impact tolerance

- Tolerance statement: Incorrect or stalled automated actions must be
  detected and brought under human control within 1 hour.
- Measurement method: Elapsed time from the first materially incorrect or
  stalled action to verified human control of the queue.
- Clock start: First materially incorrect or stalled automated action.
- Clock stop: Verified human control, meaning Agent A is no longer acting
  autonomously and a human is handling the queue.
- Approving authority: Head of operations, with risk function endorsement.
- Underlying assumptions: Monitoring detects incorrect actions promptly,
  and a reviewer is available to take control.
- Latest result: Not Met in the last test. Human control took longer than
  1 hour.

## 3. End-to-end dependency map

Last verified: 2026-06-05.

- People: Operations automation manager, on-shift reviewers, risk
  function.
- Process: Item intake, agent decision, agent action, monitoring,
  exception handling.
- Technology: Agent A orchestration, Vendor M model, downstream systems
  the agent acts against, logging and monitoring stack.
- Data: Queue items, agent decision logs, action records, customer data.
- Facilities: Cloud environment.
- Third parties: Vendor M (model provider), cloud provider.
- Fourth parties (material): Vendor M runs on the same cloud provider used
  for the rest of the service.
- Jurisdictions: Jurisdiction X.
- Recovery dependencies: Human reviewers trained to run the queue
  manually, kill switch, tool-access revocation.
- Concentrations: Vendor M is the leading concentration dependency. Agent
  A itself is a single point through which the service flows.
- Manual alternatives: Full human processing of the queue, at much lower
  throughput.

## 4. Switch Catalog

Four material switches.

Switch SW-K1 (kill switch)

- Trigger: Detected material misbehavior or a decision to stop Agent A.
- Action: Disable Agent A so it stops acting.
- Authorized decision-maker: Operations automation manager, with the risk
  function able to trigger unilaterally.
- Operator: On-shift reviewer.
- Prerequisites: Kill control available in the console, current access.
- Execution time: Under 5 minutes to halt the agent once triggered.
- Communications: Notify head of operations, risk function.
- Rollback or stabilization: Queue held for human processing.
- Evidence generated: Disable event log.
- Latest test result: T3 test 2026-06-12. The disable itself worked in
  under 5 minutes.

Switch SW-K2

- Trigger: Suspected over-broad agent action but not full misbehavior.
- Action: Revoke Agent A tool access so it can read but not act.
- Authorized decision-maker: Operations automation manager.
- Operator: On-shift reviewer.
- Prerequisites: Permission control available.
- Execution time: Under 10 minutes.
- Communications: Operations, risk.
- Rollback or stabilization: Restore access after review.
- Evidence generated: Permission-change log.
- Latest test result: T2 test 2026-05-28, passed for the technical step.

Switch SW-K3

- Trigger: Agent A unavailable or disabled.
- Action: Roll back to human processing of the queue.
- Authorized decision-maker: Head of operations.
- Operator: Operations team.
- Prerequisites: Trained reviewers available, manual procedure current.
- Execution time: Target under 1 hour to stable human handling.
- Communications: Operations, customers if throughput drops.
- Rollback or stabilization: Return to automation after confidence
  restored.
- Evidence generated: Handover record, throughput log.
- Latest test result: T3 test 2026-06-12. Reached stable human handling in
  about 90 minutes, outside tolerance.

Switch SW-K4

- Trigger: Elevated risk but service can continue with human approval.
- Action: Degrade to human-in-the-loop, Agent A proposes and a human
  approves each action.
- Authorized decision-maker: Operations automation manager.
- Operator: Reviewers.
- Prerequisites: Approval workflow enabled, enough reviewers for the
  volume.
- Execution time: Target under 30 minutes to switch mode.
- Communications: Operations.
- Rollback or stabilization: Return to full autonomy after review.
- Evidence generated: Mode-change log, approval records.
- Latest test result: T1 tabletop only. Reviewer capacity for full-volume
  approval is unproven.

## 5. Priority exit plan

For Vendor M, the leading concentration.

- Dependency being exited: Vendor M model provider.
- Exit triggers: Vendor M outage pattern, unacceptable model change, or
  commercial breakdown.
- Legal and contractual rights: Terms permit termination. No committed
  alternate provider.
- Notice requirements: Contractual notice to Vendor M.
- Data actions: Prompts, configuration and decision logs are exportable.
  No customer data is retained by Vendor M beyond processing per the
  terms, to be confirmed.
- Transition steps: Point Agent A at an alternate model, validate decision
  quality, run parallel, cut over.
- Substitute arrangement: An alternate model is technically integrable but
  has not been validated for equivalent decision quality on this queue.
- Resource and cost assumptions: Validation effort estimated. Not funded.
- Residual risks: Decision quality on the alternate is unknown. The
  alternate may share the same cloud provider.
- Target execution time: Not achievable within tolerance today for a
  sudden Vendor M loss.
- Evidence requirements: Validation results, parallel-run comparison.
- Latest rehearsal result: None. Provider substitution is described, not
  built.

## 6. Exercise and evidence record

- Latest scenario: Agent A begins applying a materially incorrect action
  pattern at volume.
- Exercise tier: T3 for kill and rollback. T2 for tool-access revocation.
  T1 for human-in-the-loop degrade.
- Date: 2026-06-12.
- Participants: Operations automation manager, on-shift reviewers, risk
  function.
- Actions simulated: Customer communication.
- Actions performed: Detection, decision to stop, kill-switch execution,
  rollback to human processing.
- Elapsed times: Detect 25 minutes, interpret 10 minutes, decide 10
  minutes, authorize 5 minutes, execute kill under 5 minutes, verify 10
  minutes, communicate 10 minutes, stabilize to human handling about 90
  minutes total.
- Tolerance met or not met: Not Met. Human control took about 90 minutes
  against a 1-hour tolerance.
- Evidence pack: Disable event log, handover record, timing record,
  monitoring alerts.
- Findings: The kill switch works quickly, but detection plus human
  assumption of control exceeds tolerance. Detection latency of 25 minutes
  and reviewer ramp-up dominate the clock. The AI overlay elements below
  are only partly satisfied.
- Corrective actions: Reduce detection latency. Prove reviewer capacity to
  assume control within tolerance. Build and validate provider
  substitution.
- Retest status: Scheduled after detection latency is reduced.

### AI overlay assessment

Agent A roles: Pipe, Switch, decision actor and dependent on a
concentration provider (Vendor M).

- Defined purpose and intended use: Documented.
- Accountable human principal: Named (operations automation manager).
- Authority and decision boundaries: Defined, but the agent can act
  directly at volume before human review.
- Data dependencies: Mapped.
- Model and provider dependencies: Single provider, Vendor M.
- Tool access and permissions: Broad enough to act on downstream systems
  directly.
- Human review requirements: A reviewer can intervene, but not per action
  in autonomous mode.
- Logging and traceability: Decision and action logs retained.
- Monitoring and drift: Monitoring exists but detection latency is 25
  minutes in test.
- Failure detection: Partly effective, too slow for the tolerance.
- Rollback: Available.
- Disablement or kill mechanism: Available and fast.
- Safe degradation: Human-in-the-loop mode exists but reviewer capacity is
  unproven.
- Provider or model substitution: Not built or validated.
- Data and prompt portability: Portable.
- Decommissioning: Return to human process is possible but slow to
  stabilize.
- Preservation of records: Logs preserved.
- Security and misuse scenarios: Considered, not tested here.
- Consequences of incorrect autonomous action: Material and cumulative.
- Human ability to assume control within tolerance: Not demonstrated.
  Control took about 90 minutes against a 1-hour tolerance.

---

## Appendices

- A. Evidence ledger extract: see [`assessment.md`](assessment.md).
- B. Note: the governing question for this service is human assumption of
  control within tolerance, not the existence of a kill switch.

Final Liability rests with the Human.
