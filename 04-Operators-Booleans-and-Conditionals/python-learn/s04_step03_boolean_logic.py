# Concept-01: and -> True only if BOTH sides are True
# Question: How do we check if someone is BOTH a member AND old enough (need both conditions true)?
is_member = True
age = 20
print(is_member and age >= 18)  # True

# Concept-02: or -> True if EITHER side is True
# Question: How do we check if someone EITHER is a member OR is under 18 (need at least one true)?
is_member = True
age = 20
print(is_member or age < 18)  # True

# Concept-03: not -> flips True to False and False to True
# Question: How do we flip a True/False answer to the opposite, test not a member?
is_member = True
print(not is_member)  # False

# Concept-04: in -> is a value inside some text (or a collection)?
# Question: How do we check if a letter like "a" sits inside the text "Kalyan" with the in operator?
print("a" in "Kalyan")  # True: the letter a is in the text
print("z" in "Kalyan")  # False

# Concept-05: Truthy / falsy, empty things are falsy, everything else is truthy
# Question: How do we know when Python treats something as nothing/false (empty) versus true (has stuff)?
# Run 1 - FALSY: zero and empty values count as False
print(bool(0), bool(""))  # False False
# Run 2 - TRUTHY: non-zero numbers and non-empty text count as True
print(bool(5), bool("hi"))  # True True

# Concept-06: all() is True only if EVERY item is true; any() is True if AT LEAST ONE is true
# Question-1: How do we check if EVERY item in the list [True, True, False] is true with all()?
# Question-2: How do we check if AT LEAST ONE item in the list [True, True, False] is true with any()?
checks = [True, True, False]
print(all(checks))  # False: not every item is True
print(any(checks))  # True: at least one item is True

# Concept-07: not in -> the mirror of in; True when a value is NOT inside
# Question: How do we check that a letter like "z" is NOT inside the text "Kalyan" with the not in operator?
print("z" not in "Kalyan")  # True: z is not in the text
print("a" not in "Kalyan")  # False: a IS in the text, so "not in" is False

# Concept-08: Chained comparison, Python lets you write 0 <= x <= 100; and is often clearer
# Question: How do we check a value sits inside a range, like a percentage 0 to 100? (chain it, or use and)
score = 72
print(0 <= score <= 100)  # True, reads like math: 0 <= score AND score <= 100
print(score >= 0 and score <= 100)  # True: the SAME check written with and
# Chaining is neat for a simple range, but it can get hard to read; for anything more,
# and / or are clearer and can express checks that chaining cannot.

# Concept-09: Operator precedence, math runs first, then comparisons, then and / or; use ( ) to be clear
# Question: In a mixed expression, what does Python work out first? (math, then comparison, then and/or)
print(2 + 3 == 5)  # True: 2 + 3 is computed first, then ==
print(5 > 3 and 2 > 1)  # True: each comparison first, then and
print((5 > 3) and (2 > 1))  # True: same result; the parentheses just make the order obvious
