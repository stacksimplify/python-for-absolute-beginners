"""
Workshop Problem-02: tuples (Car Details) (solution)

Concepts: tuples (index, len, unpack, count, index, in, swap, new tuple, list inside a tuple).

Write a program that, for the car record car = ("Mazda", 2020, "red") (brand, year, color):
  Task-1: print the brand (first item), the color (last item, negative index), and how many fields there are.
  Task-2: unpack into brand, year, color and print "Mazda 2020 red".
  Task-3: for the service ratings (4, 5, 4, 4, 3), print how many 4s appear, the position of the 3, and whether a 5 is in there.
  Task-4: the pair (2020, "Mazda") was typed as (year, brand) by mistake, so unpack it, swap in one line, build the corrected tuple new_car, and print new_car and the original pair.
  Task-5: a car keeps a list of owners, history = ("Mazda", ["Sam"]): add "Tom" to the owners list and print history, then clear it, add "Amy", and print history again.

Expected:
Mazda
red
3
Mazda 2020 red
3
4
True
('Mazda', 2020)
(2020, 'Mazda')
('Mazda', ['Sam', 'Tom'])
('Mazda', ['Amy'])
"""

car = ("Mazda", 2020, "red")
# Task-1: print the brand, the color, and the field count
print(car[0])
print(car[-1])
print(len(car))
# Task-2: unpack into brand, year, color and print them
brand, year, color = car
print(brand, year, color)

# Task-3: count the 4s, find the position of the 3, check a 5 is in there
ratings = (4, 5, 4, 4, 3)
print(ratings.count(4))
print(ratings.index(3))
print(5 in ratings)

# Task-4: unpack the swapped pair, swap in one line, build and print the corrected tuple
pair = (2020, "Mazda")
a, b = pair
a, b = b, a
new_car = (a, b)
print(new_car)
print(pair)

# Task-5: change the inner owners list: add, print, clear, add, print again
history = ("Mazda", ["Sam"])
history[1].append("Tom")
print(history)
history[1].clear()
history[1].append("Amy")
print(history)
