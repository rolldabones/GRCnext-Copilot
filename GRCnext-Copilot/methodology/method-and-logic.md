# Method and logic

This is the conceptual foundation of GRCnext™ Copilot. The other
methodology files are operational. `capability-model.md` states what each
domain tests. `scoring-method.md` states the arithmetic.
`evidence-standard.md` states how proof is weighed. `exercise-tiers.md`
states how testing is graded. `glossary.md` fixes the terms. This file
states the reasoning underneath all of them: why the method is built the
way it is, what its primitives are for, and how to apply its logic when a
specific rule does not squarely decide a case.

Read it if you want to understand the method rather than only run it. It
is the long form of the idea that the prompt expresses in imperatives.

## 1. The governing idea: a governance control is an escapement

An escapement is the part of a mechanical timepiece that releases stored
energy a little at a time, at a controlled rate, so the movement keeps
accurate time over long periods without anyone touching it. It is a
mechanism for staying reliable over time without constant intervention, by
removing a dependence on something fragile. That is also a fair
description of good governance.

The frameworks that make up GRCnext™ are made of mechanisms in that same
spirit. A control that works only while someone is paying attention will
fail the moment attention lapses, and attention always lapses. The better
control, like the better escapement, removes the dependence. A governance
control, done properly, is an escapement. It keeps the thing honest over
time.

This is not a decorative analogy. It decides what the method credits and
what it refuses to credit. A policy that permits an action depends on
someone reading it, understanding it, being available and choosing to act
inside the tolerance. That is a dependence on attention. A tested switch
with delegated authority, current access and a rehearsed sequence does not
depend on attention in the same way. It has been built into the system in
advance so it holds when no one is watching. GRCnext™ credits the second
and not the first, and every rule in the method is downstream of that
choice.

Two consequences run through everything below. First, the unit of credit
is the mechanism, not the permission. Second, a mechanism is bounded by
its weakest engaging part, which is why the weakest of the structural
components governs the constraint. Both come straight from the escapement
idea.

## 2. What the method measures: Global Optionality

GRCnext™ measures one thing: whether an organization holds Global
Optionality. That is the set of choices it can actually execute when a
critical service, dependency, provider, jurisdiction, technology or
operating assumption becomes unavailable or unacceptable, as opposed to
the set of choices it is merely permitted to consider.

The distinction is the whole method in one line. A policy that permits an
action is not optionality. Optionality is an authorized person executing
that action, within the impact tolerance, using tested procedures that
produce recoverable evidence. Everything the Copilot does is an attempt to
tell those two apart under stress, because under stress is the only
condition that matters. A choice that exists on a calm Tuesday and
evaporates during an incident was never optionality. It was the appearance
of it.

This is why the method is preoccupied with execution, timing and evidence
rather than with documents. Documents describe intended choices. Execution
under a severe but plausible scenario, measured against a tolerance and
recorded in evidence, is the only thing that demonstrates a choice was
real.

## 3. Why the unit of analysis is the critical service

The method assesses critical services, not applications, departments,
vendors, process steps, assets or org-chart entries. A critical service is
an outcome delivered to a defined customer or stakeholder whose disruption
beyond an approved period or level would create material harm.

The reason is that optionality is only meaningful with respect to an
outcome that matters to someone. You cannot say whether a choice is worth
preserving until you know what outcome it protects and what harm follows
if that outcome fails. An application can be down without the service
failing, if there is a switch. A vendor can be lost without the service
failing, if there is an exit. Anchoring the assessment to the outcome, and
treating applications, vendors and the rest as dependencies of that
outcome, is what lets the method reason about switches and exits at all.
Anchor to an asset instead and you end up protecting the asset rather than
the outcome, which is how organizations come to have well-defended systems
and undefended customers.

## 4. The five primitives and why each exists

GRCnext™ is built from five primitives: Services, Tolerances, Pipes,
Switches and Exits. They are the design vocabulary of the method. Each one
builds optionality into a system before it runs, and each answers a single
question. The capability model scores them. This section explains why each
one is a primitive at all.

**Services** are the outcome the method keeps honest. A Service is a
primitive because without a defined outcome there is nothing to bound, to
steer or to leave. It is the subject of every other primitive. Get the
Service wrong, by naming a system or a team instead of an outcome, and
every later judgment inherits the error.

**Tolerances** are the bound the Service must stay inside. A Tolerance is a
primitive because it is the regulated rate of the escapement. It is the
standard that makes every other judgment measurable. A switch is not good
or bad in the abstract. It is fast enough or too slow against a tolerance.
An exit is not adequate in the abstract. It is inside or outside a
tolerable time and cost. Remove the Tolerance and the method loses its
unit of measure, and assessments collapse into opinion. A tolerance is
real only when it is measurable, approved by someone with standing to
accept the underlying risk and started from the correct event rather than
from the moment the organization happens to notice.

**Pipes** are the dependencies through which the Service is delivered. Pipes
are a primitive because you cannot steer or leave what you have not
mapped. The Pipe map is how the organization knows what is fragile, and
fragility is what switches and exits exist to address. The characteristic
Pipe failure is a map drawn once and never revisited, which is a document
rather than a decision aid. Currency is tested, not just existence,
because a stale map fails at exactly the moment it is needed.

**Switches** are authorized actions that change how the Service runs, so it
can be steered back inside its tolerance. A Switch is a primitive because
it is the escapement's lever, the thing that can be thrown. The decisive
question is never whether a runbook exists. It is whether an authorized
person could operate the switch, tonight, within tolerance, and prove it
happened. A switch that depends on one person being reachable, or on
credentials that have expired, or on a decision no one is empowered to
make out of hours, is a switch that depends on attention, and so it is not
yet a mechanism.

**Exits** are predesigned paths for leaving or replacing a dependency, so a
fragile dependence can be removed rather than merely worked around. An Exit
is a primitive because a switch changes how the Service runs while an exit
changes what it depends on, and those are different powers. A switch keeps
you inside a tolerance during a disruption. An exit lets you stop
depending on the thing that caused it. The characteristic Exit failure is
treating a clause as a capability. A clause is a right. A capability is a
rehearsed path with substitute capacity identified and data proven
portable. The method scores the second.

The five are ordered by dependence. Services and Tolerances set the
target. Pipes reveal what is fragile. Switches steer within the bound.
Exits remove the fragile dependence. Read in that order, they are not a
checklist but a chain of reasoning about how a system can be steered and
bounded and left without someone watching it every second.

## 5. From five primitives to six scored domains

The rubric scores six domains, not five. The mapping is deliberate and
worth holding clearly, because it is where readers most often expect a
one-to-one correspondence and do not find one.

Services and Tolerances combine into a single domain. They are separated
as primitives because they answer different questions, but they are scored
together because a tolerance is meaningless without the service it bounds
and a service without a tolerance cannot be assessed at all. They are one
target, so they are one score.

Pipes, Switches and Exits are one domain each. They are the three
structural components of optionality, and they are scored separately
because the method needs to see each one on its own to find the weakest.

Exercises and Evidence and improvement are the fifth and sixth domains,
and they are not primitives. This is the important part. They are the
proof domains. Exercises test whether the structure holds under stress.
Evidence and improvement determines whether any of the other five domains
can be believed. They exist because a method that scored only the design
primitives would reward paperwork. An organization could describe five
excellent primitives and have tested none of them, and a design-only
method would call that mature. The two proof domains are what make
GRCnext™ an evidence method rather than a documentation method. They are
the difference between a plan and a capability.

So the six domains are the five primitives, with Services and Tolerances
folded into one target, plus the two disciplines that decide whether the
primitives are real. Four domains describe the mechanism. Two test it.

## 6. The logic of scoring

Every assessment reports four results and a tolerance result, and refuses
to collapse them into one. The refusal is the point.

**Capability, confidence and constraint are three different questions.**
Capability is what the organization appears able to do, domain by domain.
Confidence is how strongly the evidence supports that appearance.
Constraint is which single structural component will give way first under
stress. A single overall number cannot carry all three, and the act of
producing one destroys exactly the information an auditor needs. A polished
design on weak evidence and a tested design on strong evidence can produce
the same average and are not the same thing. The method shows the profile,
the confidence and the constraint side by side so that difference stays
visible.

**The Constraint Level is the escapement principle applied to scoring.**
Constraint Level is the minimum of Pipes, Switches and Exits. A mechanism
is bounded by its weakest engaging part. The most elaborate escapement
fails at the one tooth that will not catch, and a service with strong Pipes
and Switches but a described-only Exit is constrained at the Exit, because
that is where it gives way. The minimum is not averaged with the other
domains and does not replace the capability profile. It sits beside it and
names the tooth that will not catch. This is why the method retains the
minimum rule from earlier versions but demotes it from the whole score to
one result among several. The minimum still tells you the binding
constraint. It was never the whole story, and treating it as the whole
score hid the profile that an improver needs.

**Maturity is graded on execution, not documentation.** The five maturity
levels run from Unowned to Instrumented, and the two rules that matter
most are that a discussion-based tabletop does not by itself earn the
Exercised level and that dashboards do not by themselves earn Instrumented.
Both rules exist to stop description from being mistaken for demonstration.
Exercised means the capability was exercised and measured. Instrumented
means it is monitored, periodically exercised and managed through current
metrics, defined triggers, verified evidence and closed loops. A screen is
not instrumentation. A conversation is not an exercise.

**The gates are the catch-check.** Eight core gates ask whether the
mechanism reliably catches: is there a service and owner, an approved
measurable tolerance, a mapped set of dependencies, available switch
authority, at least one executable exit for the leading concentration, at
least one completed severe but plausible exercise, evidence of the
tolerance result and owned dated corrective actions. Any one of them
failing or unknown blocks an unqualified Demonstrated conclusion, because a
mechanism that fails at any one of these does not reliably keep time,
however good the rest of it looks. The gates are deliberately blunt. They
are not scored on a scale. They pass, provisionally pass, fail, are
unknown or do not apply, and a single core failure is enough to withhold
the top decision.

**The readiness decision follows from the gates and the evidence, not from
the profile.** Demonstrated requires the core gates to pass, the capability
to have been exercised, and evidence of execution within tolerance.
Conditionally Demonstrated is for a real design with one or more elements
still provisional, partially tested or dependent on remediation. Not
Demonstrated is for a failed core gate, absent critical evidence or
execution never shown within tolerance. A strong capability profile does
not by itself produce a Demonstrated decision, because the decision is
about proof of execution, and the profile is only about apparent ability.

## 7. The logic of evidence

Credit is earned by evidence, not by description. The governing rule is
that there is no verified credit without verified evidence, and its
corollary is that not supplied is never the same as does not exist.

The corollary carries as much weight as the rule. An assessment that
inferred absence from silence would punish organizations for not having
handed over a document, and would reward whoever submitted the most paper.
So missing evidence produces an Unknown or a Not Demonstrated finding and a
request for what is missing. It never produces a finding that a capability
is absent. The Copilot records what it could not verify and asks for it. It
does not conclude from the gap.

Evidence is ranked by how close it sits to actual execution. A statement
that a procedure exists is weaker than a record that it ran. An interview
representation is weaker than a controlled document, which is weaker than a
system record, which is weaker than an observed test, an exercise record, a
production event or an independent assurance result. The method prefers
evidence of execution over statements of intended procedure at every turn,
because intention is what fails under stress and execution is what
survives it.

Two disciplines protect the evidence logic from quiet corruption.
Freshness treats evidence as current only for a period set by the
volatility of what it proves, so a rehearsal from three years ago for a
capability claimed as current is stale and drops to provisional.
Contradiction requires that when two artifacts conflict on a material
claim, the claim is marked Contradicted and cannot support a Demonstrated
decision until the conflict is reconciled, rather than being quietly
resolved in favor of the more flattering document. Both disciplines exist
because the most dangerous evidence is not absent evidence, which is
obvious, but stale or conflicting evidence that looks like proof.

## 8. The logic of the clock

The method measures the full execution sequence, not just the technical
action: detect, interpret, decide, authorize, execute, verify, communicate,
stabilize. The tolerance is met only when stabilization completes within
the approved tolerance from the correct clock-start event.

The reason is that the concealed failures live in the human steps, not the
technical one. A switch that runs in two hours can still fail a twelve-hour
tolerance if authorization and communication add eighteen more. The most
common pattern the method is built to catch is a fast technical action
sitting behind a slow human authorization, which is invisible if you
measure only execution time and obvious if you measure the whole clock.
This is also why the authorize step is tested against real out-of-hours
conditions rather than against the assumption that the right person is at
their desk. Attention always lapses, and the clock is where the lapse
shows up as elapsed time.

The clock is also what makes the human-in-the-loop analysis rigorous for
AI. The time for a human to detect that an agent has gone wrong, obtain the
authority to intervene and actually assume safe control of the service is
elapsed time on the clock. A kill switch that stops the agent in seconds
does not help if assuming safe control of the service takes longer than the
tolerance allows. The method measures that, and it is frequently the
binding constraint.

## 9. Applying the method

In practice the method runs through four movements: frame the service and
its tolerance, interrogate the facts and evidence, stress-test the claimed
capability under a severe but plausible scenario and decide. The
primitives give the interrogation its structure. You are always asking, for
this service and this tolerance, what are the Pipes, what are the Switches,
what are the Exits, and what has been exercised and evidenced.

A few traps recur often enough to name.

The asset trap is protecting a system instead of the outcome it serves. The
cure is to insist on the service definition before anything else.

The permission trap is crediting a control because a policy allows it. The
cure is the execution question: who, tonight, within tolerance, with proof.

The clause trap is treating an exit right as an exit capability. The cure is
to ask for the rehearsal, the substitute capacity and the portable data.

The tabletop trap is calling a conversation an exercise. The cure is the
tier scale and the demand to say what was simulated and what was performed.

The freshness trap is treating an old test as current proof. The cure is to
date every piece of evidence and set a freshness period.

The average trap is collapsing the profile into one number that hides the
weak component. The cure is to keep capability, confidence and constraint
apart on the face of the assessment.

Reading a result follows the same discipline. Look first at the readiness
decision and the tolerance result, because they say whether optionality was
demonstrated. Look next at the Constraint Level, because it names the
binding weakness. Look at the evidence confidence, because it says how much
to trust the rest. Only then read the full capability profile, which tells
you where the work is. An assessment read in that order tells you what to
fix first and why.

## 10. A method in the making

GRCnext™ is a work in progress and it has to be. It is not worked out in
theory and then applied. It is developed in deployments, with Clients, and
made fit for their purpose. In some sense it is all still in the making.

This is a design stance, not an apology. A governance method that claimed
to be finished would be making the same mistake it warns Clients against,
crediting a description over a demonstration. The rubric earns its
authority the same way it asks Clients to earn theirs, by being exercised
against real services and corrected when it does not fit. Where a case does
not fall cleanly inside a rule, the method asks the assessor to reason from
the escapement idea, state the assumptions and say what evidence would
settle the question. That is the method behaving consistently with its own
logic. A control that works only while someone is paying attention will
fail the moment attention lapses. So will a rubric that stops being tested.

## 11. How this fits the rest of the repository

This document is the why. The rest of the repository is the how.

For what each domain tests in detail, see `capability-model.md`. For the
maturity scale, the four results, the gates and a worked scoring
walkthrough, see `scoring-method.md`. For verification states, evidence
types, freshness and contradiction, see `evidence-standard.md`. For the
tier scale and the execution clock, see `exercise-tiers.md`. For fixed
definitions and the alignment with United Kingdom operational resilience
policy and the European Union Digital Operational Resilience Act, see
`glossary.md`.

For the operating instructions that turn this logic into an assistant, see
the prompts in `prompt/`. The long-form edition,
`prompt/GRCnext-Copilot-long-form.md`, carries this reasoning inline. The
modular edition, `prompt/GRCnext-Copilot-v2.md`, is the authoritative
prompt paired with this repository. For the method applied end to end, see
the three worked assessments in `examples/`.

Final Liability rests with the Human.
