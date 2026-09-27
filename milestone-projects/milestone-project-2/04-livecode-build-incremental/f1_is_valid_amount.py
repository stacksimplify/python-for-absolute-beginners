def is_valid_amount(amount_text):
    """True if amount_text is a positive number like '12' or '12.50' (rejects 0 and negatives)."""
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
    return float(amount_text) > 0
