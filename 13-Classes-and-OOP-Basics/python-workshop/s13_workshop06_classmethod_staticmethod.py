"""
Workshop Problem-06: class methods and static methods (Car)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

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
