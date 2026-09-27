"""
Practice Problem-03: finally (solution)

Concepts: finally always runs.
"""

"""
Problem-1: Reuse `order_cost` with a combined except that returns "Please enter a valid order.",
           and add a finally block that always prints "Order closed." Call it with "100" and "4",
           then with "100" and "0", printing each result.

Expected output:
Order closed.
25.0
Order closed.
Please enter a valid order.
"""
# Problem-1 Task-1: order_cost with a finally that always runs
def order_cost(total_price, units):
    try:
        price = int(total_price)
        units_count = int(units)
        return price / units_count
    except (ValueError, ZeroDivisionError):
        return "Please enter a valid order."
    finally:
        print("Order closed.")
# Problem-1 Task-2: print result for valid order
print(order_cost("100", "4"))
# Problem-1 Task-3: print result for zero units
print(order_cost("100", "0"))
