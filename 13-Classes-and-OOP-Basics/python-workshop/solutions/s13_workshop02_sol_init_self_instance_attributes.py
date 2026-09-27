"""
Workshop Problem-02: __init__ and attributes (Car)

Concepts: __init__, self, instance attributes.

Write a program with one class Car:
Task-1: write the class with an __init__ that takes a brand and a year.
Task-2: create c1 (Mazda, 2020) and print its brand and year on one line.
Task-3: create c2 (Tesla, 2023) and print its own brand and year on one
    line.

Expected output:
Mazda 2020
Tesla 2023
"""

# Task-1: the class, with __init__ storing each value on self
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# Task-2: create c1 and print its data
c1 = Car("Mazda", 2020)
print(c1.brand, c1.year)

# Task-3: create c2, which keeps its own data
c2 = Car("Tesla", 2023)
print(c2.brand, c2.year)
