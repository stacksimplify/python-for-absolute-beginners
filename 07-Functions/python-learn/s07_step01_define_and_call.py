# Concept-01: A function is a named block of code; define it with def, then RUN it by calling its name with ()
# Question: How do we run the same block of code many times without copying it? (def names it once; calling it runs it)
def greet():
    print("Hello, welcome to Python!")

# A name with NO () does not run the function - it just points at the function object:
# print(greet)   # <function greet at 0x...>  (the function itself, not the greeting)
greet()  # the () is what RUNS it

# Concept-02: A docstring describes what a function does; the first line inside, in triple quotes
# Question: How do we document what a function does, so we (and tools like help()) can read it later?
def welcome():
    """Print a friendly welcome message."""
    print("Glad you are here!")

welcome()
print(welcome.__doc__)
# help(welcome)   # same text, shown in the interactive help pager

# Concept-03: Define once, call many times; that is the whole point of a function (reuse, no copy-paste)
# Question: How does a function save us from writing the same lines again and again?
def divider():
    print("------------------------------")

divider()
print("Section 07: Functions")
divider()
