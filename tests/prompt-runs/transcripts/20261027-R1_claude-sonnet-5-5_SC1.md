# SC1 the minimum rule and the exit gate both bite

**Model requested:** claude-sonnet-5-5  **Model returned:** claude-sonnet-5-5  **Run:** 20261027-R1
**Prompt proper SHA-256:** 288c580084cc17a66dba3831d5797faec541337acda291fbd6146453f871186f
**Run input SHA-256:** a8d2b014da6b287f91602fe69c3fe89ffcf3cebdcf586b047a40c99cbda306b8  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 16000  **stop_reason:** end_turn  **Input tokens:** 9085  **Output tokens:** 7319
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

# GRCnext™ Developed Assessment: Service B [↻ draft]

Please do not paste secrets, credentials or protected personal data into this engagement. Neutral labels are used throughout.

## 1. Scope, basis and assumptions

- **Mode:** Assessment. **Service:** Service B (single critical service). **Evidence basis:** the facts you supplied, treated as the reviewed evidence record. Artifact IDs, dates and owners were not supplied and are recorded as Unknown.
- **A1.** The governing scenario is loss of the leading concentration dependency, with the reroute switch as the first-line response. The record does not name the scenario. If it differs, Gates 4 to 7 must be re-evaluated.
- **A2.** The T3 rehearsal used a severe but plausible scenario. If it did not, Gate 6 becomes Unknown.
- **Not supplied (Unknown / Insufficient data):** clock start and stop events, the onset event, the phase-by-phase timing record, corrective-action records, the evidence freshness period, and whether the reroute target is a qualified substitute.

## 2. Executive scorecard

| Result | Finding |
|---|---|
| Readiness decision | **Not Demonstrated** |
| Constraint Level | **L1** (minimum of Pipes 2, Switches 3 and Exits 1; set by Exits) |
| Binding constraint | Gate 5, the exit for the leading concentration dependency. In the governing scenario (A1) it limits the Execute and Stabilize phases for any path that needs the exit. Basis: the exit exists only on paper, with no transition assistance, no qualified substitute and no rehearsal. |
| Evidence confidence | **Moderate** |
| Tolerance result | **Cannot Determine** (reroute path reported within tolerance in rehearsal; exit path Not Tested) |

⧉ **Largest gap:** the exit for the leading concentration dependency is described only and cannot be executed.

## 3. Capability profile

| Domain | Score | Basis | Evidence state |
|---|---|---|---|
| 1. Services and tolerances | L2 | Service and owner defined. Tolerance approved and measurable. Onset event, clock start and clock stop are not evidenced. | Verified (definition and approval); Not evidenced (clock events) |
| 2. Pipes | L2 | Current end-to-end map with concentrations identified. L3 needs evidence the map was validated through exercise. | Verified |
| 3. Switches | L3 for the reroute path only | Delegated, tested at T3 and executed within tolerance in rehearsal. No credit extends to other switches. | Verified (reroute); Unknown (other switches) |
| 4. Exits | L1 | Written plan only. No transition assistance, no qualified substitute, no rehearsal. | Verified as described only |
| 5. Exercises | L3 for the reroute path only | One current T3 rehearsal. No exit exercise exists. Remediation records were not supplied. | Verified |
| 6. Evidence and improvement | Not scored | Insufficient data. Absence from the record is not treated as nonexistence, and no score is assigned. | Unknown |

No averaging is applied. Strong Pipes and Switches do not offset the Exits weakness.

## 4. Gate results

Each gate is classified once against the governing scenario.

| # | Gate | Result | Basis |
|---|---|---|---|
| 1 | Critical service and owner defined | **Pass** | Defined on the record. |
| 2 | Impact tolerance approved and measurable | **Pass** | Approved and measurable on the record. The onset event is still needed (see Gate 7 and action 4). |
| 3 | Material dependencies mapped | **Pass** | Current map with concentrations identified. |
| 4 | Authority to invoke essential switches | **Pass** | The reroute switch is delegated and was executed in rehearsal. This assumes reroute is the essential switch (A1). Out-of-hours availability is not separately evidenced. |
| 5 | At least one executable exit for the leading concentration dependency | **Fail** | Exit plan is written only. Without transition assistance, a qualified substitute or a rehearsal, it is not executable. |
| 6 | At least one severe but plausible exercise completed | **Pass** | T3 reroute rehearsal, subject to A2. |
| 7 | Evidence demonstrates whether tolerance was met | **Provisional Pass** | Execution within tolerance is reported, but the clock start and stop events and the onset-to-detection interval are not in the record. Conversion action: obtain the rehearsal timing record by phase from onset. |
| 8 | Material corrective actions have owners and target dates | **Unknown** | No corrective-action data supplied. The exit gaps above need register entries. |

## 5. Tolerance result: Cannot Determine

- **Clock start:** the observable onset event for Service B is not stated. Onset-to-detection is Unknown.
- **Clock stop:** verified stabilization at or above tolerance level. The stop event used in the rehearsal is not stated.
- Under the decision logic, Met requires both clock events stated and an evidenced bound on the pre-detection interval. Neither is in the record.
- **Reroute path:** reported within tolerance in a T3 rehearsal. This is Provisional until the full-clock record is reviewed.
- **Exit path:** Not Tested.

## 6. Evidence confidence: Moderate

- Evidence is current, coherent and includes an observed T3 execution of the reroute switch.
- It is not High because the exit rests on a document alone. The clock events and the Evidence and improvement domain are also unevidenced.
- It is not Low because the core Pipes and Switches claims rest on exercise evidence, not representations.

## 7. Evidence ledger (condensed)

| ID | Claim | Evidence type | Status | Credit | Conversion action |
|---|---|---|---|---|---|
| E1 | Service, owner and tolerance defined and approved | Controlled document (per record) | Verified | Gates 1 and 2 | Record approval date and authority |
| E2 | Dependency map current, concentrations identified | System or controlled record (per record) | Verified | Gate 3, L2 | Record date and owner; show exercise validation for L3 |
| E3 | Reroute delegated, T3 executed within tolerance | Exercise record (per record) | Verified (execution); Provisional (full-clock timing) | Gates 4 and 6; Switches L3 for reroute path | Obtain phase timing from onset |
| E4 | Exit plan exists | Controlled document | Verified as written only | None toward Gate 5 | See actions 1 to 3 |
| E5 | No transition assistance, substitute or rehearsal | Per record | Verified absence | Gate 5 Fail | See actions 1 to 3 |

Owner, date and source location are Unknown for all items. No contradictions were identified. One question needs an answer: does the reroute target depend on the unqualified substitute? If it does, the reroute credit and the Exits finding interact and must be reconciled.

## 8. Top breakpoints

1. The exit for the leading concentration dependency is not executable (Gate 5 Fail).
2. The full clock is not evidenced, so the tolerance result cannot be determined.
3. The corrective-action loop is unknown (Gate 8, Domain 6).
4. Switch and exercise credit covers one path only.

## 9. Prioritized actions

| # | Action | Acceptance test | Evidence required | Decision or escalation |
|---|---|---|---|---|
| 1 | Secure transition assistance for the leading concentration dependency (contractual or agreed arrangement) | Written, executable commitment with scope, timing and cost | Executed agreement or contract amendment | Business owner. ESCALATE to counsel if contractual rights are absent or disputed |
| 2 | Qualify a substitute for that dependency | Substitute meets service requirements and can carry load within tolerance | Qualification record, capacity evidence | Service owner and risk owner |
| 3 | Rehearse the exit (T2 for components, then T3 end to end) | Exit executed within tolerance, with full-clock timing from onset | Exercise record and evidence pack | Service owner approves scenario |
| 4 | Document the onset event and clock stop for Service B, then reconstruct rehearsal timing by phase | Detect to Stabilize timings from onset, with a bound on the pre-detection interval | Timing record, onset definition | Tolerance approving authority |
| 5 | Open corrective-action entries for actions 1 to 3 with owners and dates | Register entries with owner, date and verification-based closure | Corrective-action register | Service owner |
| 6 | Confirm whether the reroute depends on the unqualified substitute | Written dependency analysis | Dependency map update | Service owner |

Actions 4 to 6 are low effort and can precede the 90-day exit work. The sequence is 1, then 2, then 3, because the rehearsal needs the arrangement and substitute in place.

## 10. Decisions required

- Confirm or correct the governing scenario (A1) and the severity of the rehearsal scenario (A2).
- Name the executive owner and funding for actions 1 and 2.
- Decide the target date for the exit rehearsal.
- No regulatory or compliance conclusion is drawn. No ⚠ item arises on this record. If transition-assistance rights are contractually absent, refer to counsel through a Contract Exit Review.

## 11. Closing blocks

**[Purpose]** Assess the executable optionality of Service B on the supplied evidence record.

**[Decisions Made]** Readiness: Not Demonstrated. Constraint Level: L1, bound by Gate 5. Tolerance result: Cannot Determine. Evidence confidence: Moderate.

**[Outstanding Items]** Governing scenario confirmation; clock events and phase timing; Domain 6 data and Gate 8 status; artifact IDs, dates and owners; reroute target dependency; actions 1 to 6.

Final Liability rests with the Human.

❓ needs input

<!-- end of transcript; written by tests/run_prompt_cases.py -->
