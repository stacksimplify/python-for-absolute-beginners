"""
Practice Problem-01: try / except basics (solution)

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
# Problem-1 Task-1: define order_cost with try/except
def order_cost(total_price, units):
    try:
        price = int(total_price)
        units_count = int(units)
        return price / units_count
    except Exception:
        return "Could not price this order."
# Problem-1 Task-2: print result for valid order
print(order_cost("100", "4"))
# Problem-1 Task-3: print result for bad price
print(order_cost("abc", "4"))
# Problem-1 Task-4: print result for zero units
print(order_cost("100", "0"))

"""
Problem-2 (Write a Program): ask the user for a total price and a number of units, pass them
           to `order_cost`, and print the cost of each unit.

Example run (you type 100 then 4): Cost per unit: 25.0
"""
# Problem-2 Task-1: read total price from user
total_in = input("Total price: ")
# Problem-2 Task-2: read number of units from user
units_in = input("Number of units: ")
# Problem-2 Task-3: print cost per unit
print("Cost per unit:", order_cost(total_in, units_in))
