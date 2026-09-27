"""
Workshop Problem-06: class methods and static methods (Car) (solution)

Concepts: the decorators @classmethod (an alternate constructor: it receives the
class as cls) and @staticmethod (a related helper: it takes neither self nor cls),
and asking the helper about an object the class method just built.

Write a program with one class Car:
Task-1: write the class with an __init__ that takes a brand and a year, a
    @classmethod from_dict(cls, data) that builds a Car from a dict with
    keys brand and year, and a @staticmethod is_vintage(year) that returns
    True when year is below 1990.
Task-2: print Car.is_vintage(1985).
Task-3: build a car from {"brand": "Mazda", "year": 2020} using from_dict,
    and print its brand and year.
Task-4: print whether that car is vintage, by passing its year to
    is_vintage.

Expected output:
True
Mazda 2020
False
"""

# Task-1: the class, with the two decorated methods
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    @classmethod
    def from_dict(cls, data):
        return cls(data["brand"], data["year"])

    @staticmethod
    def is_vintage(year):
        return year < 1990

# Task-2: a static helper, no object needed
print(Car.is_vintage(1985))

# Task-3: an alternate constructor that builds a Car from a dict
c = Car.from_dict({"brand": "Mazda", "year": 2020})
print(c.brand, c.year)

# Task-4: the same static helper, now asked about the car we just built
print(Car.is_vintage(c.year))
