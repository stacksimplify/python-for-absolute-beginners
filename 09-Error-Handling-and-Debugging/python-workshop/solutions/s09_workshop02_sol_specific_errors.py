"""
Workshop Problem-02: specific errors (Rental Cost) (solution)

Concepts: specific except (separate blocks).
"""

"""
Problem-1: Reuse `cost_per_day`, but catch the two problems separately: if the values are not
           whole numbers catch the ValueError and return "Cost and days must be whole numbers.";
           if there are zero days catch the ZeroDivisionError and return "There must be at least
           one day." Call it with "300" and "3", "abc" and "3", then "300" and "0", printing
           each result.

Expected output:
100.0
Cost and days must be whole numbers.
There must be at least one day.
"""
# Problem-1 Task-1: cost_per_day catching ValueError and ZeroDivisionError separately
def cost_per_day(total_cost, days):
    try:
        cost = int(total_cost)
        count = int(days)
        return cost / count
    except ValueError:
        return "Cost and days must be whole numbers."
    except ZeroDivisionError:
        return "There must be at least one day."
# Problem-1 Task-2: print result for valid rental
print(cost_per_day("300", "3"))
# Problem-1 Task-3: print result for bad cost
print(cost_per_day("abc", "3"))
# Problem-1 Task-4: print result for zero days
print(cost_per_day("300", "0"))
