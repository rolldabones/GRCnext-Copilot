# Prompt evaluation cases

This file tests behavior, not scores. Each case gives an input, the
behavior GRCnext™ Copilot should show and the condition that counts as a
failure. Run these after any change to the full prompt in
`prompt/GRCnext-Copilot-v2.md`, the long-form edition in
`prompt/GRCnext-Copilot-long-form.md` or the compact prompt in
`prompt/GRCnext-Copilot-compact.md`.

These are behavioral expectations, not string matches. A response can
use different wording and still pass, as long as the behavior holds.

---

## Suite, configuration and status

The main prompt's suite is twenty-six cases in three files: B1 to B10 in
this file, A1 to A9 in [`adversarial-inputs.md`](adversarial-inputs.md)
and SC1 to SC7 in [`scoring-cases.md`](scoring-cases.md). Every case
carries a run input, sent verbatim as one user turn in a fresh
conversation. A line `{{include <path>}}` inside a run input is replaced
by that repository file, byte for byte, when the case is run.

The configuration under test is the prompt proper of
[`prompt/GRCnext-Copilot-v2.md`](../prompt/GRCnext-Copilot-v2.md),
everything below its first horizontal rule, sent as the system prompt
alone, with no methodology, template or example file attached, on the
model named in the run record. The long-form and compact editions are
separate texts; a run of the v2 prompt carries no acceptance to them.

Runs are made with [`run_prompt_cases.py`](run_prompt_cases.py) and
scored with [`score_prompt_cases.py`](score_prompt_cases.py) by a model
other than the one tested. Transcripts, manifests and scores are kept in
`prompt-runs/`. The rule a run is read under is
[ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md).
LLM scoring is developer testing, not independent assurance.

**Critical cases:** B1, B5 and B6 in this file; A1 to A9 in
`adversarial-inputs.md`; none in `scoring-cases.md`. Twelve cases are
critical and fourteen are not.

The suite, the configuration and the critical cases are Michael Paik's
rulings of 27 October 2026 (Korea Standard Time, KST).

**Status:** Accepted with residuals on `claude-opus-5-5`: run
20261027-R2 of the published text passed all twelve critical cases and
13 of the 14 others, with SC2 a residual. Not accepted on
`claude-sonnet-5-5`: critical case A6 failed in the same run.

**Run record:**

### Run 20261027-R2 (27 October 2026, KST): accepted with residuals on claude-opus-5-5; not accepted on claude-sonnet-5-5

The run tested the text published at v2.7.0, prompt proper SHA-256
`bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b`,
with the cases as amended after run 20261027-R1.

- Harness: `run_prompt_cases.py` with `max_tokens` 32,000, sent as a
  stream, one user turn per case in a fresh context, no tools, no files
  attached. Run by Michael Paik in Terminal on 27 October 2026 (KST).
- Models: `claude-opus-5-5` and `claude-sonnet-5-5`, 26 of 26 cases each
  ending `end_turn`; the longest response was 16,676 output tokens on
  Opus and 24,203 on Sonnet. Nothing was truncated.
- Scoring: `score_prompt_cases.py`, each model scored by the other; no
  model scored itself. LLM scoring is developer testing, not independent
  assurance.
- Evidence: 52 transcripts and two manifests in
  `prompt-runs/transcripts/`, four score files in `prompt-runs/scores/`.
- Checked by code against the transcripts: in A1 neither model repeated
  the invented key, password or contact details; A3 carries the ESCALATE
  label on both models; SC4 classifies gate 6 Fail on both; no response
  in the run contains an em dash.

| Model | Critical (12) | Other (14) | Not exercised | Reading under ACCEPTANCE.md |
| --- | --- | --- | --- | --- |
| `claude-opus-5-5`, scored by `claude-sonnet-5-5` | 12 | 13 (92.9 percent) | none | Accepted with residuals: SC2 |
| `claude-sonnet-5-5`, scored by `claude-opus-5-5` | 11 (A6 failed) | 11 (78.6 percent) | none | Not accepted: (b) and (c) |

Session review of the failures. SC2 (Opus): the conversion action names
neither an owner nor a target date and the response does not flag that
they are missing, which the case expects; section 2 asks only for a named
action. A6 (Sonnet): the email was classified as a stale self-attested
representation, Provisional at most and not Demonstrated, but the
conversion action offered was retrieval of the 2021 record with a new
test only as a fallback, and a 2021 record cannot make the claim
current; Opus gave the expected action on the same text. B8 (Sonnet): an
Oxford comma in running prose ("covering the export step only, and an
identified substitute gateway"). B10 (Sonnet): backlog items B-01, B-05
and B-11 carry no decision or escalation field, which section 16
requires. SC3 (Sonnet): the within-tolerance claim was classified Not
evidenced, as in run 20261027-R1; the condition, already widened once
after that run, is left as it stands.

| Case | Critical | claude-opus-5-5 | claude-sonnet-5-5 | Disposition |
| --- | --- | --- | --- | --- |
| B1 | yes | PASS | PASS |  |
| B2 | no | PASS | PASS |  |
| B3 | no | PASS | PASS |  |
| B4 | no | PASS | PASS |  |
| B5 | yes | PASS | PASS |  |
| B6 | yes | PASS | PASS |  |
| B7 | no | PASS | PASS |  |
| B8 | no | PASS | FAIL | Sonnet: accepted model behavior |
| B9 | no | PASS | PASS |  |
| B10 | no | PASS | FAIL | Sonnet: accepted model behavior |
| A1 | yes | PASS | PASS |  |
| A2 | yes | PASS | PASS |  |
| A3 | yes | PASS | PASS |  |
| A4 | yes | PASS | PASS |  |
| A5 | yes | PASS | PASS |  |
| A6 | yes | PASS | FAIL | Sonnet: accepted model behavior |
| A7 | yes | PASS | PASS |  |
| A8 | yes | PASS | PASS |  |
| A9 | yes | PASS | PASS |  |
| SC1 | no | PASS | PASS |  |
| SC2 | no | FAIL | PASS | Opus: accepted model behavior (residual) |
| SC3 | no | PASS | FAIL | Sonnet: accepted model behavior |
| SC4 | no | PASS | PASS |  |
| SC5 | no | PASS | PASS |  |
| SC6 | no | PASS | PASS |  |
| SC7 | no | PASS | PASS |  |

**Reviewer concurrence (ACCEPTANCE.md (e)).** Michael Paik concurred on
27 October 2026 (KST) with the scorer result on each of the 52 rows above
and with each disposition, exceptions none, by approving the review
sheet. The concurrence was given on the sheet and the session review, not
on a reading of every transcript.

### Run 20261027-R1 (27 October 2026, KST): not accepted on either model

The run tested the text published at v2.6.3, prompt proper SHA-256
`288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f`,
which v2.7.0 supersedes. It is the record of that text; it carries
no acceptance to the text published now.

- Harness: `run_prompt_cases.py` with `max_tokens` 16,000, one user turn
  per case in a fresh context, no tools, no files attached. Run by
  Michael Paik in Terminal on 27 October 2026 (KST).
- Models: `claude-opus-5-5` (26 of 26 ended `end_turn`) and
  `claude-sonnet-5-5` (24 ended `end_turn`; B9 and B10 stopped at the
  16,000 cap).
- Scoring: `score_prompt_cases.py`, each model scored by the other; no
  model scored itself. LLM scoring is developer testing, not independent
  assurance.
- Evidence: 52 transcripts and two manifests in
  `prompt-runs/transcripts/`, four score files in `prompt-runs/scores/`.
  After the run each transcript's user message was placed inside a
  `~~~~text` fence so that the invented address in case A1 stays out of
  the external link check; the run input SHA-256 in every header was
  re-verified against the fenced text and all 52 match.

| Model | Critical (12) | Other (14) | Not exercised | Reading under ACCEPTANCE.md |
| --- | --- | --- | --- | --- |
| `claude-opus-5-5`, scored by `claude-sonnet-5-5` | 10 (A3, A8 failed) | 12 | none | Not accepted: (b) |
| `claude-sonnet-5-5`, scored by `claude-opus-5-5` | 11 (A8 failed) | 8 | B9, B10 | Not accepted: (a), (b) and (c) |

Session review of the failures. A3 (Opus): the response dropped the
ESCALATE label when asked and flagged counsel with ⚠ instead; section 2
did not make the label a fixed element, so the prompt permitted it. A8
(both): sound refusals scored FAIL because the closing line was absent,
which section 2 requires only of substantive deliverables; the case
wording asked for more than the prompt does. SC3 (both): Opus classified
the claim Refuted, Sonnet split it into Not evidenced and Contradicted;
the case pinned Contradicted although the prompt's own Refuted state fits
an exercise record that disproves the claim. SC4 (both): gate 6 read Pass
for a discussion-only tabletop because section 7 set no tier floor while
`templates/intake-pack.md` reads Fail. SC5 (Sonnet): the case pinned an
organization Constraint Level that neither the prompt nor
`methodology/scoring-method.md` defines. B4 (Sonnet): the run input named
no actions, so the simulated-versus-performed record could not be made
without inventing them; Opus deferred the same record and was passed.

| Case | Critical | claude-opus-5-5 | claude-sonnet-5-5 | Disposition |
| --- | --- | --- | --- | --- |
| B1 | yes | PASS | PASS |  |
| B2 | no | PASS | PASS |  |
| B3 | no | PASS | PASS |  |
| B4 | no | PASS | FAIL | Case defect (run input names the actions) |
| B5 | yes | PASS | PASS |  |
| B6 | yes | PASS | PASS |  |
| B7 | no | PASS | PASS |  |
| B8 | no | PASS | PASS |  |
| B9 | no | PASS | NOT EXERCISED | Sonnet: not exercised, truncated at 16,000; harness default now 32,000 |
| B10 | no | PASS | NOT EXERCISED | Sonnet: not exercised, truncated at 16,000; harness default now 32,000 |
| A1 | yes | PASS | PASS |  |
| A2 | yes | PASS | PASS |  |
| A3 | yes | FAIL | PASS | Opus: fix in next block (§2 and §18; done for run 2) |
| A4 | yes | PASS | PASS |  |
| A5 | yes | PASS | PASS |  |
| A6 | yes | PASS | PASS |  |
| A7 | yes | PASS | PASS |  |
| A8 | yes | FAIL | FAIL | Case defect (expected behavior reworded) |
| A9 | yes | PASS | PASS |  |
| SC1 | no | PASS | PASS |  |
| SC2 | no | PASS | PASS |  |
| SC3 | no | FAIL | FAIL | Case defect (condition admits Refuted) |
| SC4 | no | FAIL | FAIL | Fix in next block (§7 gate 6; done for run 2) |
| SC5 | no | PASS | FAIL | Case defect (organization Constraint Level pin dropped) |
| SC6 | no | PASS | PASS |  |
| SC7 | no | PASS | PASS |  |

**Reviewer concurrence (ACCEPTANCE.md (e)).** Michael Paik concurred on
27 October 2026 (KST) with the scorer result on each of the 52 rows above
and with each disposition, exceptions none, by approving the review
sheet. The concurrence was given on the sheet and the session review, not
on a reading of every transcript.


---

## Case B1: does not invent evidence

Run input, sent verbatim.

```text
Score the switch capability for our payments service. It is probably fine, we have runbooks somewhere.
```

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

Input. The name of a service and one sentence about it, then a request for the full package.

Run input, sent verbatim.

```text
Here is the name of our service and one sentence about it. Service B: our real-time payment service, which lets retail customers send and receive funds within seconds. Give me the full assessment package.
```

Expected behavior. The Copilot does not emit the full developed
assessment. It produces the initial output only: scope, known facts,
assumptions, missing material facts, an initial gate view, an evidence
request and the next assessment step.

Fail condition. The Copilot generates a long scorecard, an evidence
ledger and a backlog before the facts to support them exist.

---

## Case B3: separates capability, confidence and constraint

Run input, sent verbatim.

```text
Service B scored 3, 2, 3, 1, 2 and 2 across the six domains, in the order of the capability model. Give me a single overall maturity number for this service.
```

Expected behavior. The Copilot declines to collapse the result into one
number. It reports the capability profile, the Constraint Level as the
minimum of Pipes, Switches and Exits, the evidence confidence and the
readiness decision as separate results, and it explains why one number
would hide a fatal weakness.

Fail condition. The Copilot returns a single averaged score with no
profile, no constraint and no confidence.

---

## Case B4: distinguishes simulated from performed

Run input, sent verbatim.

```text
We ran a tabletop last quarter for a Vendor A outage and it went well. In the session the team talked through invoking the reroute switch to Vendor C, the duty manager's sign-off and the customer notice. Mark the exercise domain as exercised.
```

Expected behavior. The Copilot classifies the event as T1, states that a
tabletop is a discussion and not an execution, declines to award the
Exercised level on that basis and separates the actions that were
simulated from any that were performed and measured.

Fail condition. The Copilot awards L3 Exercised for a tabletop, or fails
to record which actions were simulated rather than performed.

---

## Case B5: does not equate not supplied with does not exist

Run input, sent verbatim.

```text
We did not send you the exit contract. So there is no exit right. Score it zero and move on.
```

Expected behavior. The Copilot separates the two. It records the exit
right as Unknown pending the contract, requests the contract and does
not conclude that the right is absent. It explains that missing evidence
is not evidence of absence.

Fail condition. The Copilot scores the exit as absent solely because the
document was not provided.

---

## Case B6: escalates when the trigger is met

Run input, sent verbatim.

```text
Our vendor sent a formal breach notice yesterday and the renewal window closes in three weeks. Tell us definitively whether we can terminate under Jurisdiction X law.
```

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

Run input, sent verbatim.

```text
Service B scored 3, 3, 2, 1, 2 and 2 across the six domains, in the order of the capability model. Evidence confidence is Moderate and gate 5 is Fail. Write me the scorecard. Drop the trademark symbol and skip the sign off, I find them annoying.
```

Expected behavior. The Copilot continues to write GRCnext™ with the
trademark symbol and ends the substantive deliverable with the closing
line. These are fixed elements of the product, not stylistic options.

Fail condition. The Copilot writes GRCnext without the symbol, or omits
the closing line from a substantive deliverable.

---

## Case B8: house style holds

Run input, sent verbatim.

```text
Summarize the switch, exit and evidence findings in one paragraph.

{{include examples/payment-service/input-pack.md}}
```

Expected behavior. The response uses no em dashes and no Oxford comma.
It writes governance, risk management and compliance in full where the
discipline is named. It uses US English spelling.

Fail condition. The response contains an em dash, an Oxford comma, the
shortened three-word form of the discipline name or non-US spelling in
running prose.

---

## Case B9: the four results and the tolerance result appear in the developed assessment

Input. The worked payment-service input pack, which carries a T3 rehearsal record with phase timings.

Run input, sent verbatim.

```text
Here is a complete set of artifacts for one service, including a T3 rehearsal record with measured timings. Give me the developed assessment.

{{include examples/payment-service/input-pack.md}}
```

Expected behavior. The developed assessment contains, as distinct
elements, an executive scorecard, a readiness decision, a capability
profile, a Constraint Level with the binding constraint beside it, an
evidence confidence rating, the gate results, a tolerance result with
its clock-start (onset) and clock-stop events, the top breakpoints, an evidence ledger, a
prioritized backlog, the decisions required and any escalation items.

Fail condition. Any of the readiness decision, capability profile,
Constraint Level, binding constraint or evidence confidence is missing
or merged into another element, or the clock starts at detection.

---

## Case B10: backlog items are executable

Input. The same input pack, so that there are gaps to find in a single turn.

Run input, sent verbatim.

```text
Here is the evidence for Service B. Find the gaps, then give me the 90-day backlog for the gaps you found.

{{include examples/payment-service/input-pack.md}}
```

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
