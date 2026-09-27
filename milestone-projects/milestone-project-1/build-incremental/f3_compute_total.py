"""f3: compute_total lives here.

main.py imports it. You will see it work when the Total action prints the sum.
"""


def compute_total(expenses):
    """Return the sum of every expense amount."""
    total = 0.0
    for expense in expenses:
        total += expense["amount"]
    return total
