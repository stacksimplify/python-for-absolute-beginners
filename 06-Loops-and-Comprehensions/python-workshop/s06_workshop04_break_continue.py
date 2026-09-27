"""
Workshop Problem-04: break, continue, else, pass (Find the First Affordable Car)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: for loop, continue, break, loop else, pass, a while loop with break.

Write a program that, for a lot with the prices 30000, 0, 18000, 9000, 25000 (a 0
means the car is sold) and a budget of 12000:
- Task-1: skip any sold car and at the first car within budget (12000 or less)
  print Buying at: followed by that price and stop looking; if no car fits, print
  Nothing in budget instead.
- Task-2: loop the same prices again and, for a sold car (0), do nothing yet with
  pass (a placeholder branch); for every other car print Available: and its price.
- Task-3: starting with 5 units of fuel, use a while loop to print fuel: F and burn
  1 unit each check, but break the instant the gauge reads 2 (low fuel, stopping).

Expected output:
Buying at: 9000
Available: 30000
Available: 18000
Available: 9000
Available: 25000
fuel: 5
fuel: 4
fuel: 3
low fuel, stopping
"""

"""
Task-4: a while that finishes on its own

Starting with 3 units of fuel, print fuel: F and burn 1 unit each turn.
Add an else to the while that prints made it home.
Because no break fires this time, the else runs.

Expected output:
fuel: 3
fuel: 2
fuel: 1
made it home
"""
