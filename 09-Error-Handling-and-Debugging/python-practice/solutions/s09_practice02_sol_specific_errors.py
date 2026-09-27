"""
Practice Problem-02: specific errors (solution)

Concepts: specific except, else, except (A, B).
"""

"""
Problem-1: Reuse `order_cost`, but catch the two problems separately: if the price is not a
           whole number (a bad price input) catch the ValueError and return "Prices must be
           whole numbers."; if the item is out of stock with zero units catch the
           ZeroDivisionError and return "There must be at least one unit in stock." Call it
           with "100" and "4", "abc" and "4", then "100" and "0", printing each result.

Expected output:
25.0
Prices must be whole numbers.
There must be at least one unit in stock.
"""
# Problem-1 Task-1: order_cost catching ValueError and ZeroDivisionError separately
def order_cost(total_price, units):
    try:
        price = int(total_price)
        units_count = int(units)
        return price / units_count
    except ValueError:
        return "Prices must be whole numbers."
    except ZeroDivisionError:
        return "There must be at least one unit in stock."
# Problem-1 Task-2: print result for valid order
print(order_cost("100", "4"))
# Problem-1 Task-3: print result for bad price
print(order_cost("abc", "4"))
# Problem-1 Task-4: print result for zero units
print(order_cost("100", "0"))

"""
Problem-2: Add an else block that runs only when the pricing worked: print "Order priced."
           and then return the cost of each unit. Call it with "100" and "4", then with
           "abc" and "4", printing each result.

Expected output:
Order priced.
25.0
Prices must be whole numbers.
"""
# Problem-2 Task-1: order_cost with an else block on success
def order_cost(total_price, units):
    try:
        price = int(total_price)
        units_count = int(units)
        per_unit = price / units_count
    except ValueError:
        return "Prices must be whole numbers."
    except ZeroDivisionError:
        return "There must be at least one unit in stock."
    else:
        print("Order priced.")
        return per_unit
# Problem-2 Task-2: print result for valid order
print(order_cost("100", "4"))
# Problem-2 Task-3: print result for bad price
print(order_cost("abc", "4"))

"""
Problem-3: When both problems deserve the same reply, catch them together with
           except (ValueError, ZeroDivisionError) and return "Please enter a valid order.".
           Call it with "abc" and "4", then with "100" and "0", printing each result.

Expected output:
Please enter a valid order.
Please enter a valid order.
"""
# Problem-3 Task-1: order_cost catching both errors together
def order_cost(total_price, units):
    try:
        price = int(total_price)
        units_count = int(units)
        return price / units_count
    except (ValueError, ZeroDivisionError):
        return "Please enter a valid order."
# Problem-3 Task-2: print result for bad price
print(order_cost("abc", "4"))
# Problem-3 Task-3: print result for zero units
print(order_cost("100", "0"))
