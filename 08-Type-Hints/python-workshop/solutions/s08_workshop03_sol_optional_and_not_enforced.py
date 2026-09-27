"""
Workshop Problem-03: optional and not enforced (Price Lookup) (solution)

Concepts: int | None (optional), .get().

Write a function `find_car_price` that takes a car brand and looks it up in a price list (Mazda at 15000 and Tesla at 42000), returning the matching price or nothing when the brand is missing, with type hints saying it takes a `str` and returns either an `int` or `None`. Call it for "Mazda" (known) and "Kia" (unknown) and print each result.

Expected output:
15000
None
"""

def find_car_price(brand: str) -> int | None:
    prices = {"Mazda": 15000, "Tesla": 42000}
    return prices.get(brand)
print(find_car_price("Mazda"))
print(find_car_price("Kia"))
