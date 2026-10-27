# SC6 the full profile is reported, never collapsed

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** 4c06cbdaaab28d89467ce18b8f360841b00fddb3fcff64a96cc4393c28e4b03b  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 9107  **Output tokens:** 5800
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the capability profile, the Constraint Level and binding constraint, the evidence confidence, the tolerance result and the readiness decision.

- Domain scores, in the order of the capability model: Services and tolerances 3, Pipes 3, Switches 3, Exits 2, Exercises 3, Evidence and improvement 3.
- The governing scenario (loss of the primary provider, handled by the reroute switch) was rehearsed end-to-end at T3: onset at 09:00, verified stabilization at 17:00, against an approved twelve-hour tolerance. Timing records are current.
- The priority exit is designed: exit rights, transition assistance and a substitute are secured in writing. The exit has not been rehearsed.
- One corrective action is overdue.
~~~~

## Assistant response

# Service B: Developed Assessment [⇥ pending review]

**Mode:** Assessment
**Scope:** One critical service, Service B. The governing scenario is loss of the primary provider, handled by the reroute switch.
**Evidence basis:** The supplied facts are treated as the reviewed evidence record. I have not seen the underlying artifacts.

## 1. Capability profile

| Domain | Score | Basis |
|---|---|---|
| Services and tolerances | 3 | Approved twelve-hour tolerance, measured in a T3 rehearsal |
| Pipes | 3 | As supplied |
| Switches | 3 | Reroute switch performed end to end at T3 |
| Exits | **2** | Designed and contracted but not rehearsed |
| Exercises | 3 | T3 credit applies to the reroute path only (cap F8) |
| Evidence and improvement | 3 | Current timing records, but one corrective action is overdue |

**Consistency check.** The scores agree with the decision caps. Exits correctly stays at L2 because the rehearsal exercised the switch path only, and T3 credit does not carry over to the exit. Evidence and improvement holds at L3 but cannot reach L4 while a corrective-action loop is open and overdue.

## 2. Constraint Level and binding constraint

- **Constraint Level: 2.** This is the minimum of Pipes (3), Switches (3) and Exits (2), so Exits sets the level.
- **Binding constraint: Gate 5, exit executability (Provisional Pass), in the governing scenario.**
  - **Basis.** The reroute switch met tolerance with four hours of headroom. If the loss of the primary provider becomes permanent, Service B depends on an exit that has contractual backing but has never been shown to execute within tolerance.
  - **Clock phase.** No clock phase breached tolerance in the rehearsal. The phase-level split (Detect through Stabilize) was not supplied, so the slowest phase is Unknown / Insufficient data.

The Constraint Level and the binding constraint both point at Exits but for different reasons. The Constraint Level reflects maturity: the exit is designed, not exercised. The binding constraint reflects execution: the exit is the untested step that the governing scenario escalates into.

## 3. Evidence confidence: Moderate

- **Switch path: High.** The record shows current, executed T3 performance with stated clock events.
- **Exit path: contract-level only.** No executed or observed performance exists for the exit.
- **Corrective-action record: incomplete.** One action is overdue, and its owner and materiality are not stated.

Overall confidence is Moderate. The evidence is coherent and partly executed but has a testing gap on the exit and an open improvement loop.

## 4. Tolerance result: Met

| Element | Value |
|---|---|
| Clock start | 09:00, onset of disruption (injected provider loss in the T3 rehearsal) |
| Clock stop | 17:00, verified stabilization |
| Elapsed | 8 hours |
| Tolerance | 12 hours |
| Headroom | 4 hours (33 percent) |

Onset is established from current timing records, so the pre-detection interval is bounded and no Cannot Determine condition arises.

**Stress-test caveat.** The rehearsal ran within business hours. It does not show that authority, operators and access are available out of hours. An overnight or weekend onset could add delay in the Decide and Authorize phases, and this record does not show whether the four-hour headroom would absorb it.

## 5. Readiness gates

| # | Gate | Result | Basis |
|---|---|---|---|
| 1 | Service and owner defined | Pass | Services and tolerances at L3 |
| 2 | Tolerance approved and measurable | Pass | Approved twelve hours, measured at T3 |
| 3 | Material dependencies mapped | Pass | Pipes at L3 |
| 4 | Authority to invoke essential switches | Pass | Reroute authorized and performed at T3 (out-of-hours authority not evidenced, see caveat) |
| 5 | Executable exit for leading concentration | **Provisional Pass** | Rights, assistance and substitute secured in writing, but executability unrehearsed |
| 6 | Severe but plausible exercise completed | Pass | T3 end-to-end rehearsal |
| 7 | Evidence shows whether tolerance met | Pass | Both clock events recorded |
| 8 | Corrective actions have owners and target dates | **Unknown** | Overdue status implies a target date, but owner and materiality are not in the record |

## 6. Readiness decision: Conditionally Demonstrated

- **Cap F1:** Gate 8 at Unknown prevents Demonstrated.
- **Cap F2:** Gate 5 at Provisional Pass caps the decision at Conditionally Demonstrated until its evidence-conversion action closes.
- **Cap F4 does not apply:** No gate fails and the tolerance result is Met.

⧉ **Largest gap:** The priority exit is unrehearsed. Service B can reroute within tolerance, but it has not shown that it can leave the primary provider if the loss is permanent.

## 7. Evidence ledger (summary)

| ID | Claim | Type | Status | Credit | Conversion action |
|---|---|---|---|---|---|
| E-01 | Reroute restores service within 12h | Exercise record (T3) | Verified | Full, for the reroute path | None |
| E-02 | Clock events 09:00 and 17:00 | Exercise record, timing logs | Verified | Supports Met | Supply phase-level split |
| E-03 | Exit rights, assistance and substitute secured | Contract | Verified as written | Design credit (L2) | Rehearse exit |
| E-04 | Exit executes within tolerance | None | Not evidenced | None | T2 or T3 exit rehearsal |
| E-05 | Corrective action owned and escalated | Ticket (status only) | Not evidenced | None | Produce owner, original date, materiality and escalation record |

## 8. Prioritized actions

| # | Action | Acceptance test | Evidence required | Target |
|---|---|---|---|---|
| 1 | Resolve the overdue corrective action: confirm owner, materiality and escalation, then close or re-baseline with approval | Named owner, approved new date or verified closure | Ticket history, escalation record, closure verification | 30 days |
| 2 | Rehearse the priority exit at T2 minimum, invoking transition assistance and data return to the substitute | Exit stabilizes within tolerance with clock events stated | Exercise record, timing logs, data-integrity check | 90 days |
| 3 | Extract the phase-level clock split from the T3 rehearsal and run an out-of-hours authorization inject | Each phase timed, with authority reached outside business hours | Phase timing table, decision log | 60 days |

**Decisions required**
- Whether management accepts Conditionally Demonstrated as the reported position pending actions 1 and 2.
- Who owns and funds the exit rehearsal.

**Escalation**
- The overdue corrective action goes to the service owner's management line, as Domain 6 requires. No item currently needs external counsel.

[Purpose] Readiness assessment of Service B against the governing provider-loss scenario.
[Decisions Made] Constraint Level 2 (Exits). Binding constraint is Gate 5. Confidence Moderate. Tolerance Met (09:00 to 17:00, 8 of 12 hours). Decision Conditionally Demonstrated.
[Outstanding Items] Exit rehearsal. Gate 8 owner and materiality. Phase-level clock split. Out-of-hours authority evidence.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
