"""
Practice Problem-01: lists

Concepts: lists (append, insert, extend, pop, clear, sort, reverse, indexing, slicing, in / not in, index / count, copy, nested lists, split(), join(), input()).
"""
"""
Problem-1. Catalog Prices:
  Write a program that, starting from the product prices 40, 95, 25 with 60 added in:
    Task-1: print the prices sorted from lowest to highest.
    Task-2: print the highest price.

Expected output:
[25, 40, 60, 95]
95
"""
"""
Problem-2. Split and Join:
  Write a program that:
    Task-1: split the product code "TEC-2024-15" on "-" into a list and print the list.
    Task-2: join the label words "wireless", "gaming", "mouse" with a single space into one string and print it.

Expected output:
['TEC', '2024', '15']
wireless gaming mouse
"""
"""
Problem-3 (Write a Program):
  Write a program that asks for catalog items separated by commas (no spaces), splits the text into a list, prints the list, and then prints "count:" followed by how many items there are.

Example run (you type "mouse,keyboard,monitor"): ['mouse', 'keyboard', 'monitor'] / count: 3
"""

"""
Problem-4. Add and Remove Items:
  Write a program that, starting from the cart items "mouse", "keyboard":
    Task-1: insert "monitor" at index 1 and print the cart.
    Task-2: extend the cart with ["cable", "webcam"] and print the cart.
    Task-3: remove the last item with pop() and print what was removed.
    Task-4: clear the cart and print it.

Expected output:
['mouse', 'monitor', 'keyboard']
['mouse', 'monitor', 'keyboard', 'cable', 'webcam']
webcam
[]
"""

"""
Problem-5. Find, Copy, and Reorder:
  Write a program that, starting from the order statuses "pending", "shipped", "pending", "delivered":
    Task-1: print the index of "shipped".
    Task-2: print how many times "pending" appears.
    Task-3: make a copy of the list, append "returned" to the copy only, then print the original list and the copy.
    Task-4: reverse the original list and print it.

Expected output:
1
2
['pending', 'shipped', 'pending', 'delivered']
['pending', 'shipped', 'pending', 'delivered', 'returned']
['delivered', 'pending', 'shipped', 'pending']
"""

"""
Problem-6. Slice and Membership:
  Write a program that, for the price list 15, 30, 45, 60, 75:
    Task-1: print the slice from index 1 up to (but not including) index 4.
    Task-2: print whether 45 is in the list.
    Task-3: print whether 99 is not in the list.

Expected output:
[30, 45, 60]
True
True
"""

"""
Problem-7. Nested Lists:
  Write a program that, starting from the order table order_rows = [["mouse", 25], ["keyboard", 45], ["monitor", 120]] (each inner list is one [product, price] row):
    Task-1: print the whole first row.
    Task-2: print the product name from the first row.
    Task-3: print the price from the last row.

Expected output:
['mouse', 25]
mouse
120
"""
