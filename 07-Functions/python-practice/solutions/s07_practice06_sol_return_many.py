"""
Practice Problem-06: return many values (solution)

Concepts: returning several values comma-separated (a tuple), tuple unpacking.
"""

"""
Problem-1. Cheapest and Dearest:
  Write a function `price_range` that takes a list `prices` and returns two values, the lowest and the highest. Then, for the list [40, 95, 25, 70]:
    Task-1: call `price_range`, store the single returned value, and print it (you will see a tuple).
    Task-2: call `price_range` again, unpack the two returned values into `low` and `high` in one line, and print "low: 25" and "high: 95".

Expected output:
(25, 95)
low: 25
high: 95
"""
def price_range(prices):
    return min(prices), max(prices)

# Problem-1 Task-1: store and print the returned tuple
spread = price_range([40, 95, 25, 70])
print(spread)

# Problem-1 Task-2: unpack the two returned values
low, high = price_range([40, 95, 25, 70])
print("low:", low)
print("high:", high)

"""
Problem-2. Split a Product Code:
  Write a function `split_code` that takes a `product_code` and returns two values, the first part and the last part (split on "-"). Call it with "TEC-2024-15", unpack the two returned values into `prefix` and `suffix`, and print "prefix = TEC" and "suffix = 15".

Expected output:
prefix = TEC
suffix = 15
"""
# Problem-2: return first and last parts, then unpack them
def split_code(product_code):
    parts = product_code.split("-")
    return parts[0], parts[-1]

prefix, suffix = split_code("TEC-2024-15")
print(f"prefix = {prefix}")
print(f"suffix = {suffix}")

"""
Problem-3. Three Price Stats:
  Write a function `price_stats` that takes a list `prices` and returns three values, the lowest, the highest, and how many prices there are. Call it with [40, 95, 25, 70], unpack the three returned values into `low`, `high`, and `count` in one line, and print "low: 25", "high: 95", and "count: 4".

Expected output:
low: 25
high: 95
count: 4
"""
# Problem-3: return three values (low, high, count) and unpack them into three names
def price_stats(prices):
    return min(prices), max(prices), len(prices)

low, high, count = price_stats([40, 95, 25, 70])
print("low:", low)
print("high:", high)
print("count:", count)
