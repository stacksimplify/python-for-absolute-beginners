"""
Practice Problem-01: why objects, a class, and objects

Concepts: a class as a blueprint, a class attribute, creating objects.

Write a program with one class Song:
Task-1: write the class with a single class attribute app set to Tunefy.
Task-2: create two songs s1 and s2 from it, and print each one's app.
Task-3: print s1 itself, to see what a plain object looks like.

Expected output:
Tunefy
Tunefy
<__main__.Song object at 0x...>
"""

# Task-1: the class, with one value shared by every Song
class Song:
    app = "Tunefy"

# Task-2: create two songs and print the shared app
s1 = Song()
s2 = Song()
print(s1.app)
print(s2.app)

# Task-3: print the object itself, which shows a memory address, not data
print(s1)
