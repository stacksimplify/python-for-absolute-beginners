"""
f5_actions.py: Menu Actions

This is your own Milestone 1 file, edited stage by stage. Each function still:
- Gets input from the user.
- Calls the helpers.
- Displays the results.

What changed: every action now receives the ExpenseBook instead of a bare list, so
`expenses` became `book` in each signature. The imports of f3 and f4 are gone, because
those two helpers became ExpenseBook methods.

main.py imports these functions and calls them based on the user's menu choice.
"""

from expense_book import ExpenseBook
from f1_is_valid_amount import is_valid_amount
from rich.console import Console

from f2_format_row import make_table


def add_expense(book: ExpenseBook) -> None:
    """Prompt the user for a new expense and add it to the book."""
    description = input("Description: ").strip()

    if description == "":
        description = "(no description)"

    amount_text = input("Amount: ").strip()

    if not is_valid_amount(amount_text):
        print("Invalid amount - enter a positive number like 12.50")
        return

    category = input("Category: ").strip().lower()

    if category == "":
        category = "uncategorized"

    amount = float(amount_text)

    # The book builds the Expense object, stamps it with the time, and keeps it.
    expense = book.store_expense(description, amount, category)

    print(f"Added: {expense.description} ({expense.amount:,.2f}) [{expense.category}]")


def list_expenses(book: ExpenseBook) -> None:
    """Display all recorded expenses."""
    if not book.expenses:
        print("No expenses yet.")
        return

    Console().print(make_table(book.expenses))


def show_total(book: ExpenseBook) -> None:
    """Display the total amount spent."""
    print(f"Total spent: {book.compute_total():,.2f}")


def show_by_category(book: ExpenseBook) -> None:
    """Display the total spent in each category."""
    totals = book.compute_by_category()

    if not totals:
        print("No expenses yet.")
        return

    for category, total in totals.items():
        print(f"{category:<14} {total:>10,.2f}")


def filter_by_category(book: ExpenseBook) -> None:
    """Display expenses that belong to one category."""
    wanted_category = input("Category to show: ").strip().lower()

    matches = book.filter(wanted_category)

    if not matches:
        print(f"No expenses in '{wanted_category}'.")
        return

    Console().print(make_table(matches))
