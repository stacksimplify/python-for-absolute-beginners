"""
Practice Problem-03: range (solution)

Concepts: for loop, range(), the step argument, a running total, input(), f-strings.
"""

"""
Problem-1 (Even Shelf Numbers):
  Write a program that uses range() with a step of 2 to print the even shelf
  numbers from 0 to 10, one per line, and then prints "total:" followed by
  their sum.

Expected output: 0, 2, 4, 6, 8, 10, then total: 30
"""
shelf_sum = 0
# Problem-1 Task-1: print even shelf numbers and their total
for shelf in range(0, 11, 2):
    print(shelf)
    shelf_sum += shelf
print("total:", shelf_sum)

"""
Problem-2 (Write a Program), Bulk Price Table:
  Write a program that asks the user for a unit price, then prints the cost for
  1 to 5 units, with each line like 3 units cost 9.

Example run (you type 3): 1 units cost 3 ... 5 units cost 15
"""
# Problem-2 Task-1: print the cost for 1 to 5 units
unit_price = int(input("Enter the unit price: "))
for units in range(1, 6):
    print(f"{units} units cost {unit_price * units}")
