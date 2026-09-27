"""
Practice Problem-10: lambda (solution)

Concepts: lambda, a one-line anonymous function (lambda args: expression), passing a
lambda as a key= to sorted() and to max().
"""

"""
Problem-1. A One-Line Function:
  A lambda has no name, so to name a function you use `def`. Build a one-line `lambda` that takes `n` and gives back `n` multiplied by 2, and call it directly with 7 and then with 10, printing each result. Do not store the lambda in a variable.

Expected output:
14
20
"""
# Problem-1: build the lambda and call it on the spot, with no name
print((lambda n: n * 2)(7))
print((lambda n: n * 2)(10))

"""
Problem-2. Sort Products by Name Length:
  For the list of product names "pear", "fig", "banana", "kiwi", print the names sorted from shortest to longest, using `sorted()` with a `lambda` as the `key=`.

Expected output:
['fig', 'pear', 'kiwi', 'banana']
"""
# Problem-2: sort names by length with a lambda key
product_names = ["pear", "fig", "banana", "kiwi"]
print(sorted(product_names, key=lambda name: len(name)))

"""
Problem-3. Sort Products by Price, and Find the Dearest:
  Task-1: For the list of (product, price) pairs ("Monitor", 200), ("Mouse", 80), ("Keyboard", 95), print the pairs sorted by price (the second item of each pair), using `sorted()` with a `lambda` as the `key=`.
  Task-2: Print the single most expensive pair, using `max()` with the same `lambda` as the `key=`.

Expected output:
[('Mouse', 80), ('Keyboard', 95), ('Monitor', 200)]
('Monitor', 200)
"""
# Problem-3 Task-1: sort pairs by price with a lambda key
priced_items = [("Monitor", 200), ("Mouse", 80), ("Keyboard", 95)]
print(sorted(priced_items, key=lambda pair: pair[1]))
# Problem-3 Task-2: the dearest pair, same lambda as the key
print(max(priced_items, key=lambda pair: pair[1]))
