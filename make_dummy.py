from pathlib import Path

# The name of the practice folder we will create
dummy_folder = Path("dummy_folder")

# Create the folder. exist_ok=True means "don't crash if it already exists"
dummy_folder.mkdir(exist_ok=True)

# A list of fake file names, mixing every type the firm receives
fake_files = [
    "scan001.pdf",
    "Contract_FINAL_v3.docx",
    "old_agreement.doc",
    "IMG_4827.jpg",
    "IMG_4828.jpeg",
    "accident_scene.png",
    "court_filing_2024.pdf",
    "client_email.eml",
    "meeting_notes.txt",
    "invoice_data.xlsx",
    "presentation.pptx",
    "SCAN_ID.PDF",
    "no_extension_file",
    "no_extension_file",
    "witness_statement.docx",
    "site_photo.PNG",
]


# Go through the list and create each file
for name in fake_files:
    file_path = dummy_folder / name
    file_path.write_text("dummy content for testing")

print(f"Created {len(fake_files)} dummy files in '{dummy_folder}'")