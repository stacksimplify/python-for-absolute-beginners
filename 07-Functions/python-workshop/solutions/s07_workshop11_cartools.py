"""Workshop Problem-11 helper module (solution): cartools.

Imported by s07_workshop11_sol_modules_imports.py.
"""


def price_with_tax(price, rate):
    """Return price plus tax at the given rate."""
    return price + price * rate


def label(brand, model):
    """Return 'brand model'."""
    return f"{brand} {model}"

