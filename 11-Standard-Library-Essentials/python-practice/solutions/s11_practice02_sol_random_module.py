"""
Practice Problem-02: random module (solution)

Concepts: random.seed, randint, choice, shuffle.

Problem-1 (Featured Product Picker): Write a program that seeds random with 5 (use random.seed) so the output repeats, then prints these labeled lines:
  Task-1: the number of orders today, a whole number from 50 to 150 (use random.randint).
  Task-2: one featured product picked at random (use random.choice) from the list Laptop, Headphones, Keyboard, Monitor.
  Task-3: the list Laptop, Headphones, Keyboard, Monitor shuffled in place for a fresh homepage order (use random.shuffle).

Expected output (with seed 5):
orders today: 129
featured product: Keyboard
homepage order: ['Headphones', 'Laptop', 'Monitor', 'Keyboard']
"""
import random

random.seed(5)

# Task-1: print random order count from 50 to 150
print("orders today:", random.randint(50, 150))

# Task-2: pick and print one featured product
featured_products = ["Laptop", "Headphones", "Keyboard", "Monitor"]
print("featured product:", random.choice(featured_products))

# Task-3: shuffle the list and print homepage order
homepage_lineup = ["Laptop", "Headphones", "Keyboard", "Monitor"]
random.shuffle(homepage_lineup)
print("homepage order:", homepage_lineup)
