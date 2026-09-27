"""
Workshop Problem-03: finally (Rental Cost) (solution)

Concepts: finally always runs.
"""

"""
Problem-1: Reuse `cost_per_day` with a combined except that returns "Please enter valid
           numbers.", and add a finally block that always prints "Rental closed." Call it with
           "300" and "3", then with "300" and "0", printing each result.

Expected output:
Rental closed.
100.0
Rental closed.
Please enter valid numbers.
"""
# Problem-1 Task-1: cost_per_day with a finally that always runs
def cost_per_day(total_cost, days):
    try:
        cost = int(total_cost)
        count = int(days)
        return cost / count
    except (ValueError, ZeroDivisionError):
        return "Please enter valid numbers."
    finally:
        print("Rental closed.")
# Problem-1 Task-2: print result for valid rental
print(cost_per_day("300", "3"))
# Problem-1 Task-3: print result for zero days
print(cost_per_day("300", "0"))
