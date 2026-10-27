# SC4 exercise tier gates the maturity level

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 8ae2878ad749f1baf0f85cdfcc7da03625202c56594331bd2401ef6a4ed73fb1  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9168  **Output tokens:** 2227
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Score the Exercises domain, classify the exercise gate and give the tolerance result.

- A T1 facilitated tabletop was run for the governing severe but plausible scenario.
- Participants included the accountable owner and the relevant authority.
- Findings and notional decisions were recorded. No switch or exit was invoked. No timing was measured against tolerance.
- The capability could be put to a controlled test; nothing prevents one.
~~~~

## Assistant response

# Service B: Exercises Assessment

**Scope.** This assessment covers the Exercises domain score, core readiness gate 6 and the tolerance result for Service B. It treats the four supplied facts as the reviewed evidence record.

## Results

| Item | Result | Evidence state |
|---|---|---|
| Exercises domain | **L2 Designed** (ceiling on this record) | Verified |
| Gate 6 (severe but plausible exercise) | **Fail** | Verified |
| Tolerance result | **Not Tested** | Verified |

## Exercises domain: L2 Designed

**Supports L2**
- A severe but plausible scenario for the governing case exists and was used.
- The accountable owner and the relevant authority took part.
- Findings and notional decisions were recorded, so some evidence was preserved.

**Prevents L3**
- **Tier cap applies.** A T0 or T1 exercise alone does not earn L3 (Section 6 and decision cap F8).
- **Exception does not apply.** The narrow exception covers only a capability that genuinely could not be executed in a controlled test. The record states a controlled test is feasible and nothing prevents one.
- **Nothing was executed.** No switch or exit was invoked.
- **No timing or criteria.** No timing was captured and there were no pass or fail criteria tied to tolerance.

**Unknown / Insufficient data**
- Whether the tabletop findings produced corrective actions with owners and dates.
- Whether any remediation has been retested.

These unknowns do not lower the score below L2 on this record. They must be evidenced before any later uplift.

## Gate 6: Fail

Section 7 is explicit: a discussion-only exercise (T0 or T1) of the governing scenario is a Fail on this gate. It cannot be a Provisional Pass. That classification is reserved for exercises in which material actions were simulated or only part of the scenario was covered.

Strong participation does not change the result. The gate tests execution, and none occurred.

## Tolerance result: Not Tested

- **Clock start.** No onset-of-disruption event was exercised or recorded.
- **Clock stop.** No verified stabilization event was exercised or recorded.
- **Basis.** No elapsed time was measured against tolerance across any phase of the execution clock (Detect through Stabilize).

"Not Tested" is the correct result rather than "Cannot Determine," because no execution was attempted. The approved tolerance statement for Service B was not supplied and is Unknown.

## Decision consequence

Under decision cap F4, the Fail on gate 6 makes the Service B readiness decision **Not Demonstrated**, regardless of how the other domains score. Gate 7 (evidence of whether tolerance was met) cannot pass on this record either. That is a provisional observation outside the requested scope.

⧉ **Largest gap.** Service B's optionality for the governing scenario rests entirely on notional decisions. Nothing establishes that any switch or exit runs, or that the full clock fits within tolerance.

## Next actions

| Action | Acceptance test | Evidence required |
|---|---|---|
| Run a T2 controlled test of the primary switch for the governing scenario | The switch is invoked, and timing is captured by clock phase from the onset event through verified stabilization | Exercise record, system logs, timestamps and a decision and authorization record |
| Progress to a T3 end-to-end rehearsal covering switch and exit | Pass or fail is judged against the approved tolerance, with both clock events stated | Evidence pack, elapsed-time table, hotwash and corrective-action register |
| Supply the tabletop corrective actions | Each action has an owner, a target date and a retest requirement | Corrective-action register extract |
| Supply the approved tolerance statement | The statement is measurable, names its approving authority and starts the clock at onset | Approved tolerance document |

[⇥ pending review]

[Purpose] Score the Exercises domain, classify gate 6 and give the tolerance result for Service B.
[Decisions Made] Exercises L2; gate 6 Fail; tolerance Not Tested; readiness capped at Not Demonstrated.
[Outstanding Items] Tolerance statement; tabletop corrective actions and retest status; controlled test of the governing scenario.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
