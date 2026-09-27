# Concept-01: A variable is a name attached to a value. You create one with =
# Question: How do we create a label (name) that holds a value so we can use it later?
name = "Kalyan"
age = 30
price = 19.99

# Concept-02: Display a variable's value using print()
# Question: How do we show what value a variable holds?
name = "Kalyan"
age = 30
price = 19.99
print(name)
print(age)
print(price)

# Concept-03: Print text together with variables
# Question: How do we display a description and a variable's value together in one line?
name = "Kalyan"
age = 30
price = 19.99
print()
print("name is", name)
print("age is", age)
print("price is", price)

# Concept-04: A variable can be changed (reassigned) later
# Question: How do we update someone's age after each birthday? (reassign the same variable with =)
age = 31
print("age update-1:", age)
age = 32
print("age update-2:", age)

# Concept-05: Rules for a valid variable name (these are required)
# Question: What names are LEGAL in Python? (start with a letter or _, then letters, digits, or _ ; no spaces or symbols)
first_name = "Kalyan"   # letters
user_age = 30           # letters, underscore, and digits
_secret = True          # may start with _ (a leading _ means "internal use")
score2 = 95             # digits are allowed, but NOT as the first character
print(first_name, user_age, _secret, score2)

# These names are NOT allowed because each line would cause a SyntaxError:
# 2nd_place = "silver"   # cannot start with a digit
# first name = "Kalyan"  # no spaces allowed
# user-age = 30          # no hyphen or other symbols

# Concept-06: Naming rule: use snake_case, lowercase words joined with underscores
# Question: How do we name a variable so others know what it holds? (snake_case, lowercase words joined by underscores)
favorite_color = "blue"
print("favorite color is", favorite_color)

# Concept-07: For values that never change (constants), use UPPER_CASE by convention
# Question: How do we name a value that should stay the same for the whole program? (use UPPER_CASE by convention)
MAX_SCORE = 100
print("MAX_SCORE is", MAX_SCORE)

# Concept-08: Names are case sensitive, so age and Age are two different variables
# Question: Does capitalization matter in a name? (yes, age and Age are two different variables)
age = 1
Age = 2
print("age is", age, "and Age is", Age)
