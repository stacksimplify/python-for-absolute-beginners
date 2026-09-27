"""
Workshop Problem-02: one argument (Car Greeter) (solution)

Concepts: parameters vs arguments, passing a value, passing a variable, positional arguments (left to right).

Write a function `show_car` that takes a `brand` and prints "Car: <brand>", plus a function `car_origin` that takes a `brand` and a `country` and prints "<brand> is made in <country>". Then:
  Task-1: call `show_car` with "Audi", then store "BMW" in a variable `favorite` and call `show_car` with that variable.
  Task-2: call `car_origin` with "Toyota" and "Japan" in that order (so the first value fills `brand` and the second fills `country`).

Expected output:
Car: Audi
Car: BMW
Toyota is made in Japan
"""

# Task-1: show a car by value and by variable
def show_car(brand):
    print(f"Car: {brand}")

show_car("Audi")
favorite = "BMW"
show_car(favorite)

# Task-2: show a car origin with positional arguments
def car_origin(brand, country):
    print(f"{brand} is made in {country}")

car_origin("Toyota", "Japan")
