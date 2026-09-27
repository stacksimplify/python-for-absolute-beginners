"""
Practice Problem-01: while loops (solution)
Concepts: while loop, counting down, the -= shorthand, a running total, a truthy condition, input().
"""

"""
Problem-1: Pack the Cart
Write a program that, starting from items_left set to 10, uses a while loop to
print items_left on its own line as it counts down to 1, then prints Cart packed!

Expected output: 10, 9, 8 ... 1, then Cart packed!
"""
# Problem-1 Task-1: count down items and pack the cart
items_left = 10
while items_left >= 1:
    print(items_left)
    items_left -= 1
print("Cart packed!")

"""
Problem-2: Loyalty Points
Write a program that adds up loyalty points earned over 5 days (1 point on day 1,
2 on day 2, up to 5 on day 5) into a running total with a while loop, then prints
Points: followed by the total.

Expected output: Points: 15
"""
# Problem-2 Task-1: accumulate the daily points into one running total
total = 0
day = 1
while day <= 5:
    total += day
    day += 1
print("Points:", total)

"""
Problem-3: Empty the Shelf
Write a program that, for a shelf list holding milk, eggs, bread, uses while shelf:
(a non-empty list is truthy) to print the last item and then remove it, until the
shelf is empty.

Expected output:
bread
eggs
milk
"""
# Problem-3 Task-1: loop while the list is non-empty (truthy); pop() removes and returns the last item
shelf = ["milk", "eggs", "bread"]
while shelf:
    print(shelf.pop())

"""
Problem-4 (Write a Program): Dispatch Orders
Write a program that asks the user for a whole number of orders, then counts down
from that number to 1 with a while loop and prints All dispatched.

Example run (you type 3): Orders to dispatch: 3 -> 3, 2, 1, All dispatched
"""
# Problem-4 Task-1: count down from the user's order count
orders = int(input("Orders to dispatch: "))
while orders >= 1:
    print(orders)
    orders -= 1
print("All dispatched")
