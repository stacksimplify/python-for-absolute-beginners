"""
Workshop Problem-03: boolean logic (Can Drive?) (solution)

Concepts: and, or, not.

Problem-1. Can drive:
  Write a program that, for a fuel of 20 and engine_ok set to True:
  Task-1: print whether there is fuel left and the engine is ok.
  Task-2: print whether the fuel is above 50 or the engine is ok.
  Task-3: print the opposite of engine_ok.

Expected output:
True
True
False
"""

fuel = 20
engine_ok = True
# Task-1: fuel left and engine is ok
print(fuel > 0 and engine_ok)
# Task-2: fuel above 50 or engine is ok
print(fuel > 50 or engine_ok)
# Task-3: print the opposite of engine_ok
print(not engine_ok)

"""
Problem-2. Car features:
  Write a program that, for a list features = [True, False, True] (square brackets
    hold several values at once; lists in full in Section 05):
    Task-1: print whether every item is true.
    Task-2: print whether at least one item is true.

Expected output:
False
True
"""
features = [True, False, True]
# Task-1: whether every item is true
print(all(features))
# Task-2: whether at least one item is true
print(any(features))
