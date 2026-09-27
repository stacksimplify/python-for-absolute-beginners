"""
Practice Problem-01: define and call (solution)

Concepts: def (no parameters), calling a function with (), docstrings, __doc__,
          define once and call many times.
"""

"""
Problem-1. Define and Call:
  Write a function `print_welcome` that takes no arguments and prints "Welcome to the Online Store!", then call it two times.

Expected output:
Welcome to the Online Store!
Welcome to the Online Store!
"""
# Problem-1: define print_welcome and call it twice
def print_welcome():
    print("Welcome to the Online Store!")

print_welcome()
print_welcome()

"""
Problem-2. A Docstring:
  Write a function `store_tagline` that takes no arguments, carries the docstring "Print the store tagline.", and prints "Great prices, fast delivery.". Then:
    Task-1: call `store_tagline`.
    Task-2: print `store_tagline`'s own docstring (read it from the function's `__doc__` attribute).

Expected output:
Great prices, fast delivery.
Print the store tagline.
"""
def store_tagline():
    """Print the store tagline."""
    print("Great prices, fast delivery.")

# Problem-2 Task-1: call store_tagline
store_tagline()
# Problem-2 Task-2: print its docstring via __doc__
print(store_tagline.__doc__)

"""
Problem-3. Define Once, Call Many:
  Write a function `print_divider` that takes no arguments and prints "==============", then call it, print "Today's Deals", and call it again.

Expected output:
==============
Today's Deals
==============
"""
# Problem-3: define print_divider, call it around a label
def print_divider():
    print("==============")

print_divider()
print("Today's Deals")
print_divider()
