"""
Workshop Problem-01: define and call (Car Banner) (solution)

Concepts: def (no parameters), calling a function with (), docstrings,
          define once and call many times.

Write a function `show_banner` that takes no arguments, carries the docstring "Print the car banner.", and prints "Welcome to Sam Motors", plus a function `divider` that takes no arguments and prints "----------". Then call `divider`, `show_banner`, and `divider` again.

Expected output:
----------
Welcome to Sam Motors
----------
"""

def show_banner():
    """Print the car banner."""
    print("Welcome to Sam Motors")

def divider():
    print("----------")

divider()
show_banner()
divider()
