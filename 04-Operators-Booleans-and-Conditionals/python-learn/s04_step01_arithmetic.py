# Concept-01: The everyday math operators: + - * /
# Question: How do we add, subtract, multiply, and divide two numbers like 17 and 5 with + - * / ?
a = 17
b = 5

print(a + b)  # 22: addition
print(a - b)  # 12: subtraction
print(a * b)  # 85: multiplication
print(a / b)  # 3.4: division always gives a float (decimal)

# Concept-02: Three more, // floor division, % modulo (remainder), ** power
# Question-1: How do we get just the whole-number part of dividing 17 by 5 with // ?
# Question-2: How do we find the remainder of dividing 17 by 5 with % ?
a = 17
b = 5
print(a // b)  # 3 (floor division: the whole-number part, i.e. the quotient)
print(a % b)  # 2 (modulo: the remainder)
print(a ** 2)  # 289: power, a to the power 2

# Concept-03: Two handy number helpers, abs() for size without a sign, divmod() for quotient and remainder together
# Question-1: How do we get the size of a number ignoring its sign with abs(), like abs(-7) or abs(7)?
# Question-2: How do we get the quotient and remainder of 17 divided by 5 together in one step with divmod(17, 5)?
print(abs(-7))  # 7 (absolute value: distance from zero, never negative)
print(abs(7))  # 7
print(divmod(17, 5))  # (3, 2): the // and % answers together (quotient, remainder)

# Concept-04: Augmented assignment, update a variable using itself, in shorthand (+= -= *= and more)
# Question: How do we change a variable in place, like a running total or a counter? (x += 1 means x = x + 1)
# Run 1 - running total: += adds and -= subtracts, both on the same variable
score = 100
score += 50  # same as score = score + 50
print(score)  # 150
score -= 30  # same as score = score - 30
print(score)  # 120
# Run 2 - counter: += 1 each time (the pattern you will use in loops)
count = 0
count += 1
count += 1
print(count)  # 2
