r"""
Workshop Problem-03: print options (Car Specs) (solution)

Concepts: print() with sep and end, escapes \n and \t.
"""

"""
Problem-1: Write a program that prints "Toyota", "Camry", "2021" on one line, separated by " | ".

Expected output: Toyota | Camry | 2021
"""
# Problem-1 Task-1: print three values separated by pipe
print("Toyota", "Camry", 2021, sep=" | ")

"""
Problem-2: Write a program that prints "Checking" and "ok" on the same line, joined by "...".

Expected output: Checking...ok
"""
# Problem-2 Task-1: join two words with ... on one line
print("Checking", end="...")
print("ok")

"""
Problem-3: Write a program that prints a two-line table from a single string: "Brand:" then "Toyota", and "Year:" then "2021", lined up with tabs.

Expected output:
Brand:	Toyota
Year:	2021
"""
# Problem-3 Task-1: print a tab-aligned two-line table
print("Brand:\tToyota\nYear:\t2021")
