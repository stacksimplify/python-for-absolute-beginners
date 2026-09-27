"""expense_book.py: the list and the functions that work on it, together. NEW in Milestone 2.

In Milestone 1 every helper and every action took the same `expenses` list as its first
argument. That repetition is the reason this class exists. Milestone 1's compute_total and
compute_by_category moved in here as methods with the same names, with one word changed in each
body: `expenses` became `self.expenses`. The square brackets had already become dots at
stage 2. Then this class grows what Milestone 1 could not do: saving and loading a file.

No input() and no print() in here, so the same class could sit behind a web app later.
"""
import json
from datetime import datetime
from pathlib import Path

from expense import Expense


class ExpenseBook:
    """Holds the expenses and answers questions about them."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.expenses: list[Expense] = []

    def store_expense(self, description: str, amount: float, category: str) -> Expense:
        """Build one Expense, stamp it with the time, keep it, and hand it back."""
        stamp = datetime.now().isoformat(timespec="seconds")
        expense = Expense(description, amount, category, stamp)
        self.expenses.append(expense)
        return expense

    def compute_total(self) -> float:
        """Return the sum of every expense amount. This was Milestone 1's compute_total."""
        total = 0.0
        for expense in self.expenses:
            total += expense.amount
        return total

    def compute_by_category(self) -> dict[str, float]:
        """Return a dict of category -> total amount. This was Milestone 1's compute_by_category."""
        totals: dict[str, float] = {}
        for expense in self.expenses:
            category = expense.category
            totals[category] = totals.get(category, 0.0) + expense.amount
        return totals

    def filter(self, category: str) -> list[Expense]:
        """Return only the expenses in one category."""
        return [expense for expense in self.expenses if expense.category == category]

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
