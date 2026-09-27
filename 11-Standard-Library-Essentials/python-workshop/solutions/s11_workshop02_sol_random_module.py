"""
Workshop Problem-02: random module (Pick a Car) (solution)

Concepts: random.seed, random.choice, random.randint.

Write a program that seeds random with 3 (use random.seed), then prints these labeled lines:
  Task-1: one car picked at random (use random.choice) from the list Mazda, Tesla, Honda, Kia.
  Task-2: a lucky number from 1 to 100 (use random.randint).

Expected output:
picked: Tesla
lucky number: 76
"""
import random

random.seed(3)
# Task-1: pick and print one random car
cars = ["Mazda", "Tesla", "Honda", "Kia"]
print("picked:", random.choice(cars))
# Task-2: print a lucky number from 1 to 100
print("lucky number:", random.randint(1, 100))
