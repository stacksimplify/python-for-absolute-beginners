"""
Practice Problem-09: first-class functions

Concepts: a function is a value (store it in a variable, call it through that name),
          higher-order functions (pass a function as an argument).
"""
"""
Problem-1: Write a function `triple_price` that takes `n` and returns it multiplied by 3, store the function itself in a variable named `bulk_price` (the name with no parentheses), then call `bulk_price` with 5 and with 20, printing each result.

Expected output:
15
60
"""
"""
Problem-2: Write a function `apply_to` that takes a function `func` and a `value` and returns the result of calling `func` on `value`, plus a function `markup` that returns a number multiplied by itself and a function `markdown` that returns a number's negative. Call `apply_to` with `markup` and 6 and print the result, then call `apply_to` with `markdown` and 6 and print the result.

Expected output:
36
-6
"""
"""
Problem-3: Write a function `apply_again` that takes a function `func` and a `value` and returns the result of applying `func` to `value` twice (call `func` on `value`, then call `func` on that result), plus a function `add_fee` that returns a number plus 1. Call `apply_again` with `add_fee` and 10 and print the result.

Expected output: 12
"""
"""
Problem-4: Write a function `add_tax` that takes `n` and returns it plus 10 percent of it, worked out with whole-number division so the answer stays an int, and a function `is_pricey` that takes `n` and returns whether `n` is above 100. Define a variable `prices` as a list with the values 60, 140, 80, 210. Use `map` to apply `add_tax` to every price, turn the result into a list, and print it. Then use `filter` to keep only the prices `is_pricey` says are pricey, turn the result into a list, and print it.

Expected output:
[66, 154, 88, 231]
[140, 210]
"""
"""
Problem-5: Write a function `add_fee` that takes `n` and returns it plus 5, and a function `add_tax` that takes `n` and returns it plus 10 percent of it, worked out with whole-number division so the answer stays an int. Put both functions in a dict named `charges` under the keys `fee` and `tax` (store the function names, no parentheses). Look up the function under the key `tax`, store it in a variable named `chosen`, call `chosen` with 200, and print the result. Then look up the function under the key `fee`, call it with 200, and print the result.

Expected output:
220
205
"""
