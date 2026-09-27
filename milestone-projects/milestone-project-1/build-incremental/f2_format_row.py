"""f2: format_row lives here.

main.py imports it. You will see it in action when the List action prints a table.
"""


def format_row(expense):
    """Return one aligned table row for an expense."""
    desc = expense["description"]
    cat = expense["category"]
    amt = expense["amount"]
    return f"{desc:<20} {cat:<14} {amt:>10,.2f}"
