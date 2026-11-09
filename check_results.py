from pathlib import Path

# Where we expect each dummy file to end up
EXPECTED = {
    "Contract_FINAL_v3.docx": "Contracts",
    "old_agreement.doc": "Contracts",
    "witness_statement.docx": "Contracts",
    "IMG_4827.jpg": "Evidence",
    "IMG_4828.jpeg": "Evidence",
    "accident_scene.png": "Evidence",
    "site_photo.PNG": "Evidence",
    "scan001.pdf": "Filings",
    "court_filing_2024.pdf": "Filings",
    "SCAN_ID.PDF": "Filings",
    "client_email.eml": "Correspondence",
    "meeting_notes.txt": "Correspondence",
    "invoice_data.xlsx": "Other",
    "presentation.pptx": "Other",
    "no_extension_file": "Other",
}

folder = Path("dummy_folder")
problems = 0

# Check 1: every file is in the right subfolder
for name, category in EXPECTED.items():
    if (folder / category / name).exists():
        print(f"PASS  {name} is in {category}/")
    else:
        print(f"FAIL  {name} is NOT in {category}/")
        problems += 1

# Check 2: no loose files left behind (except the log)
loose = [f.name for f in folder.iterdir() if f.is_file() and f.name != "sort_log.txt"]
if loose:
    print(f"FAIL  Loose files remain: {loose}")
    problems += 1
else:
    print("PASS  No loose files left in the main folder")

# Check 3: the log exists and has one line per moved file
log_file = folder / "sort_log.txt"
if log_file.exists():
    lines = log_file.read_text(encoding="utf-8").splitlines()
    if len(lines) == len(EXPECTED):
        print(f"PASS  Log has {len(lines)} lines, one per file")
    else:
        print(f"FAIL  Log has {len(lines)} lines, expected {len(EXPECTED)}")
        problems += 1
else:
    print("FAIL  sort_log.txt is missing")
    problems += 1

# Final verdict
if problems == 0:
    print("\nALL CHECKS PASSED")
else:
    print(f"\n{problems} CHECK(S) FAILED")