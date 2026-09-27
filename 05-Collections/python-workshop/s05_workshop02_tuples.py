"""
Workshop Problem-02: tuples (Car Details)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

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
