# Model configuration notes

GRCnext™ Copilot is model-neutral. It is a prompt and a method, not a
model. It runs on any capable general-purpose assistant that can follow
long structured instructions and, where a platform allows, read attached
files. This note covers deployment on Claude and on ChatGPT, and gives
general guidance for other platforms.

Three prompt files support deployment:

- [`GRCnext-Copilot-v2.md`](GRCnext-Copilot-v2.md) is the authoritative
  modular prompt. Use it wherever the instruction field is large enough
  and you want it paired with the repository.
- [`GRCnext-Copilot-long-form.md`](GRCnext-Copilot-long-form.md) is a
  self-contained edition that carries the methodology reasoning inline.
  Use it on a strong reasoning model, or on any platform that cannot read
  attached files, when you want the fullest single-file expression of the
  method.
- [`compact-custom-gpt-version.md`](compact-custom-gpt-version.md) is a
  reduced version that fits an 8,000-character instruction field. It
  carries the full behavioral spine so the Copilot behaves correctly even
  before it reads any attached file.

The three are consistent. They differ in length and in how much reasoning
is stated inline, not in what the Copilot does.

## Claude

Claude Projects and custom instruction fields accept long instructions,
so the full prompt fits directly.

1. Create a Project.
2. Paste the contents of
   [`GRCnext-Copilot-v2.md`](GRCnext-Copilot-v2.md) into the Project
   instructions.
3. Optionally add the `methodology/`, `templates/` and `examples/`
   files as Project knowledge so the Copilot can reuse the templates and
   follow the worked examples.
4. Start a chat in the Project. The Copilot defaults to Assessment mode.

No compaction is needed on Claude. Use the full prompt.

## ChatGPT Custom GPT

The Custom GPT instructions field has a hard limit of 8,000 characters.
The full prompt exceeds that, so split the deployment.

1. In the GPT editor, open Configure.
2. Paste the contents of
   [`compact-custom-gpt-version.md`](compact-custom-gpt-version.md) into
   the Instructions field. It is sized to fit under 8,000 characters.
3. Under Knowledge, upload
   [`GRCnext-Copilot-v2.md`](GRCnext-Copilot-v2.md). This gives the GPT
   the full method as a reference it can open on demand.
4. Optionally upload the `templates/` files and one or more `examples/`
   files as additional Knowledge.
5. Enable Code Interpreter. The GPT needs it to read Knowledge files and
   to open any CSV or JSON you attach or paste.
6. Name the GPT, add a description and set a profile image.

Data Controls. Turn off model training in your Data Controls before you
use the GPT on any nonpublic material. Assessment inputs often contain
sensitive operational detail even when you use neutral labels.

Memory caveat. Enabling Memory changes outputs. The Copilot is designed
to reason from the material in front of it, not from remembered facts
about your organization. If you enable Memory, treat any conclusion that
appears to rely on remembered context as provisional and re-verify it
against supplied evidence.

## Long-form model-agnostic edition

Use [`GRCnext-Copilot-long-form.md`](GRCnext-Copilot-long-form.md) when
you want a single self-contained prompt that needs no attached files.

1. Open the system prompt, custom instruction or project field of your
   platform.
2. Paste the entire contents of the long-form edition.
3. Optionally attach the `templates/` and `examples/` files if the
   platform supports file input, but the prompt does not require them.
4. Start the session. The Copilot defaults to Assessment mode.

This edition suits stronger reasoning models with large context windows,
because it states the methodology reasoning inline rather than relying on
a separate reference. It is also the right choice for any platform that
accepts a long instruction but cannot read attachments. Its behavior
matches the modular prompt. Verify it against the tests the same way.

## Other platforms

For any other assistant:

- If the instruction or system field accepts the full prompt, use
  [`GRCnext-Copilot-v2.md`](GRCnext-Copilot-v2.md).
- If the field is capped near 8,000 characters, use
  [`compact-custom-gpt-version.md`](compact-custom-gpt-version.md) in the
  field and provide the full prompt as an attachment or a first-message
  reference if the platform supports file input.
- If the platform cannot read attachments, paste the full prompt as the
  first message of the session, then proceed.

## Model selection

Use a current, capable reasoning model. Do not hard-code a specific model
name into your deployment. Model quality on long structured reasoning
changes over time, so re-select periodically and verify behavior against
the tests in [`../tests/`](../tests/) after any model change.

Whatever model you choose, the guardrails hold: evidence precedes credit,
critical weakness is preserved, and the Copilot does not invent facts,
authority or scores.

## Verifying a deployment

After you deploy, run a few cases from
[`../tests/prompt-evaluation-cases.md`](../tests/prompt-evaluation-cases.md)
and
[`../tests/adversarial-inputs.md`](../tests/adversarial-inputs.md). Confirm
that the Copilot refuses to invent evidence, uses progressive disclosure,
flags escalation items, keeps the GRCnext™ mark and produces the
three-part conclusion. If any check fails, the instructions were likely
truncated or the model is underpowered for the task.

Final Liability rests with the Human.
