"""
Practice Problem-03: save and load JSON (solution)

Concepts: json.dump, json.load, input().
"""
import json
from pathlib import Path

"""
Problem-1: Save a Product.
Write a program that saves a product dict with name "Wireless Mouse", category "Audio", and
           price 25 to "product.json", loads it back, then (after loading) removes the file.
           From the loaded dict:
             Task-1: print the whole loaded dict.
             Task-2: print the name value as "name is: <name>".
             Task-3: print the price value as "price is: <price>".
             Task-4: turn the loaded dict into a JSON string with json.dumps() and print it, then print its type().

Expected output:
{'name': 'Wireless Mouse', 'category': 'Audio', 'price': 25}
name is: Wireless Mouse
price is: 25
{"name": "Wireless Mouse", "category": "Audio", "price": 25}
<class 'str'>
"""
product = {"name": "Wireless Mouse", "category": "Audio", "price": 25}
with open("product.json", "w", encoding="utf-8") as f:
    json.dump(product, f, indent=2)
with open("product.json", "r", encoding="utf-8") as f:
    loaded_product = json.load(f)
# Problem-1 Task-1: print the whole loaded dict
print(loaded_product)
# Problem-1 Task-2: print the name value
print("name is:", loaded_product["name"])
# Problem-1 Task-3: print the price value
print("price is:", loaded_product["price"])

# Problem-1 Task-4: json.dumps turns the dict into a JSON string (text), not a file
text = json.dumps(loaded_product)
print(text)
print(type(text))
Path("product.json").unlink()

"""
Problem-2 (Write a Program): Save a Cart Item.
Write a program that asks the user for a product, saves {"product": <product>} to "cart.json", loads it back and prints it, then removes the file.

Example run (you type "Keyboard"): {'product': 'Keyboard'}
"""
chosen = input("Enter a product: ")
cart_item = {"product": chosen}
with open("cart.json", "w", encoding="utf-8") as f:
    json.dump(cart_item, f)
with open("cart.json", "r", encoding="utf-8") as f:
    print(json.load(f))
Path("cart.json").unlink()
