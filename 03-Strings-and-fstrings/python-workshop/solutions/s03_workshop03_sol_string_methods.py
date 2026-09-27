"""
Workshop Problem-03: string methods (Plate Case) (solution)

Concepts: upper(), replace().

Problem-1. Plate case:
  Write a program that, for a plate "tn09xy5678":
  Task-1: print it in UPPER CASE.
  Task-2: print it again with "tn" replaced by "TN".

Expected output:
TN09XY5678
TN09xy5678
"""

plate = "tn09xy5678"
# Problem-03 Task-1: print the plate in upper case
print(plate.upper())

# Problem-03 Task-2: print plate with "tn" replaced by "TN"
print(plate.replace("tn", "TN"))

"""
Problem-2. Plate digits:
  Write a program that prints whether "5678" is all digits and whether "tn09" is
  all digits.

Expected output:
True
False
"""
print("5678".isdigit())
print("tn09".isdigit())
