"""
Warm-up 1: One Expense as an Object (a class), and One Aligned Row

Write a program that models ONE expense as an object using a class, then formats that expense
as a single aligned table row. In Milestone 1 an expense was a dictionary, so you read a field with
a key: expense["amount"]. Now it is a real object, so you read a field with a dot: expense.amount.
That one change is the whole point of this warm-up.

Task-1:
Create an Expense class: write __init__ to store four fields (description, amount, category,
created_at) and __repr__ for a readable print.

Task-2:
Create a format_row() function that turns one Expense into a neat aligned table row, reading its
fields with attribute access.

Python concepts practiced:
1. A class with __init__ to bundle fields into one object (you store each on self).
2. Storing fields on self: self.description = description.
3. Creating an object: Expense("Coffee", 3.5, "food", "2026-01-01T09:00:00").
4. Attribute access with a dot: expense.amount (Milestone 1 used expense["amount"]).
5. __repr__ so print(expense) shows a readable line instead of a memory address.
6. Type hints on a function: def format_row(expense: Expense) -> str.
7. Format specifiers: <20 and <14 left-align text, >10 right-aligns the number.
8. ,.2f for money: two decimals plus thousands commas.

Project connection:
The Expense class becomes expense.py, and format_row() is the f2_format_row.py you already have from
Milestone 1, with three lines changed inside it. Both are a straight copy-paste into the project.
ExpenseBook (expense_book.py) stores Expense objects, and the List action prints each one with
format_row.
"""


# ===== Task-1: One Expense as a Class =====
# Write __init__ to store the four fields on self, and __repr__ so printing an Expense shows a
# readable line. There is no dictionary here anymore. Each field is an attribute.
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


# Make one expense and read its fields with a dot.
expense1 = Expense("Coffee", 3.5, "food", "2026-01-01T09:00:00")
print(expense1)
print("description:", expense1.description)
print("amount     :", expense1.amount)
print("category   :", expense1.category)


# ===== Task-2: Format One Expense as an Aligned Row =====
# Same column widths as Milestone 1 (20 / 14 / 10), but the values now come from ATTRIBUTES
# (expense.description) instead of dictionary keys (expense["description"]).
def format_row(expense: Expense) -> str:
    """Return one aligned table row for an expense."""
    desc = expense.description
    cat = expense.category
    amt = expense.amount
    return f"{desc:<20} {cat:<14} {amt:>10,.2f}"


print()
print(f"{'Description':<20} {'Category':<14} {'Amount':>10}")
print(format_row(expense1))
print(format_row(Expense("Laptop", 1250.00, "electronics", "2026-01-02T10:30:00")))
