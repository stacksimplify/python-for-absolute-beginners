"""
Practice Problem-02: tuples (solution)

Concepts: tuples (create, index, len, immutable, count, index, slice, in / not in, packing, one-item tuple, unpack, swap, list inside a tuple).
"""

"""
Problem-1. A Product Row:
  Write a program that, for the product row product = ("Mouse", 25, "SKU100") (name, price, sku):
    Task-1: print the name (first item), the sku (last item, negative index), and how many fields it has.
    Task-2: unpack the row into name, price, sku and print "Mouse costs 25".

Expected output:
Mouse
SKU100
3
Mouse costs 25
"""
product = ("Mouse", 25, "SKU100")
# Problem-1 Task-1: print name, sku, and field count
print(product[0])
print(product[-1])
print(len(product))
# Problem-1 Task-2: unpack the row and print name costs price
name, price, sku = product
print(name, "costs", price)

"""
Problem-2. Product Ratings:
  Write a program that, for the star ratings ratings = (5, 4, 5, 3, 5, 4, 5):
    Task-1: print how many 5-star ratings there are, and the position of the first 3-star.
    Task-2: print the first three ratings (a slice); then the last rating two ways: as a one-item tuple (ratings[-1:]) and as a plain number (ratings[-1]).
    Task-3: check that a 3-star rating is in the ratings (in), and that a 1-star rating is not (not in).

Expected output:
4
3
(5, 4, 5)
(5,)
5
True
True
"""
ratings = (5, 4, 5, 3, 5, 4, 5)
# Problem-2 Task-1: count 5-star and find position of the first 3-star
print(ratings.count(5))
print(ratings.index(3))
# Problem-2 Task-2: slice the first three, then the last two ways
print(ratings[0:3])
print(ratings[-1:])
print(ratings[-1])
# Problem-2 Task-3: membership checks with in and not in
print(3 in ratings)
print(1 not in ratings)

"""
Problem-3. Build Tuples:
  Write a program that:
    Task-1: build a product row row from the name "Keyboard" and the price 45, writing
    no brackets around them (packing), and print it.
    Task-2: make a one-item tuple holding just the price 45 (a trailing comma is required), and a plain (45) with no comma; print both type names.

Expected output:
('Keyboard', 45)
tuple int
"""
# Problem-3 Task-1: pack a row without brackets
row = "Keyboard", 45
print(row)
# Problem-3 Task-2: one-item tuple vs plain value, print both type names
one_price = (45,)
not_a_tuple = (45)
print(type(one_price).__name__, type(not_a_tuple).__name__)

"""
Problem-4. Fix Swapped Prices:
  Write a program that, for prices = (45, 25) (the mouse and keyboard prices, entered the wrong way round):
    Task-1: unpack prices into mouse and keyboard, then swap them in one line.
    Task-2: since a tuple cannot change, pack the corrected order into a new tuple
    new_prices and print it.
    Task-3: print the original prices tuple to show it did not change.

Expected output:
(25, 45)
(45, 25)
"""
prices = (45, 25)
# Problem-4 Task-1: unpack then swap in one line
mouse, keyboard = prices
mouse, keyboard = keyboard, mouse
# Problem-4 Task-2: build a new corrected tuple and print it
new_prices = (mouse, keyboard)
print(new_prices)
# Problem-4 Task-3: print the original to show it is unchanged
print(prices)

"""
Problem-5. An Order's Item List:
  Write a program that, for the order order = ("SKU100", ["mouse", "pad"]) (a fixed sku and a changeable list of items):
    Task-1: add "cable" to the items list and print the order.
    Task-2: clear the items list, then add "keyboard" and "monitor", and print the order.
    Task-3: print the sku (order[0]) to show the fixed part is unchanged.

Expected output:
('SKU100', ['mouse', 'pad', 'cable'])
('SKU100', ['keyboard', 'monitor'])
SKU100
"""
order = ("SKU100", ["mouse", "pad"])
# Problem-5 Task-1: append to the inner items list and print the order
order[1].append("cable")
print(order)
# Problem-5 Task-2: clear the list, add two items, print the order
order[1].clear()
order[1].append("keyboard")
order[1].append("monitor")
print(order)
# Problem-5 Task-3: print the sku to show the fixed part is unchanged
print(order[0])
