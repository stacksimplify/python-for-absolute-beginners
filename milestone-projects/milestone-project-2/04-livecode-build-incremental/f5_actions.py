from f1_is_valid_amount import is_valid_amount
from f2_format_row import format_row
from f3_compute_total import compute_total
from f4_compute_by_category import compute_by_category


def add_expense(expenses):
    """Prompt the user for a new expense and add it to the list."""
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

    expense = {
        "description": description,
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)

    print(f"Added: {description} ({amount:,.2f}) [{category}]")


def list_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("No expenses yet.")
        return

    print(f"{'Description':<20} {'Category':<14} {'Amount':>10}")

    for expense in expenses:
        print(format_row(expense))


def show_total(expenses):
    """Display the total amount spent."""
    print(f"Total spent: {compute_total(expenses):,.2f}")


def show_by_category(expenses):
    """Display the total spent in each category."""
    totals = compute_by_category(expenses)

    if not totals:
        print("No expenses yet.")
        return

    for category, total in totals.items():
        print(f"{category:<14} {total:>10,.2f}")


def filter_by_category(expenses):
    """Display expenses that belong to one category."""
    wanted_category = input("Category to show: ").strip().lower()

    matches = [
        expense
        for expense in expenses
        if expense["category"] == wanted_category
    ]

    if not matches:
        print(f"No expenses in '{wanted_category}'.")
        return

    print(f"{'Description':<20} {'Category':<14} {'Amount':>10}")

    for expense in matches:
        print(format_row(expense))
