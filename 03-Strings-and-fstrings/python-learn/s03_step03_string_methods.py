# Concept-01: A method is an action you call on a value with a dot: value.method()
# Question-1: How do we trim the stray spaces around "  kalyan reddy  " and fix its case to upper or lower? (.strip(), .upper(), .lower())
# Question-2: How do we swap one piece of text for another, like turning "kalyan reddy" into "kalyan r"? (.replace("reddy", "r"))
name = "  kalyan reddy  "
print(name.strip())                          # kalyan reddy (spaces at both ends removed)
print(name.strip().upper())                  # KALYAN REDDY (chain: strip then UPPER)
print("KALYAN".lower())                      # kalyan
print("kalyan reddy".replace("reddy", "r"))  # kalyan r (swap one piece of text for another)

# Concept-02: title() makes the first letter of each word a capital
# Question: How do we turn Kalyan's lowercase name into a nicely capitalized "Kalyan Reddy"? (text.title())
print("kalyan reddy".title())  # Kalyan Reddy

# Concept-03: count() tells how many times a piece of text appears
# Question: How many times does the letter "a" appear in Kalyan's name? (text.count("a"))
print("kalyan reddy".count("a"))  # 2 (the letter a appears twice)

# Concept-04: isdigit() tells if text is all digits; handy to check input before turning it into a number
# Question: How do we check that Kalyan's typed age "30" is a whole number before we trust it? (text.isdigit())
print("30".isdigit())     # True (all characters are digits)
print("30yrs".isdigit())  # False (has letters)
print("".isdigit())       # False (empty text is not a number)

# Concept-05: startswith() / endswith() check the ends; find() / index() locate text inside
# Question-1: How do we check if the email "kalyan@example.com" starts with "kalyan" or ends with ".com"? (.startswith, .endswith)
# Question-2: How do we find where the "@" sits in "kalyan@example.com"? (.find, .index)
email = "kalyan@example.com"
print(email.startswith("kalyan"))  # True (begins with this text)
print(email.endswith(".com"))      # True (ends with this text)
print(email.find("@"))             # 6: position of the first match (-1 if not found)
print(email.index("@"))            # 6: like find(), but errors if the text is missing
