"""
Practice Problem-09: first-class functions (solution)

Concepts: a function is a value (store it in a variable, call it through that name),
          higher-order functions (pass a function as an argument).
"""

"""
Problem-1: Write a function `triple_price` that takes `n` and returns it multiplied by 3, store the function itself in a variable named `bulk_price` (the name with no parentheses), then call `bulk_price` with 5 and with 20, printing each result.

Expected output:
15
60
"""
# Problem-1: store the function in a variable and call it
def triple_price(n):
    return n * 3
bulk_price = triple_price          # store the function itself; note: no parentheses
print(bulk_price(5))
print(bulk_price(20))

"""
Problem-2: Write a function `apply_to` that takes a function `func` and a `value` and returns the result of calling `func` on `value`, plus a function `markup` that returns a number multiplied by itself and a function `markdown` that returns a number's negative. Call `apply_to` with `markup` and 6 and print the result, then call `apply_to` with `markdown` and 6 and print the result.

Expected output:
36
-6
"""
# Problem-2: pass a function as an argument
def apply_to(func, value):
    return func(value)

def markup(n):
    return n * n

def markdown(n):
    return -n

print(apply_to(markup, 6))
print(apply_to(markdown, 6))

"""
Problem-3: Write a function `apply_again` that takes a function `func` and a `value` and returns the result of applying `func` to `value` twice (call `func` on `value`, then call `func` on that result), plus a function `add_fee` that returns a number plus 1. Call `apply_again` with `add_fee` and 10 and print the result.

Expected output: 12
"""
# Problem-3: apply the passed function twice
def apply_again(func, value):
    return func(func(value))

def add_fee(n):
    return n + 1

print(apply_again(add_fee, 10))

"""
Problem-4: Write a function `add_tax` that takes `n` and returns it plus 10 percent of it, worked out with whole-number division so the answer stays an int, and a function `is_pricey` that takes `n` and returns whether `n` is above 100. Define a variable `prices` as a list with the values 60, 140, 80, 210. Use `map` to apply `add_tax` to every price, turn the result into a list, and print it. Then use `filter` to keep only the prices `is_pricey` says are pricey, turn the result into a list, and print it.

Expected output:
[66, 154, 88, 231]
[140, 210]
"""
# Problem-4: map applies a function to every item, filter keeps the ones that pass a test
def add_tax(n):
    return n + n // 10

def is_pricey(n):
    return n > 100

prices = [60, 140, 80, 210]
print(list(map(add_tax, prices)))      # apply add_tax to each price
print(list(filter(is_pricey, prices)))  # keep only the pricey ones

"""
Problem-5: Write a function `add_fee` that takes `n` and returns it plus 5, and a function `add_tax` that takes `n` and returns it plus 10 percent of it, worked out with whole-number division so the answer stays an int. Put both functions in a dict named `charges` under the keys `fee` and `tax` (store the function names, no parentheses). Look up the function under the key `tax`, store it in a variable named `chosen`, call `chosen` with 200, and print the result. Then look up the function under the key `fee`, call it with 200, and print the result.

Expected output:
220
205
"""
# Problem-5: functions live in a dict and are picked by key (dispatch)
def add_fee(n):
    return n + 5

def add_tax(n):
    return n + n // 10

charges = {"fee": add_fee, "tax": add_tax}  # store the functions, no parentheses
chosen = charges["tax"]                      # look up the function by key
print(chosen(200))                           # then call it
print(charges["fee"](200))                   # look up and call in one step
