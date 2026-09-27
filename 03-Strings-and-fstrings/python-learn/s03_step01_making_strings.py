# Concept-01: A string is text; use single quotes or double quotes (both work)
# Question: How do we store a person's name like "Kalyan" (or a greeting 'Hello') so we can print it later? (single or double quotes both work)
first_name = "Kalyan"
greeting = 'Hello'
print(first_name)
print(greeting)

# Concept-02: Use the other quote style when your text itself contains a quote
# Question: How do we write text that contains quotes inside it, like "It's a sunny day" or 'She said "hi"', without breaking the code?
# Double quotes outside, so the ' inside is fine
sentence = "It's a sunny day"
# Single quotes outside, so the " inside is fine
quote = 'She said "hi"'
print(sentence)
print(quote)

# Concept-03: Join strings together with + (this is called concatenation)
# Question: How do we build a full name from first and last names like "Kalyan" + " " + "Reddy" stored in separate variables?
full_name = "Kalyan" + " " + "Reddy"
print(full_name)

# Concept-04: len() tells you how many characters are in a string
# Question: How do we count the characters in a name or sentence, like "Python" or "Kalyan Reddy"? (len(text))
print(len("Python"))
full_name = "Kalyan" + " " + "Reddy"
print(len(full_name))

# Concept-05: Triple quotes """...""" make a multiline string; real text kept across several lines
# Question: How do we store a block of text that spans several lines, like the short bio "Kalyan Reddy / Python Teacher / Hyderabad", in one variable? (wrap it in triple quotes)
bio = """Kalyan Reddy
Python Teacher
Hyderabad"""
print(bio)
print(len(bio))
