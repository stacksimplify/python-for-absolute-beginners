# Concept-01: Convert text to an integer using int()
# Question: How do we turn typed text like "25" into a whole number so we can do math? (int(text))
age_text = "25"
# Error: cannot add a string and a number
# print(age_text + 5)
print("age_text type:", type(age_text))

age = int(age_text)  # str -> int
print("age type:", type(age))
print(age + 5)  # Now math works


# Concept-02: Convert text to a decimal number using float()
# Question: How do we turn text like "19.99" into a decimal number? (float(text))
price_text = "19.99"
# Error: cannot add a string and a number
# print(price_text + 5)
print()
print("price_text type:", type(price_text))

price = float(price_text)  # str -> float
print("price type:", type(price))
print(price + 5)


# Concept-03: Convert a number to text using str()
# Question: How do we join a number like 3 into a sentence of text like "I have 3 items" without an error? (str(number) turns it into text)
count = 3
# Error: cannot join text and a number
# print("I have " + count + " items")
print()
print("I have " + str(count) + " items")  # int -> str


# Concept-04: input() always returns a str. Convert it before doing math.
# Question: How do we use a typed-in number in math when input() gives back text? (wrap it in int() or float() first)
# Program-01: Get input for a and b and print the sum
a = input("Enter value for a: ")
b = input("Enter value for b: ")
total = a + b
print(total)

"""
Program-01 Observations:
1. input() always returns a string.
2. If you enter "kalyan" and "reddy", Python joins them as "kalyanreddy".
3. If you enter "10" and "20", Python joins them as "1020".
4. To perform math, convert the inputs to integers using int().
"""

# Concept-04 (Program-02): Convert input values to integers
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
total = a + b
print(total)

"""
Program-02 Observations:
1. If you enter 10 and 20, the output is 30.
2. The inputs are converted from strings to integers before addition.
3. If you enter text such as "kalyan", Python raises a ValueError.
"""

