# Concept-01: A function is a value (an object). You can store it in a variable and call it through that name
# Question: How do we give a long function name a short alias we can call instead? (assign the function to a variable, with no parentheses)
def shout(text):
    return text.upper() + "!"

# NO parentheses: the variable holds the FUNCTION itself
yeller = shout  # store the function itself; note: no parentheses
print(yeller("hello"))  # call it through the new name

# WITH parentheses: the variable holds the RESULT of running it
result = shout("hello")
print(result)
# print(result("x"))  # uncomment: TypeError, 'str' object is not callable

# Concept-02: A function can take ANOTHER function as an argument (a higher-order function)
# Question: How do we pass one function into another so it runs once, twice or three times? (pass the function NAME as the argument, with no parentheses)
# First, a plain function we already know how to write:
def add_three(n):
    return n + 3

# Now higher-order functions: each one TAKES a function (func) and runs it on a value:
def apply_once(func, value):
    return func(value)

def apply_twice(func, value):
    return func(func(value))

def apply_thrice(func, value):
    return func(func(func(value)))

# Pass add_three itself as the argument - its NAME, with no ():
print(apply_once(add_three, 10))
print(apply_twice(add_three, 10))
print(apply_thrice(add_three, 10))

# Concept-03: map applies a function to EVERY item of a list and gives back the transformed results (a built-in higher-order function)
# Question: How do we apply one function to a whole list at once, like adding 3 to every price in [10, 20, 30, 40]? (map(add_three, prices) transforms each)
# Same add_three as Concept-02, repeated so this block stands on its own
def add_three(n):
    return n + 3

prices = [10, 20, 30, 40]
prices_new = list(map(add_three, prices))  # map gives a map object; list() turns it into a list
print(prices_new)
print(type(prices_new))

# Concept-04: filter keeps only the items a function says True to, and drops the rest (a built-in higher-order function)
# Question: How do we keep only the items in [50, 120, 90, 200] that pass a test, like the ones over 100? (filter(is_big, prices) selects)
def is_big(n):
    return n > 100

prices = [50, 120, 90, 200]
print(list(filter(is_big, prices)))  # keep only the big ones -> [120, 200]

# Concept-05: Functions are objects, so they can live in a dict and be picked by key at runtime (dispatch)
# Question: How do we pick which checkout operation to run - shipping, tax, or a coupon - without a big if-chain? (store the functions in a dict, look one up by key)
# E1: the long way: an if/elif chain, and it grows by one branch for every new operation
def run_operation(name, total):
    if name == "shipping":
        return total + 50
    elif name == "tax":
        return total + (total // 10)
    elif name == "coupon":
        return total - 100
    else:
        return total  # unknown name: hand the total back unchanged, never None
print(run_operation("tax", 1000))  # 1100
print(run_operation("gift", 1000))  # 1000 - unknown name, total unchanged

# E2: dict dispatch: store the functions in a dictionary and pick which one to run by key
# A new operation is just one more key-value pair - no if/elif chain
def add_shipping(total):
    return total + 50

def add_tax(total):
    return total + (total // 10)

def apply_coupon(total):
    return total - 100

operations = {
    "shipping": add_shipping,
    "tax": add_tax,
    "coupon": apply_coupon
}

# Get the function stored under the "tax" key - this does NOT call the function
print(operations["tax"])  # <function add_tax at ...>

# Store the selected function in a variable, then CALL it with 1000 as the argument
chosen = operations["tax"]
print(chosen(1000))  # 1100

# Or get the function and CALL it directly with 1000 as the argument
print(operations["tax"](1000))  # 1100

# Other options: pick a different operation by changing only the key
print(operations["shipping"](1000))  # 1050
print(operations["coupon"](1000))  # 900
