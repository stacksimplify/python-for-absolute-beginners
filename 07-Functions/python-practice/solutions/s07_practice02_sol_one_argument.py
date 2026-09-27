"""
Practice Problem-02: one argument (solution)

Concepts: parameters vs arguments, passing a value, passing a variable, positional arguments (left to right), input().
"""

"""
Problem-1. Greet a Customer:
  Write a function `greet_customer` that takes a `customer` and prints "Hello, <customer>!". Call it with "Ben", then with "Joe", then store "Zoe" in a variable `shopper` and call it with that variable.

Expected output:
Hello, Ben!
Hello, Joe!
Hello, Zoe!
"""
# Problem-1: greet each customer by value and by variable
def greet_customer(customer):
    print(f"Hello, {customer}!")

greet_customer("Ben")
greet_customer("Joe")
shopper = "Zoe"
greet_customer(shopper)

"""
Problem-2. Positional Arguments:
  Write a function `label_product` that takes a `product` and a `section` and prints "<product> is in <section>". Call it with "Mouse" and "Audio" in that order (so the first value fills `product` and the second fills `section`), then call it again with "Cable" and "Video".

Expected output:
Mouse is in Audio
Cable is in Video
"""
# Problem-2: label products with positional arguments
def label_product(product, section):
    print(f"{product} is in {section}")

label_product("Mouse", "Audio")
label_product("Cable", "Video")

"""
Problem-3 (Write a Program). Greet Any Shopper:
  Write a program that asks the user for a shopper name, then calls `greet_customer` with what they typed.

Example run:
Shopper name: Ravi
Hello, Ravi!
"""
# Problem-3: read the name, then reuse the same function
shopper_name = input("Shopper name: ")
greet_customer(shopper_name)
