# SC1 the minimum rule and the exit gate both bite

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** a8d2b014da6b287f91602fe69c3fe89ffcf3cebdcf586b047a40c99cbda306b8  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 9085  **Output tokens:** 7937
**Truncated:** no

## User message

~~~~text
Treat the facts below as the reviewed evidence record for one critical service, Service B. Give the developed assessment: the capability profile, the Constraint Level and binding constraint, the evidence confidence, the gate results, the tolerance result and the readiness decision.

- Service and owner defined. Impact tolerance approved and measurable.
- Pipes: end-to-end dependency map current, concentrations identified. Strong.
- Switches: reroute switch delegated, tested at T3, executed within tolerance in the rehearsal. Strong.
- Exits: a written exit plan for the leading concentration dependency exists. No transition assistance secured, no substitute qualified, no rehearsal. Described only.
- Exercises: the reroute rehearsal was T3. Evidence current.
~~~~

## Assistant response

# GRCnext™ Developed Assessment: Service B [⇥ pending review]

**Mode:** Assessment (developed), limited to the requested results
**Evidence basis:** The facts supplied, treated as the reviewed evidence record. Items stated in the record are classified Verified. Items the record does not address are Not evidenced. This does not mean they are absent.
**Assessment date and evidence cut-off:** Not supplied. Unknown / Insufficient data.

## 1. Governing scenario

**The leading concentration dependency becomes unavailable or unacceptable on a sustained basis, so Service B must leave or replace it.**

This is the core optionality question for Service B. The reroute switch addresses disruption. It does not, on this record, replace the dependency. The record also does not state whether the reroute path itself avoids the concentration dependency.

## 2. Capability profile

| Domain | Score | Finding status | Basis |
|---|---|---|---|
| 1. Services and tolerances | **L2 Designed** | Verified; clock basis Not evidenced | Service, owner and approved measurable tolerance are verified. The record does not show that the tolerance clock starts at onset of disruption rather than at detection. It also does not show documented assumptions. L3 is withheld until the tolerance statement evidences an onset-based clock. |
| 2. Pipes | **L3 Exercised** | Verified | The dependency map is current and concentrations are identified. The T3 rehearsal executed against the mapped path. Fourth parties, recovery dependencies and manual alternatives are Not evidenced. L4 is not supported because monitoring and current metrics are Not evidenced. |
| 3. Switches | **L3 Exercised** | Verified | The reroute switch is delegated, was tested at T3 and was executed within tolerance in rehearsal. L4 is not supported because monitoring, periodic re-exercise and closed corrective-action loops are Not evidenced. |
| 4. Exits | **L1 Described** | Verified | A written exit plan exists. Three elements are verified as absent: secured transition assistance, a qualified substitute and a rehearsal. Execution depends on assumptions. |
| 5. Exercises | **L2 Designed** | Verified; partial | One T3 rehearsal exists. Under decision cap 8, its L3 credit attaches only to the reroute path. The exit path is unexercised. Findings, corrective actions and retest status are Not evidenced. |
| 6. Evidence and improvement | **L1 Described** | Mostly Not evidenced | Evidence is stated to be current. The record does not address artifact ownership, version control, freshness periods, decision records, corrective-action ownership or verified closure. |

No averaging is applied.

## 3. Constraint Level and binding constraint

**Constraint Level: L1.** This is the minimum of Pipes (L3), Switches (L3) and Exits (L1). Exits is the weakest structural component.

**Binding constraint: Gate 5, at the Execute phase of the exit path.**
- **Scenario:** sustained unavailability or unacceptability of the leading concentration dependency.
- **Basis:** No qualified substitute and no secured transition assistance exist. Even with authorization granted, the exit has nothing to execute against within tolerance.

⧉ **Largest gap:** Service B can switch but cannot leave. Its optionality ends where the reroute ends.

## 4. Evidence confidence

**Moderate.**
- Switch and pipe evidence is current and includes observed T3 performance, which is strong.
- Confidence is held at Moderate for four reasons:
  - the rehearsal's clock start and stop events are not stated in the record;
  - the onset-based clock definition is Not evidenced;
  - corrective-action and evidence-governance elements are Not evidenced;
  - whether the reroute path is independent of the concentration dependency is Unknown.
- The weakness of the exit is itself evidenced with reasonable confidence.

## 5. Readiness gates

| # | Gate | Result | Basis |
|---|---|---|---|
| 1 | Critical service and owner defined | **Pass** | Verified |
| 2 | Impact tolerance approved and measurable | **Pass** | Verified. The onset-based clock is flagged under Domain 1 but does not defeat approval or measurability. |
| 3 | Material dependencies mapped | **Pass** | Verified. Current map with concentrations identified. |
| 4 | Authority to invoke essential switches available | **Pass** | Verified. Reroute authority is delegated and was exercised at T3. |
| 5 | Executable exit exists for leading concentration dependency | **Fail** | Verified absence. A plan exists, but there is no substitute, no transition assistance and no rehearsal. A written plan is not an executable exit. |
| 6 | At least one severe but plausible exercise completed | **Pass** | Verified. T3 reroute rehearsal. It did not exercise the exit path. |
| 7 | Evidence demonstrates whether the tolerance was met | **Fail** | No exercise of the governing scenario exists, so no evidence shows whether the tolerance can be met when the dependency must be exited. |
| 8 | Material corrective actions have owners and target dates | **Unknown** | Not evidenced |

## 6. Tolerance result

**Governing scenario: Not Tested.**
- **Clock start (defined, not observed):** onset of disruption. This is the moment the leading concentration dependency stops delivering at the level Service B requires, or is formally determined unacceptable, putting Service B outside normal delivery.
- **Clock stop (defined, not observed):** verified stabilization of Service B on a substitute arrangement at or above its tolerance level.
- No events have been recorded because the exit has never been executed.

**Reroute rehearsal (subsidiary path):** The record reports execution within tolerance. The start and stop events are not stated. This result is therefore **Provisional**.
- **Evidence-conversion action:** extract the onset, detection and stabilization timestamps from the T3 exercise record. Confirm that elapsed time was measured from onset rather than from detection.

## 7. Readiness decision

**Not Demonstrated.**
- Gate 5 and Gate 7 fail, which triggers decision cap 4.
- Gate 8 is Unknown, which separately bars Demonstrated under cap 1.
- The reroute capability is a genuine strength (L3). It does not carry the service through the governing scenario.

## 8. Evidence-conversion actions (minimum, tied to findings)

1. **Exit (Gate 5).** Qualify a substitute for the leading concentration dependency and secure transition assistance in contract.
   - **Acceptance test:** substitute capacity confirmed in writing and the transition assistance clause executed.
   - **Evidence:** qualification record and signed contract or amendment.
   - Route the contract work through a Contract Exit Review.
2. **Exit rehearsal (Gate 7).** Run at least a T2 test of the critical exit components, such as data retrieval in usable form and cutover to the substitute, then progress to T3.
   - **Acceptance test:** full clock measured from onset, Detect through Stabilize, against tolerance.
   - **Evidence:** timestamped exercise record.
3. **Corrective actions (Gate 8).** Produce the corrective-action register for Service B.
   - **Acceptance test:** every material finding has a named owner and target date.
   - **Evidence:** register extract.
4. **Reroute independence (Unknown).** Confirm whether the reroute path depends on the leading concentration dependency or its fourth parties.
   - **Evidence:** dependency map extract for the reroute path.
   - If a dependency is found, the Switches credit narrows.
5. **Clock basis (Domain 1).** Amend or confirm the tolerance statement so the clock starts at onset of disruption.
   - **Evidence:** approved tolerance document.

[Purpose] Developed GRCnext™ assessment of Service B against the supplied evidence record.

[Decisions Made] Governing scenario set as sustained exit of the leading concentration dependency. Domain scores L2/L3/L3/L1/L2/L1. Constraint Level L1. Binding constraint is Gate 5 at Execute. Confidence Moderate. Tolerance Not Tested. Readiness Not Demonstrated.

[Outstanding Items]
- Assessment date and evidence cut-off.
- Rehearsal clock events.
- Onset-based clock definition.
- Corrective-action register.
- Reroute path independence.
- Decision required now: which accountable owner funds and authorizes substitute qualification and contract renegotiation for the leading concentration dependency, and by what date. Until that decision is made, Service B holds no exit.

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
