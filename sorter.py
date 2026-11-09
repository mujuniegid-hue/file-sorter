from pathlib import Path
from datetime import datetime  # NEW
import shutil
import argparse

CATEGORIES = {
    "Contracts": [".docx", ".doc"],
    "Evidence": [".jpg", ".jpeg", ".png"],
    "Filings": [".pdf"],
    "Correspondence": [".txt", ".eml"],
}

LOG_NAME = "sort_log.txt"  # NEW


def get_category(file_path):
    """Return the folder name a file belongs in."""
    extension = file_path.suffix.lower()
    for folder_name, extensions in CATEGORIES.items():
        if extension in extensions:
            return folder_name
    return "Other"


def write_log(log_path, original, destination):  # NEW
    """Add one line to the log file recording a move."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} | MOVED | {original} | {destination}\n"
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(line)


def sort_folder(target_folder):
    """Move every file in target_folder into its category subfolder."""
    target = Path(target_folder)
    log_path = target / LOG_NAME  # NEW

    files = [
        item for item in target.iterdir()
        if item.is_file() and item.name != LOG_NAME  # NEW: ignore the log
    ]

    for file_path in sorted(files):
        category = get_category(file_path)
        destination_folder = target / category
        destination_folder.mkdir(exist_ok=True)

        destination = destination_folder / file_path.name

        if destination.exists():
            print(f"SKIPPED (already exists): {file_path.name}")
            continue

        original_full = file_path.resolve()  # NEW: record before moving
        shutil.move(str(file_path), str(destination))
        write_log(log_path, original_full, destination.resolve())  # NEW
        print(f"{file_path.name} -> {category}")


def main():
    """Read the folder path typed by the user, check it, and sort it."""
    parser = argparse.ArgumentParser(
        description="Sort a folder of client documents into subfolders by file type."
    )
    parser.add_argument("folder", help="Path to the folder you want to sort")
    args = parser.parse_args()

    target = Path(args.folder)

    if not target.is_dir():
        print(f"Error: '{args.folder}' is not a folder that exists.")
        return

    sort_folder(target)


if __name__ == "__main__":
    main()