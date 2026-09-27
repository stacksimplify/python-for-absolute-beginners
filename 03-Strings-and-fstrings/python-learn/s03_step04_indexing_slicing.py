# Concept-01: A string is a sequence; each character has a position (index), starting at 0
# Question: How do we get a single character from a word like "Python", like the first letter (word[0]) or the last letter (word[-1])?
word = "Python"

print(word[0])  # P: first character (index 0)
print(word[1])  # y (second character)
print(word[-1])  # n: last character (a negative index counts from the end)

# Concept-02: A slice takes a range: word[start:stop]; start is included, stop is not
# Question: How do we pull out a chunk of a word like "Python", like the first three letters (word[0:3]) or from the middle to the end (word[3:])?
word = "Python"
print(word[0:3])  # Pyt: characters 0, 1, 2
print(word[3:])  # hon (from index 3 to the end)
print(word[:2])  # Py: from the start up to (not including) index 2

# Concept-03: A slice can take a step, written word[start:stop:step]; a step of -1 reverses
# Question-1: How do we take every second character of a word like "Python" in one line? (word[::2] steps by 2)
# Question-2: How do we reverse a whole word like "Python" in one line? (word[::-1] reverses)
word = "Python"
print(word[::2])  # Pto (every 2nd letter: index 0, 2, 4)
print(word[::-1])  # nohtyP (the whole word reversed)

# Concept-04: A negative index counts from the END (-1 = last); word[-N:] takes the last N characters
# Question: How do we read the end of a string like the plate "ka05ab1234", like its last 4 digits? (word[-1] last char, word[-4:] last 4)
plate = "ka05ab1234"
print(plate[-1])  # 4 (the last character)
print(plate[-4:])  # 1234 (the last 4 characters - the plate number)
print(plate[:2].upper())  # KA (the first two characters - the state code)

# Concept-05: A string is immutable; you can READ a character but you cannot change one in place
# Question: Can we change one letter of a string by assigning to its index, like word[0] = "J"? (no, strings are immutable)
word = "Python"
# Run 1 - READ a character (allowed): indexing to read is fine
print(word[0])  # P
# word[0] = "J"  # ERROR: 'str' object does not support item assignment (cannot change in place)
# Run 2 - build a NEW string (the way to "change" one): the original stays the same
print("J" + word[1:])  # Jython (a brand new string)
print(word)  # Python (the original is unchanged)
