r"""
Practice Problem-03: print options and escapes (solution)

Concepts: print() with sep and end, and the escapes \n and \t.
"""

"""
Problem-1: Write a program that prints "red", "green", "blue" on one line, separated by ", ".

Expected output: red, green, blue
"""
# Problem-1 Task-1: print three colors separated by comma
print("red", "green", "blue", sep=", ")

"""
Problem-2: Write a program that prints "Loading" and "done" on the same line, joined by "..." (no line break between them).

Expected output: Loading...done
"""
# Problem-2 Task-1: join two words with ... on one line
print("Loading", end="...")
print("done")

"""
Problem-3: Write a program that prints a two-line table from a single string: "Name:" then "Kalyan", and "City:" then "Hyderabad", with the values lined up by a tab.

Expected output:
Name:	Kalyan
City:	Hyderabad
"""
# Problem-3 Task-1: print a tab-aligned two-line table
print("Name:\tKalyan\nCity:\tHyderabad")

r"""
Problem-4: Write a program that prints the Windows path C:\Temp\data on one line and She said "Hi" on the next. You will need to escape the backslashes and the quotes.

Expected output:
C:\Temp\data
She said "Hi"
"""
# Problem-4 Task-1: print escaped path and quoted text
print("C:\\Temp\\data")
print("She said \"Hi\"")
