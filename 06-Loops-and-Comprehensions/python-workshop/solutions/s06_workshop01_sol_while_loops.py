"""
Workshop Problem-01: while loops (Fuel Countdown) (solution)

Concepts: while loop, counting down, the -= shorthand, a truthy condition.

Write a program that, for a car:
- Task-1: starting with 4 units of fuel, uses a while loop to print the fuel left
  each turn (like Fuel left: 4) as it drops to 1, burning 1 unit each turn, then
  prints Tank empty.
- Task-2: for a boot holding the items bag, box, cooler, uses while items: (a
  non-empty list is truthy) to print the last item and remove it, until empty.

Expected output:
Fuel left: 4
Fuel left: 3
Fuel left: 2
Fuel left: 1
Tank empty
cooler
box
bag
"""

# Task-1: count the fuel down with -= until the tank is empty
fuel = 4
while fuel >= 1:
    print("Fuel left:", fuel)
    fuel -= 1
print("Tank empty")

# Task-2: loop while the list is non-empty (truthy); pop() removes and returns the last item
items = ["bag", "box", "cooler"]
while items:
    print(items.pop())
