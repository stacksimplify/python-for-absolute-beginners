"""
Workshop Problem-01: class and objects (Car)

Concepts: a class as a blueprint, a class attribute, creating objects.

Write a program with one class Car:
Task-1: write the class with a class attribute wheels set to 4.
Task-2: create two cars c1 and c2, and print each one's wheels.
Task-3: print c1 itself, to see a plain object.

Expected output:
4
4
<__main__.Car object at 0x...>
"""

# Task-1: the class, with one value shared by every Car
class Car:
    wheels = 4

# Task-2: create two cars and print the shared wheels
c1 = Car()
c2 = Car()
print(c1.wheels)
print(c2.wheels)
# Task-3: print the object itself, which shows a memory address, not data
print(c1)
