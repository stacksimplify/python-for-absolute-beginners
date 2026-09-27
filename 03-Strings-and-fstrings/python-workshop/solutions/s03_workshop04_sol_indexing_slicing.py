"""
Workshop Problem-04: indexing and slicing (Model Code) (solution)

Concepts: slicing.

Write a program that, for a car code "Civic2022LX", using slices:
  Task-1: print the model (Civic, the first 5 letters).
  Task-2: print the year (2022, the four characters in the middle).
  Task-3: print the trim (LX, the rest at the end).

Expected output:
Civic
2022
LX
"""

code = "Civic2022LX"
# Task-1: print the model (first 5 letters)
print(code[:5])   # Civic (the model)
# Task-2: print the year (four middle characters)
print(code[5:9])  # 2022 (the year)
# Task-3: print the trim (the rest at the end)
print(code[9:])   # LX (the trim)
