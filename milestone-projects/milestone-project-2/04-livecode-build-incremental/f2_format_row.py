def format_row(expense):
    """Return one aligned table row for an expense."""
    desc = expense["description"]
    cat = expense["category"]
    amt = expense["amount"]
    return f"{desc:<20} {cat:<14} {amt:>10,.2f}"
