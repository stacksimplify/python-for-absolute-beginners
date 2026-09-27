"""
Workshop Problem-04: methods (Car)

Concepts: a method uses self, returning vs printing.

Write a program with one class Car:
Task-1: write the class with an __init__ that takes a brand and a speed, a
    method accelerate that adds an amount to the speed, and a method status
    that RETURNS <brand> at <speed> km/h.
Task-2: create c1 (Mazda, 40), accelerate it by 20, and print
    c1.status().

Expected output:
Mazda at 60 km/h
"""

# Task-1: the class, with accelerate() that ACTS and status() that RETURNS
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

    def status(self):
        return f"{self.brand} at {self.speed} km/h"

# Task-2: create the car, accelerate it, then print what status() RETURNS
c1 = Car("Mazda", 40)
c1.accelerate(20)
print(c1.status())
