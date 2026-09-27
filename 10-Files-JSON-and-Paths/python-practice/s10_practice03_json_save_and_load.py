"""
Practice Problem-03: save and load JSON

Concepts: json.dump, json.load, input().
"""
"""
Problem-1: Save a Product.
Write a program that saves a product dict with name "Wireless Mouse", category "Audio", and price 25
to "product.json", loads it back, then (after loading) removes the file. From the loaded dict:
  Task-1: print the whole loaded dict.
  Task-2: print the name value as "name is: <name>".
  Task-3: print the price value as "price is: <price>".
  Task-4: turn the loaded dict into a JSON string with json.dumps() and print it, then print its
    type() to prove it is text and not a dict.

Expected output:
{'name': 'Wireless Mouse', 'category': 'Audio', 'price': 25}
name is: Wireless Mouse
price is: 25
{"name": "Wireless Mouse", "category": "Audio", "price": 25}
<class 'str'>
"""
"""
Problem-2 (Write a Program): Save a Cart Item.
Write a program that asks the user for a product, saves {"product": <product>} to "cart.json", loads it back and prints it, then removes the file.

Example run (you type "Keyboard"): {'product': 'Keyboard'}
"""
