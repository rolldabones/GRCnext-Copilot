# SC1 the minimum rule and the exit gate both bite

**Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261027-R2
**Prompt proper SHA-256:** bea208c313a6c5ed022e946e58ab1d807b5dccbe8850b4ad4bc10099c7b11f7b
**Run input SHA-256:** a8d2b014da6b287f91602fe69c3fe89ffcf3cebdcf586b047a40c99cbda306b8  **Case file:** tests/scoring-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 9257  **Output tokens:** 7405
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

# GRCnext™ Developed Assessment: Service B

[⇥ pending review]

**Basis.** The facts you supplied are treated as the reviewed evidence record. The record is a summary: it gives no artifact identifiers, dates, owners or clock events. Where a criterion is not addressed, the finding is Unknown or Not evidenced. That is a statement about the record, not about the organization.

**Governing scenario.** The leading concentration dependency becomes unavailable or unacceptable for longer than the reroute switch can sustain, so the service must leave it. Every gate below is classified against this scenario.

## Executive scorecard

| Result | Position |
|---|---|
| Readiness decision | **Not Demonstrated** |
| Constraint Level | **L1** (Exits) |
| Binding constraint | **Gate 5, Execute phase of the exit path** |
| Evidence confidence | **Moderate** |
| Tolerance result (governing scenario) | **Not Tested** |

⧉ **Largest gap.** Service B has no executable exit from its leading concentration dependency. The reroute switch is strong, but it can only buy time. If the dependency cannot come back, nothing executable and tested follows the reroute.

## Capability profile

| Domain | Score | Basis |
|---|---|---|
| 1. Services and tolerances | L2 Designed | Service, owner and tolerance are defined, approved and measurable (Verified). The record does not show that the clock starts at onset rather than at detection. It also does not show that tolerance assumptions are documented. L3 is withheld until the onset-based clock rule is evidenced. |
| 2. Pipes | L3 Exercised | The dependency map is current and concentrations are identified (Verified). The T3 reroute rehearsal exercised the dependencies on the reroute path. L3 applies to that path only (cap F8). Fourth parties, recovery dependencies and manual alternatives are not evidenced, so L4 is out of reach. |
| 3. Switches | L3 Exercised | The reroute switch is delegated, was rehearsed at T3 and was executed within tolerance (Verified). L4 would need monitoring, current metrics and closed corrective-action loops, none of which are evidenced. |
| 4. Exits | L1 Described | A written exit plan exists (Verified). No transition assistance is secured, no substitute is qualified and there has been no rehearsal (Verified absences). Execution depends on arrangements that do not exist yet. |
| 5. Exercises | L2 Designed | One current T3 rehearsal covers the switch path. The exit path has never been exercised. Pass and fail criteria, hotwash, findings and retest status are not evidenced. |
| 6. Evidence and improvement | L1 Described | Evidence currency is Verified. Artifact ownership, version control, freshness periods, decision records and corrective-action closure are not evidenced. The score reflects missing evidence, not a finding that these controls are absent. |

No averaging is applied. The Exits score at L1 is the structural weakness.

## Constraint Level and binding constraint

**Constraint Level = min(Pipes L3, Switches L3, Exits L1) = L1.**

**Binding constraint:** gate 5, Execute phase, in the governing scenario.

The clock cannot complete Execute on the exit path for three reasons:
- there is no qualified substitute to move to;
- there is no secured transition assistance from the incumbent;
- the sequence has never been timed.

Detect, Decide and Authorize on the exit path are also unevidenced. They are not binding until Execute becomes possible.

## Gate results

| # | Gate | Result | Basis |
|---|---|---|---|
| 1 | Service and owner defined | Pass | Verified |
| 2 | Tolerance approved and measurable | Pass | Verified. The onset clock rule remains a Domain 1 gap. |
| 3 | Material dependencies mapped | Pass | Current map with concentrations identified |
| 4 | Authority to invoke essential switches | Pass | Reroute delegated and used in the T3 rehearsal |
| 5 | Executable exit for leading concentration | **Fail** | Plan only: no substitute, no transition assistance, no rehearsal |
| 6 | Severe but plausible exercise of governing scenario | **Provisional Pass** | T3 covered the reroute portion only. The exit portion is unexercised. Conversion action: B-03. |
| 7 | Evidence shows whether tolerance was met | **Fail** | No exercise of the full governing scenario exists, so no tolerance evidence exists for it |
| 8 | Corrective actions have owners and dates | **Unknown** | No owners or dates supplied for the exit gaps |

## Tolerance result

**Governing scenario: Not Tested.** The exit path has never run, so no clock start or clock stop event exists for the full sequence.

**Reroute component (secondary).** The record says the switch executed within tolerance at T3. It does not state:
- the onset event that started the clock;
- the stabilization event that stopped it;
- whether the pre-detection interval was bounded.

This supports component credit for Switches and Pipes. It cannot support a Met result under Section 8E until both clock events are produced from the rehearsal record.

## Readiness decision

**Not Demonstrated.** Three caps apply:
- Gates 5 and 7 Fail (caps F1 and F4).
- Gate 8 is Unknown (cap F1).
- The governing tolerance result is Not Tested (cap F5).

Clearing gate 5 alone would not lift the decision to Demonstrated. Gate 6 would still hold a Provisional Pass until the exit is rehearsed (cap F2).

## Evidence ledger (summary)

| ID | Claim tested | State | Credit | Evidence-conversion action |
|---|---|---|---|---|
| E-01 | Service, owner and tolerance defined and approved | Verified | Gates 1 and 2 | Attach the approval record and the clock-start definition |
| E-02 | Dependency map current, concentrations identified | Verified | Gate 3, Pipes L3 (reroute path) | Record fourth parties, recovery dependencies and manual alternatives |
| E-03 | Reroute delegated, T3 rehearsal, within tolerance | Verified | Gate 4, Switches L3 | Extract onset and stabilization timestamps and the phase timings |
| E-04 | Written exit plan exists | Verified | Exits L1 only | None until the substantive gaps close |
| E-05 | Transition assistance, substitute and exit rehearsal | Not evidenced (absence stated) | None | Backlog B-01 to B-03 |
| E-06 | Corrective-action owners and dates | Not evidenced | None | Backlog B-04 |

## Prioritized actions

| # | Action | Acceptance test | Evidence required | Escalation |
|---|---|---|---|---|
| B-01 | Secure transition assistance from the incumbent | Executed contractual term or amendment covering duration, scope, data return format and cost | Signed instrument, clause references mapped to exit steps | ⚠ Counsel review |
| B-02 | Qualify a substitute arrangement for the concentration dependency | Substitute meets defined capacity and onboarding-time criteria within tolerance assumptions | Qualification record, capacity test, commercial readiness | Funding decision |
| B-03 | Rehearse the exit at T2 for the data return and cutover components, then at T3 end-to-end | Full clock measured from onset to verified stabilization, with pass or fail against tolerance | Exercise record with phase timings and the simulated versus performed split | None |
| B-04 | Assign owners and target dates to B-01 to B-03 | Each item has a named owner and date in the corrective-action register | Register entry | ESCALATE if no owner accepts |
| B-05 | Evidence an onset-based clock start for the tolerance and recover the reroute clock events | Definition approved, reroute timestamps recorded | Updated tolerance statement, rehearsal log extract | None |

⚠ **B-01.** Termination rights, notice periods and assistance terms depend on the governing law and contract text. Neither is in the record. Jurisdiction-specific conclusions are reserved for qualified counsel.

## Escalation

**ESCALATE: risk position on a critical service with no executable exit**
- **Issue:** Service B cannot leave its leading concentration dependency within tolerance.
- **Operational consequence:** Prolonged or permanent loss of the dependency exceeds what the reroute switch can sustain, and harm continues past tolerance.
- **Facts required:** Renewal and termination dates, plus the reroute's sustainable duration.
- **Evidence required:** B-01 to B-03 outputs.
- **Interim control:** Document the maximum period the reroute can sustain the service, and treat it as the exit decision deadline.
- **Decision owner:** The Service B accountable owner, with senior management for risk acceptance and funding.
- **Questions for counsel and management:**
  - Is the current exposure accepted for a defined period?
  - Who funds substitute qualification?
  - Does any renewal window create negotiation leverage now?

## Decision required now

Service B's owner must decide one of two things:
- fund and own B-01 to B-03 with target dates; or
- formally accept operating without an executable exit for a defined period.

---

**[Purpose]** Developed assessment of Service B readiness against the governing exit scenario.

**[Decisions Made]** Scores, gate results, Constraint Level L1, binding constraint at gate 5 Execute, evidence confidence Moderate, tolerance Not Tested, readiness Not Demonstrated.

**[Outstanding Items]**
- Clock events from the reroute rehearsal
- Onset clock rule
- Contract terms and governing law
- Corrective-action owners and dates
- Fourth-party and manual-alternative mapping

Final Liability rests with the Human.

✅ complete

<!-- end of transcript; written by tests/run_prompt_cases.py -->
