"""
Workshop Problem-10: lambda (Sort Cars) (solution)

Concepts: lambda, passing a lambda as a key= to sorted().
"""

"""
Problem-1. Sort Cars by Price:
  For the list of (brand, price) pairs ("Audi", 40000), ("Kia", 25000), ("BMW", 50000):
    Task-1: print the pairs sorted by price (the second item of each pair), using `sorted()` with a `lambda` as the `key=`.
    Task-2: print the cheapest car (the first item of that sorted list).
    Task-3: for a second fleet of (brand, price) pairs ("Ford", 30000), ("Tata", 18000), ("Benz", 60000), print the pairs sorted by price, again using `sorted()` with a `lambda` as the `key=`.

Expected output:
[('Kia', 25000), ('Audi', 40000), ('BMW', 50000)]
('Kia', 25000)
[('Tata', 18000), ('Ford', 30000), ('Benz', 60000)]
"""
cars = [("Audi", 40000), ("Kia", 25000), ("BMW", 50000)]
# Task-1: sort cars by price with a lambda key
cars_by_price = sorted(cars, key=lambda car: car[1])
print(cars_by_price)
# Task-2: print the cheapest car
print(cars_by_price[0])
# Task-3: sort a second fleet by price with a lambda key
fleet = [("Ford", 30000), ("Tata", 18000), ("Benz", 60000)]
print(sorted(fleet, key=lambda car: car[1]))
