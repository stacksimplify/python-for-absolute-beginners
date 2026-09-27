"""
Workshop Problem-04: parameters and logic (Service Cost and Status)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: many parameters (positional), if/elif/else inside a function,
          a loop inside a function that builds up a total.

Task-1: write a function `service_cost` that takes `hours` and `rate` and returns their product (a labor cost), then call it with 3 and 40 and with 2 and 55, printing each result.
Task-2: write a function `fuel_status` that takes `liters` and returns a word: "Full" for 40 or more, "OK" for 15 or more, otherwise "Low". Call it with 50, with 20, and with 5, printing each result.
Task-3: write a function `fleet_distance` that takes a list `distances` and returns the total kilometers driven, adding them up itself (do not use the built-in sum()). Call it with [120, 80, 200] and print the result.
Task-4: write a function `any_low_tank` that takes a list `levels` and a `reserve` and returns True the moment it finds the first level below `reserve` (return right there, do not keep checking), otherwise returns False after the loop. Call it with [60, 10, 45] and 15 and print the result, then call it with [60, 40, 45] and 15 and print the result.

Expected output:
120
110
Full
OK
Low
400
True
False
"""
