"""Milestone Project 1: CLI Expense Tracker (solution).

Uses only Sections 01-07: input(), f-strings, conditionals, lists,
dicts, loops and functions. No try/except (09), no files (10), no
classes (13).
"""


def is_valid_amount(amount_text):
    """True if amount_text is a positive number like '12' or '12.50' (rejects 0 and negatives).

    Uses string methods and float(). No try/except (that is Section 09).
    """
    amount_text = amount_text.strip()
    decimal_parts = amount_text.split(".")
    if len(decimal_parts) == 1:
        is_valid_format = decimal_parts[0].isdecimal()
    elif len(decimal_parts) == 2:
        is_valid_format = (
            decimal_parts[0].isdecimal() and
            decimal_parts[1].isdecimal()
        )
    else:
        is_valid_format = False
    if not is_valid_format:
        return False
    # every character is a digit now, so float() is safe: a real amount is above zero
    return float(amount_text) > 0


def compute_total(expenses):
    """Return the sum of every expense amount."""
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total


def compute_by_category(expenses):
    """Return a dict of category -> total amount."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0.0) + expense["amount"]
    return totals


def format_row(expense):
    """Return one aligned table row for an expense."""
    desc = expense["description"]
    cat = expense["category"]
    amt = expense["amount"]
    return f"{desc:<20} {cat:<14} {amt:>10,.2f}"


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

    # Create one expense dictionary and add it to the expenses list.
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


def show_menu():
    print()
    print("==== Expense Tracker ====")
    print("1) Add expense")
    print("2) List expenses")
    print("3) Total spent")
    print("4) Spending by category")
    print("5) Show one category")
    print("6) Quit")


def main():
    expenses = []
    while True:
        show_menu()
        choice = input("Choose 1-6: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_by_category(expenses)
        elif choice == "5":
            filter_by_category(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")


main()
