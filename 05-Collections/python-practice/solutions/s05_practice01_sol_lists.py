"""
Practice Problem-01: lists (solution)

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
catalog_prices = [40, 95, 25]
catalog_prices.append(60)
# Problem-1 Task-1: print prices sorted low to high
catalog_prices.sort()
print(catalog_prices)
# Problem-1 Task-2: print the highest price
print(catalog_prices[-1])

"""
Problem-2. Split and Join:
  Write a program that:
    Task-1: split the product code "TEC-2024-15" on "-" into a list and print the list.
    Task-2: join the label words "wireless", "gaming", "mouse" with a single space into one string and print it.

Expected output:
['TEC', '2024', '15']
wireless gaming mouse
"""
# Problem-2 Task-1: split the product code on "-"
product_code = "TEC-2024-15"
print(product_code.split("-"))
# Problem-2 Task-2: join the label words with a space
label_words = ["wireless", "gaming", "mouse"]
print(" ".join(label_words))

"""
Problem-3 (Write a Program):
  Write a program that asks for catalog items separated by commas (no spaces), splits the text into a list, prints the list, and then prints "count:" followed by how many items there are.

Example run (you type "mouse,keyboard,monitor"): ['mouse', 'keyboard', 'monitor'] / count: 3
"""
# Problem-3: read items, split into a list, print list and count
entered = input("Items separated by commas (no spaces): ")
catalog_items = entered.split(",")
print(catalog_items)
print("count:", len(catalog_items))

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
cart = ["mouse", "keyboard"]
# Problem-4 Task-1: insert "monitor" at index 1
cart.insert(1, "monitor")
print(cart)
# Problem-4 Task-2: extend the cart with two items
cart.extend(["cable", "webcam"])
print(cart)
# Problem-4 Task-3: pop the last item and print it
removed = cart.pop()
print(removed)
# Problem-4 Task-4: clear the cart
cart.clear()
print(cart)

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
order_statuses = ["pending", "shipped", "pending", "delivered"]
# Problem-5 Task-1: print the index of "shipped"
print(order_statuses.index("shipped"))
# Problem-5 Task-2: count how many times "pending" appears
print(order_statuses.count("pending"))
# Problem-5 Task-3: copy the list, append to the copy only, print both
statuses_copy = order_statuses.copy()
statuses_copy.append("returned")
print(order_statuses)
print(statuses_copy)
# Problem-5 Task-4: reverse the original list
order_statuses.reverse()
print(order_statuses)

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
price_list = [15, 30, 45, 60, 75]
# Problem-6 Task-1: print the slice from index 1 to 4
print(price_list[1:4])
# Problem-6 Task-2: print whether 45 is in the list
print(45 in price_list)
# Problem-6 Task-3: print whether 99 is not in the list
print(99 not in price_list)

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
order_rows = [["mouse", 25], ["keyboard", 45], ["monitor", 120]]
# Problem-7 Task-1: print the whole first row
print(order_rows[0])
# Problem-7 Task-2: print the product name from the first row
print(order_rows[0][0])
# Problem-7 Task-3: print the price from the last row
print(order_rows[2][1])
