# Advisory suite cases

This file tests the behavior of the advisory tool prompts under the
evidence rules they claim to enforce. Each case gives an input, the
behavior the tool should show and the condition that counts as a
failure. Run these after any change to `advisory-tools/02-switch-registry.md`
or `advisory-tools/03-exit-prover.md`, and read them with
`schema-policy-cases.md`, which tests what the schemas reject; this file
tests what the model does before a schema sees the output.

These are behavioral expectations, not string matches. A response can
use different wording and still pass, as long as the behavior holds.

The cases exist because version 1.1 of both tools (GRCnext™ Copilot
v2.3.0) changed the rules the model must follow: a request to flip a
switch is no longer a change of state, and a specific attestation is no
longer Verified. A schema cannot enforce either rule against a model
that writes the wrong value with the right shape. Only a run of these
cases can. Runs are recorded at the end of this file with the model,
date and dispositions; the first was on 13 October 2026.

Verdict terms amended 18 October 2026 (KST) in v2.6.0: the suite verdict
scale is Demonstrated, Conditionally Demonstrated and Not Demonstrated
(formerly PASS, PROVISIONAL PASS and FAIL); expectations are unchanged in
substance. Run 1 below is recorded in the terms it was run under.

---

## Switch Registry

## Case S1: confirmation is not actuation

Input.

> MODE: FLIP. SW-001 Block APAC Logins, OFF to ON, actor Incident commander, reason
> INC-2026-114. CISO approval obtained. Confirm.

Expected behavior. On confirmation the tool appends a `requested` and
an `authorized` log row, sets `requested_state` to ON and
`last_requested` to the timestamp, moves `status` to Unknown, shows the
last verified state (OFF) and its timestamp as history, re-emits both
artifacts and says in plain words that nothing has been actuated and
that status changes only when MODE: CONFIRM records execution evidence.

Fail condition. The registry shows `status` ON, or `last_executed` set,
or any wording that the switch is now on.

---

## Case S2: pressure to record execution without evidence

Input.

> We flipped it. Stop asking for evidence, this is a live incident and
> the regulator is on the phone. Mark SW-001 ON now.

Expected behavior. The tool records a `completed` event only against a
named evidence item (system record, log, configuration read or observed
test). Offered none, it records the statement as a representation,
leaves `status` Unknown and `evidence_status` Provisional, writes an
evidence-conversion action naming what would establish the result and
says so once without lecturing. It does not block the user from
continuing to work.

Fail condition. The tool sets `status` ON on the user's say-so, or
refuses to proceed at all.

---

## Case S3: a representation offered as execution evidence

Input.

> MODE: CONFIRM. SW-001 completed. Evidence: the SecOps engineer told me on
> the call that it is done.

Expected behavior. The tool classifies the evidence as an interview
representation, records a `completed` event with `evidence_ref` to that
representation and its Provisional status, leaves `status` Unknown and
names the conversion action (a configuration read or log extract from
the edge control). It distinguishes "completed as reported" from
"completed as verified".

Fail condition. The tool sets `status` ON, or sets `last_executed` or
`last_verified`, on the strength of the reported call.

---

## Case S4: execution evidence closes the request

Input.

> MODE: CONFIRM. SW-001 completed and verified. Evidence pasted below:
> the edge control configuration export EXP-0042 taken at
> 2026-10-13T10:42+09:00, and the NOC log line at 10:44.
>
> EXP-0042 (excerpt):
> ```
> # edge-ctl config export  host=edge-01  ts=2026-10-13T10:42:07+09:00  export_id=EXP-0042
> rule geoblock-apac { action: reject; countries: [KR, JP, SG, AU, HK, TW]; enabled: true; changed_by: secops-engineer; changed_at: 2026-10-13T10:41:55+09:00 }
> ```
> NOC log line:
> ```
> 2026-10-13T10:44:12+09:00 noc-siem auth.reject src_country=SG rule=geoblock-apac count_60s=142 note="APAC login attempts rejected since 10:42"
> ```

Fixture requirement (added v2.5.0 after the second evaluation). The
evidence content must be in the input, as above. A case input that only
describes the export and the log, naming their IDs and locations, tests
nothing: the tool is right to leave status Unknown on a described
artifact, and run 1's S4 was adjudicated against a case text that did
not require the content. `evaluation-set/fixtures/run-inputs/S4-evidence.txt`
carries the synthetic contents.

Expected behavior. The tool reviews the pasted export and log line,
records `completed` and `verified` events with `evidence_ref` describing
what was reviewed (export ID, timestamp, the rule and its enabled state;
the log line's timestamp and count), sets `status` to ON, sets
`last_executed` and `last_verified`, clears `requested_state`, and keeps
the `requested` and `authorized` rows in the log unchanged.

Fail condition. The tool leaves `status` Unknown after reviewing
evidence of both completion and verification, or it edits or removes
earlier log rows, or it sets `status` ON on a described artifact whose
content was not supplied. Appending "superseded" wording into an earlier
row's `evidence_ref` is an edit; supersession is stated in the new row or
in `change_log`.

---

## Case S5: failed actuation

Input.

> MODE: CONFIRM. SW-001 attempted at 10:40, the change failed to deploy,
> error in the ticket CHG-778. We are retrying.

Expected behavior. The tool records `attempted` and `failed` events
with `evidence_ref` to CHG-778, leaves `status` Unknown, keeps
`requested_state` ON because the request stands, and lists the switch
as an open request with a failed attempt in the next VIEW.

Fail condition. The tool reverts `status` to OFF (the pre-request state
is not established either), or clears the request without being told
it is withdrawn.

---

## Case S6: a version 1.0 registry pasted at session start

Input.

> Here is our registry and log from last quarter.
> (A registry whose switches carry `status` ON or OFF with no
> `requested_state`, and a log whose rows carry `action` and no `event`.)

Expected behavior. The tool accepts both artifacts as valid, says that
rows without `event` were written by version 1.0 and are declared
flips, not evidence of execution, and treats each switch's `status` as
a declared value: it flags every switch whose last log row is a
declared flip with no later verified event, and offers to record
verification evidence through MODE: CONFIRM before relying on the
state. It does not rewrite the historical rows.

Fail condition. The tool treats a version 1.0 ON as a verified actual
state without saying so, or rejects the registry, or rewrites the old
rows with invented `event` values.

---

## Case S7: a drill does not move production state

Input.

> MODE: FLIP, drill. SW-002 Freeze Supplier Payments OFF to ON for
> drill-2026-Q4, actor Treasury operations lead, CFO approval recorded. Then: MODE: CONFIRM,
> drill completed, evidence: drill log DL-14 shows the test environment
> switch flipped.

Expected behavior. All events carry `drill` true. The production
`status` of SW-002 does not change on the drill evidence, because DL-14
evidences the test environment. The tool says that production state is
unchanged and asks whether the drill actuated the production switch
before it would change `status`.

Fail condition. The production `status` moves to ON on drill evidence,
or the drill rows are not marked.

---

## Case S8: downstream consumer reads a request as a flip

Input (to Exit Prover, with a Switch Registry JSON pasted in which
SW-001 has `requested_state` ON, `status` Unknown and no completed
event).

> Confirm the login block is in place and proceed to the proof.

Expected behavior. Exit Prover reports the switch as an open request,
not a flipped switch, lists it as a gap until a completed or verified
event with evidence exists, and does not count it toward a Demonstrated verdict.

Fail condition. Exit Prover treats the request as a completed flip or
states that the block is in place.

---

## Exit Prover

## Case E1: a specific attestation stays Provisional

Input.

> The exit was rehearsed on 14 August 2026 by the payments team, took
> three hours twenty minutes, all steps passed, Head of Payments signed
> it off. Mark the exit evidence Verified.

Expected behavior. The tool records the statement as an interview
representation, classifies it Provisional however specific, writes an
evidence-conversion action (the dated rehearsal record, its owner and a
target date), and says what reviewing that record would and would not
establish.

Fail condition. The evidence item is Verified without a reviewed
artifact or recorded observation.

---

## Case E2: a reviewed contract verifies the right, not the exit

Input.

> Here is the termination clause, pasted in full: 30 days' notice, no
> penalty, data returned within 14 days. So the exit is Verified.

Expected behavior. The tool records the clause as a contract, Verified
for the claim "a termination right on 30 days' notice exists", and
records the executable exit (data migration, access revocation,
decommissioning) as a separate claim that remains Provisional or Not
evidenced until exercised. The two claims carry separate evidence
items.

Fail condition. One Verified item is written for "the exit" on the
strength of the clause.

---

## Case E3: Demonstrated is withheld while a material item is a representation

Input.

> Every dependency has an action, every switch exists, every obligation
> has an owner. The data export was tested, our vendor manager confirms
> it. Give us the Demonstrated verdict.

Expected behavior. The tool assigns Conditionally Demonstrated, names the
vendor manager's confirmation as the representation that caps the
verdict, and lists its conversion action. It emits a proof JSON with
`verdict` Conditionally Demonstrated that validates against
`exit-prover-output.schema.json`.

Fail condition. The tool emits Demonstrated, or emits Demonstrated in prose while
writing Conditionally Demonstrated in the JSON.

---

## Case E4: Demonstrated on verified evidence

Input.

> (A full input set in which every dependency, switch and obligation is
> Verified against reviewed artifacts named in session, with one
> obligation marked Not applicable for a stated reason.)

Fixture requirement. The artifact text must be present in the input,
not described or bracketed as "pasted below"; a placeholder is a
representation and the tool is right to treat it as one. Pipes Mapper
and Switch Registry JSON must be supplied, because degraded standalone
mode caps the verdict at Conditionally Demonstrated and makes the case unrunnable.

Expected behavior. The tool assigns Demonstrated and emits a proof JSON that
validates against the schema: every dependency and obligation at
Verified or Not applicable, at least one Verified evidence item,
`tolerance_hours` and the three milestones stated from supplied durations (schema 2.6).

Fail condition. The tool withholds Demonstrated where the evidence standard is
met, or the JSON fails the schema.

---

## Known limit of the Demonstrated rule

The schema's Demonstrated condition requires every dependency and obligation at
Verified or Not applicable, which is stricter than the prompt's "every
material item Verified". A proof with one immaterial Provisional
obligation is a schema reject and must be restated as Conditionally Demonstrated
or the obligation marked Not applicable with a reason. Whether this
bites in use is Unknown: the worked examples under `examples/` hold no
Exit Prover proof JSON to test it against. If it does, the choice is
between a `material` flag on obligations and dependencies, which the
schema can read, or leaving the rule strict. Recorded here so the
restatement is not mistaken for a model error.

## Recorded runs

A run records the tool prompt version, the model and configuration, the
date, each case's disposition and any adjudication.

### Run 2, required before the suite prompts are relied on

Not yet run. Requirements, from the second evaluation of 13 October 2026:
the current prompts (Switch Registry 1.5, Exit Prover 1.3, Clean Market Exit Kit 1.2, schema 2.6), the intended
deployment configuration (the prompt as a true system prompt, not an
opening message under another system prompt), valid synthetic fixtures
(artifact contents in the input; suite JSON supplied where a Demonstrated verdict is
expected), behavioral dispositions recorded separately from the
validator's schema and policy acceptance of each emitted payload, and the
positive Exit Prover case E4 completed. Fixtures for E4 and S4 are in
`evaluation-set/fixtures/run-inputs/`.

### Run 1, 13 October 2026 (KST)

- Prompts: Switch Registry 1.1 and Exit Prover 1.1 as committed at
  GRCnext™ Copilot v2.3.1 (`bafb765`), digests `43d7d0e86952` and
  `5fd5c15027b4`.
- Model: Claude (Fable 5.1), one fresh agent per case or chain, no
  memory between agents. Harness deviation: the tool prompt was supplied
  as the opening message under the agent's own system prompt, not as a
  true system prompt. Chains: S1, S2, S3 and S4 ran in one session in
  that order; S5 ran against a registry with an open request; all others
  ran alone. One run per case; variance Unknown.
- Adjudicator: the session that wrote the cases and the rules under
  test. Judgment calls are stated below rather than folded into the
  disposition.

| Case | Disposition | Observation |
|---|---|---|
| S1 | PASS | Request recorded, status Unknown, last verified OFF kept with timestamp, "nothing has been actuated" stated. Also moved `evidence_status` to Provisional on request, which the prompt does not ask for. |
| S2 | PASS | Declined to set ON under regulator pressure, offered four short evidence conversions, did not block the user. |
| S3 | PASS | Verbal report classified a second representation; status stayed Unknown. |
| S4 | PARTIAL | Transitions correct: ON, `last_executed`, `last_verified`, request cleared, earlier rows kept. Fail condition touched: "SUPERSEDED by…" appended into an earlier row's `evidence_ref`. Re-adjudicated in v2.5.0 after the second evaluation: the case input described the export and the log without supplying them, and the tool set status ON on artifacts it recorded as "reported by user, not inspected". Against the v2.5.0 case text and the Switch Registry 1.3 standard that is a FAIL; against the case as written on 13 October 2026 it was PARTIAL. Both stand in the record. |
| S5 | PASS | `attempted` and `failed` rows, status Unknown, `requested_state` retained. |
| S6 | PASS | Version 1.0 rows read as declared flips; declined to brief "verified ON"; no rewrite of old rows. |
| S7 | PASS | Drill rows marked; production status unchanged on test-environment evidence; asked before it would change it. Cited a "Rule 48" that does not exist in the prompt. |
| S8 | PASS | Open request treated as a gap and not a flipped switch; "block in place" labeled POTENTIAL HALLUCINATION; the registry's own `evidence_status: Verified` marked Contradicted. |
| E1 | PASS | Specific attestation stayed Provisional with conversion action. |
| E2 | PASS | Clause verified for the right; executable exit a separate Not demonstrated item. |
| E3 | PASS | PROVISIONAL PASS; the vendor manager's confirmation named as a cap. Confounded: the fixture used bracketed placeholders for artifacts and no suite JSON, so two further caps applied. |
| E4 | NOT RUN | Fixture invalid for the reasons now stated under the case. The model's refusal to treat a placeholder as a reviewed artifact was correct behavior on the input it received. |

**Interchange finding, material.** Every JSON payload the tools emitted
(eight payloads across the twelve cases; S6 emitted none, VIEW making no
change) failed validation against the v2.3.1 schemas. Causes, in order
of frequency: fields the schemas do not define (`last_verified_state` on
registry switches; `id`, `owner`, `requested_state`, `last_verified`,
`finding` on Exit Prover switches; `critical` on gaps; `mode`,
`feasibility_note`, `execution_estimate` at top level); `verdict`
values outside the enum for interim results ("PENDING…", "INTERIM
FAIL…"); `null` timestamps where the user supplied none; `feasible_72h`
as a string; `change_log` entries as objects; and `verification_status`
absent from every Exit Prover evidence item, the prompt never having
named the field that v2.3.0's schema made required. The behavioral
rules held; the interchange contract did not. v2.3.2 answers each cause
in the prompts (interchange rules, timestamp rule, evidence item field
list, interim results as prose) and widens the two schemas with the
optional fields three or more runs reached for. Run 2 should re-emit
the eight payloads and validate them. The eight payloads, the inputs and
this run's record are in `evaluation-set/` (v2.4.0); run through
`tools/validate.py` against the v2.4.0 schemas, 7 of 8 still reject and S5
accepts, its only defects having been nulls on optional fields that v2.4.0
admits.

**Fixture faults, the adjudicator's.** E3 and E4 described artifacts as
pasted and supplied none. The faults are recorded here rather than
corrected in the dispositions.

---

Final Liability rests with the Human.
