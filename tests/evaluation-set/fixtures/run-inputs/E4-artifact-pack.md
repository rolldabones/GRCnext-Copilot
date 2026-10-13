# Synthetic artifact pack for case E4 (advisory-suite-cases.md)

Paste the whole file into the Exit Prover input together with `E4-pipes.json` and `E4-switch-registry.json`. Every artifact below is synthetic. The case expects PASS: every dependency, switch and obligation Verified against these reviewed artifacts, one obligation Not applicable with the stated reason.

## RR-2026-09-18, T3 reroute rehearsal record
Service: payments. Scenario: Vendor A gateway unavailable. Start 2026-09-18 09:00 (outage declared, clock start). SW-010 flipped 09:12 (CHG-1041). Traffic on Vendor B 11:40. Reconciliation of in-flight transactions complete 12:05. Verified by Head of Payments 12:15 (clock stop). Elapsed 3h15m against 12h tolerance. Observers: Head of Payments, Internal Audit (J. Park). Rollback not exercised. Dependency map unchanged since.

## OT-44, observed test, 2026-10-02
Reporting feed switched from Vendor A pull to internal report job RPT-INT-7 at 14:00 by SW-011; first internal report produced 14:52; row counts matched Vendor A feed for 2026-10-01 (18,204 rows). Assessor sign-off: Data Eng lead, 15:10.

## Switch registry extract (also supplied as E4-switch-registry.json)
SW-010 Route Payments to Vendor B: status OFF, last_verified 2026-09-18T12:15:00+09:00 (RR-2026-09-18), last_verified_state OFF (reverted after rehearsal, CHG-1042), owner Payments Ops.
SW-011 Disable Vendor A reporting pull: status OFF, last_verified 2026-10-02T15:10:00+09:00 (OT-44), last_verified_state OFF, owner Data Eng.

## MSA clause 12.2
"Either party may terminate this Agreement for convenience on thirty (30) days' written notice to the other party. No termination fee or penalty shall apply."

## MSA clause 12.4
"Supplier acknowledges that Customer may change payment processor without notice to Customer's end users where continuity of service is maintained."

## NT-2, notice template (approved Legal 2026-08-30)
"To Vendor A: Pursuant to clause 12.2 of the MSA dated [date], Customer gives thirty (30) days' notice of termination for convenience, effective [date]. ..."

## NTC-2026-09, notice issued in rehearsal
Draft notice on NT-2 completed and approved by Legal 2026-09-18 09:40 in the rehearsal; not sent (drill).

## DX-31, export test record, 2026-09-18
Full export of Vendor A transaction records for 2026-01-01 to 2026-09-17: 2,418,662 rows; reconciled 100 percent against internal ledger; duration 5h50m; owner Data Eng; observer Internal Audit (J. Park).

## Durations (all observed in RR-2026-09-18, OT-44 and DX-31 except notice)
Notice 1h at T0 (estimate); reroute 2h40m; reporting switch 52m; export 5h50m; verification 1h.
