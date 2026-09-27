"""
Practice Problem-02: f-strings (solution)

Concepts: f-strings, math inside braces, format specs.

Write a program that, using a name (Srihan), an age (27), and a price (2499.95)
with f-strings:
  Task-1: print "Hi Srihan, you are 27".
  Task-2: print "Next year you will be 28" (the age plus 1).
  Task-3: print the price formatted with 2 decimals and a thousands separator as
          "Price: 2,499.95".

Expected output:
Hi Srihan, you are 27
Next year you will be 28
Price: 2,499.95
"""

name = "Srihan"
age = 27
price = 2499.95
# Task-1: print greeting with name and age
print(f"Hi {name}, you are {age}")

# Task-2: print next year's age
print(f"Next year you will be {age + 1}")

# Task-3: print price with 2 decimals and thousands separator
print(f"Price: {price:,.2f}")
