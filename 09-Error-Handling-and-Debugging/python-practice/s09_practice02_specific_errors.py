"""
Practice Problem-02: specific errors

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
"""
Problem-2: Add an else block that runs only when the pricing worked: print "Order priced."
           and then return the cost of each unit. Call it with "100" and "4", then with
           "abc" and "4", printing each result.

Expected output:
Order priced.
25.0
Prices must be whole numbers.
"""
"""
Problem-3: When both problems deserve the same reply, catch them together with
           except (ValueError, ZeroDivisionError) and return "Please enter a valid order.".
           Call it with "abc" and "4", then with "100" and "0", printing each result.

Expected output:
Please enter a valid order.
Please enter a valid order.
"""
