# Concept-01: Return MANY values at once by separating them with commas; you get a tuple
# Question: How does a function hand back more than one result, like the lowest and highest of [4, 9, 2, 7]? (return them comma-separated; it becomes a tuple)
def low_high(numbers):
    # A function returns ONE object. The commas (not the brackets) pack both values
    # into a single tuple, so we can catch it whole (result) or unpack it (lo, hi).
    return min(numbers), max(numbers)

result = low_high([4, 9, 2, 7])
print(result)

# Concept-02: Unpack the returned tuple into separate variables in one line
# Question: How do we catch several returned values into their own names? (unpack them: lo, hi = low_high(...))
# Same low_high function as Concept-01, repeated so this block stands on its own
def low_high(numbers):
    return min(numbers), max(numbers)

lo, hi = low_high([4, 9, 2, 7])
print("low:", lo)
print("high:", hi)
# lo, hi, extra = low_high([4, 9, 2, 7])  # ValueError: not enough values to unpack (expected 3, got 2)

# Concept-03: Return three values and unpack them into three names
# Question: How do we hand back the low, high, AND count of [4, 9, 2, 7] at once? (return three, comma-separated; unpack into three names)
def low_high_count(numbers):
    return min(numbers), max(numbers), len(numbers)

lo, hi, count = low_high_count([4, 9, 2, 7])
print("low:", lo)
print("high:", hi)
print("count:", count)
