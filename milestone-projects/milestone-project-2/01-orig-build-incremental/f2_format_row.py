"""f2: format_row, carried over from Milestone 1 and taught to read an object.

This is your own Milestone 1 file. Stage 2 changes three lines inside it: an expense is
an Expense object now, so the square brackets become dots. The f-string never changes.
"""
from expense import Expense


def format_row(expense: Expense) -> str:
    """Return one aligned table row for an expense."""
    desc = expense.description
    cat = expense.category
    amt = expense.amount
    return f"{desc:<20} {cat:<14} {amt:>10,.2f}"
