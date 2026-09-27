"""
Practice Problem-07: *args, **kwargs, unpacking, keyword-only args

Concepts: *args (gather into a tuple), **kwargs (gather into a dict),
          call-site unpacking with * and **, keyword-only args with a bare *.
"""
"""
Problem-1: Write a function `sum_prices` that gathers any number of positional arguments (use `*amounts`) and returns their sum. Then:
    Task-1: call `sum_prices` with 4, 5, 6 and print the result.
    Task-2: call `sum_prices` with 25, 35, 45, 55 and print the result.
    Task-3: define a list `line_items` holding 8, 12, 20, call `sum_prices` with that list unpacked into the call (use `*line_items`), and print the result.

Expected output:
15
160
40
"""
"""
Problem-2: Write a function `print_order` that gathers any number of named arguments (use `**fields`) and prints each "key: value" pair on its own line. Then:
    Task-1: call `print_order` with the named arguments product="Mouse" and price=25.
    Task-2: define a dict `order_fields` mapping "product" to "Keyboard" and "price" to 45, then call `print_order` with that dict unpacked into the call (use `**order_fields`).

Expected output:
  product: Mouse
  price: 25
  product: Keyboard
  price: 45
"""
"""
Problem-3: Write a function `pack_size` that takes keyword-only parameters `length` and `width` (a bare `*` before them forces callers to pass them by name) and returns their product. Call it with length=3 and width=4 and print the result.

Expected output: 12
"""
"""
Problem-4: Write a function `place_order` that gathers any number of positional arguments into `*items` and any number of named arguments into `**options` (the `*items` must come BEFORE `**options`), and prints "items:" followed by the items tuple on one line, then "options:" followed by the options dict on the next line. Call it with the positional arguments "mouse" and "cable" and the named arguments express=True and note="Gift".

Expected output:
  items: ('mouse', 'cable')
  options: {'express': True, 'note': 'Gift'}
"""
