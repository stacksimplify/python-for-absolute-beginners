"""f1: is_valid_amount, carried over from Milestone 1 with its body untouched.

This is your own Milestone 1 file. Stage 1 adds the type hints Section 08 taught you;
every line below the signature is the same code you already wrote and already trust.
"""


def is_valid_amount(amount_text: str) -> bool:
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
