# SC3 contradictory evidence blocks Demonstrated

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** 031db8d348aaeeac5dd9fffdd01540ba609908c3029f26dc9712336773ecf952  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9139  **Output tokens:** 3201
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Can the exit be marked Demonstrated?

- A summary report states the exit was rehearsed end-to-end and completed within the approved tolerance.
- The exercise record for the same event shows a T1 facilitated tabletop. No system actions were performed. The stated completion time is an estimate produced in discussion, not a measured elapsed time.
~~~~

## Assistant response

# Service B Exit: Evidence Review and Readiness Decision [⇥ pending review]

**No. The exit cannot be marked Demonstrated.** The decision is **Not Demonstrated**. The exercise record for the event refutes the summary report's claim, the exit was discussed rather than executed and no measured elapsed time exists.

## 1. What the evidence shows

The two artifacts describe the same event and cannot both be true.

| Evidence ID | Claim tested | Artifact | Evidence type | Status | Credit |
|---|---|---|---|---|---|
| B-EV-01 | Exit rehearsed end-to-end (T3) | Summary report | Controlled document | **Refuted** by B-EV-02 | None |
| B-EV-02 | Nature of the exercise | Exercise record | Exercise record | **Verified** as T1 facilitated tabletop, no system actions | T1 credit only |
| B-EV-03 | Exit completed within approved tolerance | Summary report, relying on B-EV-02 | Controlled document | **Refuted** as a measured result. The figure is a discussion estimate. | None |

The exercise record is the primary record of the event and is the stronger evidence type. It affirmatively shows that no system actions were performed and that the completion time was estimated. This refutes the summary's statements that the exit was "rehearsed end-to-end" and "completed within the approved tolerance."

## 2. Gate and result view

| Item | Result | Basis |
|---|---|---|
| Gate 6: severe but plausible exercise completed | **Fail** | The only exercise of the governing scenario is T1, which is discussion-only. |
| Gate 7: evidence shows whether tolerance was met | **Fail** | No measured elapsed time exists. An estimate cannot stand in for one. |
| Gate 5: executable exit exists | **Unknown** | Executability was never tested. Exit design artifacts were not supplied. |
| Gates 1 to 4 and 8 | **Unknown** | Not supplied. This does not mean they do not exist. |
| Tolerance result | **Not Tested** | No clock start or clock stop event was observed or recorded. The onset event is unknown. |
| Exercise tier | **T1** | All actions were simulated in discussion. No actions were performed. |
| Exits domain | Below L3 (exact score: Unknown / Insufficient data) | Cap 8: T1 alone cannot earn L3. |
| Evidence confidence | **Low** | The positive claim rests on a refuted summary and an estimate. |
| Binding constraint | **Gate 6** in the Service B exit scenario (scenario details not supplied) | The Execute, Verify and Stabilize phases of the exit have never been performed, so nothing establishes that the exit can run within tolerance. |

These decision caps apply:
- **Cap 1:** a Fail on any core gate prevents Demonstrated.
- **Cap 4:** a Fail on any core gate makes the decision Not Demonstrated.
- **Cap 5:** Demonstrated requires a tolerance result of Met with both clock events stated. Neither event exists here.

⧉ **Largest risk:** Management has been told that the Service B exit works within tolerance. The only record of the event shows that the exit has never been executed. Any reliance on this claim, such as a renewal, a concentration risk acceptance or a regulatory attestation, rests on a refuted statement.

## 3. Required actions

| # | Action | Owner | Acceptance test | Evidence required |
|---|---|---|---|---|
| 1 | Correct or withdraw the summary report and notify everyone who relied on it | Unknown (to be named) | A corrected report states T1, simulated actions only and tolerance Not Tested | Revised report with version history and a distribution record |
| 2 | Design and run a T2 test of the critical exit components, such as data retrieval in usable form and substitute provisioning | Unknown | Components execute and the elapsed time is measured | System records, logs and timestamps |
| 3 | Run a T3 end-to-end exit rehearsal that measures the full clock from the onset of disruption through Detect, Interpret, Decide, Authorize, Execute, Verify, Communicate and Stabilize | Unknown | Measured elapsed time is compared to the tolerance, with clock start and stop events stated | Exercise record, timestamps and decision records |
| 4 | Supply the exit plan, approved tolerance and dependency map | Unknown | Gates 1 to 5 can be classified | Controlled documents with owners and dates |

## 4. Escalation

**ESCALATE: overstated readiness reporting.**
- **Issue:** A summary report described a T1 tabletop as an end-to-end rehearsal completed within tolerance.
- **Operational consequence:** Decisions about Service B may rest on a refuted claim of exit readiness.
- **Facts required:** Who authored and approved the summary, who received it and what decisions or attestations relied on it.
- **Evidence required:** The distribution record and any downstream decision or attestation records.
- **Interim control:** Mark the Service B exit Not Demonstrated in all reporting until Action 3 closes.
- **Decision owner:** The accountable owner for Service B, or the risk committee if no owner is named.
- **Questions for senior management:** Was any external or regulatory statement based on this summary? If so, does it require correction?

---

**[Purpose]** Determine whether the Service B exit can be marked Demonstrated on the reviewed evidence.
**[Decisions Made]** Not Demonstrated. Gates 6 and 7 Fail. Tolerance Not Tested. The summary report's claims are Refuted.
**[Outstanding Items]** Name the owners. Supply the exit plan, tolerance and dependency map. Run the T2 and T3 tests. Correct the summary report. Resolve the escalation.

Please do not paste credentials, secrets or protected personal data in follow-up material. Neutral labels are sufficient.

Final Liability rests with the Human.

❓ needs input

<!-- end of transcript; written by tests/run_prompt_cases.py -->
