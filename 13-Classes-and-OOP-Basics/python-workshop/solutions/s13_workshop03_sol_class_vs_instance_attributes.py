"""
Workshop Problem-03: class vs instance attributes (Car)

Concepts: class attribute shared by all, instance attributes per object.

Write a program with one class Car:
Task-1: write the class with a class attribute wheels set to 4 and an
    __init__ taking brand and year.
Task-2: create c1 (Mazda, 2020) and c2 (Tesla, 2023), print c1.wheels, then
    print Car.wheels straight from the class.
Task-3: change c1.year to 2021, then print both cars' years.

Expected output:
4
4
2021
2023
"""

# Task-1: the class, with a shared class attribute and per-object data
class Car:
    wheels = 4

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

# Task-2: both cars, then the class attribute read from the object and from the class
c1 = Car("Mazda", 2020)
c2 = Car("Tesla", 2023)
print(c1.wheels)
print(Car.wheels)

# Task-3: an instance attribute changes for c1 only
c1.year = 2021
print(c1.year)
print(c2.year)
