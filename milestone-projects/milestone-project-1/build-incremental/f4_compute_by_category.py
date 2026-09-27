"""f4: compute_by_category lives here.

main.py imports it. You will see it work when the Spending-by-category action runs.
"""


def compute_by_category(expenses):
    """Return a dict of category -> total amount."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0.0) + expense["amount"]
    return totals
