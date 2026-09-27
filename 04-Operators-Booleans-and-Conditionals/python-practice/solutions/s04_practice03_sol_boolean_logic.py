"""
Practice Problem-03: boolean logic (solution)

Concepts: and, or, not, in.

Problem-1: Order Check.
Write a program that, for an order total of 30 and in_stock set to True:
  Task-1: print whether the total is above 25 and it is in stock.
  Task-2: print whether the total is above 40 or it is in stock.
  Task-3: print the opposite of in_stock.
  Task-4: print whether the letter o appears in the word order.

Expected output:
True
True
False
True
"""

total = 30
in_stock = True
# Task-1: total above 25 and in stock
print(total > 25 and in_stock)
# Task-2: total above 40 or in stock
print(total > 40 or in_stock)
# Task-3: print the opposite of in_stock
print(not in_stock)

# Task-4: whether "o" appears in "order"
print("o" in "order")

"""
Problem-2: All In Stock?
  Write a program that, for a list in_stock_flags = [True, False, True] (square
  brackets hold several values at once; lists in full in Section 05), holding the values
  True, False, True:
    Task-1: print whether every item is true.
    Task-2: print whether at least one item is true.

Expected output:
False
True
"""
in_stock_flags = [True, False, True]
# Task-1: whether every item is true
print(all(in_stock_flags))
# Task-2: whether at least one item is true
print(any(in_stock_flags))

"""
Problem-3: More Checks
  Write a program that prints these boolean checks:
    Task-1: whether the letter z does NOT appear in the word store.
    Task-2: for a price of 85, whether it sits between 0 and 100
            inclusive, written as one chained comparison.
    Task-3: the same price check written with and.
    Task-4: whether 2 + 3 equals 5 (the math runs before the comparison).

Expected output:
True
True
True
True
"""
# Task-1: whether "z" is NOT in "store"
print("z" not in "store")
price = 85
# Task-2: price between 0 and 100 as chained comparison
print(0 <= price <= 100)
# Task-3: same price check written with and
print(price >= 0 and price <= 100)
# Task-4: whether 2 + 3 equals 5
print(2 + 3 == 5)
