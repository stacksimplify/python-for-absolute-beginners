# Concept-01: An f-string drops values into text; put f before the quotes, then {variable}
# Question: How do we drop a name "Kalyan" and age 30 into a sentence so it reads naturally? (f"...{name}...{age}")
name = "Kalyan"
age = 30
# Run 1 - without f-string: glue the pieces with + and convert age with str()
print("My name is " + name + " and I am " + str(age))
# Run 2 - with f-string: drop {name} and {age} straight in
print(f"My name is {name} and I am {age}")

"""
Observation:
1. Without an f-string you glue the pieces together with +, which is fiddly and easy to get wrong.
2. You must convert non-text values yourself, like str(age), or Python raises a TypeError.
3. The f-string is shorter and reads like the final sentence: drop {name} and {age} straight in - no + and no str().
"""

# Concept-02: You can do math inside the braces too
# Question: How do we show a value like next year's age (age = 30, so {age + 1} gives 31) without a separate line of math? (put the math inside the braces: {age + 1})
age = 30
# Run 1 - without f-string: pass the math as a second print argument (comma)
print("Next year I will be", age + 1)
# Run 2 - with f-string: do the math inside the braces {age + 1}
print(f"Next year I will be {age + 1}")

# Concept-03: A format spec after a colon sets the number of decimal places: {value:.Nf}
# Question: How do we show a price like 1234.4321 with a fixed number of decimal places - 3, 2, 1, or 0? (a format spec after a colon, like {price:.2f})
price = 1234.4321
p1 = f"{price:.3f}"
print(p1)
print(type(p1))
p2 = f"{price:.2f}"
print(p2)
p3 = f"{price:.1f}"
print(p3)
p4 = f"{price:.0f}"
print(p4)

# Concept-04: A comma in the format spec groups thousands with commas: {value:,.2f}
# Question: How do we show a big number like 1234.4321 with thousands separators, like 1,234.43? (add a comma before the decimals: {price:,.2f})
price = 1234.4321
t1 = f"{price:,.2f}"
print(t1)

# Concept-05: A percent sign in the spec shows a fraction as a percentage: {value:.N%}
# Question: How do we show a fraction like 0.875432 as a percentage with N decimals? ({ratio:.1%} gives 87.5%)
ratio = 0.875432
percentage = f"{ratio:.1%}"
print(percentage)
percentage = f"{ratio:.2%}"
print(percentage)
percentage = f"{ratio:.3%}"
print(percentage)
