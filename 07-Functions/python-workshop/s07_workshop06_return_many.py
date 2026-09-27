"""
Workshop Problem-06: return many values (Car Min and Max Price)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: returning several values comma-separated (a tuple), tuple unpacking.

Write a function `price_range` that takes a list `prices` and returns two values, the cheapest and the most expensive, plus a function `price_stats` that takes a list `prices` and returns three values, the cheapest, the most expensive, and how many prices there are. Then, for the list [1200000, 800000, 1500000]:
  Task-1: call `price_range`, store the single returned value, and print it (you will see a tuple).
  Task-2: call `price_range` again, unpack the two returned values into `cheapest` and `dearest` in one line, and print "cheapest: 800000" and "dearest: 1500000".
  Task-3: call `price_stats`, unpack the three returned values into `cheapest`, `dearest`, and `count` in one line, and print "cheapest: 800000", "dearest: 1500000", and "count: 3".

Expected output:
(800000, 1500000)
cheapest: 800000
dearest: 1500000
cheapest: 800000
dearest: 1500000
count: 3
"""
