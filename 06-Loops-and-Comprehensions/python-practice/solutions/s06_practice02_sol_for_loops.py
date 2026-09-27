"""
Practice Problem-02: for loops (solution)

Concepts: for loop, a running total, len(), split(), input().
"""

"""
Problem-1 (Total the Bill):
  Write a program that, for the order line prices 50, 120, 65, 85:
    Task-1: print each price on its own line with a for loop.
    Task-2: print total: followed by the sum of the prices.
    Task-3: print average: followed by the sum divided by the number of prices.

Expected output: 50, 120, 65, 85, total: 320, average: 80.0
"""
order_prices = [50, 120, 65, 85]
bill = 0
# Problem-1 Task-1: print each price with a for loop
for price in order_prices:
    print(price)
    bill += price
# Problem-1 Task-2: print the total of the prices
print("total:", bill)
# Problem-1 Task-3: print the average price
print("average:", bill / len(order_prices))

"""
Problem-2 (Write a Program):
  Write a program that asks the user for product names separated by spaces, then
  uses a for loop to print each product on its own line.

Example run (you type "mouse keyboard monitor"): mouse / keyboard / monitor
"""
# Problem-2 Task-1: print each product the user typed
product_line = input("Enter products separated by spaces: ")
for product in product_line.split():
    print(product)

"""
Problem-3. Loop a product code:
  Define a variable product_code with the value B4X2. Write a program that prints
  each character of the code on its own line.

Expected output:
B
4
X
2
"""
# Problem-3 Task-1: a string is a sequence, so a for loop reads it one character at a time
product_code = "B4X2"
for character in product_code:
    print(character)
