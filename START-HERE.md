# Start here

One route, for one critical service, from an empty assistant to a
validated assessment and a Service Dossier. The payment example
([`examples/payment-service/`](examples/payment-service/)) is the worked
route at every step.

## What you need

- One critical service, named by the outcome its customers receive, with
  an accountable owner.
- Its approved impact tolerance in hours and the onset event that starts
  the clock (the moment the service first falls outside its normal level
  of delivery, not the moment someone notices).
- The artifacts you hold for that service: definitions, dependency map,
  switch catalog, contracts, exercise records, corrective actions.
- A current assistant that takes a system prompt or project instructions.
- Python 3.8 or later with `jsonschema` (`pip install jsonschema`) for
  step 7.

## 1. Load the prompt

Paste [`prompt/GRCnext-Copilot-v2.md`](prompt/GRCnext-Copilot-v2.md) as
the system prompt or project instructions of the assistant: Claude
Project instructions, or a system prompt through the API. Paste nothing
else. Methodology files, templates and examples are not needed for the
run.

## 2. Fill the intake pack

Copy [`templates/intake-pack.md`](templates/intake-pack.md) and fill it:
the service facts block, then, for each of the eight gates, the artifacts
you hold with an ID and what each establishes. Record what you do not
have under "Not supplied".

Worked route: [`examples/payment-service/input-pack.md`](examples/payment-service/input-pack.md).

## 3. Send the first message

Paste the filled pack after this message:

> Assess one critical service under GRCnext™. Start with the initial
> output only: scope, known facts, assumptions, missing material facts,
> initial gate view, evidence request and proposed next step. Do not
> score until I supply the evidence you request. The intake pack
> follows.

## 4. Read the initial output

The Copilot discloses progressively (section 17 of the v2 prompt). The
first reply is the initial output: scope, known facts, assumptions,
missing material facts, an initial view of the eight gates, an evidence
request and the proposed next step. It does not score yet. If it scores
before it has evidence, say so and ask for the initial output.

For the payment example, expect an initial gate view that flags the
tolerance's clock start (the approved text names detection) and the
exit's lack of an end-to-end rehearsal, and an evidence request for
what the pack lists as not supplied: the exit rehearsal, the substitute
gateway's peak capacity and a re-approved onset clock.

## 5. Supply evidence, receive the developed assessment

Answer the evidence request with the artifacts asked for, or say plainly
that they do not exist. When the evidence is sufficient the Copilot
returns the developed assessment: executive scorecard, readiness
decision, capability profile, Constraint Level, binding constraint,
evidence confidence, gate results, tolerance result with both clock
events, top breakpoints, evidence ledger, prioritized backlog, decisions
required and escalation items.

Worked route: [`examples/payment-service/assessment.md`](examples/payment-service/assessment.md).
Its profile is 3, 3, 3, 2, 3, 3; the Constraint Level is 2, set by Exits;
the binding constraint is the Authorize phase (3 hours of 9) for the
reroute and gate 5 for the exit; the decision is Conditionally
Demonstrated.

## 6. Ask for the JSON and save it

Send:

> Emit this assessment as one assessment_result JSON object with
> schema_version "2.6", conforming to schemas/assessment-result.schema.json.
> JSON only.

Save the reply as `result.json`.

Worked route: [`examples/payment-service/assessment-result.json`](examples/payment-service/assessment-result.json).

## 7. Validate the record

From the repository root:

```
pip install jsonschema
python3 tools/validate.py result.json
```

Read the verdict line. ACCEPT means the record follows the repository's
own rules: the schema, the eight gates, the Constraint Level arithmetic
and the decision caps. REJECT lists each finding with the rule it breaks;
correct the assessment, not the JSON, and emit it again. WARN findings do
not change the verdict but need a human look.

The validator checks that the record follows the repository's rules. It
does not check that the service is ready, that the evidence is true or
that the conclusion is right.

## 8. Write the Service Dossier

Fill [`templates/service-dossier.md`](templates/service-dossier.md) from
the developed assessment, or ask the Copilot to build it. Keep the six
core sections. Put the switch rows, evidence items and corrective actions
in your own copies of
[`templates/switch-catalog.csv`](templates/switch-catalog.csv),
[`templates/evidence-ledger.csv`](templates/evidence-ledger.csv) and
[`templates/capa-register.csv`](templates/capa-register.csv), which ship
header-only.

Worked route:
[`examples/payment-service/service-dossier.md`](examples/payment-service/service-dossier.md)
with its [`capa-register.csv`](examples/payment-service/capa-register.csv),
[`evidence-ledger.csv`](examples/payment-service/evidence-ledger.csv) and
[`switch-catalog.csv`](examples/payment-service/switch-catalog.csv).

## Next

Two more worked services follow the same route:
[`examples/agentic-ai-service/`](examples/agentic-ai-service/) (AI
overlay, Not Demonstrated) and
[`examples/manufacturing-service/`](examples/manufacturing-service/)
(safety-critical, Not Demonstrated). The method behind the scores is in
[`methodology/scoring-method.md`](methodology/scoring-method.md).

Final Liability rests with the Human.
