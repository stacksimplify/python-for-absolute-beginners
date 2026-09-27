"""
Practice Problem-08: scope (local, global, enclosing, LEGB, global/nonlocal)

Concepts: local scope, reading a global, enclosing scope (nested functions),
LEGB rule, the global statement, the nonlocal statement.
"""
"""
Problem-1. Local and global:
  Define a global variable `status` set to "open", then write a function `set_status` that takes no arguments, sets its OWN local `status` to "closed", and prints it. Call `set_status`, then print the global `status` to show it did not change.

Expected output:
closed
open
"""
"""
Problem-2. The global statement:
  Define a global variable `cart_count` set to 0, then write a function `add_item` that takes no arguments, declares `cart_count` with the `global` statement, and increases `cart_count` by 10. Call `add_item` twice, then print `cart_count`.

Expected output: 20
"""
"""
Problem-3. Enclosing scope and nonlocal:
  Write a function `make_register` that starts a local variable `tally` at 0 and holds a nested function `ring_up` which declares `tally` with `nonlocal`, increases it by 1, and returns it; inside `make_register`, call `ring_up` twice and print each result. Then call `make_register`.

Expected output:
1
2
"""
