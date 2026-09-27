"""
Workshop Problem-07: comprehensions (Car Price Lists)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: list comprehension, a filter condition, dict comprehension (plain and filtered), set comprehension, an if/else in a comprehension.

Write a program that:
  Task-1: for the prices 15000, 8000, 23000, use a list comprehension to print a list of each price plus 500.
  Task-2: for the same prices, use a list comprehension and a filter to print a list of only the prices over 10000.
  Task-3: for the cars Audi, BMW, Kia, use a dict comprehension to print a dict mapping each car to the length of its name.
  Task-4: with a dict comprehension and a filter, map only the prices over 10000 to their discounted value (price - 1000).
  Task-5: for the same cars, use a set comprehension to print the sorted distinct name lengths.
  Task-6: with an if/else in a list comprehension, label each price "premium" (10000 or more) or "budget".

Expected output:
[15500, 8500, 23500]
[15000, 23000]
{'Audi': 4, 'BMW': 3, 'Kia': 3}
{15000: 14000, 23000: 22000}
[3, 4]
['premium', 'budget', 'premium']
"""

"""
Problem-2. Discount with a comprehension:
  You will see map()/filter() do this in other code; we prefer comprehensions.
  Write a program that, for prices holding 100 and 200, uses a comprehension to
  take 10% off each price and prints the resulting list.

Expected output: [90.0, 180.0]
"""
