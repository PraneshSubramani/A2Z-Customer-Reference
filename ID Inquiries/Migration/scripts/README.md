# v5 Intake Template — Build & Test Scripts

## build_v5_template.py
Builds `4593_ID_Inquiries_Migration_Intake_v5.xlsx` from scratch.
The build is fully reproducible — re-run after any column / picklist change.

```bash
pip install openpyxl
python3 build_v5_template.py
```

Edit the `COLUMNS` list at the top to add / remove columns (e.g. after Alison's
Pre-Fill Data Audit reply lands).

## test_v5_template.py
End-to-end test harness. Injects 9 scenarios (valid + invalid combinations)
into the template, runs LibreOffice headless to recalculate formulas, then
verifies per-row diagnostics + the Submission Readiness dashboard against
expected values.

```bash
sudo apt-get install libreoffice
pip install openpyxl
python3 test_v5_template.py
```

Expected output: `OVERALL: 14 PASS, 0 FAIL`.

## Notes on formulas
- The Missing Fields formula in column X uses `&` concat + `SUBSTITUTE` to
  strip the leading separator. This is intentional — the prior `TEXTJOIN`
  approach throws `#NAME?` in LibreOffice and Excel < 2019 unless the
  `_xlfn.` prefix is emitted, which openpyxl does not auto-prefix.
- The Submission Readiness banner uses a single nested IF tied to the
  total / valid / incomplete counts.

