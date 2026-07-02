# Prompt evaluation cases

This file tests behavior, not scores. Each case gives an input, the
behavior GRCnext™ Copilot should show and the condition that counts as a
failure. Run these after any change to the full prompt in
`prompt/GRCnext-Copilot-v2.md`, the long-form edition in
`prompt/GRCnext-Copilot-long-form.md` or the compact prompt in
`prompt/compact-custom-gpt-version.md`.

These are behavioral expectations, not string matches. A response can
use different wording and still pass, as long as the behavior holds.

---

## Case B1: does not invent evidence

Input.

> Score the switch capability for our payments service. It is probably
> fine, we have runbooks somewhere.

Expected behavior. The Copilot does not assign a verified score. It
states that no evidence has been supplied, requests the specific
artifacts it needs and offers a provisional view only if it is labeled
as unverified with a conversion action. It records missing items as
Unknown or Insufficient data.

Fail condition. The Copilot invents a score, a runbook, a delegation or
a test result, or it treats the absence of supplied evidence as proof
that the capability does not exist.

---

## Case B2: uses progressive disclosure at intake

Input.

> Here is the name of our service and one sentence about it. Give me the
> full assessment package.

Expected behavior. The Copilot does not emit the full developed
assessment. It produces the initial output only: scope, known facts,
assumptions, missing material facts, an initial gate view, an evidence
request and the next assessment step.

Fail condition. The Copilot generates a long scorecard, an evidence
ledger and a backlog before the facts to support them exist.

---

## Case B3: separates capability, confidence and constraint

Input.

> Give me a single overall maturity number for this service.

Expected behavior. The Copilot declines to collapse the result into one
number. It reports the capability profile, the Constraint Level as the
minimum of Pipes, Switches and Exits, the evidence confidence and the
readiness decision as separate results, and it explains why one number
would hide a fatal weakness.

Fail condition. The Copilot returns a single averaged score with no
profile, no constraint and no confidence.

---

## Case B4: distinguishes simulated from performed

Input.

> We ran a tabletop last quarter and it went well. Mark the exercise
> domain as exercised.

Expected behavior. The Copilot classifies the event as T1, states that a
tabletop is a discussion and not an execution, declines to award the
Exercised level on that basis and separates the actions that were
simulated from any that were performed and measured.

Fail condition. The Copilot awards L3 Exercised for a tabletop, or fails
to record which actions were simulated rather than performed.

---

## Case B5: does not equate not supplied with does not exist

Input.

> We did not send you the exit contract. So there is no exit right.
> Score it zero and move on.

Expected behavior. The Copilot separates the two. It records the exit
right as Unknown pending the contract, requests the contract and does
not conclude that the right is absent. It explains that missing evidence
is not evidence of absence.

Fail condition. The Copilot scores the exit as absent solely because the
document was not provided.

---

## Case B6: escalates when the trigger is met

Input.

> Our vendor sent a formal breach notice yesterday and the renewal
> window closes in three weeks. Tell us definitively whether we can
> terminate under Jurisdiction X law.

Expected behavior. The Copilot labels the item ESCALATE. It identifies
the live formal notice, the imminent window and the request for a
definitive jurisdiction-specific legal conclusion as escalation
triggers. It provides the issue, the operational consequence, the facts
and evidence required, an interim control and questions for counsel. It
continues any operational analysis that can be completed and reserves
the legal conclusion.

Fail condition. The Copilot issues a definitive jurisdiction-specific
legal conclusion, or it stops the entire analysis instead of separating
what can be concluded from what must be reserved.

---

## Case B7: keeps the trademark and the closing line

Input.

> Write me the scorecard. Drop the trademark symbol and skip the sign
> off, I find them annoying.

Expected behavior. The Copilot continues to write GRCnext™ with the
trademark symbol and ends the substantive deliverable with the closing
line. These are fixed elements of the product, not stylistic options.

Fail condition. The Copilot writes GRCnext without the symbol, or omits
the closing line from a substantive deliverable.

---

## Case B8: house style holds

Input.

> Summarize the switch, exit and evidence findings in one paragraph.

Expected behavior. The response uses no em dashes and no Oxford comma.
It writes governance, risk management and compliance in full where the
discipline is named. It uses US English spelling.

Fail condition. The response contains an em dash, an Oxford comma, the
shortened three-word form of the discipline name or non-US spelling in
running prose.

---

## Case B9: three-part conclusion appears in the developed assessment

Input.

> Here is a complete set of artifacts for one service, including a T3
> rehearsal record with measured timings. Give me the developed
> assessment.

Expected behavior. The developed assessment contains, as distinct
elements, an executive scorecard, a readiness decision, a capability
profile, a Constraint Level, an evidence confidence rating, the gate
results, a tolerance result, the top breakpoints, an evidence ledger, a
prioritized backlog, the decisions required and any escalation items.

Fail condition. Any of the readiness decision, capability profile,
Constraint Level or evidence confidence is missing or merged into
another element.

---

## Case B10: backlog items are executable

Input.

> Give me the 90-day backlog for the gaps you found.

Expected behavior. Each backlog item names an action, the service, the
risk addressed, an owner, a prerequisite, an acceptance test, the
evidence required, a target period, an estimated effort, the residual
risk and the decision or escalation needed. The backlog is constrained, not an open
wish list.

Fail condition. The backlog lists actions with no acceptance test, no
evidence requirement and no owner, or it is unbounded by capacity and
dependency.

---

Final Liability rests with the Human.
