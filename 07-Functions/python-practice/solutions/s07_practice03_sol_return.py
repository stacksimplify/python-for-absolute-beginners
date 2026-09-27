"""
Practice Problem-03: return (solution)

Concepts: return a value to reuse it, print vs return (None), return a True/False answer.
"""

"""
Problem-1. Return and Reuse:
  Write a function `order_total` that takes a `price` and a `quantity` and returns their product. Call it with 2 and 3, store the result in `total_due`, print `total_due`, then print `total_due` multiplied by 10.

Expected output:
6
60
"""
# Problem-1: return price times quantity, then reuse it
def order_total(price, quantity):
    return price * quantity
total_due = order_total(2, 3)
print(total_due)
print(total_due * 10)

"""
Problem-2. Print vs Return:
  Write a function `print_receipt_line` that takes a `price` and a `quantity` and only PRINTS their product (it has no return, so it hands back None). Call it with 75 and 4, store what it hands back in `handed_back`, and print `handed_back`.

Expected output:
300
None
"""
# Problem-2: print only, so the call hands back None
def print_receipt_line(price, quantity):
    print(price * quantity)
handed_back = print_receipt_line(75, 4)
print(handed_back)

"""
Problem-3. A Yes or No Answer:
  Write a function `in_budget` that takes an `amount` and returns whether `amount` is 100 or less (a True/False answer). Call it with 90 and print the result, then call it with 150 and print the result.

Expected output:
True
False
"""
# Problem-3: return a True/False budget answer
def in_budget(amount):
    return amount <= 100
print(in_budget(90))
print(in_budget(150))
