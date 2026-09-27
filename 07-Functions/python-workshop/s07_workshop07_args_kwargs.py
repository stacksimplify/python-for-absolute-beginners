"""
Workshop Problem-07: *args, **kwargs, unpacking, keyword-only args (Car Tools)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: *args (gather into a tuple), **kwargs (gather into a dict),
          call-site unpacking with * and **, keyword-only args with a bare *.
"""
"""
Problem-1: gather positional args and unpack a list
  Write a function `service_total` that gathers any number of positional arguments (use `*prices`) and returns their sum. Then:
    Task-1: call `service_total` with 1500, 800, 2300 and print the result.
    Task-2: define a list `repairs` holding 500, 250, call `service_total` with that list unpacked into the call (use `*repairs`), and print the result.

Expected output:
  4600
  750
"""
"""
Problem-2: gather named args and unpack a dict
  Write a function `show_car` that gathers any number of named arguments (use `**details`) and prints each "key: value" pair on its own line. Then:
    Task-1: call `show_car` with the named arguments brand="Mazda" and year=2020.
    Task-2: define a dict `car` mapping "brand" to "Audi" and "year" to 2021, then call `show_car` with that dict unpacked into the call (use `**car`).

Expected output:
  brand: Mazda
  year: 2020
  brand: Audi
  year: 2021
"""
"""
Problem-3: keyword-only arguments with a bare *
  Write a function `price_after_tax` that takes keyword-only parameters `price` and `tax` (a bare `*` before them forces callers to pass them by name) and returns their sum. Call it with price=20000 and tax=1800 and print the result.

Expected output:
  21800
"""
"""
Problem-4: one function with both *args and **kwargs
  Write a function `make_booking` that gathers any number of positional arguments into `*extras` and any number of named arguments into `**details` (the `*extras` must come BEFORE `**details`), and prints "extras:" followed by the extras tuple on one line, then "details:" followed by the details dict on the next line. Call it with the positional arguments "GPS" and "child seat" and the named arguments model="Creta" and days=3.

Expected output:
  extras: ('GPS', 'child seat')
  details: {'model': 'Creta', 'days': 3}
"""
