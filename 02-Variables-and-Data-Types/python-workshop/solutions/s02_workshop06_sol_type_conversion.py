"""
Workshop Problem-06: type conversion (Car Count) (solution)

Concepts: int(), float(), str().

Write a program that makes three conversions:
  Task-1: the number of cars in a lot arrives as the text "8". Turn it into a whole
          number, add the 2 cars that just arrived, and print the new total.
  Task-2: turn the text "1499.50" into a decimal and print it.
  Task-3: build the text "cars 8" by joining "cars " with the number 8, and print it.

Expected output:
10
1499.5
cars 8
"""

# Task-1: convert the text count to a number, add the new cars, print
cars = int("8")
print(cars + 2)

# Task-2: convert text to float and print
print(float("1499.50"))
# Task-3: join text with a number and print
print("cars " + str(cars))
