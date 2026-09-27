"""
Warm-up 5: Load the Book Back, Safely (json + try/except)

Write a program that reads the saved file back into real Expense objects, and survives the two
things that go wrong in real life: the file is not there yet (first ever run), and the file is
there but corrupt. A missing file is normal, so we just start empty. A corrupt file is an error,
so we CATCH it and warn instead of crashing.

Task-1:
Build ExpenseBook.load(), the real method, which starts empty when the file is missing, and
otherwise rebuilds every Expense object from the saved dicts.

Task-2:
Guard against a corrupt file with try / except, the same guard main.py puts
around book.load() at startup.

Python concepts practiced:
1. path.exists() to check for a file before reading it.
2. An early return for the "nothing saved yet" case.
3. json.loads(text): JSON text back into a list of dicts.
4. Reading a dict by key to rebuild the object: row["description"], row["amount"] ...
5. A list comprehension that rebuilds every object, one row at a time.
6. try / except with three errors, to catch a corrupt file instead of crashing:
   JSONDecodeError (not JSON at all), TypeError and KeyError (valid JSON, wrong shape).
7. Catching the SPECIFIC error, not a bare except.

Project connection:
load() becomes the last method of ExpenseBook in expense_book.py. Paste it in and the class is
complete. Task-2 is the shape of main.py's startup: it wraps book.load() in try/except so a corrupt
expenses.json prints "Warning: data file is corrupt; starting empty." and the app keeps running.
save() (warm-up 04) turns objects into text; load() turns that text back into objects, a round trip.
"""
import json
from datetime import datetime
from pathlib import Path


# The Expense from warm-up 01. Repeated so this drill runs on its own.
class Expense:
    """One expense: what it was, how much, which category, and when it was added."""

    def __init__(self, description: str, amount: float,
                 category: str, created_at: str) -> None:
        self.description = description
        self.amount = amount
        self.category = category
        self.created_at = created_at

    def __repr__(self) -> str:
        """Show every field, so printing an Expense at a Python prompt is readable."""
        return (f"Expense(description={self.description!r}, amount={self.amount!r}, "
                f"category={self.category!r}, created_at={self.created_at!r})")


# ===== Task-1: load() as a Real ExpenseBook Method =====
# __init__ / add / save are the ones from warm-ups 03 and 05. They are here so this drill has a
# file to read back. load() is the NEW method that goes into expense_book.py.
class ExpenseBook:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.expenses: list[Expense] = []

    def store_expense(self, description: str, amount: float, category: str) -> Expense:
        """Build one Expense, stamp it with the time, keep it, and hand it back."""
        stamp = datetime.now().isoformat(timespec="seconds")
        expense = Expense(description, amount, category, stamp)
        self.expenses.append(expense)
        return expense

    def save(self) -> None:
        """Write every expense to the JSON file, making the data folder if it is missing."""
        rows = [{"description": expense.description, "amount": expense.amount,
                 "category": expense.category, "created_at": expense.created_at}
                for expense in self.expenses]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(rows, indent=2))

    def load(self) -> None:
        """Read the JSON file back into Expense objects. A missing file just means no expenses yet."""
        if not self.path.exists():
            self.expenses = []
            return
        rows = json.loads(self.path.read_text())
        self.expenses = [Expense(row["description"], row["amount"],
                                 row["category"], row["created_at"]) for row in rows]


# A file that does not exist yet: load() just starts empty, no error.
fresh = ExpenseBook(Path("_no_such_file.json"))
fresh.load()
print("missing file -> expenses:", fresh.expenses)

# Save two, then load them back into a BRAND NEW book: the round trip.
book = ExpenseBook(Path("_warmup_expenses.json"))
book.store_expense("Coffee", 3.5, "food")
book.store_expense("Bus", 2.0, "transport")
book.save()

reloaded = ExpenseBook(Path("_warmup_expenses.json"))
reloaded.load()
print("loaded back  :", len(reloaded.expenses), "expenses ->", reloaded.expenses[0])
book.path.unlink()


# ===== Task-2: Guard Against a Corrupt File =====
# A missing file is normal; a CORRUPT file is an error. A file can be broken three ways, so the
# guard names three errors: json.loads raises JSONDecodeError when the text is not JSON at all,
# and rebuilding the objects raises TypeError or KeyError when it is JSON of the wrong shape. So we
# catch that one error and start empty instead of crashing. This is exactly what main.py does
# around book.load() when the app starts.
bad = ExpenseBook(Path("_bad.json"))
bad.path.write_text("{ not valid json")
try:
    bad.load()
except (json.JSONDecodeError, TypeError, KeyError):
    print("corrupt file -> Warning: data file is corrupt; starting empty.")
    bad.expenses = []
print("after guard  :", bad.expenses)
bad.path.unlink()
