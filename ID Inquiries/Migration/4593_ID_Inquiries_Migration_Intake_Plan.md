# ID Inquiries — Migration Intake Plan (v5.1 — Final)

**Project:** #4593 — ID Inquiries Ltd
**Prepared by:** A2Z Cloud — Sam (Pranesh)
**Date:** April 2026
**Status:** Final plan — ready to build

---

## TL;DR

Single hardened Excel file `4593_ID_Inquiries_Migration_Intake_v5.xlsx` goes to Alison **after** a quick Pre-Fill Data Audit confirms we're capturing every field she actually has. The template:

- Locks every dropdown to live-CRM picklist values (sourced from `picklist_report.json`)
- Hard-stops missing required fields with a live **Submission Readiness** dashboard
- Captures the pending portal-user list on a separate tab
- Covers every system-mandatory CRM field across all 6 target modules
- Is open to expansion — additional columns added pre-fill if Alison has more data

She fills ~300 rows, the dashboard goes green, she sends it back, and we run a deterministic Python pipeline that:

1. Validates against the live CRM picklist contract
2. Splits the flat intake into the 6 strict-order import files
3. Splits client full names into First_Name / Last_Name
4. Injects fixed values (Pipeline = "Music", Owner = "ID Inquiries Admin", etc.)
5. Generates a Premises → Investigator mapping for the post-import workaround
6. Produces a pre-import diff report

---

## 1. System-mandatory field coverage matrix

Every Zoho-system-mandatory field across the 6 target modules, mapped to where it comes from in the intake:

| CRM Module | Mandatory Field | API Name | Type | Source in v5 Intake | Method |
|---|---|---|---|---|---|
| **Accounts** (Client Accounts) | Client Account Name | `Account_Name` | text | `Instructing Company` column | Direct, deduplicated |
| **Contacts** (Clients) | Last Name | `Last_Name` | text | `Instructing Client` column → split | Conversion script splits "Michael Green" → First_Name="Michael", Last_Name="Green" using lookup table for known clients + whitespace split for unknowns |
| **Deals** (Instructions) | Instruction Name | `Deal_Name` | text | `Premises Name` column | Direct (consistent with current CRM convention) |
| **Deals** (Instructions) | Stage | `Stage` | picklist | Derived from `Instruction Status` column | Status mapping (see §5) |
| **Deals** (Instructions) | **Pipeline** | `Pipeline` | picklist | **Fixed value: "Music"** | Conversion-script injection — only valid Pipeline value per `picklist_report.json` |
| **Investigators** | Investigator Name | `Name` | text | `Investigator Assigned` column | Direct, deduplicated, excluding blank/ON HOLD |
| **Premises** | Premise Name | `Name` | text | `Premises Name` column | Direct, deduplicated |
| **Premises_Checks** (Licence Checks) | *(none)* | — | — | — | No mandatory enforcement needed |

**Result:** every system-mandatory field is either captured directly from the intake, derived from intake values via deterministic rules, or hard-coded in the conversion script. Zero risk of import rejection on mandatory-field grounds.

## 2. Pre-Fill Data Audit with Alison (NEW — happens before template ships)

Before Alison opens v5 we confirm:

> "Here's what we're capturing per record. If you have any other data points in your manual records — even ones we haven't asked for — tell us now and we'll add columns to the template. It's much cheaper to add a column before you start filling than to chase missing data after."

**The audit doc lists current capture + suggests additional fields she may have:**

| Module | Current capture | Additional fields we could add if she has them |
|---|---|---|
| Client Accounts | Firm name | Phone, billing address, website |
| Clients | Full name, Firm | Email, mobile, salutation, role, secondary email |
| Investigators | Name (only — rest from internal records) | Skillsets, areas covered (regions), exclusions, languages, equipment available, rates if non-default |
| Premises | Name, address, postcode, PLH, DPS, licensing authority | Address Line 2, capacity, licence type, opening hours, special access notes |
| Instructions | Date, type, status, notes | Priority Level (High / Normal / Specific Date), Specific Date, Instructions to Investigator, expected duration, special access requirements |
| Licence Checks | Council request method/date, response, notes | Date information received, specific check type, council reference number |

If Alison says "yes, we have X" → we add those columns to v5 before sending. If "no, that's everything" → we ship v5 as-is. Either way, no wasted fill-time.

This audit is a 15-minute call or a single email reply. Quickest possible step.

## 3. v4 → v5 — what changes

| Area | v4 (current) | v5 (final) | Why |
|---|---|---|---|
| Required fields | Marked with `*` only | `*` + red-fill when blank + live readiness counter | Hard-stop visibility |
| Picklists | Static list | Live-CRM-verified list (`picklist_report.json`) | Eliminates picklist mismatch errors |
| Venue type | "Basic" passes through | Dropdown matches CRM `Instruction_Type` exactly (20 values) | Removes the "Basic isn't valid" mapping problem |
| Submission readiness | None | New `Submission Readiness` sheet with row-by-row diagnostics | Self-service QA — Alison sees gaps without us |
| Portal users | Implicit / not handled | New `Portal Users` sheet | Captures Alison's pending list cleanly, decouples from main migration |
| Cover sheet | Single Guide tab | Cover + Guide + status legend + 1-page how-to | Lower friction onboarding |
| Sheet protection | None | Locked everywhere except input cells on Instructions + Portal Users | Prevents accidental column rename / picklist edit |
| Pre-allocated rows | 492 empty rows | 400 rows with formulas auto-extending | Less intimidating, still enough headroom |
| Dependent dropdowns | No | Instructing Client filtered by Instructing Firm via INDIRECT | Reduces orphaned-link errors |
| Dates | Plain DD/MM/YYYY | Same, but cell format locked + warning if text-typed | Catches the silent killer of mistyped dates |
| Field set | 22 columns | 22 + any agreed additions from Pre-Fill Data Audit | Captures everything Alison has, not just the test extract |

## 4. Required-field rules (hard-stop)

**Required on every row:**

- Premises Name, Street Address, City, Postcode, Licensing Authority
- Instruction Status, Instructing Company, Instructing Client
- Date of Instruction, Instruction Type, Is Reinstruction?

**Conditionally required:**

- Investigator Assigned + Date Assigned → required IFF Instruction Status = `Allocated`
- Licence Check Notes → required IFF Council Response = `Yes`

**Optional:** County, PLH, DPS, Client Ref, Instruction Notes, Council Request Method, Council Request Date, plus any extras agreed in the Pre-Fill Audit.

The `Submission Readiness` sheet computes live:

- Total rows entered
- Rows fully valid (green)
- Rows missing required fields (with row numbers)
- Rows with invalid picklist values (covers paste-overrides)
- Allocated rows missing investigator/date
- "Other" picks (firm/client/investigator) flagged for A2Z follow-up
- Single **READY TO SEND: YES/NO** indicator

She sends only when `READY TO SEND = YES`.

## 5. Dropdown content (live-CRM-aligned)

| Field | Allowed values |
|---|---|
| **Instruction Status** | On Hold, Unallocated, Ready for Allocation, Allocated |
| **Instruction Type** | Pub/Bar – background, Pub/Bar – event, Restaurant//Café, Cafe, Nightclub, Stripclub, Gentleman's Club, Shop, Shop – High Street, Shop – Warehouse/Industrial, Beauty Salon, Barber (Gents), Hairdresser, Nail Salon, Tattoo Parlour, Gym, Hotel – Bedroom, Hotel – Common Areas, Festival, Other |
| **Is Reinstruction?** | Yes, No |
| **Council Request Method** | Public Register Online, Email, Form Submitted *(no "FOI request" — v1 error)* |
| **Council Response** | Yes, No, Awaiting Response |
| **Instructing Firm** | Hamlins LLP, Seddons-GSC, Brodies LLP, Burness Paull LLP, Other – advise A2Z Cloud |
| **Instructing Client** | Full pre-split list with `(Firm)` suffix + Other option |
| **Investigator** | 16 known investigators + Other option |

Every "Other" pick triggers a flag in Submission Readiness — meaning we pre-create that record before import.

## 6. The conversion pipeline

`intake_to_imports.py`:

```
intake_v5.xlsx
   │
   ├─→ Validation pass (vs live CRM picklist contract)
   │      └─→ validation_report.html
   │
   ├─→ Deduplication pass
   │      ├─→ unique Client Accounts (from Instructing Company)
   │      ├─→ unique Clients          (from Instructing Client + Firm)
   │      ├─→ unique Premises         (from Premises Name + Postcode)
   │      ├─→ unique Investigators    (from Investigator Assigned, excl blank/ON HOLD)
   │      └─→ unique Licence Checks   (1 per instruction with council fields populated)
   │
   ├─→ Name splitting (NEW)
   │      Full name → First_Name / Last_Name using:
   │        1. Lookup table for known dropdown clients (pre-split, covers 100%
   │           of current names since they're all clean two-word names)
   │        2. Whitespace split fallback for "Other" entries
   │        3. Manual-review flag for compound surnames (de la, van der, etc.)
   │
   ├─→ Fixed-value injection
   │      ├─ Pipeline = "Music"                     ← NEW: covers Deal mandatory
   │      ├─ Owner = "ID Inquiries Admin"
   │      ├─ Country = "United Kingdom"
   │      ├─ Industry = "Large Enterprise"
   │      ├─ Ownership = "Private"
   │      ├─ Premises Source / Instruction Source = "CRM"
   │      ├─ Premises Status = "Approved"
   │      └─ Rating = "Active"
   │
   ├─→ Stage mapping
   │      ├─ Status "On Hold"             → ON HOLD
   │      ├─ Status "Unallocated"          → COMPLETED CHECKS - READY FOR ALLOCATION
   │      ├─ Status "Ready for Allocation" → COMPLETED CHECKS - READY FOR ALLOCATION
   │      └─ Status "Allocated"            → COMPLETED CHECKS - READY FOR ALLOCATION
   │                                            (Investigator left blank — workaround handles)
   │
   └─→ Output (in CRM template format, pre-validated)
          ├─ 1_Client_Accounts.xlsx
          ├─ 2_Clients.xlsx
          ├─ 3_Investigators.xlsx
          ├─ 4_Premises.xlsx
          ├─ 5_Licence_Checks.xlsx
          ├─ 6_Instructions.xlsx
          └─ allocated_investigator_mapping.csv
```

## 7. The post-import workaround

`apply_allocated_workaround.py` — reads `allocated_investigator_mapping.csv`, finds each Instruction in CRM by Premises Name match, sets the Investigator lookup field, bumps stage from `COMPLETED CHECKS - READY FOR ALLOCATION` to `INSTRUCTION ALLOCATED`. Single API run, idempotent, logs every record updated.

## 8. Portal Users — the side ask

Separate `Portal Users` tab in the same v5 file:

| Column | Type |
|---|---|
| Client Name | Dropdown (from Clients list) |
| Firm | Auto-fill from Client |
| Email | Required free text |
| Phone | Optional |
| Activate Portal? | Yes / Defer |

Decouples "Alison still confirming portal users" from the main migration — instructions data ships first, portal users patched in later.

## 9. Communication plan with Alison (revised)

| Step | What | Format | When |
|---|---|---|---|
| **0** | **Pre-Fill Data Audit** — share field list, ask for additions | Short email or 15-min call | Before template ships |
| 1 | Apply audit feedback → finalise v5 → send template | Email + v5 file + 1-page how-to PDF | Day 0 |
| 2 | Optional 5-min walkthrough video | Loom — fill 1 row end-to-end | Day 0 |
| 3 | Handover call | Zoom 30-min — Q&A, watch her fill 2 rows | Day 0 / Day 1 |
| 4 | Daily check-in during fill | 1-line email/WhatsApp | Day 1–3 |
| 5 | "Submission Readiness = green, sending" | Alison emails the file | Day 3 |
| 6 | "Received, running validation" | Email | Day 4 |
| 7 | Validation report + import confirmation | Email | Day 4 |
| 8 | "Imported, please verify map pins" | Email + CRM access | Day 7 |
| 9 | Sign-off | Email | Day 12 |

## 10. Timeline

| Day | A2Z Cloud | ID Inquiries |
|---|---|---|
| –1 | Pre-Fill Data Audit ask | Audit reply |
| 0 | Send v5 template + handover call | — |
| 1–3 | On-call support | Fill template (~300 rows) |
| 4 | Receive + run validation | — |
| 5 | Run conversion script + diff review | — |
| 6 | Import 6 files in sequence | — |
| 7 | Apply allocated workaround | — |
| 8–10 | On-call support | Manual map-pin verification |
| 11 | Reconciliation pass | Data accuracy verification |
| 12 | Final sign-off | Sign-off |
| 13 | **Go-live** | **Go-live** |

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Alison overwrites a dropdown cell with raw text | Sheet protection + Submission Readiness flags it red |
| Lookup field mismatch ("Hamlins" vs "Hamlins LLP") | Conversion script does fuzzy match → raises manual-review item |
| Map pins all default to postcode centroids | Build a "premises pending verification" report in CRM |
| Alison runs out of time, sends partial file | v5 supports incremental: import what's done, top up later |
| New investigator/firm not in dropdown | "Other" pick → flagged in readiness → we pre-create the record |
| Date field typed as text | Cell format locked + readiness sheet flags non-date values |
| Compound surname not splitting cleanly | Conversion script flags for manual review rather than failing |
| Picklist drift between intake send and import day | Re-run picklist API extract on import day; regenerate dropdowns if changed |
| Alison has more data we didn't ask for | Pre-Fill Data Audit catches this before fill starts |
| Pipeline / other system-mandatory field not populated | Coverage matrix in §1 + conversion script enforces all mandatory fields |

## 12. Build queue

In order:

1. **Pre-Fill Data Audit doc / email** — 1-page field-list ask for Alison
2. **`4593_ID_Inquiries_Migration_Intake_v5.xlsx`** — upgraded template (locked picklists, conditional formatting, Submission Readiness dashboard, Portal Users tab, Cover + Guide)
3. **`intake_to_imports.py`** — Python conversion + validation pipeline (with Last_Name split + Pipeline injection)
4. **`apply_allocated_workaround.py`** — Zoho CRM API post-import workaround
5. **One-page intake how-to PDF** for Alison
6. **Email draft** to send Alison with the template attached
7. **Submission Readiness logic spec** — formulas/conditions in plain English for Buket/Navya review

---

*A2Z Cloud | Project #4593 — ID Inquiries Ltd | Confidential*
