"""
Workshop Problem-05: default and keyword arguments (Car Rental) (solution)

Concepts: default parameter values, keyword arguments (name=value in the call),
the mutable-default trap (use None, not []).

Task-1: write a function `rent_car` that takes a `model`, a `days` that defaults to 1, and an `insurance` that defaults to "basic", and returns "<model>: <days> days, <insurance> insurance". Call it with "Swift" only (all defaults), then with "Creta" and days=3, then with "Innova" and insurance="full", printing each result.
Task-2: write a function `add_extra` that takes an `extra` and an `extras` that defaults to None, starts a fresh empty list when `extras` is None, adds `extra` to it, and returns it. Call it with "GPS" and print the result, then call it with "child seat" and print the result (each call must start with a fresh list).

Expected output:
Swift: 1 days, basic insurance
Creta: 3 days, basic insurance
Innova: 1 days, full insurance
['GPS']
['child seat']
"""

# Task-1: default days and insurance parameters
def rent_car(model, days=1, insurance="basic"):
    return f"{model}: {days} days, {insurance} insurance"

print(rent_car("Swift"))
print(rent_car("Creta", days=3))
print(rent_car("Innova", insurance="full"))

# Task-2: use None default to avoid the mutable-default trap
def add_extra(extra, extras=None):
    if extras is None:
        extras = []
    extras.append(extra)
    return extras

print(add_extra("GPS"))
print(add_extra("child seat"))
