"""
Workshop Problem-04: raise (Rental Cost)

Concepts: raise, except ... as err.
"""
"""
Problem-1: Reuse `cost_per_day`, turning both inputs into whole numbers, then enforce two rules
           before dividing: if the total cost is negative, raise a ValueError with "cost cannot
           be negative"; if there is less than one day, raise a ValueError with "there must be at
           least one day". Otherwise return the cost for each day. Print the result of calling it
           with "300" and "3". Then call it with "300" and "0" inside a try/except that catches
           the error as `err`, and print "Caught:" followed by the error. Finally print
           "Still running.".

Expected output:
100.0
Caught: there must be at least one day
Still running.
"""
