def compute_total(expenses):
    """Return the sum of every expense amount."""
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total
