"""
Workshop Problem-09: first-class functions (Car Tools)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

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
