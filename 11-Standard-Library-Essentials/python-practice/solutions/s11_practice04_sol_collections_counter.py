"""
Practice Problem-04: collections.Counter (solution)

Concepts: Counter, most_common, input().

Problem (Write a Program, Best-Selling Letter): Write a program that asks the user for a product name, then prints these labeled lines:
                             Task-1: how many times each letter appears in the product name (use Counter).
                             Task-2: the single most frequent letter (use most_common(1)).
                             Task-3: the count of the letter z (index the Counter with "z"). A Counter returns 0 for a letter that is not there.

Example run:
Enter a product name: sensors
letter counts: Counter({'s': 3, 'e': 1, 'n': 1, 'o': 1, 'r': 1})
most common: [('s', 3)]
count of z: 0
"""
from collections import Counter

product_name = input("Enter a product name: ")

# Task-1: count and print how many times each letter appears
letter_tally = Counter(product_name)
print("letter counts:", letter_tally)
# Task-2: print the single most frequent letter
print("most common:", letter_tally.most_common(1))
# Task-3: a Counter returns 0 for a letter that never appeared, instead of an error
print("count of z:", letter_tally["z"])
