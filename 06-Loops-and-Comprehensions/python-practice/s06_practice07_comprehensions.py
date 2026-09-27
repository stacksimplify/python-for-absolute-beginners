"""
Practice Problem-07: comprehensions

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
"""
Problem-2 (Write a Program):
  Write a program that asks the user for quantities separated by spaces, then
  prints a list of their squares (use a comprehension to turn the text into ints).

Example run (you type "2 3 4"): [4, 9, 16]
"""

"""
Problem-3, Comprehension vs map (reading note):
  Other code often uses map() with a lambda to transform a list. Using a
  comprehension instead, write a program that, for unit_counts holding 1, 2, 3, 4,
  doubles each value and prints the resulting list.

Expected output:
[2, 4, 6, 8]
"""
