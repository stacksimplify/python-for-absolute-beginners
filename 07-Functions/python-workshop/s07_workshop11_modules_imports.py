"""
Workshop Problem-11: modules and imports (Car Toolkit)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: import a standard-library module and call module.function(),
from module import name, import from your OWN .py module.

Task-1: import `math`, then apply `math.floor` to 7.5 and `math.sqrt` to 144, printing each result.
Task-2: from `math`, import `ceil`, then apply `ceil` to 3.2 and print the result.
Task-3: create `s07_workshop11_cartools.py` next to this file holding a `price_with_tax` function (takes a price and a rate, returns the price plus the price times the rate) and a `label` function (takes a brand and a model, returns them joined as "<brand> <model>"). Then, in THIS file, import both `price_with_tax` and `label` from that module, call `price_with_tax` with 1000 and 0.1 and print the result, and call `label` with "Mazda" and "CX5" and print the result.
Task-4: import the `math` module under the short alias `m` and apply `m.floor` to 6.7, then from `math` import the name `factorial` under the alias `fact` and apply `fact` to 4, printing each result.

Expected (running THIS file):
7
12.0
4
1100.0
Mazda CX5
6
24
"""
