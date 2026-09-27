# Concept-01: Import a function from Python's standard library and use it
# Question: How do we use ready-made functions that come with Python, like a square root? (import the module, then module.function())
import math

print(math.sqrt(144))
print(math.floor(3.7))

# Concept-02: Import specific names with "from module import name"
# Question: How do we pull just the names we need from a module? (from module import name1, name2)
from math import pi, ceil

print(pi)
print(ceil(4.1))

# Concept-03: Give a module (or name) a short alias with "as"
# Question: How do we give a long module name a short handle, the way pros write import numpy as np? (import module as alias)
import math as m
print(m.sqrt(49))

from math import factorial as fact
print(fact(5))

# Concept-04: Make your OWN module, then import from it - a .py file of functions sitting next to this one
# Question: How do we reuse functions we wrote in another file? (put them in their own .py, then import from it)
# STEP 1 - create a file named texttools.py in THIS folder, containing exactly this:
#
#     def make_upper(text):
#         return text.upper()
#
#     def make_lower(text):
#         return text.lower()
#
# STEP 2 - now import from it. Python finds texttools because it sits in the same folder as this file.
from texttools import make_upper, make_lower

print(make_upper("welcome"))
print(make_lower("WELCOME"))

# Beyond the standard library: other people publish modules on PyPI. Install one from your
# terminal (NOT inside Python), for example:  pip install requests
# then use it with "import requests", just like math above.
