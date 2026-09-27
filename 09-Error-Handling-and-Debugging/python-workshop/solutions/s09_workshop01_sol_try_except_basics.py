"""
Workshop Problem-01: try / except basics (Rental Cost) (solution)

Concepts: try / except.
"""

"""
Problem-1: Write a function `cost_per_day` that takes a total cost and a number of days, turns
           both into whole numbers, and returns the cost for each day. Wrap the risky lines in a
           try/except so a bad value returns "Something went wrong with the rental." instead of
           crashing. Call it with "300" and "3", then "abc" and "3", then "300" and "0",
           printing each result.

Expected output:
100.0
Something went wrong with the rental.
Something went wrong with the rental.
"""
# Problem-1 Task-1: define cost_per_day with try/except
def cost_per_day(total_cost, days):
    try:
        cost = int(total_cost)
        count = int(days)
        return cost / count
    except Exception:
        return "Something went wrong with the rental."
# Problem-1 Task-2: print result for valid rental
print(cost_per_day("300", "3"))
# Problem-1 Task-3: print result for bad cost
print(cost_per_day("abc", "3"))
# Problem-1 Task-4: print result for zero days
print(cost_per_day("300", "0"))
