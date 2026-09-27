"""
Workshop Problem-05: data types (Car Details) (solution)

Concepts: data types (str, int, float, bool), type(x).__name__.

Write a program that stores a car's model ("Tesla Model 3"), seats (5), price (42999.50), and in_stock (True), one value of each core type. Print all four values, then print each value's type name.

Expected output:
Tesla Model 3
5
42999.5
True
str
int
float
bool
"""

model = "Tesla Model 3"
seats = 5
price = 42999.50
in_stock = True

print(model)
print(seats)
print(price)
print(in_stock)

print(type(model).__name__)
print(type(seats).__name__)
print(type(price).__name__)
print(type(in_stock).__name__)
