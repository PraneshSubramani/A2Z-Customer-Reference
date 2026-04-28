"""
Build the ID Inquiries Migration Intake Template v5.

Outputs: 4593_ID_Inquiries_Migration_Intake_v5.xlsx

Sheets (in order):
  1. Instructions          - main data entry (22 cols + 2 diagnostic, 400 rows)
  2. Client Accounts       - reference: pre-populated from CRM import files
  3. Clients               - reference: pre-populated
  4. Investigators         - reference: pre-populated
  5. Portal Users          - separate intake for portal user emails
  6. Submission Readiness  - live dashboard with READY TO SEND indicator
  7. Picklists             - hidden, drives the Instructions dropdowns
"""

import os
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

# ============================================================
#   PATHS — discover CRM import data directory
# ============================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CRM_DATA_DIR_CANDIDATES = [
    os.path.join(SCRIPT_DIR, "..", "CRM import data files"),
    "/tmp/A2Z-Customer-Reference/ID Inquiries/Migration/CRM import data files",
]
CRM_DATA_DIR = next((d for d in CRM_DATA_DIR_CANDIDATES if os.path.exists(d)), None)
if CRM_DATA_DIR is None:
    raise FileNotFoundError(
        f"CRM import data files not found; tried: {CRM_DATA_DIR_CANDIDATES}"
    )

# ============================================================
#   LOAD EXISTING CRM IMPORT DATA
# ============================================================

def load_crm_data():
    """Load Client Accounts, Clients, Investigators from existing import files."""

    def _read_sheet(filename):
        path = os.path.join(CRM_DATA_DIR, filename)
        wb = load_workbook(path, data_only=True)
        ws = wb[wb.sheetnames[0]]
        rows = list(ws.iter_rows(values_only=True))
        header = [c if c is not None else "" for c in rows[0]]
        # strip trailing empty header columns
        while header and header[-1] == "":
            header.pop()
        # only keep rows where the first column is non-empty
        data = []
        for r in rows[1:]:
            if r[0] is None or str(r[0]).strip() == "":
                continue
            data.append(tuple(r[i] if i < len(r) else None for i in range(len(header))))
        return header, data

    accounts_header, accounts_data = _read_sheet("Client_Accounts.xlsx")
    clients_header, clients_data = _read_sheet("Clients.xlsx")
    investigators_header, investigators_data = _read_sheet("Investigators.xlsx")
    return {
        "accounts": (accounts_header, accounts_data),
        "clients": (clients_header, clients_data),
        "investigators": (investigators_header, investigators_data),
    }


CRM_DATA = load_crm_data()

# ============================================================
#   DERIVE PICKLISTS FROM LIVE DATA
# ============================================================

# Firms — unique Client Account Names from the Client_Accounts sheet,
# excluding test accounts. + "Other – advise A2Z Cloud" sentinel.
_real_firms = [
    row[2] for row in CRM_DATA["accounts"][1]
    if row[2] and not str(row[2]).lower().startswith("test client")
]
FIRMS = list(dict.fromkeys(_real_firms)) + ["Other – advise A2Z Cloud"]

# Clients — "{Client Name} ({Firm})" formatted, excluding test accounts.
_real_clients = [
    f"{row[0]} ({row[1]})" for row in CRM_DATA["clients"][1]
    if row[0] and row[1] and not str(row[1]).lower().startswith("test client")
]
CLIENTS = list(dict.fromkeys(_real_clients)) + ["Other – advise A2Z Cloud"]

# Investigators — names from the Investigators sheet.
_real_investigators = [row[0] for row in CRM_DATA["investigators"][1] if row[0]]
INVESTIGATORS = list(dict.fromkeys(_real_investigators)) + ["Other – advise A2Z Cloud"]

# Static picklists — sourced from picklist_report.json
INSTRUCTION_STATUS = ["On Hold", "Unallocated", "Ready for Allocation", "Allocated"]
INSTRUCTION_TYPE = [
    "Pub/Bar – background", "Pub/Bar – event", "Restaurant//Café", "Cafe",
    "Nightclub", "Stripclub", "Gentleman's Club", "Shop",
    "Shop – High Street", "Shop – Warehouse/Industrial", "Beauty Salon",
    "Barber (Gents)", "Hairdresser", "Nail Salon", "Tattoo Parlour", "Gym",
    "Hotel – Bedroom", "Hotel – Common Areas", "Festival", "Other",
]
YES_NO = ["Yes", "No"]
COUNCIL_METHOD = ["Public Register Online", "Email", "Form Submitted"]
COUNCIL_RESPONSE = ["Yes", "No", "Awaiting Response"]
ACTIVATE_PORTAL = ["Yes", "Defer"]

# ============================================================
#   STYLES
# ============================================================

NAVY = "1F3864"
LIGHT_NAVY = "2E5395"
ACCENT = "C00000"
SOFT_RED = "FCE4E4"
SOFT_AMBER = "FFF2CC"
SOFT_GREEN = "E2EFDA"
HEADER_GREY = "F2F2F2"
EXAMPLE_BLUE = "DDEBF7"
PREFILL_BLUE = "EAF1FA"
WHITE = "FFFFFF"

font_section = Font(name="Calibri", size=14, bold=True, color=NAVY)
font_header = Font(name="Calibri", size=11, bold=True, color=WHITE)
font_subheader = Font(name="Calibri", size=10, bold=True, color=NAVY)
font_required = Font(name="Calibri", size=11, bold=True, color=ACCENT)
font_body = Font(name="Calibri", size=11)
font_body_bold = Font(name="Calibri", size=11, bold=True)
font_descr = Font(name="Calibri", size=9, italic=True, color="595959")
font_example = Font(name="Calibri", size=10, color="305496")
font_diag = Font(name="Calibri", size=10, italic=True, color="595959")
font_big = Font(name="Calibri", size=20, bold=True, color=WHITE)
font_prefill = Font(name="Calibri", size=10, color="1F3864")

fill_subheader = PatternFill("solid", fgColor=HEADER_GREY)
fill_example = PatternFill("solid", fgColor=EXAMPLE_BLUE)
fill_amber = PatternFill("solid", fgColor=SOFT_AMBER)
fill_green = PatternFill("solid", fgColor=SOFT_GREEN)
fill_red = PatternFill("solid", fgColor=SOFT_RED)
fill_navy = PatternFill("solid", fgColor=NAVY)
fill_prefill = PatternFill("solid", fgColor=PREFILL_BLUE)

thin = Side(border_style="thin", color="BFBFBF")
thick = Side(border_style="medium", color=NAVY)
border_all = Border(left=thin, right=thin, top=thin, bottom=thin)
border_header = Border(left=thin, right=thin, top=thick, bottom=thick)

align_centre = Alignment(horizontal="center", vertical="center", wrap_text=True)
align_left = Alignment(horizontal="left", vertical="center", wrap_text=True)
align_left_top = Alignment(horizontal="left", vertical="top", wrap_text=True)


# ============================================================
#   COLUMN SCHEMA — Instructions sheet
# ============================================================

COLUMNS = [
    # PREMISES (A-H)
    ("A", "PREMISES",     "Premises Name",            True,  "Name of the licensed venue exactly as on the licence.", None, 28),
    ("B", "PREMISES",     "Street Address",           True,  "Full street address.", None, 30),
    ("C", "PREMISES",     "City",                     True,  "Town or city.", None, 16),
    ("D", "PREMISES",     "County",                   False, "County (optional).", None, 16),
    ("E", "PREMISES",     "Postcode",                 True,  "Full UK postcode.", None, 11),
    ("F", "PREMISES",     "Licensing Authority",      True,  "Council that issued the licence.", None, 26),
    ("G", "PREMISES",     "Premises Licence Holder",  False, "Legal entity holding the premises licence.", None, 24),
    ("H", "PREMISES",     "DPS",                      False, "Designated Premises Supervisor full name.", None, 22),
    # INSTRUCTION (I-P)
    ("I", "INSTRUCTION",  "Instruction Status",       True,  "Current status of this instruction.", "InstructionStatus", 18),
    ("J", "INSTRUCTION",  "Instructing Company",      True,  "Law firm.", "Firms", 22),
    ("K", "INSTRUCTION",  "Instructing Client",       True,  "Individual lawyer (firm in brackets).", "Clients", 28),
    ("L", "INSTRUCTION",  "Client Ref",               False, "Client's own reference number.", None, 18),
    ("M", "INSTRUCTION",  "Date of Instruction",      True,  "DD/MM/YYYY.", None, 14),
    ("N", "INSTRUCTION",  "Instruction Type",         True,  "Venue type.", "InstructionType", 22),
    ("O", "INSTRUCTION",  "Is Reinstruction?",        True,  "Repeat visit to same premises?", "YesNo", 12),
    ("P", "INSTRUCTION",  "Instruction Notes",        False, "Special instructions for the investigator.", None, 36),
    # INVESTIGATOR (Q-R)
    ("Q", "INVESTIGATOR", "Investigator Assigned",    False, "Required IF Status = Allocated.", "Investigators", 22),
    ("R", "INVESTIGATOR", "Date Assigned",            False, "Required IF Status = Allocated. DD/MM/YYYY.", None, 14),
    # LICENCE CHECK (S-V)
    ("S", "LICENCE CHECK","Council Request Method",   False, "How licence details were requested.", "CouncilMethod", 22),
    ("T", "LICENCE CHECK","Council Request Date",     False, "Date council was contacted. DD/MM/YYYY.", None, 14),
    ("U", "LICENCE CHECK","Council Response?",        False, "Has the council responded?", "CouncilResponse", 18),
    ("V", "LICENCE CHECK","Licence Check Notes",      False, "Required IF Council Response = Yes.", None, 36),
    # DIAGNOSTICS (W-X)
    ("W", "DIAGNOSTICS",  "Row Status",               False, "Auto-calculated.", None, 14),
    ("X", "DIAGNOSTICS",  "Missing Fields",           False, "Auto-calculated.", None, 40),
]

SECTION_COLOURS = {
    "PREMISES":      "1F3864",
    "INSTRUCTION":   "2E5395",
    "INVESTIGATOR":  "548235",
    "LICENCE CHECK": "BF8F00",
    "DIAGNOSTICS":   "595959",
}

DATA_FIRST_ROW = 6
DATA_LAST_ROW = 405
EXAMPLE_ROW = 4

EXAMPLE_VALUES = {
    "A": "The Swan Inn", "B": "14 Greengate Street", "C": "Stafford",
    "D": "Staffordshire", "E": "ST16 3RW", "F": "Staffordshire County Council",
    "G": "Trust Inns Ltd", "H": "Edward Paul Bolton",
    "I": "On Hold", "J": "Hamlins LLP", "K": "Michael Green (Hamlins LLP)",
    "L": "591/PPLPRS1734", "M": "02/05/2024", "N": "Pub/Bar – background",
    "O": "No", "P": "Confirm Licensee and DPS. Attempt to obtain bank details.",
    "Q": "Gary Hall", "R": "16/05/2024",
    "S": "Public Register Online", "T": "07/05/2024", "U": "Yes",
    "V": "Email from Michael asking to put on hold — linked premises found.",
}


# ============================================================
#   HELPERS
# ============================================================

def unlock(cell):
    cell.protection = Protection(locked=False)


def set_widths(ws, widths):
    for col_idx, width in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(col_idx)].width = width


# ============================================================
#   SHEETS
# ============================================================

def build_picklists(wb):
    ws = wb.create_sheet("Picklists")
    ws.sheet_state = "hidden"

    columns = [
        ("Firms",             FIRMS),
        ("Clients",           CLIENTS),
        ("Investigators",     INVESTIGATORS),
        ("InstructionStatus", INSTRUCTION_STATUS),
        ("InstructionType",   INSTRUCTION_TYPE),
        ("YesNo",             YES_NO),
        ("CouncilMethod",     COUNCIL_METHOD),
        ("CouncilResponse",   COUNCIL_RESPONSE),
        ("ActivatePortal",    ACTIVATE_PORTAL),
    ]
    for idx, (name, values) in enumerate(columns, start=1):
        col = get_column_letter(idx)
        ws[f"{col}1"] = name
        ws[f"{col}1"].font = font_subheader
        ws[f"{col}1"].fill = fill_subheader
        for row, v in enumerate(values, start=2):
            ws[f"{col}{row}"] = v
        ws.column_dimensions[col].width = max(
            len(name), max((len(str(v)) for v in values), default=10)
        ) + 2
        last_row = 1 + len(values)
        ref = f"Picklists!${col}$2:${col}${last_row}"
        wb.defined_names[name] = DefinedName(name=name, attr_text=ref)

    ws.protection.sheet = True
    return ws


def build_instructions(wb):
    ws = wb.create_sheet("Instructions")
    ws.sheet_view.showGridLines = False

    # Row 1: section bands
    sections_grouped = []
    last_section = None
    start = None
    prev_col = None
    for col_letter, section, *_ in COLUMNS:
        if section != last_section:
            if last_section is not None:
                sections_grouped.append((last_section, start, prev_col))
            last_section = section
            start = col_letter
        prev_col = col_letter
    sections_grouped.append((last_section, start, prev_col))

    for section, c0, c1 in sections_grouped:
        ws.merge_cells(f"{c0}1:{c1}1")
        cell = ws[f"{c0}1"]
        cell.value = section
        cell.font = font_header
        cell.fill = PatternFill("solid", fgColor=SECTION_COLOURS[section])
        cell.alignment = align_centre
        cell.border = border_header
    ws.row_dimensions[1].height = 24

    # Row 2: column headers
    for col_letter, _, header, required, _, _, width in COLUMNS:
        cell = ws[f"{col_letter}2"]
        cell.value = f"{header} *" if required else header
        cell.font = font_required if required else font_subheader
        cell.fill = fill_subheader
        cell.alignment = align_centre
        cell.border = border_all
        ws.column_dimensions[col_letter].width = width
    ws.row_dimensions[2].height = 32

    # Row 3: descriptions
    for col_letter, _, _, _, descr, _, _ in COLUMNS:
        cell = ws[f"{col_letter}3"]
        cell.value = descr
        cell.font = font_descr
        cell.alignment = align_left_top
        cell.border = border_all
    ws.row_dimensions[3].height = 50

    # Row 4: example
    for col_letter, *_ in COLUMNS:
        cell = ws[f"{col_letter}{EXAMPLE_ROW}"]
        cell.value = EXAMPLE_VALUES.get(col_letter, "")
        cell.font = font_example
        cell.fill = fill_example
        cell.alignment = align_left
        cell.border = border_all
    ws.row_dimensions[EXAMPLE_ROW].height = 20

    # Row 5: hint
    ws.merge_cells("A5:V5")
    hint = ws["A5"]
    hint.value = (
        "▶  Row 4 is an EXAMPLE — leave it as a reference. "
        "Start filling your real data from row 6 below."
    )
    hint.font = font_descr
    hint.fill = fill_amber
    hint.alignment = align_centre
    ws.row_dimensions[5].height = 22

    # Diagnostic formulas in W and X
    for r in range(DATA_FIRST_ROW, DATA_LAST_ROW + 1):
        cond_parts = [f'A{r}=""']
        for c in ["B", "C", "E", "F", "I", "J", "K", "M", "N", "O"]:
            cond_parts.append(f'{c}{r}=""')
        cond_parts.append(f'AND(I{r}="Allocated",OR(Q{r}="",R{r}=""))')
        cond_parts.append(f'AND(U{r}="Yes",V{r}="")')
        condition = "OR(" + ",".join(cond_parts) + ')'
        ws[f"W{r}"] = (
            f'=IF(A{r}="","",IF({condition},"Incomplete","Ready"))'
        )
        ws[f"W{r}"].font = font_diag
        ws[f"W{r}"].alignment = align_centre

        labels = {
            "B": "Street Address", "C": "City", "E": "Postcode",
            "F": "Licensing Authority", "I": "Status", "J": "Firm",
            "K": "Client", "M": "Date of Instruction", "N": "Instruction Type",
            "O": "Reinstruction",
        }
        miss_parts = [f'IF({c}{r}="",", {l}","")' for c, l in labels.items()]
        miss_parts.append(
            f'IF(AND(I{r}="Allocated",Q{r}=""),", Investigator","")'
        )
        miss_parts.append(
            f'IF(AND(I{r}="Allocated",R{r}=""),", Date Assigned","")'
        )
        miss_parts.append(
            f'IF(AND(U{r}="Yes",V{r}=""),", Licence Check Notes","")'
        )
        concat = "&".join(miss_parts)
        ws[f"X{r}"] = (
            f'=IF(W{r}<>"Incomplete","",SUBSTITUTE({concat},", ","",1))'
        )
        ws[f"X{r}"].font = font_diag
        ws[f"X{r}"].alignment = align_left

    # Unlock data entry cells
    for r in range(DATA_FIRST_ROW, DATA_LAST_ROW + 1):
        for col_letter in [c for c, *_ in COLUMNS if c not in ("W", "X")]:
            unlock(ws[f"{col_letter}{r}"])

    # Data validations
    for col_letter, _, _, _, _, picklist, _ in COLUMNS:
        if picklist is None:
            continue
        dv = DataValidation(
            type="list",
            formula1=f"={picklist}",
            allow_blank=True,
            showErrorMessage=True,
            errorTitle="Invalid value",
            error="Pick from the dropdown list.",
        )
        ws.add_data_validation(dv)
        dv.add(f"{col_letter}{DATA_FIRST_ROW}:{col_letter}{DATA_LAST_ROW}")

    # Date validations on M, R, T
    for col in ["M", "R", "T"]:
        dv = DataValidation(
            type="date",
            allow_blank=True,
            showErrorMessage=True,
            errorTitle="Date format",
            error="Please enter a valid date in DD/MM/YYYY format.",
        )
        ws.add_data_validation(dv)
        dv.add(f"{col}{DATA_FIRST_ROW}:{col}{DATA_LAST_ROW}")

    # Conditional formatting
    REQUIRED_COLS_INC_FIRST = ["A", "B", "C", "E", "F", "I", "J", "K", "M", "N", "O"]
    for col in REQUIRED_COLS_INC_FIRST:
        rule = FormulaRule(
            formula=[
                f'AND(${col}{DATA_FIRST_ROW}="",$A{DATA_FIRST_ROW}<>"",ROW()>={DATA_FIRST_ROW})'
            ],
            stopIfTrue=False, fill=fill_red,
        )
        ws.conditional_formatting.add(
            f"{col}{DATA_FIRST_ROW}:{col}{DATA_LAST_ROW}", rule
        )

    for col in ["Q", "R"]:
        rule = FormulaRule(
            formula=[f'AND(${col}{DATA_FIRST_ROW}="",$I{DATA_FIRST_ROW}="Allocated")'],
            stopIfTrue=False, fill=fill_red,
        )
        ws.conditional_formatting.add(
            f"{col}{DATA_FIRST_ROW}:{col}{DATA_LAST_ROW}", rule
        )

    rule = FormulaRule(
        formula=[f'AND($V{DATA_FIRST_ROW}="",$U{DATA_FIRST_ROW}="Yes")'],
        stopIfTrue=False, fill=fill_red,
    )
    ws.conditional_formatting.add(
        f"V{DATA_FIRST_ROW}:V{DATA_LAST_ROW}", rule
    )

    rule_ready = FormulaRule(
        formula=[f'$W{DATA_FIRST_ROW}="Ready"'], stopIfTrue=False, fill=fill_green,
    )
    rule_inc = FormulaRule(
        formula=[f'$W{DATA_FIRST_ROW}="Incomplete"'], stopIfTrue=False, fill=fill_amber,
    )
    ws.conditional_formatting.add(
        f"W{DATA_FIRST_ROW}:W{DATA_LAST_ROW}", rule_ready
    )
    ws.conditional_formatting.add(
        f"W{DATA_FIRST_ROW}:W{DATA_LAST_ROW}", rule_inc
    )

    for col in ["J", "K", "Q"]:
        rule_other = FormulaRule(
            formula=[f'${col}{DATA_FIRST_ROW}="Other – advise A2Z Cloud"'],
            stopIfTrue=False, fill=fill_amber,
        )
        ws.conditional_formatting.add(
            f"{col}{DATA_FIRST_ROW}:{col}{DATA_LAST_ROW}", rule_other,
        )

    ws.freeze_panes = "B6"
    ws.protection.sheet = True
    ws.protection.formatColumns = False
    ws.protection.formatRows = False
    return ws


def _build_reference_sheet(wb, sheet_name, header, data, widths, intro_text):
    """Generic builder for the 3 reference sheets (Client Accounts, Clients, Investigators)."""
    ws = wb.create_sheet(sheet_name)
    ws.sheet_view.showGridLines = False

    # Row 1: title banner
    last_col = get_column_letter(len(header))
    ws.merge_cells(f"A1:{last_col}1")
    ws["A1"] = intro_text
    ws["A1"].font = font_header
    ws["A1"].fill = fill_navy
    ws["A1"].alignment = align_centre
    ws.row_dimensions[1].height = 28

    # Row 2: column headers
    for col_idx, h in enumerate(header, start=1):
        cell = ws.cell(row=2, column=col_idx, value=h)
        cell.font = font_subheader
        cell.fill = fill_subheader
        cell.alignment = align_centre
        cell.border = border_all
    ws.row_dimensions[2].height = 26

    # Apply column widths
    set_widths(ws, widths)

    # Pre-populated data starts at row 3 — light-blue tint to indicate
    # "already in CRM, edit only if outdated".
    for row_offset, row_data in enumerate(data, start=3):
        for col_idx, val in enumerate(row_data, start=1):
            cell = ws.cell(row=row_offset, column=col_idx, value=val)
            cell.font = font_prefill
            cell.fill = fill_prefill
            cell.alignment = align_left
            cell.border = border_all
            unlock(cell)
        ws.row_dimensions[row_offset].height = 20

    # Empty rows below — for new entries Alison wants to add.
    empty_first = 3 + len(data)
    empty_last = empty_first + 50
    for r in range(empty_first, empty_last + 1):
        for col_idx in range(1, len(header) + 1):
            cell = ws.cell(row=r, column=col_idx)
            cell.font = font_body
            cell.alignment = align_left
            cell.border = border_all
            unlock(cell)
        ws.row_dimensions[r].height = 18

    ws.freeze_panes = "A3"
    ws.protection.sheet = True
    ws.protection.formatColumns = False
    ws.protection.formatRows = False
    return ws


def build_client_accounts(wb):
    header, data = CRM_DATA["accounts"]
    widths = [22, 12, 24, 16, 22, 22, 14, 18, 14, 18, 26, 16, 14, 14, 16, 18, 18]
    widths = (widths + [14] * 30)[: len(header)]
    return _build_reference_sheet(
        wb, "Client Accounts", header, data, widths,
        "Client Accounts — law firms already imported into CRM. Edit only if details are outdated. Add new firms in the empty rows below."
    )


def build_clients(wb):
    header, data = CRM_DATA["clients"]
    widths = [22, 22, 32, 16]
    widths = (widths + [14] * 10)[: len(header)]
    return _build_reference_sheet(
        wb, "Clients", header, data, widths,
        "Clients — individual lawyers already imported into CRM. Edit only if details are outdated. Add new clients in the empty rows below."
    )


def build_investigators(wb):
    header, data = CRM_DATA["investigators"]
    widths = [22, 28, 18, 22, 14, 12, 28, 24, 22, 28, 12, 12]
    widths = (widths + [14] * 10)[: len(header)]
    return _build_reference_sheet(
        wb, "Investigators", header, data, widths,
        "Investigators — field investigators already imported into CRM. Edit only if details are outdated. Add new investigators in the empty rows below."
    )


def build_portal_users(wb):
    ws = wb.create_sheet("Portal Users")
    ws.sheet_view.showGridLines = False

    ws.merge_cells("A1:E1")
    ws["A1"] = "Portal Users — clients who need login access to submit instructions"
    ws["A1"].font = font_header
    ws["A1"].fill = fill_navy
    ws["A1"].alignment = align_centre
    ws.row_dimensions[1].height = 26

    headers = [
        ("A", "Client Name", 32, "Clients"),
        ("B", "Firm", 24, None),
        ("C", "Email", 30, None),
        ("D", "Phone", 18, None),
        ("E", "Activate Portal?", 16, "ActivatePortal"),
    ]
    for col, h, w, _ in headers:
        cell = ws[f"{col}2"]
        cell.value = f"{h} *" if h in ("Client Name", "Email") else h
        cell.font = font_required if h in ("Client Name", "Email") else font_subheader
        cell.fill = fill_subheader
        cell.alignment = align_centre
        cell.border = border_all
        ws.column_dimensions[col].width = w
    ws.row_dimensions[2].height = 26

    descrs = {
        "A": "Pick from dropdown.",
        "B": "Auto-fill — leave blank.",
        "C": "REQUIRED. Direct email.",
        "D": "Optional.",
        "E": "Yes = activate now. Defer = set up later.",
    }
    for col, txt in descrs.items():
        cell = ws[f"{col}3"]
        cell.value = txt
        cell.font = font_descr
        cell.alignment = align_left_top
        cell.border = border_all
    ws.row_dimensions[3].height = 32

    portal_first, portal_last = 4, 53
    for r in range(portal_first, portal_last + 1):
        for col, _, _, _ in headers:
            unlock(ws[f"{col}{r}"])

    dv_clients = DataValidation(type="list", formula1="=Clients", allow_blank=True)
    ws.add_data_validation(dv_clients)
    dv_clients.add(f"A{portal_first}:A{portal_last}")

    dv_act = DataValidation(type="list", formula1="=ActivatePortal", allow_blank=True)
    ws.add_data_validation(dv_act)
    dv_act.add(f"E{portal_first}:E{portal_last}")

    ws.freeze_panes = "A4"
    ws.protection.sheet = True
    return ws


def build_readiness(wb):
    ws = wb.create_sheet("Submission Readiness")
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 4
    ws.column_dimensions["B"].width = 42
    ws.column_dimensions["C"].width = 14
    ws.column_dimensions["D"].width = 60

    ws.merge_cells("B2:D2")
    ws["B2"] = (
        '=IF(AND(C5>0,C7=0),'
        '"READY TO SEND ✓  —  Email this file back to A2Z Cloud",'
        '"NOT READY  ×  —  Fix the issues below before sending")'
    )
    ws["B2"].font = font_big
    ws["B2"].alignment = align_centre
    ws.row_dimensions[2].height = 50

    rule_green_banner = FormulaRule(
        formula=['AND(C5>0,C7=0)'], stopIfTrue=False, fill=fill_navy,
    )
    rule_red_banner = FormulaRule(
        formula=['NOT(AND(C5>0,C7=0))'], stopIfTrue=False,
        fill=PatternFill("solid", fgColor=ACCENT),
    )
    ws.conditional_formatting.add("B2:D2", rule_green_banner)
    ws.conditional_formatting.add("B2:D2", rule_red_banner)

    ws["B4"] = "Headline counts"
    ws["B4"].font = font_section

    counts = [
        ("Total rows entered",
         '=COUNTA(Instructions!A6:A405)'),
        ("Rows fully valid (Ready)",
         '=COUNTIF(Instructions!W6:W405,"Ready")'),
        ("Rows incomplete",
         '=COUNTIF(Instructions!W6:W405,"Incomplete")'),
    ]
    for i, (label, formula) in enumerate(counts):
        r = 5 + i
        ws[f"B{r}"] = label
        ws[f"B{r}"].font = font_body
        ws[f"C{r}"] = formula
        ws[f"C{r}"].font = font_body_bold
        ws[f"C{r}"].alignment = align_centre
        ws[f"B{r}"].border = border_all
        ws[f"C{r}"].border = border_all
        ws.row_dimensions[r].height = 22

    ws["B9"] = "Issue breakdown"
    ws["B9"].font = font_section

    headers_dash = ["Issue", "Count", "First example row"]
    for i, h in enumerate(headers_dash):
        cell = ws.cell(row=10, column=2 + i, value=h)
        cell.font = font_header
        cell.fill = fill_navy
        cell.alignment = align_centre
        cell.border = border_all
    ws.row_dimensions[10].height = 22

    issues = [
        ("Missing Street Address",
         '=SUMPRODUCT((Instructions!A6:A405<>"")*(Instructions!B6:B405=""))',
         '=IFERROR(MATCH(1,(Instructions!A6:A405<>"")*(Instructions!B6:B405=""),0)+5,"—")'),
        ("Missing Licensing Authority",
         '=SUMPRODUCT((Instructions!A6:A405<>"")*(Instructions!F6:F405=""))',
         '=IFERROR(MATCH(1,(Instructions!A6:A405<>"")*(Instructions!F6:F405=""),0)+5,"—")'),
        ("Missing Postcode",
         '=SUMPRODUCT((Instructions!A6:A405<>"")*(Instructions!E6:E405=""))',
         '=IFERROR(MATCH(1,(Instructions!A6:A405<>"")*(Instructions!E6:E405=""),0)+5,"—")'),
        ("Missing Status / Firm / Client",
         '=SUMPRODUCT((Instructions!A6:A405<>"")*((Instructions!I6:I405="")+(Instructions!J6:J405="")+(Instructions!K6:K405="")>0))',
         '=IFERROR(MATCH(1,(Instructions!A6:A405<>"")*((Instructions!I6:I405="")+(Instructions!J6:J405="")+(Instructions!K6:K405="")>0),0)+5,"—")'),
        ("Missing Date / Type / Reinstruction flag",
         '=SUMPRODUCT((Instructions!A6:A405<>"")*((Instructions!M6:M405="")+(Instructions!N6:N405="")+(Instructions!O6:O405="")>0))',
         '=IFERROR(MATCH(1,(Instructions!A6:A405<>"")*((Instructions!M6:M405="")+(Instructions!N6:N405="")+(Instructions!O6:O405="")>0),0)+5,"—")'),
        ("Allocated rows missing investigator/date",
         '=SUMPRODUCT((Instructions!I6:I405="Allocated")*((Instructions!Q6:Q405="")+(Instructions!R6:R405="")>0))',
         '=IFERROR(MATCH(1,(Instructions!I6:I405="Allocated")*((Instructions!Q6:Q405="")+(Instructions!R6:R405="")>0),0)+5,"—")'),
        ("Council Response = Yes but no notes",
         '=SUMPRODUCT((Instructions!U6:U405="Yes")*(Instructions!V6:V405=""))',
         '=IFERROR(MATCH(1,(Instructions!U6:U405="Yes")*(Instructions!V6:V405=""),0)+5,"—")'),
        ("'Other' firm picked (needs A2Z follow-up)",
         '=COUNTIF(Instructions!J6:J405,"Other – advise A2Z Cloud")',
         '=IFERROR(MATCH("Other – advise A2Z Cloud",Instructions!J6:J405,0)+5,"—")'),
        ("'Other' client picked (needs A2Z follow-up)",
         '=COUNTIF(Instructions!K6:K405,"Other – advise A2Z Cloud")',
         '=IFERROR(MATCH("Other – advise A2Z Cloud",Instructions!K6:K405,0)+5,"—")'),
        ("'Other' investigator picked (needs A2Z follow-up)",
         '=COUNTIF(Instructions!Q6:Q405,"Other – advise A2Z Cloud")',
         '=IFERROR(MATCH("Other – advise A2Z Cloud",Instructions!Q6:Q405,0)+5,"—")'),
    ]
    for i, (issue, count_f, ex_f) in enumerate(issues):
        r = 11 + i
        ws[f"B{r}"] = issue
        ws[f"B{r}"].font = font_body
        ws[f"B{r}"].alignment = align_left
        ws[f"B{r}"].border = border_all
        ws[f"C{r}"] = count_f
        ws[f"C{r}"].font = font_body_bold
        ws[f"C{r}"].alignment = align_centre
        ws[f"C{r}"].border = border_all
        ws[f"D{r}"] = ex_f
        ws[f"D{r}"].font = font_body
        ws[f"D{r}"].alignment = align_centre
        ws[f"D{r}"].border = border_all
        ws.row_dimensions[r].height = 20

        cf_rule = FormulaRule(
            formula=[f'$C{r}>0'], stopIfTrue=False, fill=fill_amber,
        )
        ws.conditional_formatting.add(f"C{r}:D{r}", cf_rule)

    last_issue_row = 10 + len(issues)
    note_row = last_issue_row + 2
    ws.merge_cells(f"B{note_row}:D{note_row}")
    ws[f"B{note_row}"] = (
        "This dashboard updates live as you fill rows. The banner above turns green "
        "when there are no issues left and at least one row has been entered."
    )
    ws[f"B{note_row}"].font = font_descr
    ws[f"B{note_row}"].alignment = align_left
    ws.row_dimensions[note_row].height = 30

    ws.protection.sheet = True
    return ws


# ============================================================
#   ASSEMBLE
# ============================================================

def build():
    wb = Workbook()
    wb.remove(wb.active)

    build_picklists(wb)            # build first so defined names exist
    build_instructions(wb)
    build_client_accounts(wb)
    build_clients(wb)
    build_investigators(wb)
    build_portal_users(wb)
    build_readiness(wb)

    order = [
        "Instructions",
        "Client Accounts",
        "Clients",
        "Investigators",
        "Portal Users",
        "Submission Readiness",
        "Picklists",
    ]
    wb._sheets = [wb[name] for name in order]
    wb.active = 0

    out_paths = [
        "/tmp/A2Z-Customer-Reference/ID Inquiries/Migration/4593_ID_Inquiries_Migration_Intake_v5.xlsx",
        "/Users/rg/Documents/rg-system/4593_ID_Inquiries_Migration_Intake_v5.xlsx",
    ]
    for p in out_paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        wb.save(p)
        print(f"Wrote {p}")


if __name__ == "__main__":
    build()
