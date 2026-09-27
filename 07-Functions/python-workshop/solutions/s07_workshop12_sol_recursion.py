"""
Workshop Problem-12: recursion (Car Countdown) (solution)

Concepts: recursion (a function that calls itself), base case to stop.
"""

"""
Problem-1: Write a recursive function `laps_to_go` that takes `n`: when `n` is 0 it prints "Race over!" and stops (the base case), otherwise it prints "Laps left: <n>" and counts down from one less. Call it with 3.

Expected output:
Laps left: 3
Laps left: 2
Laps left: 1
Race over!
"""
def laps_to_go(n):
    if n == 0:
        print("Race over!")
        return
    print(f"Laps left: {n}")
    laps_to_go(n - 1)
laps_to_go(3)
