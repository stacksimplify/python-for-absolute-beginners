"""
Warm-up 3: The ExpenseBook Class (data and behavior together)

Write a program that builds the ExpenseBook class, the heart of the tracker. It HOLDS the expenses
and knows what to do with them: add one, add up the total, group the totals by category, and pick
out one category. This is the OOP idea: the data (the list) and the behavior (the methods) live in
the SAME object. Notice none of these METHODS print; that is the menu's job, not the book's. (The
try-it-out lines at the bottom print, just so this drill shows something when you run it.)

Task-1:
Create the ExpenseBook class with __init__ (remember the data file path, start an empty list) and
store_expense() (stamp a new expense and keep it).

Task-2:
Add compute_total() and compute_by_category(), the two methods that turn the stored expenses into numbers.

Task-3:
Add filter(): hand back just the expenses in one category, using a list comprehension.

Python concepts practiced:
1. class with __init__ to set up an object's own data (self.path, self.expenses).
2. self: how a method reaches the object's own data.
3. Methods that RETURN a value and never print (pure logic a web app could reuse).
4. Type hints on methods: (self, category: str) -> list[Expense] and -> dict[str, float].
5. list[Expense] and dict[str, float] to type a list and a dict.
6. Building an object inside a method and appending it to self.expenses.
7. An accumulator (total = 0.0) added up in a loop.
8. dict.get(key, default) to total by category without first checking whether the key is already there.
9. A list comprehension with a condition, to filter.

Project connection:
This class IS expense_book.py, the heart of the project. Warm-ups 04 and 05 add its last
two methods (save and load) and then the class is complete. The menu actions in
f5_actions.py do all the talking; ExpenseBook only computes and returns.
"""
from datetime import datetime
from pathlib import Path


# The Expense you built in warm-up 01 (it becomes expense.py). Repeated so this drill runs
# on its own.
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


# ===== Task-1: The Class, __init__ and store_expense() =====
# __init__ runs when you create the book: it remembers WHERE the data file lives and starts an
# empty list. store_expense() makes the timestamp (warm-up 02), builds the Expense, keeps it, returns it.
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

    # ===== Task-2: compute_total() and compute_by_category() =====
    # compute_total() adds every amount into one number. compute_by_category() builds a dict of category -> total,
    # using totals.get(cat, 0.0) so a brand-new category simply starts at zero.
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

    # ===== Task-3: filter() =====
    # Keep only the expenses whose category matches, and hand back a NEW, smaller list.
    def filter(self, category: str) -> list[Expense]:
        """Return only the expenses in one category."""
        return [expense for expense in self.expenses if expense.category == category]


# Try the book out. The menu actions will do exactly this later.
book = ExpenseBook(Path("expenses.json"))
book.store_expense("Coffee", 3.5, "food")
book.store_expense("Bus", 2.0, "transport")
book.store_expense("Lunch", 6.5, "food")

print("expenses stored:", len(book.expenses))
print("total          :", f"{book.compute_total():,.2f}")
print("by category    :", book.compute_by_category())
print("food only      :", len(book.filter("food")), "expenses")
