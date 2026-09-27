"""
Workshop Problem-03: save and load JSON (Car Record) (solution)

Concepts: json.dump, json.load.

Write a program that saves the dict {"brand": "Mazda", "year": 2020} to car.json, loads it back,
then (after loading) removes the file. From the loaded dict:
  Task-1: print the whole loaded dict.
  Task-2: print the brand value.

Expected output:
{'brand': 'Mazda', 'year': 2020}
Mazda
"""
import json
from pathlib import Path

car = {"brand": "Mazda", "year": 2020}
with open("car.json", "w", encoding="utf-8") as f:
    json.dump(car, f)
with open("car.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
# Task-1: print the whole loaded dict
print(loaded)
# Task-2: print the brand value
print(loaded["brand"])
Path("car.json").unlink()
