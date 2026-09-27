"""
Practice Problem-04: raise

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
"""
Problem-2 (Write a Program): ask the user for a total price and a number of units. Pass them
           to `order_cost` inside a try/except; print the cost of each unit, or the caught error.

Example run (you type 100 then 0): Caught a problem: there must be at least one unit
"""
