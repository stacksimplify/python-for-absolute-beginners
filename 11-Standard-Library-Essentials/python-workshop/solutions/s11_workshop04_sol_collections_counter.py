"""
Workshop Problem-04: collections.Counter (Brand Tally) (solution)

Concepts: Counter, most_common.

Write a program that, for the list of brands Mazda, Tesla, Mazda, Honda, Tesla, Mazda, prints these lines:
  Task-1: how many times each brand appears (use Counter).
  Task-2: the single most frequent brand (use most_common(1)).

Expected output:
Counter({'Mazda': 3, 'Tesla': 2, 'Honda': 1})
[('Mazda', 3)]
"""
from collections import Counter

brands = ["Mazda", "Tesla", "Mazda", "Honda", "Tesla", "Mazda"]
# Task-1: count and print how many times each brand appears
counts = Counter(brands)
print(counts)
# Task-2: print the single most frequent brand
print(counts.most_common(1))
