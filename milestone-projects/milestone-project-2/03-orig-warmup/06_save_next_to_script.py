"""
Warm-up 6: Save Next to the Script (a data/ folder)

Write a program that saves a file where you can always FIND it (right next to your code, in a
data/ folder) no matter which folder you run the program from. A plain name like
Path("expenses.json") lands wherever you happen to run from, so the file seems to "disappear". The
fix is to build the path from THIS script's own location.

Task-1:
Build a path that points at a data/ folder next to this script, and print the full location so you
see exactly where it is.

Task-2:
Create the data/ folder, write a small JSON file into it, read it back, and confirm it is really
there, the same move ExpenseBook.save() makes.

Python concepts practiced:
1. __file__: the path to THIS script file (Section 10).
2. Path(__file__).parent: the folder the script sits in, so paths do not depend on where you run.
3. The / operator to join path parts: ... / "data" / "expenses.json".
4. Path.mkdir(parents=True, exist_ok=True): create the folder (and parents) without error if it exists.
5. path.write_text(...) / path.read_text(): write and read the whole file in one call.

Project connection:
This is the exact path you pass to the book in main.py:
    book = ExpenseBook(Path(__file__).parent / "data" / "expenses.json")
That is why the tracker's expenses.json always appears in 01-orig-build-incremental/data/,
next to your code, never lost in whatever folder you launched from. save() runs the mkdir line for you.
"""
import json
from pathlib import Path


# ===== Task-1: Build a path NEXT TO this script =====
# __file__ is this script's own path. .parent is the folder it lives in. Join a data/ folder and a
# file name with the / operator. This path is the SAME no matter which folder you run from.
data_file = Path(__file__).parent / "data" / "expenses.json"
print("the file will be saved at:", data_file)
print("its folder is:", data_file.parent)


# ===== Task-2: Make the folder, then write and read the file =====
# mkdir(parents=True, exist_ok=True) creates data/ the first time and does nothing if it already exists.
data_file.parent.mkdir(parents=True, exist_ok=True)

rows = [{"description": "Coffee", "amount": 3.5, "category": "food",
         "created_at": "2026-01-01T09:00:00"}]
data_file.write_text(json.dumps(rows, indent=2))
print()
print("saved. reading it back:")
print(data_file.read_text())

# Tidy up: this is only a drill, so remove the demo file. We only remove the folder when it is
# empty. If the real app has already saved expenses in there, we leave it alone.
data_file.unlink()
if not any(data_file.parent.iterdir()):
    data_file.parent.rmdir()
