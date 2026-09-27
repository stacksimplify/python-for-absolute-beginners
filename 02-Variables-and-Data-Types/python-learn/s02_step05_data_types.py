# Concept-01: The four everyday data types
# Question: How do we pick the right data type for a value? (str text, int whole number, float decimal, bool True/False)
title = "Python Basics"  # str: text, written in quotes
lessons = 12  # int: a whole number
rating = 4.5  # float: a decimal number
is_free = True  # bool: True or False

print(title)
print(lessons)
print(rating)
print(is_free)

# Concept-02: type(x) returns the data type of a value.
# Question: How do we find out what type a value is when we are unsure? (type(value) returns its type)
title = "Python Basics"  # str: text, written in quotes
lessons = 12  # int: a whole number
rating = 4.5  # float: a decimal number
is_free = True  # bool: True or False
print()
print("Types using type():")
print(type(title))
print(type(lessons))
print(type(rating))
print(type(is_free))

# Concept-03: type(x).__name__ gives the short name.
# Question: How do we get just the short name of a data type, like 'str' or 'int', instead of '<class ...>'?
title = "Python Basics"  # str: text, written in quotes
lessons = 12  # int: a whole number
rating = 4.5  # float: a decimal number
is_free = True  # bool: True or False
print()
print("Type names using type(x).__name__:")
print("title   ->", type(title).__name__)
print("lessons ->", type(lessons).__name__)
print("rating  ->", type(rating).__name__)
print("is_free ->", type(is_free).__name__)

# Concept-04: bool holds only True or False (note the CAPITAL T and F)
# Question: How do we write a True or False value correctly? (only True or False, with a capital first letter)
print()
is_member = True
is_admin = False
print("is_member:", is_member)
print("is_admin:", is_admin)
print("bool type:", type(is_member).__name__)

# Python is case sensitive: True and False must be capitalized.
# Lowercase true / false are NOT booleans and would cause a NameError.

# Concept-05: round() shortens a long decimal; round(value, digits)
# Question: How do we shorten a long decimal like 3.14159 to 2 places? (round(value, 2); to FORMAT one for display, an f-string :.2f comes in Section 03)
pi = 3.14159
print("round(pi, 2) keeps 2 decimals:", round(pi, 2))
print("round(pi, 0) keeps 0 decimals, still a float:", round(pi, 0))
price = 19.99
print("round(price) with no digits gives a whole int:", round(price))
