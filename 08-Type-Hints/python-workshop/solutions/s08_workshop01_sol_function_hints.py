"""
Workshop Problem-01: function hints (Car Label) (solution)

Concepts: parameter and return type hints.

Write a function `label` that takes a car brand and a year and returns the text "<brand> (<year>)", with type hints saying it takes a `str` and an `int` and returns a `str`. Call it with "Mazda" and 2020 and print the result.

Expected output: Mazda (2020)
"""

def label(brand: str, year: int) -> str:
    return f"{brand} ({year})"
print(label("Mazda", 2020))
