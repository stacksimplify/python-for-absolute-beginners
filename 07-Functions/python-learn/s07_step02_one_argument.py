# Concept-01: A parameter is the name in the def line; an argument is the value you pass when you call
# Question: How do we make one function greet ANY name we give it, like "Sam" or "Tom"? (put a parameter in the def, pass an argument in the call)
def greet(name):
    print(f"Hello, {name}!")

greet("Sam")
greet("Tom")
# `name` exists ONLY inside greet - it is created fresh each call (more on this in Scope)

# Concept-02: The argument can be a variable, not just a typed-in value
# Question: How do we greet a name we already stored in a variable, like "Amy"?
# Same greet function as Concept-01, repeated so this block stands on its own
def greet(name):
    print(f"Hello, {name}!")

student = "Amy"
greet(student)

# Concept-03: Arguments fill parameters by POSITION, left to right (positional arguments)
# Question: How does Python know which value goes to which parameter? (by position: first value -> first parameter)
def describe(name, city):
    print(f"{name} is from {city}")

describe("Sam", "Hyderabad")
# A positional call must pass exactly as many values as there are parameters:
# describe("Sam")   # TypeError: missing 'city'
# describe("Sam", "Hyderabad", "India")   # TypeError: too many arguments
