"""
Workshop Problem-04: break, continue, else, pass (Find the First Affordable Car) (solution)

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

# Task-1: first affordable car with continue / break / else
prices = [30000, 0, 18000, 9000, 25000]
budget = 12000
for price in prices:
    if price == 0:
        continue              # car already sold; skip it
    if price <= budget:
        print("Buying at:", price)
        break
else:
    print("Nothing in budget")

# Task-2: list available cars; a sold car (0) hits pass, which does nothing
for price in prices:
    if price == 0:
        pass                  # placeholder: nothing to do for a sold car yet
    else:
        print("Available:", price)

# Task-3: check the fuel gauge with a while loop, break the instant it reads low
fuel = 5
while fuel > 0:
    if fuel == 2:
        print("low fuel, stopping")
        break
    print("fuel:", fuel)
    fuel -= 1

# Task-4: no break fires, so the while else runs: compare with Task-3, where the break skipped it
fuel = 3
while fuel > 0:
    print("fuel:", fuel)
    fuel -= 1
else:
    print("made it home")
