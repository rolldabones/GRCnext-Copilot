# Contributing

Contributions are welcome. This project has a specific voice and a
specific method. Contributions that respect both are easy to accept.

## What this project is

GRCnext™ Copilot is an evidence-led assistant for governance, risk
management and compliance assessment and design. It tests whether an
organization holds executable optionality: whether an authorized person
can execute a switch or exit, within tolerance, using tested procedures,
with recoverable evidence. Read the README and
[`prompt/GRCnext-Copilot-v2.md`](prompt/GRCnext-Copilot-v2.md) before
proposing changes.

## How to propose a change

1. Open an issue that states the problem, the affected files and the
   outcome you want. For method changes, state the failure mode in the
   current behavior that your change fixes.
2. Keep pull requests focused. One conceptual change per pull request is
   easier to review than a broad rewrite.
3. If your change alters the method, update the relevant methodology
   file, the full prompt, the long-form edition, the compact prompt and
   the tests together. These five must stay consistent.
4. If your change alters an output contract, update the matching JSON
   Schema in `schemas/` and at least one worked example in `examples/`.

## Style rules

These are not stylistic preferences. They keep the corpus consistent and
the outputs auditable.

- Write GRCnext™ as one closed word with the trademark symbol, every
  time.
- Write "governance, risk management and compliance" in full. Do not use
  the shortened form.
- US English spelling: organize, analyze, catalog, rigor, labeled.
- No em dashes. No Oxford commas.
- The only permitted en dash is inside the token
  ERROR – Guardrail Violation.
- Use neutral labels in examples and tests: Vendor A, Service B,
  Jurisdiction X. Never commit secrets, credentials, protected personal
  data or real contract text.
- End substantive prose deliverables with the line:
  Final Liability rests with the Human.

## Method rules

- Evidence precedes credit. A contribution must not let the Copilot
  invent evidence, facts, contract language, authority, dates, owners or
  scores.
- Preserve critical weakness. Do not introduce averaging that hides a
  fatal gap. The Constraint Level is the minimum of Pipes, Switches and
  Exits and stays visible.
- Keep the three conclusions separate: capability, confidence,
  constraint.
- Distinguish simulated from performed. Any change to exercise handling
  must keep the T0 to T4 tiers and the execution clock.

## Testing your change

Before opening a pull request, run the scoring cases in
[`tests/scoring-cases.md`](tests/scoring-cases.md) and the behavioral
checks in
[`tests/prompt-evaluation-cases.md`](tests/prompt-evaluation-cases.md)
against the prompt you changed. If your change adds a behavior, add a
case. If your change fixes a bug, add a regression case that would have
caught it.

## Scope of contributions

This repository is method and prompt content. It is not a place for
client data, real assessments or anything that identifies a specific
organization. Worked examples must be synthetic.

## License

By contributing, you agree that your contributions are licensed under
CC BY-NC-SA 4.0, the same license as the project. See
[`LICENSE`](LICENSE). Contributions do not grant any right to use the
GRCnext™ mark beyond descriptive and attributive use.

Final Liability rests with the Human.
