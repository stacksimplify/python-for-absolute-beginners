"""
Workshop Problem-05: enumerate and dict (Numbered Cars + Brand Prices) (solution)

Concepts: enumerate(start=1), looping a dict with .items(), f-strings.
"""

"""
Problem-1: Write a program that, for a list of cars Audi, BMW, Kia, uses
  enumerate(start=1) to print each car with its position from 1, like 1. Audi.

Expected output:
1. Audi
2. BMW
3. Kia
"""
# Problem-1 Task-1: number each car with enumerate
cars = ["Audi", "BMW", "Kia"]
for position, car in enumerate(cars, start=1):
    print(f"{position}. {car}")

"""
Problem-2: Write a program that, for a dict of brand to price Audi set to 40000,
  BMW set to 50000, and Kia set to 25000, loops it with .items() and prints each
  pair like Audi: 40000, then prints total: and the sum of every price via .values().

Expected output:
Audi: 40000
BMW: 50000
Kia: 25000
total: 115000
"""
# Problem-2 Task-1: print each brand and price with .items()
prices = {"Audi": 40000, "BMW": 50000, "Kia": 25000}
for brand, price in prices.items():
    print(f"{brand}: {price}")
# Problem-2 Task-2: total every price with a running total over .values()
total = 0
for price in prices.values():
    total += price
print("total:", total)

"""
Problem-3. Pair cars with prices (zip):
  Write a program that, for brands holding "Honda" and "Mazda" and prices holding
  20000 and 25000, loops over both lists together with zip() and prints each pair
  like Honda: 20000.

Expected output:
Honda: 20000
Mazda: 25000
"""
# Problem-3 Task-1: pair each car with its price using zip
brands = ["Honda", "Mazda"]
prices = [20000, 25000]
for brand, price in zip(brands, prices):
    print(f"{brand}: {price}")
