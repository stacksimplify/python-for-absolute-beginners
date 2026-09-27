def compute_by_category(expenses):
    """Return a dict of category -> total amount."""
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0.0) + expense["amount"]
    return totals
