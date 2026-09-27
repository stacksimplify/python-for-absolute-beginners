"""
Workshop Problem-03: dictionaries (Car Record) (solution)

Concepts: dictionaries (look up by key, add a key, .get() default, in / not in, len,
.update(), keys / items, del / pop, a list value, a nested dict, list of dictionaries).

Write a program that, for a car dictionary with "brand" set to "Mazda" and "year" set to 2020:
  Task-1: print the brand.
  Task-2: add a "color" of "red", then print the whole car dictionary.
  Task-3: print the owner, falling back to "unknown" when there is no "owner" key.
  Task-4: print whether "brand" is a key in the car, and whether "owner" is not a key.
  Task-5: print how many fields the car has now.
  Task-6: use .update() to set "year" to 2021 and add "price" of 15000 in one call; print the car's keys, then its (key, value) pairs.
  Task-7: remove "price" with del, then remove "color" with .pop() keeping its value; print the car, then the removed color.
  Task-8: for a car that keeps a list of services ["oil", "tires"], print the first service, append "brakes", and print the services.
  Task-9: for a car with a nested owner {"name": "Sam", "city": "Delhi"}, print the owner's city.
  Task-10: for a garage list holding {"brand": "Mazda", "year": 2021} and {"brand": "Kia", "year": 2022}, print the first car's brand, then the second car's year.

Expected:
Mazda
{'brand': 'Mazda', 'year': 2020, 'color': 'red'}
unknown
True
True
3
['brand', 'year', 'color', 'price']
[('brand', 'Mazda'), ('year', 2021), ('color', 'red'), ('price', 15000)]
{'brand': 'Mazda', 'year': 2021}
red
oil
['oil', 'tires', 'brakes']
Delhi
Mazda
2022
"""

# Task-1: print the brand
car = {"brand": "Mazda", "year": 2020}
print(car["brand"])

# Task-2: add a "color" of "red", then print the whole car dictionary
car["color"] = "red"
print(car)

# Task-3: print the owner, falling back to "unknown" when there is no "owner" key
print(car.get("owner", "unknown"))

# Task-4: print whether "brand" is a key, and whether "owner" is not a key
print("brand" in car)
print("owner" not in car)

# Task-5: print how many fields the car has now
print(len(car))

# Task-6: .update() to set "year" and add "price", then print the keys and the (key, value) pairs
car.update({"year": 2021, "price": 15000})
print(list(car.keys()))
print(list(car.items()))

# Task-7: remove "price" with del, remove "color" with .pop() keeping its value
del car["price"]
removed_color = car.pop("color")
print(car)
print(removed_color)

# Task-8: a value that is a list of services, so read the first, append one, print the list
car = {"brand": "Mazda", "services": ["oil", "tires"]}
print(car["services"][0])
car["services"].append("brakes")
print(car["services"])

# Task-9: a value that is a nested owner dict, so read the city with a chained lookup
car = {"brand": "Mazda", "owner": {"name": "Sam", "city": "Delhi"}}
print(car["owner"]["city"])

# Task-10: a garage list of car dicts, so read the first car's brand and the second car's year
garage = [{"brand": "Mazda", "year": 2021}, {"brand": "Kia", "year": 2022}]
print(garage[0]["brand"])
print(garage[1]["year"])
