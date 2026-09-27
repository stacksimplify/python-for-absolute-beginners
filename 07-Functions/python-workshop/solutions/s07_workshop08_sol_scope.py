"""
Workshop Problem-08: scope (Car Counter) (solution)

Concepts: reading a global, the global statement, enclosing scope, nonlocal.
"""

"""
Problem-1: Define a global variable `cars_sold` set to 0, then write a function `sell_car` that takes no arguments, declares `cars_sold` with the `global` statement, and increases `cars_sold` by 1. Call `sell_car` three times, then print `cars_sold`.

Expected output: 3
"""
# Problem-1: global statement mutates the global
cars_sold = 0

def sell_car():
    global cars_sold
    cars_sold = cars_sold + 1

sell_car()
sell_car()
sell_car()
print(cars_sold)

"""
Problem-2: Write a function `garage` that starts a local variable `count` at 0 and holds a nested function `park` which declares `count` with `nonlocal`, increases it by 1, and returns it; inside `garage`, call `park` twice and print each result. Then call `garage`.

Expected output:
1
2
"""
# Problem-2: nonlocal updates the enclosing count
def garage():
    count = 0
    def park():
        nonlocal count
        count = count + 1
        return count
    print(park())
    print(park())

garage()
