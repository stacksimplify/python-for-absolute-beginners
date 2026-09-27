"""
Warm-up 5: Total a Field, and Total by Category

Write a program that adds up expense amounts two ways: one grand total of every
amount, and a per-category breakdown stored in a dictionary. Both are built by
looping over a list of expense dictionaries. Then display that breakdown as a
neat table.

Task-1:
Create a helper function named compute_total() that returns the sum of every
expense amount.

Task-2:
Create a helper function named compute_by_category() that returns a dictionary
mapping each category to its total amount.

Task-3:
Display the per-category totals as an aligned table, the same way the app's
"Spending by category" action shows them.

Python concepts practiced:
1. Defining functions that take a list and return a value.
2. for loops over a list of dictionaries.
3. Dictionary access using keys (expense["amount"], expense["category"]).
4. An accumulator variable (total = 0.0) that adds up inside a loop.
5. Building a dictionary while you loop.
6. dict.get(key, default) to read a running total (or 0.0 the first time).
7. Returning a number, and returning a dictionary.
8. f-strings and the project ,.2f money format to display the total.
9. Format specifiers for an aligned table (:<14, :>10,.2f), the same display
   style as warm-up 04 and the app's show_by_category action.

Project connection:
compute_total() becomes f3_compute_total.py and compute_by_category() becomes
f4_compute_by_category.py in the project, the two helpers behind the "Total spent"
and "Spending by category" menu options. The functions here are the exact ones you
will use in the app (copy-paste), so nothing is new when you build them.
"""
# ===== Task-1: Total a Field (compute_total) =====
# Loop over the expenses and add up every amount into a running total.
def compute_total(expenses):
    """Return the sum of every expense amount."""
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total


# ===== Task-2: Total by Category (compute_by_category) =====
# Loop over the expenses and add each amount into its category's running total.
# dict.get(category, 0.0) gives the current total, or 0.0 the first time we see it.
def compute_by_category(expenses):
    """Return a dict of category -> total amount."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0.0) + expense["amount"]
    return totals


# A few expenses to test the helpers.
expenses = [
    {"description": "Coffee", "amount": 3.5, "category": "food"},
    {"description": "Bus", "amount": 2.0, "category": "transport"},
    {"description": "Lunch", "amount": 6.5, "category": "food"},
]

# Task-1's helper: the grand total, shown with the project ,.2f money format.
print(f"Total: {compute_total(expenses):,.2f}")

# Task-2's helper: the per-category dict, printed raw so you see the return value.
print(compute_by_category(expenses))


# ===== Task-3: Display the Per-Category Totals (formatted) =====
# Take Task-2's dict and print it as an aligned table instead of a raw dict.
# Project link: this is exactly how the "Spending by category" menu option
# (show_by_category in f5_actions.py) shows the totals, the category left-aligned
# in 14 and the amount right-aligned in 10 with the ,.2f money format (the same
# column style as warm-up 04's table).
totals = compute_by_category(expenses)
for category, total in totals.items():
    print(f"{category:<14} {total:>10,.2f}")
