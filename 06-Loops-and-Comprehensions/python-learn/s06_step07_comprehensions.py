# Concept-01: A list comprehension builds a new list in one line:
# [expression for item in collection]
# Question: How do we double every score in [10, 20, 30, 40]
# without writing a longer for loop?
scores = [10, 20, 30, 40]

# E1: The long way - build the list step by step
doubled = []
for n in scores:
    doubled.append(n * 2)
print(doubled)

# E2: The same result with a one-line comprehension
# Read it as: "n * 2 for each n in scores"
doubled = [n * 2 for n in scores]
print(doubled)

# E3: The collection does not have to be a list
# A range() works exactly the same way
squares = [n * n for n in range(1, 6)]
print(squares)

# Concept-02: Add an if at the end to keep only items that pass a test: [expr for item in collection if test]
# Question: How do we keep only the passing scores (80 or more) in [70, 95, 88, 88] in one line? (>= includes 80)
scores = [70, 95, 88, 88]
passing = [n for n in scores if n >= 80]
print(passing)

# Concept-03: A dict comprehension builds a dictionary in one line:
# {key: value for item in collection}
# Question: How do we map each score in [10, 20, 30, 40]
# to its double in one line?
scores = [10, 20, 30, 40]

score_map = {score: score * 2 for score in scores}
print(score_map)

# Concept-04: Add an if to a dict comprehension to keep only the items that pass a test:
# {key: value for item in collection if condition}
# Question: How do we build a dictionary for only the passing scores (20 or more)
# from [10, 20, 30, 40] in one line?
scores = [10, 20, 30, 40]

passing_map = {score: score * 2 for score in scores if score >= 20}
print(passing_map)

# Concept-05: A set comprehension builds a set in one line and removes duplicates:
# {expression for item in collection}
# Question: How do we keep only the distinct scores from [70, 95, 88, 88]?
# (A set keeps each value only once.)
scores = [70, 95, 88, 88]

unique_scores = {score for score in scores}
print(sorted(unique_scores))   # Sort only for display because sets have no fixed order.

# Concept-06: Use if/else inside a comprehension to choose between two values:
# [value_if_true if condition else value_if_false for item in collection]
# Question: How do we label each score in [70, 95, 80, 65, 55, 89] as "pass" or "fail"
# - first as a list of labels, then as a dictionary that keeps each score with its label?
# (80 or more passes.)
scores = [70, 95, 80, 65, 55, 89]
print(scores)

# A LIST comprehension gives you the labels on their own
labels = ["pass" if score >= 80 else "fail" for score in scores]
print(labels)

# A DICT comprehension keeps each score WITH its label; the same if/else works here
result_map = {score: "pass" if score >= 80 else "fail" for score in scores}
print(result_map)

# map() and filter() can solve similar problems.
# This course focuses on comprehensions because they clearly show
# the collection being built in a single expression.
