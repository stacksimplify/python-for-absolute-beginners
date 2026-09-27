"""
Practice Problem-07: comprehensions (solution)

Concepts: list comprehension, a filter condition, dict comprehension (plain and filtered), set comprehension, an if/else in a comprehension, split(), input().
"""

"""
Problem-1 (Six Price Comprehensions):
  Write a program that, for the cart prices 4, 7, 2, 9, 6:
    Task-1: with a list comprehension, print a list of each price doubled.
    Task-2: with a list comprehension and a filter, print a list of only the even prices.
    Task-3: with a dict comprehension, print a dict that maps each price to its square.
    Task-4: with a dict comprehension and a filter, map only the prices over 5 to their squares.
    Task-5: for the ratings 5, 3, 5, 4, 3, use a set comprehension to print the sorted distinct ratings.
    Task-6: with an if/else in a list comprehension, label each price "pricey" (5 or more) or "cheap".

Expected output:
[8, 14, 4, 18, 12]
[4, 2, 6]
{4: 16, 7: 49, 2: 4, 9: 81, 6: 36}
{7: 49, 9: 81, 6: 36}
[3, 4, 5]
['cheap', 'pricey', 'cheap', 'pricey', 'pricey']
"""
cart_prices = [4, 7, 2, 9, 6]
# Problem-1 Task-1: print each price doubled
print([price * 2 for price in cart_prices])
# Problem-1 Task-2: print only the even prices
print([price for price in cart_prices if price % 2 == 0])
# Problem-1 Task-3: map each price to its square
print({price: price * price for price in cart_prices})
# Problem-1 Task-4: a dict comprehension can filter too: only prices over 5
print({price: price * price for price in cart_prices if price > 5})
# Problem-1 Task-5: a set comprehension drops duplicate ratings (sort it, a set is unordered)
ratings = [5, 3, 5, 4, 3]
print(sorted({rating for rating in ratings}))
# Problem-1 Task-6: an if/else inside the comprehension labels each price
print(["pricey" if price >= 5 else "cheap" for price in cart_prices])

"""
Problem-2 (Write a Program):
  Write a program that asks the user for quantities separated by spaces, then
  prints a list of their squares (use a comprehension to turn the text into ints).

Example run (you type "2 3 4"): [4, 9, 16]
"""
# Problem-2 Task-1: print the squares of the user's quantities
qty_text = input("Quantities separated by spaces: ")
quantities = [int(x) for x in qty_text.split()]
print([qty * qty for qty in quantities])

"""
Problem-3, Comprehension vs map (reading note):
  Other code often uses map() with a lambda to transform a list. Using a
  comprehension instead, write a program that, for unit_counts holding 1, 2, 3, 4,
  doubles each value and prints the resulting list.

Expected output:
[2, 4, 6, 8]
"""
# Problem-3 Task-1: double each value with a comprehension instead of map
unit_counts = [1, 2, 3, 4]
print([x * 2 for x in unit_counts])
