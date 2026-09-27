"""Practice Problem-11 helper module (solution): pricetools.

Imported by s07_practice11_sol_modules_imports.py.
"""


def tag(text):
    """Return the product name in capitals with an exclamation mark."""
    return text.upper() + "!"


def with_tax(price):
    """Return the price with 10 percent tax added, rounded to 2 decimals."""
    return round(price * 1.1, 2)
