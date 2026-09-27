"""
Workshop Problem-03: return (Car Price Check) (solution)

Concepts: return a value to reuse it, return a True/False answer.

Write a function `service_cost` that takes `parts` and `labor` and returns their sum, plus a function `is_affordable` that takes a `price` and a `budget` and returns whether the price is within budget (a True/False answer). Then:
  Task-1: call `service_cost` with 200 and 150, store the result in `cost`, print `cost`, then print `cost` plus 50 (a tax fee).
  Task-2: call `is_affordable` with 350 and 500 and print the result, then call it with 700 and 500 and print the result.

Expected output:
350
400
True
False
"""

# Task-1: return the service cost, then reuse it
def service_cost(parts, labor):
    return parts + labor
cost = service_cost(200, 150)
print(cost)
print(cost + 50)

# Task-2: return a True/False affordability answer
def is_affordable(price, budget):
    return price <= budget
print(is_affordable(350, 500))
print(is_affordable(700, 500))
