"""
Practice Problem-06: type conversion (solution)

Concepts: int(), float(), str(), input().
"""

"""
Problem-1:
  Write a program that makes three conversions:
    Task-1: turn the text "15" into a whole number, add 10, and print the result.
    Task-2: turn the text "3.5" into a decimal number and print it.
    Task-3: build the text "age 30" by joining "age " with the number 30 and print it.

Expected output:
25
3.5
age 30
"""
# Problem-1 Task-1: convert text to int, add 10, print
quantity = int("15")
print(quantity + 10)
# Problem-1 Task-2: convert text to float and print
print(float("3.5"))
# Problem-1 Task-3: join text with a number and print
print("age " + str(30))

"""
Problem-2 (Write a Program): Write a program that asks the user for two numbers and prints
their sum. (Remember: what the user types comes in as text, so convert it before adding.)

Example run:
Enter the first number: 10
Enter the second number: 20
30
"""
# Problem-2 Task-1: read two numbers and print their sum
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(a + b)

"""
Problem-3 (Write a Program): Write a program that asks for a name and an age, then greets
the user and tells them how old they will be next year, for example "Hi Kalyan, next year
you will be 31".

Example run:
Enter your name: Kalyan
Enter your age: 30
Hi Kalyan, next year you will be 31
"""
# Problem-3 Task-1: read name and age, greet with next-year age
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hi " + name + ", next year you will be " + str(age + 1))
