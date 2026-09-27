"""
Workshop Problem-01: making strings (Car Label) (solution)

Concepts: joining strings with +, len().

Write a program that joins a brand (Honda) and a model (Civic) into a label with
a space between them, prints the label, and prints its length.

Expected output:
Honda Civic
11
"""

brand = "Honda"
model = "Civic"
label = brand + " " + model
print(label)
print(len(label))
