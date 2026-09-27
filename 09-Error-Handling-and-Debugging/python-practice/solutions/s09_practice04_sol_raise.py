"""
Practice Problem-04: raise (solution)

Concepts: raise, except ... as err, input().
"""

"""
Problem-1: Reuse `order_cost`, turning both inputs into whole numbers, then enforce two rules
           before dividing: if the price is negative, raise a ValueError with "price cannot be
           negative"; if there is less than one unit, raise a ValueError with "there must be
           at least one unit". Otherwise return the cost of each unit. Print the result of
           calling it with "100" and "4". Then call it with "100" and "0" inside a try/except
           that catches the error as `err`, and print "Caught a problem:" followed by the error.
           Finally print "Still running.".

Expected output:
25.0
Caught a problem: there must be at least one unit
Still running.
"""
# Problem-1 Task-1: order_cost that raises ValueError on bad rules
def order_cost(total_price, units):
    price = int(total_price)
    units_count = int(units)
    if price < 0:
        raise ValueError("price cannot be negative")
    if units_count < 1:
        raise ValueError("there must be at least one unit")
    return price / units_count
# Problem-1 Task-2: print result for valid order
print(order_cost("100", "4"))
# Problem-1 Task-3: call with zero units and catch the error
try:
    order_cost("100", "0")
except ValueError as err:
    print("Caught a problem:", err)
# Problem-1 Task-4: show the program keeps running
print("Still running.")

"""
Problem-2 (Write a Program): ask the user for a total price and a number of units. Pass them
           to `order_cost` inside a try/except; print the cost of each unit, or the caught error.

Example run (you type 100 then 0): Caught a problem: there must be at least one unit
"""
# Problem-2 Task-1: read total price from user
total_in = input("Total price: ")
# Problem-2 Task-2: read number of units from user
units_in = input("Number of units: ")
# Problem-2 Task-3: price the order and catch any error
try:
    print("Cost per unit:", order_cost(total_in, units_in))
except ValueError as err:
    print("Caught a problem:", err)
