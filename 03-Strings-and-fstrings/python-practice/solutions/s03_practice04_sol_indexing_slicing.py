"""
Practice Problem-04: indexing and slicing (solution)

Concepts: indexing, slicing, input().
"""

"""
Problem-1:
  Write a program that, for the word "Rocket":
    Task-1: print its first letter.
    Task-2: print its first 3 letters.
    Task-3: print its last 3 letters.

Expected output:
R
Roc
ket
"""
word = "Rocket"
# Problem-1 Task-1: print the first letter
print(word[0])
# Problem-1 Task-2: print the first 3 letters
print(word[0:3])
# Problem-1 Task-3: print the last 3 letters
print(word[-3:])

"""
Problem-2 (Write a Program): write a program that asks the user for a word and
prints its first letter and its last letter.

Example run:
Type a word: Mazda
M
a
"""
typed = input("Type a word: ")
print(typed[0])
print(typed[-1])

"""
Problem-3. Step and Reverse:
  Write a program that, for the word "Rocket":
    Task-1: print every second character.
    Task-2: print the word reversed.
    Task-3: print the word with its first letter changed to "J" (remember strings
            are immutable, so build a new string).

Expected output:
Rce
tekcoR
Jocket
"""
word = "Rocket"
# Problem-3 Task-1: print every second character
print(word[::2])
# Problem-3 Task-2: print the word reversed
print(word[::-1])
# Problem-3 Task-3: build word with first letter changed to J
print("J" + word[1:])
