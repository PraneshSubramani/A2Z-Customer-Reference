# ID Inquiries Ltd — Zoho Portal Project Documentation

**Document Type:** Enterprise Project Documentation  
**Version:** 1.0  
**Prepared By:** A2Z Cloud  
**Client:** ID Inquiries Ltd  
**Status:** UAT Phase  
**Last Updated:** April 2026

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Stakeholders](#2-stakeholders)
3. [System Architecture](#3-system-architecture)
4. [Zoho Products Used](#4-zoho-products-used)
5. [User Roles & Access Levels](#5-user-roles--access-levels)
6. [Core Modules](#6-core-modules)
7. [Instruction Lifecycle & Workflow](#7-instruction-lifecycle--workflow)
8. [On Hold Workflow](#8-on-hold-workflow)
9. [Invoicing & Payment Flow](#9-invoicing--payment-flow)
10. [Automation & Notifications](#10-automation--notifications)
11. [Reports](#11-reports)
12. [Data Migration Plan](#12-data-migration-plan)
13. [Known Issues & Resolutions](#13-known-issues--resolutions)
14. [Go-Live Plan](#14-go-live-plan)
15. [Post Go-Live](#15-post-go-live)

---

## 1. Project Overview

ID Inquiries Ltd is a Scottish legal investigation firm that conducts on-site visits to licensed premises (pubs, restaurants, venues) on behalf of lawyers and legal clients. Their core business involves:

- Receiving instructions from legal clients (lawyers/law firms)
- Performing licensing compliance site visits through field investigators
- Recording music track listings and other evidence during visits
- Generating legal reports and sending them to clients
- Invoicing clients and paying investigators

Prior to this project, all operations were managed manually via spreadsheets. The objective of this project is to fully digitise and automate this end-to-end process using the **Zoho ecosystem**, replacing the manual spreadsheet workflow with a structured, automated portal system.

---

## 2. Stakeholders

### Client — ID Inquiries Ltd

| Name | Role | Responsibility |
|------|------|----------------|
| Alison McInnes | Managing Director | Primary decision maker, overall system sign-off |
| John McGowan | Operations / Admin | Instruction management, investigator allocation, report review |
| Melissa Anderson | Finance | Invoicing, client billing, investigator payments |
| Gregory Duncan | Admin / ID Staff | Internal admin, UAT testing (used as test ID account) |
| Jackie Stevenson | Admin / ID Staff | Internal admin |
| Mathew MacMillan | Investigator | Field investigator, site visit reports |

### Investigators & Clients (Portal Users)
- **Investigators** — Field agents who carry out site visits and submit reports via the investigator portal
- **Clients** — Law firms / lawyers who instruct ID Inquiries to carry out site visits via the client portal

### A2Z Cloud Team

| Name | Role |
|------|------|
| Buket Stallard | Head of Operations / Project Manager |
| Sam (Pranesh) | Lead Developer |
| Navya R Nandi | Zoho Developer |
| Akanksha Anand | Zoho Consultant |

---

## 3. System Architecture

The system is built on two primary Zoho platforms working in tandem:

```
┌─────────────────────────────────────────────────────────┐
│                     ZOHO CRM                            │
│  - Internal user interface for ID Inquiries staff       │
│  - Instruction management                               │
│  - Investigator & Client account management             │
│  - Assignment Map widget                                │
│  - Reports & Dashboards                                 │
│  - Email notifications & workflow automations           │
└─────────────────┬───────────────────────────────────────┘
                  │
                  │ Sync / Integration
                  │
┌─────────────────▼───────────────────────────────────────┐
│                  ZOHO CREATOR                           │
│  - Client Portal (law firms submit instructions)        │
│  - Investigator Portal (field agents submit reports)    │
│  - Assignment Map (geographic investigator allocation)  │
│  - Site Visit forms                                     │
│  - Report generation                                    │
└─────────────────┬───────────────────────────────────────┘
                  │
                  │ File Storage
                  │
┌─────────────────▼───────────────────────────────────────┐
│                 ZOHO WORKDRIVE                          │
│  - Auto-created folders per instruction                 │
│  - Audio files, sketch plans, expense receipts          │
│  - Generated reports (Zoho Writer format)               │
│  - PDF reports for client delivery                      │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Zoho Products Used

| Product | Purpose |
|---------|---------|
| **Zoho CRM** | Core internal system — instructions, clients, investigators, workflows |
| **Zoho Creator** | Client portal, Investigator portal, Assignment Map, Visit forms |
| **Zoho WorkDrive** | File storage — audio files, reports, invoices |
| **Zoho Writer** | Report generation and editing |
| **Zoho Books** | Invoicing (planned integration for go-live) |

---

## 5. User Roles & Access Levels

### Internal Users (Zoho CRM Licensed Seats)

| Role | Access |
|------|--------|
| Admin (Alison, John) | Full access — all modules, reports, workflows |
| Finance (Melissa) | Invoicing module, payment reports |
| Admin Staff (Gregory, Jackie) | Instructions, reports |

### Portal Users (Zoho Creator Portal — Add-on Licences)

| Role | Portal | Access |
|------|--------|--------|
| Client (Law Firms) | Client Portal | Submit instructions, view reports, track status |
| Investigator | Investigator Portal | View assigned instructions, submit visit reports, upload files |

> **Licensing Note:** Internal ID Inquiries staff use standard Zoho CRM seats (14 licences confirmed). Investigators and Clients access the system as Zoho Creator portal users, which are covered under a separate portal user add-on licence.

---

## 6. Core Modules

### 6.1 Instructions (Deals Module — Zoho CRM)

The central module of the system. Each instruction represents a single site visit request from a legal client.

**Key Fields:**
- Premises Name & Full Address
- Postcode
- Client Account
- Assigned Investigator
- Instruction Stage (see Workflow section)
- Audio Files Available (checkbox)
- Initial Review Complete (checkbox)
- Site Visit Review Complete (checkbox)
- On Hold (stage)
- Client Reference

**Linked Records:**
- Premises
- Client Account
- Investigator
- Site Visit Records (Zoho Creator)
- WorkDrive Folder (auto-created)

---

### 6.2 Premises

Each premises is a unique record representing a licensed venue.

**Key Fields:**
- Premises Name
- Full Address
- Postcode
- Licensing Authority
- Map Coordinates (Latitude / Longitude — manually verified)

> **Note:** Map coordinates cannot be bulk imported. Each premises location must be manually verified post-migration to obtain accurate lat/long values for the Assignment Map.

---

### 6.3 Client Accounts

Represents the law firm or legal organisation instructing ID Inquiries.

**Key Fields:**
- Client Account Name
- Contact Details
- Client Rate (charge per hour — currently being reviewed for dynamic configuration)

---

### 6.4 Investigators

Field agents who carry out site visits.

**Key Fields:**
- Investigator Name
- Contact Details
- Investigator Rate (£ per hour — configurable per investigator in CRM)
- Assigned Instructions

> **Rate Note:** Investigator rate (£25/hr) and Client charge rate (£50/hr) are separate. The investigator rate is already configurable per record in CRM. Client rate dynamic configuration is pending confirmation from ID Inquiries on preferred setup.

---

### 6.5 Site Visit Records (Zoho Creator)

Created automatically when an instruction is allocated to an investigator. Linked to the instruction in CRM.

**Key Fields:**
- Site Visit Reference (auto-generated from premises name + postcode)
- Accepted Date & Time
- Accept Investigation (Yes/No)
- Visit Report Status (Draft / Visit Report Completed)
- Audio Files Upload
- Sketch Plan Upload
- Expense Receipts Upload
- Music Track Listings (time entries — 24-hour format in report)

---

## 7. Instruction Lifecycle & Workflow

### Stage Flow

```
OPEN
  │
  ▼
COMPUTER CHECKS / READY FOR ALLOCATION
  │
  │ (Investigator assigned via Assignment Map in Zoho Creator)
  ▼
INSTRUCTION ALLOCATED
  │
  │ (Investigator accepts via Investigator Portal)
  ▼
VISIT COMPLETE
  │
  ▼
AWAITING INITIAL REVIEW
  │ (Initial Review Complete checkbox ticked by John)
  ▼
AWAITING SITE VISIT REVIEW
  │
  ├──── Audio Files Available? ────YES────▶ AWAITING AUDIO FILES TO BE SENT
  │                                               │
  │                                               ▼
  │                                        AWAITING INVOICE
  │
  └──── Audio Files Available? ────NO─────▶ AWAITING INVOICE
                                                  │
                                                  ▼
                                           Melissa notified
                                           to send invoice
                                                  │
                                                  ▼
                                           REPORT COMPLETED
```

### Key Automation Triggers

| Trigger | Action |
|---------|--------|
| Investigator assigned via Map widget | Stage auto-updates to Instruction Allocated |
| Investigator accepts in portal | Accepted Date & Time recorded |
| Visit Report Completed button clicked | Record locked, downstream workflows triggered |
| Initial Review Complete checkbox ticked | Stage moves to Awaiting Site Visit Review |
| Audio Files checkbox ticked | Stage moves to Awaiting Audio Files to be Sent |
| Audio Files checkbox NOT ticked | Stage moves directly to Awaiting Invoice |
| Awaiting Invoice stage reached | Melissa notified via email to send invoice |

---

## 8. On Hold Workflow

### Overview

Instructions can be placed on hold at any stage. This is a common occurrence in the ID Inquiries business process.

### On Hold Behaviour

| Area | Behaviour |
|------|-----------|
| CRM Stage | Updates to **On Hold** |
| Client Portal | Now displays **On Hold** (previously showed "With ID" — fixed) |
| Assignment Map | Instruction **disappears** from the map |
| Investigator Portal — My Site Visits | On Hold instructions are **hidden** from the investigator |
| Email Notifications | No automated email sent when placed on hold |
| Zoho Creator Status | Updates to **With ID** (covers Open, Computer Checks, Ready for Allocation, On Hold stages) |

### Resuming from On Hold

```
Instruction On Hold
      │
      ▼
Move stage back to: CHECKS COMPLETED / READY FOR ALLOCATION
      │
      ▼
Go to Assignment Map in Zoho Creator
      │
      ▼
Assign Investigator (same or different)
      │
      ▼
Stage auto-updates to INSTRUCTION ALLOCATED
      │
      ▼
Normal flow resumes — investigator receives allocation email
```

> **Note:** The previous investigator assignment remains stored in the background when placed on hold. If reallocating to a different investigator, the old assignment should be manually cleared in CRM before reassigning via the map.

> **Pending Enhancement:** Currently all hold-related stages display as "With ID" in Zoho Creator. A separate "On Hold" column indicator is being considered to make this clearer for admin users.

---

## 9. Invoicing & Payment Flow

### Client Invoicing

- Triggered when instruction reaches **Awaiting Invoice** stage
- Melissa receives email notification
- Invoice raised via Zoho Books (integration planned for go-live)
- Client charge rate: **£50/hour** (dynamic rate configuration pending)

### Investigator Payments

- Investigator rate: **£25/hour** (configurable per investigator record in CRM)
- Monthly payment report available in CRM
- Report features:
  - Sort by any column (ascending/descending)
  - Export to Excel
  - Invoice Date filter (select date range for specific month/period)

---

## 10. Automation & Notifications

### Email Notifications

| Event | Recipient |
|-------|-----------|
| Instruction accepted by client | Client confirmation email |
| Instruction allocated to investigator | Investigator allocation email |
| Instruction resumed after On Hold | Investigator allocation email (re-sent) |
| Audio files sent to client | Melissa & Alison notified to raise invoice |
| Instruction reaches Awaiting Invoice (no audio) | Melissa notified to raise invoice |
| Proforma email to Licensing Authority | Full premises name + postcode included |

### WorkDrive Folder Automation

- A WorkDrive folder is automatically created for each instruction when the site visit record is generated
- Folder creation requires: Client Account + Client + Investigator records to exist before instruction is created
- If these records are missing, folder creation and all downstream automations will fail

> **Important:** After any data cleanup, Client Accounts, Client records, and Investigator records must be recreated before any new instructions are entered into the system.

---

## 11. Reports

### My Site Visits (Investigator Portal)

- Shows all instructions allocated to the logged-in investigator
- Filters out On Hold and completed instructions
- Columns include: Accepted Date & Time, Accept Investigation status

### All Org Instructions (CRM)

- Shows all instructions across the organisation (merged with My Instructions)
- Allows searching across all lawyers/clients including historical records
- Useful when lawyers change firms or departments

### Investigator Payment Report

- Monthly breakdown of investigator hours and charges
- Sortable by any column
- Exportable to Excel
- Filterable by invoice date range

---

## 12. Data Migration Plan

### Scope

ID Inquiries have confirmed they will only migrate **current active instructions** (not historical data).

**Estimated Volume:** 300–350 instructions

**Stages at migration:**
- Ready for Allocation
- Allocated to Investigator (requires workaround — see below)

### Modules to Migrate

| Module | Complexity | Notes |
|--------|-----------|-------|
| Client Accounts | Low | Must be imported first |
| Clients | Low | Depends on Client Accounts |
| Investigators | Low | Must be imported before instructions |
| Premises | Medium | Address required; lat/long must be verified manually post-import |
| Instructions | High | Depends on all above modules; WorkDrive folders auto-created on import |
| Licence Checks | Medium | Linked to Premises and Instructions |

### Migration Sequence

```
1. Client Accounts
      ↓
2. Clients
      ↓
3. Investigators
      ↓
4. Premises (address data — lat/long verified manually after)
      ↓
5. Licence Checks
      ↓
6. Instructions (Ready for Allocation stage)
      ↓
7. Instructions (Allocated to Investigator stage — workaround applied)
      ↓
8. Manual verification of premises map locations
      ↓
9. Sign-off & go-live
```

### Allocated to Investigator — Migration Workaround

Instructions already allocated to an investigator will not appear in the Assignment Map (by design). The migration approach for these records:

1. Import at "Allocated to Investigator" stage without investigator linked
2. Apply a one-off workaround to assign the investigator to these records
3. Verify the assignment and confirm normal flow continues

### Import File Rules

- One row per record per sheet
- Lookup fields must match exactly across sheets (e.g. Client Account Name)
- Dates in **YYYY-MM-DD** format
- Do not modify or delete column headers
- Delete sample rows before returning files

### Estimated Migration Timeline

| Task | Estimated Time |
|------|---------------|
| Data pre-processing & lookup field mapping | 0.5 days |
| Import & validation | 0.5 days |
| Premises lat/long manual verification | Variable (per record) |
| Post-migration testing | 0.5 days |
| **Total estimate** | **1–2 days** (excluding manual premises verification) |

---

## 13. Known Issues & Resolutions

| # | Issue | Status |
|---|-------|--------|
| 1 | WorkDrive error showing in Investigator portal | **Fixed** — error message hidden |
| 2 | Site Visit Reference blank in client portal | **Fixed** — auto-populated from premises name + postcode |
| 3 | Accepted Date & Time missing from My Site Visits report | **Fixed** — column added |
| 4 | Draft/Completed checkbox confusing for investigators | **Fixed** — replaced with Save as Draft and Visit Report Completed buttons |
| 5 | All Org Instructions not showing all records | **Fixed** — My Instructions merged into All Org Instructions |
| 6 | Melissa's invoice notification going to test Gmail | **Fixed** — updated to correct email address |
| 7 | Seconds showing in music track listing report | **Fixed** — seconds removed, hours and minutes only |
| 8 | Time format mismatch (12hr form vs 24hr report) | **Fixed** — report now correctly displays 24-hour format |
| 9 | Duplicate email sent when resuming from On Hold | **Fixed** |
| 10 | Client portal showing "With ID" instead of "On Hold" | **Fixed** — On Hold stage now displays correctly |
| 11 | On Hold instructions visible in Investigator portal | **Fixed** — hidden from My Site Visits when on hold |
| 12 | Proforma email to councils missing full address | **Fixed** — full address now included |
| 13 | Long reference number in licensing email | **Fixed** — replaced with postcode |
| 14 | Visit form answer sequence inconsistent | **Fixed** — sequence now consistent throughout |
| 15 | "Site Visit – Client Ref" field visible in Investigator portal | **Fixed** — field hidden (used internally for lookup only) |
| 16 | Client charge rate not dynamically configurable | **Pending** — awaiting confirmation from client on preferred setup |
| 17 | Sales Summary section in Instructions (CRM) | **Cannot fix** — default Zoho CRM Deals module section, not configurable |
| 18 | Portal button not visible outside Instructions tab | **Clarified** — portal button only available within Instructions tab by design |

---

## 14. Go-Live Plan

### Pre Go-Live Checklist

- [ ] All UAT feedback points resolved and signed off by Alison
- [ ] Live data import files completed by ID Inquiries
- [ ] Data pre-processed and imported by A2Z Cloud
- [ ] Premises map locations manually verified
- [ ] Post-migration data accuracy checked by ID Inquiries
- [ ] Email signatures collected and integrated into CRM email templates
- [ ] Zoho Books integration configured and tested
- [ ] Test client and test investigator accounts created (permanent)
- [ ] Training materials prepared for clients and investigators
- [ ] Outstanding invoice settled before final stages begin

### Go-Live Timeline (Provisional)

| Phase | Activity | Duration |
|-------|----------|----------|
| Pause Period | Clients instructed to pause new instructions | ~2 weeks |
| Data Freeze | ID Inquiries freeze spreadsheet updates | Day of migration |
| Data Migration | A2Z Cloud imports and validates all data | 1–2 days |
| Data Verification | ID Inquiries verify imported data accuracy | 2–3 days |
| Training | Client and investigator training sessions | TBC |
| Go-Live | System goes live | Target: Mid–Late April 2026 |

---

## 15. Post Go-Live

### Ongoing Considerations

- **Test Accounts:** A permanent test client and test investigator will be maintained on the system for training new clients and investigators
- **Zoho Books:** Full invoicing integration to be finalised post go-live if not completed before launch
- **On Hold Enhancement:** Adding a dedicated "On Hold" status indicator in Zoho Creator (currently shows as "With ID") — to be reviewed post go-live
- **Client Rate Configuration:** Dynamic client charge rate field to be added once ID Inquiries confirm their preferred setup
- **PDF Automation:** Automating the Writer-to-PDF conversion and WorkDrive upload (currently a manual step) — estimated ~20 hours of development work; estimate to be sent separately

### Support

All post go-live support requests should be raised through the A2Z Cloud support ticket system. Direct communication via WhatsApp or informal channels should be avoided to ensure all issues are properly tracked and resolved.

---

*Document prepared by A2Z Cloud — for internal and client reference purposes.*  
*All information based on UAT communications and development logs as of April 2026.*
