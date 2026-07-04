# Assessment: Service K agentic resolution

Status: [✓ final]
Assessment date: 2026-06-25 (Asia/Seoul)
Evidence cut-off date: 2026-06-20
AI overlay: applied

Synthetic example. Neutral labels. Not legal or regulatory advice.

## TL;DR

- Agent A has a fast, tested kill switch, but the service still fails its
  1-hour tolerance because a human cannot assume control quickly enough.
- ⧉ The single biggest gap is human assumption of control. It took about
  90 minutes in a T3 test against a 1-hour tolerance. A kill switch that
  halts the agent is not the same as a human running the queue safely
  within tolerance.
- The Constraint Level is 2, set by Exits, because provider substitution
  is not built.
- Readiness decision is Not Demonstrated. The tolerance was Not Met in
  test.
- Detection latency of 25 minutes and unproven reviewer capacity dominate
  the execution clock.

## A. Capability profile

| Domain | Score | Basis |
|---|---|---|
| Services and tolerances | 3 | Defined, owned, 1-hour tolerance approved with explicit clock events, but detection evidence is Provisional (E-K3), so instrumentation is not shown |
| Pipes | 3 | Mapped, Vendor M concentration and shared cloud fourth-party identified, Agent A itself a single point |
| Switches | 3 | Kill and rollback tested at T3, but rollback stabilizes outside tolerance and degrade mode is only T1 |
| Exits | 2 | Prompts portable, but provider substitution not built or validated for decision quality |
| Exercises | 3 | A genuine T3 stop-and-rollback test with full clock timing, though degrade and exit are weaker |
| Evidence and improvement | 3 | Strong logging and a real timed test, but key corrective actions are open |

## B. Constraint level

Constraint Level = minimum of Pipes (3), Switches (3), Exits (2) = 2.

The exit is the weakest structural component. The organization can stop
Agent A but cannot move it off Vendor M within tolerance, and the
alternate model is unvalidated for decision quality.

## C. Evidence confidence

Moderate overall, but the governing finding is High-confidence and
negative.

The stop-and-rollback test is well evidenced with full execution-clock
timing. That evidence clearly shows the tolerance was missed. So
confidence in the negative result is High. Confidence in the exit and
degrade paths is Low because they are untested.

## D. Readiness decision

Not Demonstrated.

The kill switch works, but the readiness question is whether the service
can bring incorrect autonomous action under human control within 1 hour.
In test it could not. Core gate 7 shows the tolerance was Not Met, and the
human-assumption-of-control element of the AI overlay is not demonstrated.
That governs the decision regardless of the strong kill-switch score.

## E. Tolerance result

Not Met.

- Clock start: first materially incorrect automated action.
- Clock stop: verified human control of the queue.
- Elapsed: about 90 minutes against a 1-hour tolerance. Detection took 25
  minutes and reviewer ramp-up to stable human handling took most of the
  rest.

## Gate results

| Gate | Status | Note |
|---|---|---|
| Service and owner defined | Pass | Head of operations accountable, named human principal for the agent |
| Tolerance approved and measurable | Pass | 1 hour, clock events explicit |
| Dependencies mapped | Pass | Vendor M concentration, shared cloud, agent single point identified |
| Switch authority available | Pass | Kill authority immediate, risk function can trigger |
| Executable exit for leading concentration | Fail | Provider substitution not built or validated |
| Severe but plausible exercise completed | Pass | T3 stop-and-rollback with full clock timing |
| Evidence shows tolerance result | Pass | Evidence shows the tolerance was Not Met |
| Corrective actions have owners and dates | Provisional Pass | Actions identified, some without firm dates |

Gate 7 passing here is important. The evidence did show a tolerance
result. The result was negative. Gate 5 is a hard Fail on a core gate.

## AI overlay finding

The AI overlay resolves to one governing question: can a human assume
control within tolerance. The answer is no, for three reasons.

1. Detection latency. Monitoring took 25 minutes to surface the incorrect
   action pattern. The clock was already a quarter gone before anyone
   acted.
2. Reviewer capacity. Rolling the queue back to human handling reached
   stable operation in about 90 minutes. Reviewers exist but cannot absorb
   full volume quickly.
3. Degrade path unproven. Human-in-the-loop mode is only a tabletop.
   Reviewer capacity to approve at full volume is unproven, so the milder
   intervention is not yet a real option.

The kill switch is fast and works. That is necessary but not sufficient. A
stopped agent leaves a queue that a human must then run safely within the
tolerance, and that is where the service fails.

## Top breakpoints

1. Human assumption of control exceeds tolerance (about 90 minutes against
   1 hour).
2. Detection latency of 25 minutes consumes much of the clock.
3. No built or validated provider substitution for Vendor M.
4. Human-in-the-loop degrade mode unproven at volume.

## Evidence ledger extract

| Evidence ID | Claim | Type | Status | Freshness | Limitation |
|---|---|---|---|---|---|
| E-K1 | Kill switch halts Agent A within 5 minutes | observed test | Verified | Current | Halts agent, does not run the queue |
| E-K2 | Human control achievable within tolerance | exercise record | Refuted | Current | Test shows about 90 minutes, outside 1 hour |
| E-K3 | Detection surfaces incorrect actions promptly | exercise record | Provisional | Current | 25-minute latency in test |
| E-K4 | Alternate model preserves decision quality | none | Not demonstrated | n.a. | No validation run |

## Prioritized backlog

| Action | Risk addressed | Owner | Acceptance test | Target |
|---|---|---|---|---|
| Reduce detection latency for incorrect action patterns | Clock lost before intervention | Automation manager | Detection within a set fraction of tolerance in retest | 30 days |
| Prove reviewer capacity to assume control within 1 hour | Human control too slow | Head of operations | Timed retest reaching human control within tolerance | 45 days |
| Validate a human-in-the-loop degrade mode at volume | Milder intervention unavailable | Automation manager | Volume approval test | 60 days |
| Build and validate Vendor M provider substitution | No exit for the concentration | AI platform lead | Parallel-run decision-quality comparison | 90 days |

## Decisions required

- Whether Agent A should continue to act autonomously at full volume
  before detection latency and human-control time are brought within
  tolerance, or whether it should run in human-in-the-loop mode in the
  interim.
- Funding for provider-substitution validation.

## Escalation items

⚠ Autonomous action at volume with human control that exceeds tolerance is
a risk-acceptance decision for senior management and the risk function,
not an operational default. Until human assumption of control is
demonstrated within tolerance, running Agent A in a mode where a human
approves actions is the conservative position. If Service K touches
regulated decisions about customers, the autonomy posture may also raise
questions for compliance and counsel.

[Purpose] Score Service K optionality with the AI overlay and test whether
a human can assume control of an agentic system within tolerance.
[Decisions Made] Recorded Not Demonstrated. Kill switch credited as fast
and effective but insufficient because human control missed tolerance.
[Outstanding Items] Detection latency, reviewer capacity, degrade-mode
validation, provider substitution and the interim autonomy decision.

❓ needs input: interim autonomy posture pending remediation.

Final Liability rests with the Human.
