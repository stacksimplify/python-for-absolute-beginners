"""
Practice Problem-04: parameters and logic

Concepts: many parameters (positional), if/elif/else inside a function that
          returns a different value per case, a loop inside a function that
          builds up and returns a result.
"""
"""
Problem-1. Many Parameters (Shipping Fee):
  Write a function `shipping_fee` that takes a `weight` and a `rate` and returns their product. Call it with 4 and 3 and print the result, then call it with 10 and 2 and print the result.

Expected output:
12
20
"""
"""
Problem-2. Logic Inside a Function (Discount Tier):
  Write a function `discount_tier` that takes a `spend` and returns a tier label: "A" for 90 or more, "B" for 75 or more, "C" for 50 or more, otherwise "F". Call it with 95, with 80, and with 40, printing each result.

Expected output:
A
B
F
"""
"""
Problem-3. Loop Inside a Function (Cart Sum):
  Write a function `cart_sum` that takes a list `line_prices` and returns the total of its items by adding them up in a loop. Call it with [15, 25, 35] and print the result, then call it with [5, 5, 5, 5] and print the result.

Expected output:
75
20
"""
"""
Problem-4. Stop at the First Match (Over Budget):
  Write a function `any_over_budget` that takes a list `prices` and a `limit` and returns True the moment it finds the first price above `limit` (return right there, do not keep checking), otherwise returns False after the loop. Call it with [20, 45, 90] and 50 and print the result, then call it with [20, 30, 40] and 50 and print the result.

Expected output:
True
False
"""
"""
Problem-5 (Write a Program). Shipping for Any Order:
  Write a program that asks the user for a weight and a rate (both whole numbers), calls `shipping_fee` with them, and prints "Shipping:" followed by the fee.

Example run:
Weight: 6
Rate: 4
Shipping: 24
"""
