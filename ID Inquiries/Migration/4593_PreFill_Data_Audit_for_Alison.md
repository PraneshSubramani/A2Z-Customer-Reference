# Pre-Fill Data Audit — Email to Alison

**Project #4593 — ID Inquiries Ltd**
**From:** Sam, A2Z Cloud
**To:** Alison McInnes (cc: John McGowan, Buket Stallard)
**Subject:** ID Inquiries Migration — Quick Field Check Before You Start Filling

---

## Email body (copy-paste ready)

Hi Alison,

Quick one before we send over the data collection template for you to fill.

We've put together a single, hardened Excel template (one row per active instruction) so you only need to fill data in one place — we then split it across the six CRM import files on our side. Before you start, we want to make sure we're capturing **every** piece of information you actually have on each instruction, not just what was in the test extract.

Some of the fields below were missing from the sample extract but you may already keep them in your spreadsheets or notes. **If you have any of these, tell us now and we'll add a column to the template before you start filling.** Far cheaper to add a column upfront than to chase missing data after import.

Could you have a look at the table below and reply with one of:

- **YES, I have this** (and we'll add the column)
- **NO, I don't track this** (we'll skip it)
- **SOMETIMES** (we'll add the column — fill where you can, leave blank otherwise)

You can just reply inline next to each row. Should take 5–10 minutes.

---

### Field check — what could you give us per record?

| # | Module | Candidate field | What it means / sample value | YES / NO / SOMETIMES |
|---|---|---|---|---|
| **Client Accounts (law firms)** | | | | |
| 1 | Client Account | Phone (main switchboard) | e.g. 0207 355 6000 | |
| 2 | Client Account | Billing address | Street + city + postcode for the firm itself | |
| 3 | Client Account | Website | e.g. hamlins.com | |
| **Clients (individual lawyers)** | | | | |
| 4 | Client | Email address | Their direct email (needed for portal access anyway) | |
| 5 | Client | Mobile / direct line | Optional but useful for urgent contact | |
| 6 | Client | Salutation / title | Mr / Mrs / Ms / Dr | |
| 7 | Client | Role / job title | e.g. "Partner", "Associate", "Solicitor" | |
| **Investigators** | | | | |
| 8 | Investigator | Skillsets | What each investigator is qualified for (note: this picklist needs configuring on our side regardless) | |
| 9 | Investigator | Languages spoken | Where relevant for non-English-speaking premises | |
| 10 | Investigator | Equipment available | e.g. recording equipment, dashcam, etc. | |
| 11 | Investigator | Non-default rates | Anyone on a rate other than £25/hr (we already have Mathew at £20/hr) | |
| **Premises** | | | | |
| 12 | Premises | Address Line 2 | Sub-building, unit, floor — where applicable | |
| 13 | Premises | Capacity | Max occupancy if you record this | |
| 14 | Premises | Licence type | Specific licence category beyond the licensing authority | |
| 15 | Premises | Opening hours | When the venue is open (helps investigators plan visits) | |
| 16 | Premises | Special access notes | e.g. "ring buzzer at side door", "no parking", "dress code" | |
| **Instructions** | | | | |
| 17 | Instruction | Priority Level | High / Normal / Specific Date — drives investigator scheduling | |
| 18 | Instruction | Specific Date | Where a visit must happen on a particular date/event | |
| 19 | Instruction | Instructions to Investigator | Anything you'd brief the investigator on before they go | |
| 20 | Instruction | Expected duration | How long the visit typically takes | |
| **Licence Checks** | | | | |
| 21 | Licence Check | Date information received | When the council came back with details | |
| 22 | Licence Check | Council reference number | Their internal ref for the check | |
| 23 | Licence Check | Specific check type | If you categorise checks beyond the request method | |

---

If there's anything else you keep on each instruction that isn't on this list — even something we'd never have thought to ask for — flag it and we'll add it. The whole point of this audit is to capture once, not chase twice.

Once we've got your replies we'll finalise the template (we're calling it v5) and send it through with a short walkthrough video. We're aiming to get it in your hands within 24 hours of your reply.

Any questions, give me a shout.

Kind regards,

Sam
A2Z Cloud — Zoho Development Team
Project #4593 — ID Inquiries Ltd

---

## Internal notes (not part of email)

**Why we're sending this audit before v5 ships**

- Avoids a v5.1 / v5.2 / v5.3 ladder where Alison fills 100 rows and we then ask her to add a column
- Surfaces the Skillset picklist conversation up front (we need to configure it CRM-side regardless)
- Gives Alison a chance to scope-check her own data quality before she starts filling
- Shows we're capturing everything she has, not arbitrarily limiting to the extract format

**Expected outcomes**

- Most likely YES: client emails (already known requirement), special access notes, instructions to investigator
- Most likely NO: capacity, opening hours, licence type, expected duration
- Most likely SOMETIMES: priority level, specific date, council reference number, non-default rates

**Action on receipt of her reply**

- Add a column to v5 for every YES / SOMETIMES
- Mark each new column as Optional in the Submission Readiness logic (don't hard-stop on data she's only sometimes got)
- Update the conversion script to handle the new columns
- Update the data mapping guide accordingly

**Turnaround target**

- Send audit: today
- Reply received: T+1 (Alison + John 15-min discussion)
- v5 template finalised and sent: T+2

---

*A2Z Cloud | Project #4593 — ID Inquiries Ltd | Confidential*
