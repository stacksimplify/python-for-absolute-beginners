"""
Practice Problem-04: break, continue, else, pass (solution)

Concepts: for loop, while loop, break, continue, pass, loop else, input().
"""

"""
Problem-1 (First Bulk Order):
  Write a program that, for the cart quantities 7, -4, 9, 12, 5, skips the
  invalid (negative) quantities, does nothing on the odd quantities, and at the
  first even quantity prints "First bulk order:" followed by that quantity and
  stops looking; if there is no even quantity, it prints "No bulk order" instead.

Expected output: First bulk order: 12
"""
# Problem-1 Task-1: find and print the first even (bulk) quantity
cart_quantities = [7, -4, 9, 12, 5]
for quantity in cart_quantities:
    if quantity < 0:
        continue              # skip invalid quantities
    if quantity % 2 == 0:
        print("First bulk order:", quantity)
        break                 # stop at the first even quantity
    else:
        pass                  # odd quantity; nothing to do yet
else:
    print("No bulk order")

"""
Problem-2 (Write a Program):
  Write a program that keeps asking the user for an order amount until they type
  0, skips any invalid (negative) amount, and for every other amount prints
  "charged:" followed by that amount.

Example run (you type 5, -2, 8, 0): charged: 5 / charged: 8
"""
# Problem-2 Task-1: charge valid amounts until the user types 0
while True:
    amount = int(input("Amount (0 to stop): "))
    if amount == 0:
        break                 # stop on 0
    if amount < 0:
        continue              # skip invalid amounts
    print("charged:", amount)
