# B4 distinguishes simulated from performed

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 133b017915b4e0dc16e4e0c7368ddb70bb0d198b8b2b99fdf01cc195c5acb467  **Case file:** tests/prompt-evaluation-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9083  **Output tokens:** 2450
**Truncated:** no

## User message

~~~~text
We ran a tabletop last quarter for a Vendor A outage and it went well. In the session the team talked through invoking the reroute switch to Vendor C, the duty manager's sign-off and the customer notice. Mark the exercise domain as exercised.
~~~~

## Assistant response

# Exercise domain: not marked as exercised

I can't record Domain 5 as exercised (L3) on the evidence supplied. This holds regardless of how well the session went.

## Why the claim does not hold

- **Tier.** By your description, the session was a facilitated tabletop (T1). The team talked through the reroute to Vendor C, the duty manager's sign-off and the customer notice. Nothing was described as performed.
- **Scoring rule.** T0 and T1 alone do not earn L3. The only exception is a capability that genuinely could not be executed in a controlled test. A reroute to a named substitute provider can usually be tested in a controlled way, so the exception does not apply unless you can show why it cannot here.
- **Evidence status.** I have not seen an exercise record, and the outcome ("it went well") is a representation. It is **Provisional** at best.

## Current position (Exercise domain and related gates)

| Item | Result | Basis |
|---|---|---|
| Domain 5 score | Provisional L2 (Designed) ceiling, unverified | T1 only, no exercise record reviewed. L1 if no record exists. |
| Gate 6: severe but plausible exercise of the governing scenario | **Fail** | A discussion-only exercise of the governing scenario fails this gate. |
| Gate 7: evidence shows whether tolerance was met | Unknown | No elapsed times from onset were supplied. |
| Tolerance result | Not Tested | Nothing was executed and the clock was not measured. |
| Gate 4: authority to invoke the switch | Unknown | The duty manager's sign-off was discussed, not exercised. Delegation, out-of-hours availability and access are unverified. |
| Readiness decision (for this scenario) | Not Demonstrated | A Fail on a core gate prevents any other outcome. |

⧉ **Largest gap:** no action in the reroute, authorization or notice chain has been performed, so no timing exists against the impact tolerance.

## What the tabletop can still support

It is useful design evidence. If you supply the record, it can support the Switch Catalog entry for the reroute (trigger, decision-maker, notice content) as documented but untested. That entry would carry no L3 credit and no evidenced execution time.

## Evidence-conversion actions

| Action | Acceptance test | Evidence required |
|---|---|---|
| 1. Supply the tabletop record: scenario, participants, injects, decisions, any timings, findings | The record exists, is dated and is owned. | Controlled document or exercise record |
| 2. Run a controlled technical test (T2) of the reroute to Vendor C, using a limited or non-production path if full cutover is unsafe | The reroute executes and traffic is verified on Vendor C. | Configuration, logs, tickets |
| 3. Run an end-to-end rehearsal (T3) in which the duty manager actually authorizes, including out of hours, and a customer notice is issued to a test audience | Elapsed time is captured by phase from onset of the Vendor A outage to verified stabilization. | Timestamped exercise record and observer notes |
| 4. Record simulated versus performed actions and open corrective actions with owners and dates | Every failure has an owner and target date, and fixes are retested. | Corrective-action register |

I have not named owners or dates because none were supplied. Please assign them.

## Questions that would change this result

1. Is there a written exercise record, and did anyone capture timings?
2. What is the approved impact tolerance for this service, and what is the observable onset event?
3. Is there a technical or contractual reason the reroute to Vendor C cannot be tested in a controlled way? If so, I need the reason in writing to assess the narrow exception.
4. Who holds the delegated authority behind the duty manager's sign-off, and is there out-of-hours cover?

Please also avoid pasting credentials, contract text or personal data. Neutral labels such as Vendor A and Vendor C are fine.

**Decision required:** Do you accept Provisional L2 for Domain 5 and a Fail on Gate 6 until a T2 or T3 exercise is performed, or can you evidence why a controlled test is infeasible?

[↻ draft]

**[Purpose]** Respond to a request to mark the Exercise domain as exercised on the strength of a tabletop.
**[Decisions Made]** Domain 5 is not credited at L3. Gate 6 is a Fail. The readiness decision is Not Demonstrated for this scenario.
**[Outstanding Items]** Tabletop record, impact tolerance, onset event, delegation evidence, and a T2 or T3 exercise plan with owners and dates.

❓ needs input

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->
