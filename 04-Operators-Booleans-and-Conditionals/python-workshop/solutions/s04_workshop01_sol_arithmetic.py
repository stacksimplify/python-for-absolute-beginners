"""
Workshop Problem-01: arithmetic (Car Mileage) (solution)

Concepts: + - * /, //, %, **.

Problem-1. Car mileage:
  Write a program that, for a distance of 555 and fuel of 12:
  Task-1: print the distance plus the fuel.
  Task-2: print the distance divided by the fuel.
  Task-3: print the whole-number part of that division.
  Task-4: print the remainder of that division.
  Task-5: print the fuel raised to the power 2.

Expected output:
567
46.25
46
3
144
"""

distance = 555
fuel = 12
# Task-1: print the distance plus the fuel
print(distance + fuel)
# Task-2: print the distance divided by the fuel
print(distance / fuel)

# Task-3: print the whole-number part of that division
print(distance // fuel)
# Task-4: print the remainder of that division
print(distance % fuel)

# Task-5: print the fuel raised to power 2
print(fuel ** 2)

"""
Problem-2. Price helpers:
  Write a program that prints the absolute value of -50 (size of a price
  drop), then prints the quotient and remainder of 95 divided by 20 together
  as a pair (boxes of 20).

Expected output:
50
(4, 15)
"""
print(abs(-50))
print(divmod(95, 20))
