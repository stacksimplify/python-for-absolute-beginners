"""
Workshop Problem-09: first-class functions (Car Tools) (solution)

Concepts: a function is a value (store it in a variable),
          higher-order functions (pass a function as an argument),
          map/filter over a list, and picking a function from a dict by key (dispatch).
"""

"""
Problem-1:
  Task-1: Write a function `add_tax` that takes a `price` and returns the price plus 10 percent of it, store the function itself in a variable named `with_tax` (the name with no parentheses), and call `with_tax` with 20000 and print the result. Then write a function `apply_discount` that takes a function `func` and a `price`, calls `func` on `price`, and returns that result minus 500; call `apply_discount` with `with_tax` and 20000 and print the result.
  Task-2: Write a function `service_fee` that takes `km` and returns km * 2, and a function `needs_service` that takes `km` and returns whether `km` is above 10000. Define a variable `mileages` as a list with the values 5000, 12000, 8000, 20000. Use `map` to apply `service_fee` to every mileage, turn the result into a list, and print it. Then use `filter` to keep only the mileages that `needs_service` says need service, turn the result into a list, and print it.
  Task-3: Write a function `to_petrol` that takes a `brand` and returns `<brand> petrol`, and a function `to_diesel` that takes a `brand` and returns `<brand> diesel`. Put both functions in a dict named `fuels` under the keys `petrol` and `diesel` (store the function names, no parentheses). Look up the function under the key `diesel`, store it in a variable named `chosen`, call `chosen` with Audi, and print the result. Then look up the function under the key `petrol`, call it with BMW, and print the result.

Expected output:
22000
21500
[10000, 24000, 16000, 40000]
[12000, 20000]
Audi diesel
BMW petrol
"""
# Task-1: store a function in a variable, and pass a function as an argument
def add_tax(price):
    tax = price * 10 // 100
    return price + tax

with_tax = add_tax          # store the function itself; note: no parentheses
print(with_tax(20000))

def apply_discount(func, price):
    return func(price) - 500

print(apply_discount(with_tax, 20000))

# Task-2: map applies a function to every item, filter keeps the ones that pass a test
def service_fee(km):
    return km * 2

def needs_service(km):
    return km > 10000

mileages = [5000, 12000, 8000, 20000]
print(list(map(service_fee, mileages)))       # apply service_fee to each mileage
print(list(filter(needs_service, mileages)))  # keep only the ones needing service

# Task-3: functions live in a dict and are picked by key (dispatch)
def to_petrol(brand):
    return brand + " petrol"

def to_diesel(brand):
    return brand + " diesel"

fuels = {"petrol": to_petrol, "diesel": to_diesel}  # store the functions, no parentheses
chosen = fuels["diesel"]                             # look up the function by key
print(chosen("Audi"))                                # then call it
print(fuels["petrol"]("BMW"))                        # look up and call in one step
