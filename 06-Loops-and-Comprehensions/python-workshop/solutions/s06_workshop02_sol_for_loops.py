"""
Workshop Problem-02: for loops (Car Lot Totals) (solution)

Concepts: for loop, a running total, counting with if, unpacking a tuple in the loop.

Write a program that, for a car lot with the prices 15000, 8000, 23000, 12000:
  Task-1: print each price on its own line with a for loop.
  Task-2: print total: followed by the sum of the prices.
  Task-3: print over 10000: followed by how many cars cost more than 10000 (for + if).
  Task-4: for a list of (brand, price) pairs, unpack each and print brand: price.

Expected output: the 4 prices, total: 58000, over 10000: 3, Audi: 40000, BMW: 8000
"""

# one pass prints each price and adds it to the running total
prices = [15000, 8000, 23000, 12000]
total = 0
# Task-1: print each price with a for loop
for price in prices:
    print(price)
    total += price
# Task-2: print the total of the prices
print("total:", total)

# Task-3: count the cars over 10000 with a for + if
over = 0
for price in prices:
    if price > 10000:
        over += 1
print("over 10000:", over)

# Task-4: unpack each (brand, price) pair right in the for header
cars = [("Audi", 40000), ("BMW", 8000)]
for brand, price in cars:
    print(f"{brand}: {price}")
