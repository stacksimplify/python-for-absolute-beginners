"""
Practice Problem-01: try / except basics

Concepts: try / except, input().
"""
"""
Problem-1: Write a function `order_cost` that takes a total price and a number of units,
           turns both into whole numbers, and returns the cost of each unit. Wrap the
           risky lines in a try/except so a bad value returns "Could not price this
           order." instead of crashing. Call it with "100" and "4", then "abc" and "4"
           (a missing product with no real price), then "100" and "0" (an out-of-stock
           item with no units), printing each result.

Expected output:
25.0
Could not price this order.
Could not price this order.
"""
"""
Problem-2 (Write a Program): ask the user for a total price and a number of units, pass them
           to `order_cost`, and print the cost of each unit.

Example run (you type 100 then 4): Cost per unit: 25.0
"""
