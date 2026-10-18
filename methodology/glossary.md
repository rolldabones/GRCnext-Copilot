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
  authority with standing to accept the underlying risk. Measured from
  the clock start (see Clock start).

Clock start
: The onset of disruption: the moment the critical service first falls
  outside its normal level of delivery, whether or not anyone has
  noticed. Detection is not the clock start. The interval from onset to
  detection is the Detect phase, the first phase of the execution clock.
  Each service dossier names its observable onset event. Where onset
  cannot be established from evidence, the pre-detection interval is
  Unknown; a Met tolerance result then needs an evidenced bound on that
  interval, otherwise the tolerance result is Cannot Determine. The clock
  stops at verified stabilization of the service at or above its
  tolerance level.

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

How the advisory suite narrows each primitive (Services, Tolerances,
Pipes, Switches and Exits) is set out in the
[Primitives in the suite](../advisory-tools/README.md#primitives-in-the-suite)
table.

Exercise
: A structured test of a claimed capability under a scenario, classified
  by tier from T0 to T4. See [`exercise-tiers.md`](exercise-tiers.md).

Concentration dependency
: A single vendor, region, product, dataset, platform, model or interface
  whose failure impairs one service or several services at once.

Execution clock
: The full sequence measured by GRCnext™ from the clock start: Detect
  (onset to detection), Interpret, Decide, Authorize, Execute, Verify,
  Communicate, Stabilize. The tolerance is met only when stabilization
  completes within the approved tolerance measured from the clock start
  (see Clock start).

## Scoring terms

Capability profile
: The six domain scores reported individually. Never averaged.

Constraint Level
: The minimum of Pipes, Switches and Exits. The weakest structural
  component of optionality. A maturity diagnostic: it names the weakest
  domain, not what limits execution.

Binding constraint
: The clock phase or readiness gate that actually limits execution in
  the governing scenario, reported beside the Constraint Level with the
  scenario and a one-sentence basis. The minimum names the weakest
  maturity domain; the binding constraint names the tooth that will not
  catch.

Evidence confidence
: How strongly a conclusion is supported. High, Moderate, Low or
  Indeterminate.

Readiness decision
: Demonstrated, Conditionally Demonstrated or Not Demonstrated, bounded
  by the decision caps in [`scoring-method.md`](scoring-method.md).

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

Not evidenced
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

The three doctrines are used in this repository as stated in
[DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative
statement. Where this repository restates a doctrine, it restates it at its
own altitude and adds instruments, not doctrine (ECOSYSTEM.md protocol item
6). The entries below quote the canonical statements verbatim; each is an
owned doctrine of the author.

Slow AI
: **AI that cannot be governed, explained and audited should not be
  deployed, however fast it would make the business.** A precondition, not
  a speed limit ([DOCTRINE.md section 1](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#1-slow-ai)). The
  principle that GRC owns the clock is GRCnext™'s operating rule, not this
  doctrine.

Informed Intent
: **No AI system, and above all no AI agent, acts on the organization's
  behalf without prior authorization that specifies what it may do, on
  whose authority, within what boundaries and with what exit, given by a
  human who is in a position to give it.**
  ([DOCTRINE.md section 2](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#2-informed-intent))

Final Liability
: **Every material outcome produced by an AI system attaches to a named
  human owner with decision rights, oversight and the power to intervene.
  There is no such thing as an outcome the model is responsible for.**
  ([DOCTRINE.md section 3](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#3-final-liability-rests-with-the-human)).
  The source of the closing line on every substantive deliverable.

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
recovery from an assumed disruption follows that regime. PRA SS1/21
defines an impact tolerance as the maximum tolerable level of disruption
measured by a length of time (para 3.1) and counts its examples from the
disruption itself (paras 3.7 and 4.11); it names no detection trigger, so
the onset rule is GRCnext™'s, consistent with that framing ([SS1/21,
March 2021 text](https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/supervisory-statement/2021/ss121-march-21.pdf),
read 18 October 2026; the Bank of England marks that text superseded by
an updated version, which this note has not compared).

The emphasis on third-party dependency, concentration, exit and
substitutability is aligned with the European Union Digital Operational
Resilience Act, Regulation (EU) 2022/2554 of 14 December 2022
([EUR-Lex](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), read 18
October 2026), published in the Official Journal on 27 December 2022 and applicable since 17
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
