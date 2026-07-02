# Capability model

GRCnext™ Copilot assesses six domains. Each domain is scored from 0 to 4
on the maturity scale in [`scoring-method.md`](scoring-method.md). This
file defines what each domain tests and the sub-elements that evidence
must address. It is the long form of Section 5 of the full prompt. For the
reasoning behind the six domains and the five primitives they score, see
[`method-and-logic.md`](method-and-logic.md).

The six domains map to the GRCnext™ spine. Services and tolerances set
the target. Pipes, Switches and Exits are the three structural
components of optionality. Exercises test whether the structure holds
under stress. Evidence and improvement determines whether any of it can
be believed.

## Domain 1: Services and tolerances

This domain establishes the unit of analysis and the standard against
which everything else is judged.

Tested sub-elements:

- Critical services are defined as outcomes to a customer, not as
  applications, departments, vendors, process steps or assets.
- Customers and stakeholders are identified for each service.
- The material harms from disruption are identified.
- An accountable owner is named for each service.
- An impact tolerance is approved by an authority with standing to
  approve it.
- Tolerance measurement begins at the correct event, not at the moment
  the organization happens to notice.
- The assumptions underlying the tolerance are documented.
- The tolerance is operationally testable, meaning an exercise could
  produce a clear Met or Not Met result.

A common failure here is a tolerance that reads well but cannot be
measured, or a tolerance approved by someone without the authority to
accept the underlying risk.

## Domain 2: Pipes

Pipes are the people, processes, technologies, data, facilities,
providers, jurisdictions and other dependencies through which the
service is delivered. This domain tests whether the organization
actually knows how the service reaches the customer.

Tested sub-elements:

- End-to-end dependencies are mapped, not just the primary system.
- Material providers are identified.
- Fourth-party dependencies are considered where material, meaning the
  dependencies of your dependencies.
- Concentration risks are identified: a single vendor, region, product,
  dataset, platform, model or interface whose failure impairs the service or
  several services at once.
- Jurisdictional constraints are identified.
- Recovery dependencies are mapped, meaning what the recovery path
  itself relies on.
- Manual alternatives are understood, including their capacity limits.
- Dependency data is current enough to support a decision under stress.

A dependency map drawn two years ago and never revisited is a document,
not a decision aid. The Copilot tests currency, not just existence.

## Domain 3: Switches

Switches are authorized actions that alter, pause, isolate, reroute,
degrade, substitute, recover or stop service delivery. This domain tests
whether the organization can act, not merely whether it is permitted to
act.

Tested sub-elements:

- The switch is technically and operationally executable, not just
  described.
- Triggering conditions are defined.
- Decision rights are delegated to a named role.
- Authority remains available outside normal hours and during the
  absence of key individuals.
- Access, credentials and tools required to operate the switch are
  current.
- Downstream effects of operating the switch are understood.
- Communications to affected parties are part of the switch, not an
  afterthought.
- Rollback or stabilization is possible after the switch.
- Execution of the switch can be evidenced.

Representative switches: pause deployment, stop production, disable an AI
agent, isolate a system, reroute payments, invoke a manual process,
change a supplier, restrict a jurisdiction, degrade service safely,
recover from a known-good state.

The decisive question is not whether a runbook exists. It is whether an
authorized person could operate the switch, tonight, within tolerance,
and prove it happened.

## Domain 4: Exits

Exits are predesigned paths for leaving or replacing an unacceptable
dependency, provider, product, region, data arrangement or operating
model. A switch changes how the service runs. An exit changes what the
service depends on.

Tested sub-elements:

- Exit triggers are defined.
- Contractual rights support the exit.
- Transition assistance is available from the incumbent.
- Data can be retrieved in a usable form.
- Deletion at the incumbent can be evidenced.
- Intellectual property and licensing issues are addressed.
- Substitute capacity is available and identified.
- Costs and timing are understood.
- Customer and regulatory obligations during the exit are addressed.
- The exit has been rehearsed.
- Residual dependencies that remain after the exit are identified.

An exit clause in a contract is a right. An exit capability is a
rehearsed path with substitute capacity identified and data proven
portable. The Copilot scores the second, not the first.

## Domain 5: Exercises

This domain tests whether claimed capability has been demonstrated under
a severe but plausible scenario, and how far the demonstration went. It
uses the tier scale and the execution clock in
[`exercise-tiers.md`](exercise-tiers.md).

Tested sub-elements:

- Severe but plausible scenarios exist.
- Pass and fail criteria are tied to the tolerance.
- Relevant owners and authorities participate.
- Switches and exits are actually invoked where feasible.
- Timing is captured across the full execution clock.
- Assumptions and injects are recorded.
- Evidence is preserved.
- Failures produce corrective actions.
- Remediation is retested.

The tier the organization reached matters as much as whether it passed.
A pass at T1 tabletop and a pass at T3 rehearsal are different claims and
receive different maturity credit.

## Domain 6: Evidence and improvement

This domain tests whether any conclusion in the other five domains can be
relied upon, and whether the organization closes what it finds.

Tested sub-elements:

- Artifacts have owners and version control.
- Claims are traceable to evidence.
- Decision records are retained.
- Evidence has a defined freshness period.
- Contradictory evidence is resolved rather than ignored.
- Corrective and preventive actions have owners and deadlines.
- Closure requires verification, not just assertion.
- Overdue actions are escalated.
- Management receives decision-useful reporting.

This domain is where false confidence is caught. Strong scores in
Domains 1 to 5 that rest on stale, self-attested or untraceable evidence
are pulled down here, and the evidence confidence rating reflects it.

## How the domains combine

The six domain scores are reported individually as the capability
profile. The Constraint Level is the minimum of Pipes, Switches and
Exits. Exercises and Evidence set the evidence confidence and gate the
readiness decision. No domain is averaged into another. See
[`scoring-method.md`](scoring-method.md) for the full logic.

Final Liability rests with the Human.
