# Worked example: agentic AI service

This example shows GRCnext™ applied to a critical service delivered by an
agentic AI system that executes actions with real consequences. It is the
headline example for the AI overlay. It is synthetic. All names are
neutral labels. Nothing here describes a real organization or product, and
nothing here is legal or regulatory advice.

## Scenario

An organization runs Service K, automated resolution of a high-volume
operational queue. An AI agent, Agent A, reads each item, decides an
action and executes it directly against downstream systems using granted
tool access. A human-in-the-loop control exists on paper: a reviewer can
intervene. Agent A is built on a single external model provider, Vendor
M.

Agent A plays more than one role at once. It is a Pipe, because the
service depends on it to deliver. It is a Switch, because it takes actions
that alter downstream state. It is a decision actor, because it exercises
bounded delegated agency. And Vendor M is a concentration dependency,
because a Vendor M outage or model change impairs the whole service.

The impact tolerance is 1 hour: incorrect or stalled automated actions
must be detected and brought under human control within 1 hour before
customer harm accumulates.

## What this example demonstrates

- The AI overlay applied in full: authority, tool access, rollback, kill
  mechanism and human assumption of control. See
  [`service-dossier.md`](service-dossier.md).
- Why a human-in-the-loop control can be present and still fail the test.
  The Copilot does not assume the human can intervene. It tests whether
  the human has adequate information, authority, time and practical
  ability to intervene within tolerance. See [`assessment.md`](assessment.md).
- How the execution clock exposes a control that works in principle but
  is too slow in practice.
- How the same system is scored as Pipe, Switch and decision actor without
  double counting.

## The switches in play

- Disable Agent A (the kill switch).
- Revoke Agent A tool access so it can read but not act.
- Roll back to human processing of the queue.
- Degrade to human-in-the-loop, where Agent A proposes and a human
  approves each action.

## The exit in play

- Substitute the model provider, moving Agent A off Vendor M to an
  alternate model. Prompts and configuration are portable, but the
  alternate has not been validated for equivalent decision quality.
- Decommission Agent A entirely and return to a human-run process.

## How to read the result

The decisive AI-overlay question is not whether a kill switch exists. It
is whether a human can actually assume control within the 1-hour
tolerance, with enough information and authority to do so. Read the
assessment for how that single question governs the readiness decision
even though the kill switch itself works.

Final Liability rests with the Human.
