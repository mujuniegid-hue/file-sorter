# Client Document Sorter

A Python tool that automatically sorts a messy folder of client documents
into organised subfolders and keeps a log of every file it moves.

## The problem

A law firm downloads client documents into one folder all day: scanned IDs,
signed contracts, court filings, evidence photos and printed emails. By the
end of the week there are about 200 files with names like `scan001.pdf` and
`IMG_4827.jpg`. Sorting them by hand is slow and easy to get wrong.

## What it does

Sorts files into subfolders by type:

| Folder | File types |
|---|---|
| Contracts | .docx, .doc |
| Evidence | .jpg, .jpeg, .png |
| Filings | .pdf |
| Correspondence | .txt, .eml |
| Other | everything else |

- Handles uppercase extensions (e.g. `.PDF`) and files with no extension
- Never overwrites a file that already exists in the destination
- Records every move in `sort_log.txt` with a timestamp, the original path
  and the destination path

## How to run

1. Install Python 3.
2. Download this project.
3. Open a terminal in the project folder and run:

    python sorter.py "path\to\folder"

Example: `python sorter.py "C:\Clients\Downloads"`

For help: `python sorter.py --help`

## Testing

`make_dummy.py` creates a dummy folder of mixed files, including edge cases.
After sorting it, `check_results.py` verifies that every file landed in the
right place and that the log is complete.

    python make_dummy.py
    python sorter.py dummy_folder
    python check_results.py

## Time saved per week

Assumptions (estimates, not measured results):
- About 200 files per week
- About 20 seconds to open, identify and drag each file by hand
- 200 x 20 seconds = about 67 minutes per week
- The script takes a few seconds

**Estimated saving: about 1 hour per week, or about 50 hours per year.**
The firm can measure its own figure by timing one manual sorting session.

## Pricing

| Item | Price (UGX) |
|---|---|
| Optional: add file types or rules later | 50,000 per change |
| Build, test and set up on the firm's computer | 300,000 to 800,000 (one-time) |
| Optional: add file types or rules later | 50,000 per change |

These are suggested figures for a small custom tool. Final pricing depends
on the firm's needs and the time required.

## Limitations

- Sorts by file extension only, not by document content
- Does not look inside subfolders
- Runs when someone starts it. It is not automatic in the background