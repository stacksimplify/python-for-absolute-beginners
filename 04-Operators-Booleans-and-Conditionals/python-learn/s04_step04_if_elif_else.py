# Concept-01: if / elif / else, run a branch based on True/False conditions
# Question-1: What happens when an if condition is False and there is no else? (nothing in the block runs; the program carries on)
# Question-2: How do we give a second path for when the condition is False? (add an else branch)
# Question-3: How do we choose between MORE than two paths, like a letter grade? (elif, checked top to bottom)
# E1: an if on its own; the block runs ONLY when the condition is True
marks = 85
if marks >= 90:
    print("Excellent")
    print("Good Marks")
# Rest of the program
print("program finished")

# E2: if / else; exactly one of the two branches always runs
marks = 35
if marks >= 50:
    print("Result: pass")
else:
    print("Result: Fail")
# Rest of the program
print("program finished")

# E3: if / elif / else; many paths, and the FIRST True one wins
marks = 95
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")
# Rest of the program
print("program finished")

# Python checks top to bottom and runs the FIRST branch whose condition is True.
# The indented lines under a branch run only when that condition is True.

# Concept-02: The ternary, a short one-line either/or choice
# Question: How do we decide adult or minor from a person's age, in one line? (18 or older -> adult, else minor)
age = 20
label = "adult" if age >= 18 else "minor"
print(label)

# Question: How do we decide hot or cold from the temperature, in one line? (over 30 -> hot, else cold)
temperature = 32
weather = "hot" if temperature > 30 else "cold"
print(weather)

# Concept-03: A nested if, an if inside another if; the inner check runs only if the outer is True
# Question: How do we first check a user is logged in, and ONLY then check if they are an admin?
is_logged_in = True
is_admin = False

if is_logged_in:
    print("Welcome back!")
    if is_admin:
        print("You have admin access")
    else:
        print("You have standard access")
else:
    print("Please log in")

# Tip: deep nesting gets hard to read; a single if with and is often clearer,
# for example: if is_logged_in and is_admin: ...
