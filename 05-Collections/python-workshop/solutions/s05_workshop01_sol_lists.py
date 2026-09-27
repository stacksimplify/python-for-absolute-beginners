"""
Workshop Problem-01: lists (Car Inventory) (solution)

Concepts: lists (count, append, insert, extend, remove, pop, sort, reverse, copy, clear, nested lists).

Write a program that, for the cars Audi, BMW, Kia:
  Task-1: print how many cars there are.
  Task-2: add Ford to the end and print the list.
  Task-3: insert Tesla at index 1 and print the list.
  Task-4: extend the list with ["Honda", "Mazda"] and print the list.
  Task-5: remove BMW and print the list.
  Task-6: pop the last car and print what was removed.
  Task-7: sort the list, then reverse it, and print the list.
  Task-8: make a copy, clear the original, then print the original and the copy.
  Task-9: from the nested list [["Audi", 2020], ["Kia", 2022]], print the second car's year.

Expected:
3
['Audi', 'BMW', 'Kia', 'Ford']
['Audi', 'Tesla', 'BMW', 'Kia', 'Ford']
['Audi', 'Tesla', 'BMW', 'Kia', 'Ford', 'Honda', 'Mazda']
['Audi', 'Tesla', 'Kia', 'Ford', 'Honda', 'Mazda']
Mazda
['Tesla', 'Kia', 'Honda', 'Ford', 'Audi']
[]
['Tesla', 'Kia', 'Honda', 'Ford', 'Audi']
2022
"""

cars = ["Audi", "BMW", "Kia"]
# Task-1: print how many cars there are
print(len(cars))

# Task-2: add Ford to the end and print the list
cars.append("Ford")
print(cars)

# Task-3: insert Tesla at index 1 and print the list
cars.insert(1, "Tesla")
print(cars)

# Task-4: extend the list with two cars and print the list
cars.extend(["Honda", "Mazda"])
print(cars)

# Task-5: remove BMW and print the list
cars.remove("BMW")
print(cars)

# Task-6: pop the last car and print what was removed
print(cars.pop())

# Task-7: sort the list, then reverse it, and print the list
cars.sort()
cars.reverse()
print(cars)

# Task-8: copy, clear the original, print original and copy
backup = cars.copy()
cars.clear()
print(cars)
print(backup)

# Task-9: from the nested list, print the second car's year
car_years = [["Audi", 2020], ["Kia", 2022]]
print(car_years[1][1])
