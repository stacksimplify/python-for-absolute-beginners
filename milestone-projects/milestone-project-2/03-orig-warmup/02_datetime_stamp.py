"""
Warm-up 2: Stamp Every Expense With the Time (datetime)

Write a program that makes a timestamp the moment something happens, and then uses it to build an
Expense. The tracker stamps every expense with the date and time it was added, so your saved file
can tell you WHEN you spent. That is the created_at field you added in warm-up 01.

Task-1:
Make a timestamp as text with datetime.now().isoformat(timespec="seconds").

Task-2:
Use that timestamp to build an Expense, so created_at is filled the moment the expense is created.

Python concepts practiced:
1. Importing a class from a module: from datetime import datetime.
2. datetime.now() to read the current date and time.
3. .isoformat() to turn a datetime into readable text: "2026-01-01T09:00:00".
4. timespec="seconds" to cut off the microseconds, so every stamp is the same tidy length.
5. Keeping the stamp as TEXT (not a datetime object) so it saves to JSON later with no conversion.

Project connection:
This one line becomes the FIRST line of ExpenseBook.store_expense() in expense_book.py:
    stamp = datetime.now().isoformat(timespec="seconds")
Every expense the tracker adds is stamped this way. Because the stamp is text, it drops straight
into the JSON file in warm-up 04 with no extra work.
"""
from datetime import datetime


# The Expense you built in warm-up 01 (it becomes expense.py). Repeated here so this drill
# runs on its own.
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


# ===== Task-1: Make the Timestamp =====
# datetime.now() is the current date and time. .isoformat() turns it into readable text, and
# timespec="seconds" drops the microseconds so every stamp looks the same.
stamp = datetime.now().isoformat(timespec="seconds")
print("stamp:", stamp)


# ===== Task-2: Stamp a New Expense =====
# This is exactly what ExpenseBook.store_expense() does: make the stamp first, then build the Expense with
# it, so created_at is never empty.
expense = Expense("Coffee", 3.5, "food", stamp)
print(expense)
print("created_at:", expense.created_at)
