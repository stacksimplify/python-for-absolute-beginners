from rich.table import Table

from expense import Expense


def format_row(expense: Expense) -> str:
    """Return one aligned table row for an expense."""
    desc = expense.description
    cat = expense.category
    amt = expense.amount
    return f"{desc:<20} {cat:<14} {amt:>10,.2f}"


def make_table(expenses: list[Expense]) -> Table:
    """Build a rich table with one row per expense."""
    table = Table(title="Expenses")
    table.add_column("Description")
    table.add_column("Category")
    table.add_column("Amount", justify="right")
    for expense in expenses:
        table.add_row(expense.description, expense.category, f"{expense.amount:,.2f}")
    return table
