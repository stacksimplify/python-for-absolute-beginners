"""
Warm-up 4: Save the Book to a File (json + pathlib)

Write a program that writes the expenses to a JSON file so they survive after the program ends.
There is one catch: JSON cannot store a Python object, so every Expense must become a plain dict
first. You build that dict yourself, reading each field off the object with a dot.

Task-1:
Turn one Expense object into a plain dict by reading its attributes, and see why that step is needed.

Task-2:
Build ExpenseBook.save(), the real method, which converts every expense to a dict, turns the list
into JSON text, and writes it to the book's path.

Python concepts practiced:
1. Read an object's attributes to build a plain dict: {"description": one.description, ...}.
2. A list comprehension over objects that builds one dict per expense.
3. json.dumps(rows, indent=2): a list of dicts into readable JSON text.
4. pathlib: self.path.write_text(...) writes text to a file in one call.
5. Methods that return None (-> None) because their job is a side effect, not a value.

Project connection:
save() becomes a method of ExpenseBook in expense_book.py. Paste it in beside the methods from
warm-up 03. main.py calls book.save() when you choose "6) Save and quit", and warm-up 05
reads that same file back. The created_at stamp from warm-up 02 is already text, so it saves with
no conversion.
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


# ===== Task-1: An Object Is Not JSON, So Build a Dict First =====
# json.dumps() cannot write an Expense object, but it can write a plain dict. So read the four
# attributes off the object and put them in a dict. That is what makes save() possible.
one = Expense("Coffee", 3.5, "food", "2026-01-01T09:00:00")
one_dict = {"description": one.description, "amount": one.amount,
            "category": one.category, "created_at": one.created_at}
print("object:", one)
print("dict  :", one_dict)


# ===== Task-2: save() as a Real ExpenseBook Method =====
# __init__ and store_expense() are the ones from warm-up 03; save() is the NEW method that goes into
# expense_book.py.
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


book = ExpenseBook(Path("_warmup_expenses.json"))
book.store_expense("Coffee", 3.5, "food")
book.store_expense("Bus", 2.0, "transport")
book.save()

print()
print("saved to", book.path)
print(book.path.read_text())

# Tidy up: the real app keeps its expenses.json, this drill does not.
book.path.unlink()
