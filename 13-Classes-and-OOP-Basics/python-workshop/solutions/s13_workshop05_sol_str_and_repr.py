"""
Workshop Problem-05: __str__ and __repr__ (Car) (solution)

Concepts: __str__ friendly, __repr__ exact.

Write a program with one class Car:
Task-1: write the class with an __init__ that takes a brand and a year,
    __str__ returning <brand> (<year>), and __repr__ returning
    Car(brand='<brand>', year=<year>).
Task-2: create c1 (Mazda, 2020) and c2 (Tesla, 2023), and print c1.
Task-3: print a list holding both cars.

Expected output:
Mazda (2020)
[Car(brand='Mazda', year=2020), Car(brand='Tesla', year=2023)]
"""

# Task-1: the class, with both dunder methods
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.brand} ({self.year})"

    def __repr__(self):
        return f"Car(brand={self.brand!r}, year={self.year!r})"

# Task-2: create both cars; print() uses __str__
c1 = Car("Mazda", 2020)
c2 = Car("Tesla", 2023)
print(c1)
# Task-3: a list of objects uses __repr__
print([c1, c2])
