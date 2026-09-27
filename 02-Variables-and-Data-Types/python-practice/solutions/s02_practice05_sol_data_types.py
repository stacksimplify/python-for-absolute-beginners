"""
Practice Problem-05: data types (solution)

Concepts: the four data types (str, int, float, bool), type(x).__name__.

Problem-1:
  Write a program that stores a book's title ("Python Crash Notes"), pages (96),
  price (14.99), and in_stock (True), one value of each core type. Print all four
  values, then print each value's type name (in the same order).

Expected output:
Python Crash Notes
96
14.99
True
str
int
float
bool
"""

# Problem-1 Task-1: store four core-type values, print values then type names
title = "Python Crash Notes"
pages = 96
price = 14.99
in_stock = True

print(title)
print(pages)
print(price)
print(in_stock)

print(type(title).__name__)
print(type(pages).__name__)
print(type(price).__name__)
print(type(in_stock).__name__)

"""
Problem-2:
  Write a program that stores amount = 12.3456 and:
    Task-1: print it rounded to 2 decimal places.
    Task-2: print it rounded to 1 decimal place.
    Task-3: print it rounded to a whole number (no decimals).

Expected output:
12.35
12.3
12
"""
amount = 12.3456
# Problem-2 Task-1: print rounded to 2 decimals
print(round(amount, 2))
# Problem-2 Task-2: print rounded to 1 decimal
print(round(amount, 1))
# Problem-2 Task-3: print rounded to a whole number
print(round(amount))
