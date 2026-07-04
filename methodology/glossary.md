# Glossary

Defined terms used across GRCnext™ Copilot. Where a term is drawn from or
aligned with an external framework, the lineage is noted at the end.

## Core terms

GRCnext™
: Executable Global Optionality treated as governance, risk management
  and compliance. The claim that an organization holds a lawful,
  authorized and executable choice when a critical service, dependency,
  provider, jurisdiction, technology or operating assumption becomes
  unavailable or unacceptable. GRCnext™ is a trademark of GRC Solutions
  Korea and is always written as one closed word with the trademark
  symbol.

Global Optionality
: The set of choices an organization can actually execute, as opposed to
  the set it is merely permitted to consider. Optionality exists only
  when an authorized person can execute an action, within tolerance,
  using tested procedures, with recoverable evidence.

Critical service
: An outcome delivered to a defined customer or stakeholder whose
  disruption beyond an approved period or level would create material
  harm. The unit of analysis. Not an application, department, vendor,
  process step, asset or org-chart entry, though it may depend on all of
  these.

Impact tolerance
: The maximum tolerable disruption to a critical service, expressed
  against a measurable dimension such as time, and approved by an
  authority with standing to accept the underlying risk. Measurement
  starts at a defined event.

Pipe
: A dependency through which a service is delivered: people, process,
  technology, data, facilities, providers, jurisdictions and their
  interconnections.

Switch
: An authorized action that alters, pauses, isolates, reroutes, degrades,
  substitutes, recovers or stops service delivery. A switch changes how
  the service runs.

Exit
: A predesigned path for leaving or replacing an unacceptable dependency,
  provider, product, region, data arrangement or operating model. An exit
  changes what the service depends on.

Exercise
: A structured test of a claimed capability under a scenario, classified
  by tier from T0 to T4. See [`exercise-tiers.md`](exercise-tiers.md).

Concentration dependency
: A single vendor, region, product, dataset, platform, model or interface
  whose failure impairs one service or several services at once.

Execution clock
: The full sequence measured by GRCnext™: detect, interpret, decide,
  authorize, execute, verify, communicate, stabilize. The tolerance is
  met only when stabilization completes within the approved tolerance
  from the correct clock-start event.

## Scoring terms

Capability profile
: The six domain scores reported individually. Never averaged.

Constraint Level
: The minimum of Pipes, Switches and Exits. The weakest structural
  component of optionality.

Evidence confidence
: How strongly a conclusion is supported. High, Moderate, Low or
  Indeterminate.

Readiness decision
: Demonstrated, Conditionally Demonstrated or Not Demonstrated.

Tolerance result
: Met, Not Met, Not Tested or Cannot Determine, stated with clock-start
  and clock-stop events.

Readiness gate
: One of eight core conditions, each classified Pass, Provisional Pass,
  Fail, Unknown or Not Applicable. A failed or unknown core gate blocks a
  Demonstrated decision.

## Evidence terms

Verified
: Supported by evidence reviewed or observed.

Provisional
: Supported only by a representation, draft or incomplete artifact.
  Carries a mandatory evidence-conversion action.

Not demonstrated
: Evidence is absent or insufficient. Not the same as absent capability.

Contradicted
: Available evidence conflicts and the conflict is unresolved.

Refuted
: Available evidence affirmatively disproves the claim. The disproof and
  the evidence that establishes it are recorded.

Evidence-conversion action
: A named action, with owner and date, that would move a provisional
  claim to verified.

Freshness
: The period for which a given piece of evidence remains current, set by
  the volatility of what it proves. Stale evidence is treated as
  provisional.

## Maturity terms

L0 Unowned, L1 Described, L2 Designed, L3 Exercised, L4 Instrumented
: The five maturity levels applied to each domain. Defined in
  [`scoring-method.md`](scoring-method.md).

## Exercise tiers

T0 Document walkthrough, T1 Facilitated tabletop, T2 Controlled technical
or operational test, T3 End-to-end rehearsal, T4 Live invocation or
actual event
: Defined in [`exercise-tiers.md`](exercise-tiers.md).

## AI overlay terms

AI as Pipe, Switch, decision actor, evidence producer or concentration
dependency
: The roles an AI system may play relative to a critical service. Agentic
  systems additionally require analysis of authority, tool access,
  rollback, kill mechanism and human assumption of control. Defined in
  Section 12 of the full prompt.

## Doctrine terms

Slow AI
: The doctrine that governance owns the clock, and that speed without
  discipline is not a virtue in a system that can act. Owned doctrine of
  the author.

Informed Intent
: The doctrine that a decision must be traceable to a human who
  understood it. Owned doctrine of the author.

Final Liability
: The doctrine that accountability for an outcome rests with a human and
  cannot be delegated to a system. Owned doctrine of the author, and the
  source of the closing line on every substantive deliverable.

## Doctrinal lineage note

GRCnext™ is an original synthesis. Several of its load-bearing terms are
deliberately aligned with established operational-resilience regulation so
that assessments produced with this method map cleanly onto recognized
supervisory language.

The terms impact tolerance, important or critical service and severe but
plausible scenario are aligned with the United Kingdom operational
resilience regime: Financial Conduct Authority Policy Statement PS21/3,
Building operational resilience, and Prudential Regulation Authority
Policy Statement PS6/21 with Supervisory Statement SS1/21, Operational
resilience: Impact tolerances for important business services. Those rules
came into force on 31 March 2022, with firms required to be able to remain
within their impact tolerances for each important business service in a
severe but plausible disruption by 31 March 2025. The GRCnext™ emphasis on
mapping, testing against severe but plausible scenarios and measuring
recovery from an assumed disruption follows that regime.

The emphasis on third-party dependency, concentration, exit and
substitutability is aligned with the European Union Digital Operational
Resilience Act, Regulation (EU) 2022/2554 of 14 December 2022, published
in the Official Journal on 27 December 2022 and applicable since 17
January 2025. DORA established an oversight framework for critical ICT
third-party service providers and requires financial entities to manage
ICT third-party risk, test digital operational resilience and maintain
arrangements that support exit and continuity.

GRCnext™ is not limited to financial services and is not a compliance
mapping to either regime. It borrows their vocabulary because that
vocabulary is precise and supervisory-tested, and it extends the same
discipline to any critical service, including those delivered or affected
by agentic AI. Nothing in this repository asserts conformance with PS21/3,
SS1/21 or DORA. Conformance is an evidence question for a specific
organization, and the Copilot does not claim compliance without evidence.

Final Liability rests with the Human.
