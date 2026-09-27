# Concept-01: Comparison operators ask a question and answer True or False
# Question-1: How do we check if age (20) is exactly equal to 20 with == ?
# Question-2: How do we check if age (20) is not equal to 18 with != ?
age = 20

print(age == 20)  # True: equal to (note: two equals signs)
print(age != 18)  # True: not equal to

# Concept-02: The ordering comparisons: > < >= <=
# Question: How do we ask which of two values is larger or smaller, and the "or equal to" versions, for age = 20 with > < >= <= ?
age = 20
print(age > 18)  # True: greater than
print(age < 18)  # False: less than
print(age >= 20)  # True: greater than or equal to
print(age <= 19)  # False: less than or equal to

# Concept-03: Use is / is not only to compare with None (and True / False)
# Question: How do we check whether a value is empty/missing, set to None? (use is None, not == None)
result = None
print(result is None)  # True: is checks identity; the right test for None
print(result is not None)  # False
# Rule of thumb: use == for values (numbers, text); use is only with None / True / False.
