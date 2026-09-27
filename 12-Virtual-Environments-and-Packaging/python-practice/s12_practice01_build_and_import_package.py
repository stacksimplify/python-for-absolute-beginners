"""
Practice Problem-01: build and import your own package

Concepts: a package (a folder of modules) and its __init__.py front door, a module of functions,
__all__, importing your own package into a main script.

Build a package named store for an online store. Inside it, a module pricing.py holds two
functions: line_total(price, quantity) returns price * quantity, and apply_discount(total, percent)
returns the total with that percent taken off. The package's __init__.py is its front door: it
brings both functions out so a main script can import them straight from store, and it lists both
names in __all__. Then write a main script (this file) that imports line_total and apply_discount from
store, and:
  Task-1: print the line total for 2 items at price 25.0, labeled "Line total:".
  Task-2: print that line total with a 10 percent discount applied, labeled "After 10 percent off:".

Folder layout (keep the store/ package next to this file):
    store/
        __init__.py     # the front door: brings both functions out, lists them in __all__
        pricing.py      # the two functions
    s12_practice01_build_and_import_package.py   # this file

Expected output:
Line total: 50.0
After 10 percent off: 45.0

Write your solution below.
"""
