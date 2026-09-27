# Concept-01: Print several values; print puts a space between them
# Question: How do we print several values like "Python", "is", "Fun" on one line, and what goes between them? (print joins them with one space by default)
print("Python", "is", "Fun")

# Concept-02: Change the separator between values with sep
# Question: How do we put a custom character like '-' or '/' between printed values like "2026", "01", "01", as in a date? (sep="-" or sep="/")
print("2026", "01", "01", sep="-")
print("2026", "01", "01", sep="/")

# Concept-03: Change what print puts at the end with end (the default end is a new line)
# Question: How do we make the next print stay on the same line instead of dropping down? (end=" " replaces the default newline)
print("same", end=" ")
print("line")

# Concept-04: print() with nothing makes an empty line
# Question: How do we print an empty line?
print("Python", "is", "Fun")
print()
print()
print("same", end=" ")
print("line")

# Concept-05: \n starts a new line inside one string
# Question: How do we break text like "Line One\nLine Two\nLine Three" onto a new line inside one string? (put \n where the line should break)
print("Line One\nLine Two\nLine Three")

# Concept-06: \t inserts a tab
# Question: How do we line up text into neat columns, like the label "Name:" and the value "Kalyan Reddy"? (\t inserts a tab)
print("Name:\tKalyan Reddy")

# Concept-07: A backslash starts an escape, so to print a literal backslash or quote you escape it
# Question-1: How do we print a Windows path with backslashes like "C:\\Users\\Kalyan"? (\\ prints one backslash)
# Question-2: How do we print a quote mark inside the same quotes, like "She said \"Hello\"" or 'It\'s a deal'? (\" prints a double quote; \' prints a single quote)
print("C:\\Users\\Kalyan")
print("She said \"Hello\"")
print('It\'s a deal')
