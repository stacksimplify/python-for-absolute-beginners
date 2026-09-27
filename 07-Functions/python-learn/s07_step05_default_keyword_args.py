# Concept-01: A default value is used when you do NOT pass that argument
# Question: How do we make an input optional, with a sensible default? (give the parameter a default value in the def line)
def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Sam")  # both defaults used
greet("Tom", "Welcome")  # override greeting only
greet("Amy", "Hi", ".")  # override both defaults

# Concept-02: Parameters WITH defaults must come AFTER parameters without them
# Question: Why does Python reject a default before a normal parameter? (defaults must be last; the line below would be an error)
# def bad(greeting="Hi", name):   # SyntaxError: parameter without a default follows parameter with a default

# Concept-03: Keyword arguments. Name each value in the call, so the order does not matter
# Question: How do we pass arguments by NAME so we do not depend on their order? (write name=value in the call)
def describe(name, city):
    print(f"{name} lives in {city}")

describe(city="Hyderabad", name="Sam")  # all keyword: order does not matter
describe("Ben", city="Delhi")  # mix: positional first, then keyword
# At the call site, any keyword argument must come AFTER the positional ones:
# describe(name="Sam", "Hyderabad")   # SyntaxError: positional argument follows keyword argument

# Concept-04: The mutable default argument trap. A default list is created ONCE and reused across function calls.

# Question: Why does a default list seem to "remember" values from previous function calls?
# (Default parameter values are created only once when the function is defined. Use None to create a fresh list for each call.)

# E1: The TRAP - the same default list is reused on every call
def add_item(item, basket=[]):   # Avoid using a mutable object as a default value
    basket.append(item)
    return basket

print(add_item("apple"))    # ['apple']
print(add_item("banana"))   # ['apple', 'banana'] - 'apple' is still there!

# E2: The FIX - use None, then create a new list inside the function
def add_item_safe(item, basket=None):
    if basket is None:
        basket = []

    basket.append(item)
    return basket

print(add_item_safe("apple"))    # ['apple']
print(add_item_safe("banana"))   # ['banana'] - each call gets a fresh list
