"""
Workshop Problem-04: raise (Rental Cost) (solution)

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
# Problem-1 Task-1: cost_per_day that raises ValueError on bad rules
def cost_per_day(total_cost, days):
    cost = int(total_cost)
    count = int(days)
    if cost < 0:
        raise ValueError("cost cannot be negative")
    if count < 1:
        raise ValueError("there must be at least one day")
    return cost / count
# Problem-1 Task-2: print result for valid rental
print(cost_per_day("300", "3"))
# Problem-1 Task-3: call with zero days and catch the error
try:
    cost_per_day("300", "0")
except ValueError as err:
    print("Caught:", err)
# Problem-1 Task-4: show the program keeps running
print("Still running.")
