"""
Practice Problem-11: modules and imports (solution)

Concepts: import a standard-library module and call module.function(),
from module import name, import from your OWN .py module.
"""

"""
Problem-1. Use the math module:
  Import the `math` module, then:
    Task-1: apply `math.sqrt` to 81 and print the result.
    Task-2: apply `math.floor` to 9.8 and print the result.

Expected output:
9.0
9
"""
import math

# Problem-1 Task-1: math.sqrt of 81
print(math.sqrt(81))
# Problem-1 Task-2: math.floor of 9.8
print(math.floor(9.8))

"""
Problem-2. from math import name:
  From the `math` module, import the names `pi` and `ceil`, then:
    Task-1: print `pi`.
    Task-2: apply `ceil` to 7.2 and print the result.

Expected output:
3.141592653589793
8
"""
from math import pi, ceil

# Problem-2 Task-1: print pi
print(pi)
# Problem-2 Task-2: ceil of 7.2
print(ceil(7.2))

"""
Problem-3. Import from your OWN module:
    Task-1: alongside this file, s07_practice11_pricetools.py holds a `tag` function (takes a product name, returns it in capitals with "!" added) and a `with_tax` function (takes a price, returns the price with 10 percent tax added, rounded to 2 decimals).
    Task-2: in THIS file, import both `tag` and `with_tax` from that module, then call `tag` with "welcome" and print the result and call `with_tax` with 100 and print the result.

Expected output (running THIS file):
WELCOME!
110.0
"""
# Problem-3 Task-2: import from your own module and call the functions
from s07_practice11_pricetools import tag, with_tax

print(tag("welcome"))
print(with_tax(100))

"""
Problem-4. Give a module and a name a short alias with `as`:
    Task-1: import the `math` module under the short alias `m`, then apply `m.sqrt` to 49 and print the result.
    Task-2: from the `math` module, import the name `factorial` under the alias `fact`, then apply `fact` to 5 and print the result.

Expected output:
7.0
120
"""
# Problem-4 Task-1: import the module under a short alias
import math as m

print(m.sqrt(49))
# Problem-4 Task-2: import a name under an alias
from math import factorial as fact

print(fact(5))
