"""
Practice Problem-03: string methods (solution)

Concepts: string methods (strip, upper, replace), input(), f-strings, len().
"""

"""
Problem-1. Clean Up Text:
  Write a program that:
    Task-1: take a greeting "  Hello World  " (note the extra spaces) and print it
            with the surrounding spaces removed and in UPPER CASE.
    Task-2: take a date "2026-06-17" and print it with every "-" replaced by "/".

Expected output:
HELLO WORLD
2026/06/17
"""
greeting = "  Hello World  "
# Problem-1 Task-1: strip spaces and uppercase the greeting
print(greeting.strip().upper())
date = "2026-06-17"
# Problem-1 Task-2: replace dashes with slashes
print(date.replace("-", "/"))

"""
Problem-2 (Write a Program). Name Tag:
  Write a program that asks the user for a full name, then prints
  "NAME TAG: <NAME>" with the name in UPPER CASE and "Characters: <count>" with
  the number of characters in the name (spaces count).

Example run:
Enter your full name: Kalyan Reddy
NAME TAG: KALYAN REDDY
Characters: 12
"""
full_name = input("Enter your full name: ")
print(f"NAME TAG: {full_name.upper()}")
print(f"Characters: {len(full_name)}")

"""
Problem-3. Is It A Number?:
  Write a program that prints whether "2026" is all digits and whether "20a6" is
  all digits.

Expected output:
True
False
"""
print("2026".isdigit())
print("20a6".isdigit())

"""
Problem-4. Ends and Position:
  Write a program that:
    Task-1: for a filename "data.csv", print whether it starts with "data".
    Task-2: for the same filename, print whether it ends with ".csv".
    Task-3: print the position of "ss" in "mississippi", found two ways.

Expected output:
True
True
2
2
"""
filename = "data.csv"
# Problem-4 Task-1: check if filename starts with "data"
print(filename.startswith("data"))
# Problem-4 Task-2: check if filename ends with ".csv"
print(filename.endswith(".csv"))
# Problem-4 Task-3: find position of "ss" two ways
print("mississippi".find("ss"))
print("mississippi".index("ss"))
