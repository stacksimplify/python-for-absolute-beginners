"""
Practice Problem-01: making strings (solution)

Concepts: strings, joining with +, len().

Problem-1. Full name:
  Write a program that joins a first name (Srihan) and a last name (Reddy) into a
full name with a space between them, prints the full name, and prints how many
characters it has.

Expected output:
Srihan Reddy
12
"""

first_name = "Srihan"
last_name = "Reddy"
full_name = first_name + " " + last_name
print(full_name)

print(len(full_name))

"""
Problem-2. Multiline bio:
  Write a program that prints a three-line bio from a single multiline string:
  Srihan Reddy, then Python Learner, then Chennai.

Expected output:
Srihan Reddy
Python Learner
Chennai
"""
bio = """Srihan Reddy
Python Learner
Chennai"""
print(bio)
