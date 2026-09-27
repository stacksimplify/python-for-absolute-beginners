"""
Practice Problem-03: dictionaries

Concepts: dictionaries (create, look up by key, add/update, .update(), len, .get() default,
empty then fill, keys/values/items, in / not in, del / pop, a list value, a nested dict,
list of dictionaries, input()).
"""

"""
Problem-1. Build and Grow a Product Record:
  Write a program that, for a product dictionary with "name" set to "Wireless Mouse" and "price" set to 25:
    Task-1: print the name.
    Task-2: update the price to 20.
    Task-3: add a "brand" of "Logix".
    Task-4: use .update() to set "stock" to 100 and "price" to 22 in one call.
    Task-5: print how many fields the product has, then print the whole product.

Expected output:
Wireless Mouse
4
{'name': 'Wireless Mouse', 'price': 22, 'brand': 'Logix', 'stock': 100}
"""

"""
Problem-2. Safe Lookup and an Empty Cart:
  Write a program that:
    Task-1: for a product dictionary with "name" set to "Mouse" and "price" set to 25, print the value for the missing key "weight", falling back to "unknown".
    Task-2: build an empty cart dictionary, add "item1" set to "Mouse" and "item2" set to "Keyboard", then print the cart.

Expected output:
unknown
{'item1': 'Mouse', 'item2': 'Keyboard'}
"""

"""
Problem-3. Inspect a Record:
  Write a program that, for a product dictionary with "name" set to "Mouse", "price" set to 25, and "brand" set to "Logix":
    Task-1: print the list of keys.
    Task-2: print the list of values.
    Task-3: print the list of (key, value) pairs.

Expected output:
['name', 'price', 'brand']
['Mouse', 25, 'Logix']
[('name', 'Mouse'), ('price', 25), ('brand', 'Logix')]
"""

"""
Problem-4 (Write a Program). Price Lookup:
  Write a program that, for a prices dictionary with "mouse" set to 25 and "keyboard" set to 45, asks for a product name (typed in ANY capitalization) and prints that product's price, or "Not Found" when the product is not in the dictionary.

Example run (you type "Keyboard"): Enter product name for price check: Keyboard -> 45
"""

"""
Problem-5. Remove Fields, Then Check:
  Write a program that, for a product dictionary with "name" set to "Mouse", "price" set to 25, and "old" set to True:
    Task-1: remove "old" with del.
    Task-2: remove "price" with .pop(), keeping its value; print the product, then the removed price.
    Task-3: print whether "name" is a key in the product, and whether "price" is not a key.

Expected output:
{'name': 'Mouse'}
25
True
True
"""

"""
Problem-6. Records That Hold More:
  Write a program that:
    Task-1: for a product dictionary with "name" set to "Mouse" and "tags" set to the list ["wireless", "usb"], print the first tag, then append "ergonomic" and print the tags.
    Task-2: for a product dictionary with "name" set to "Mouse" and "seller" set to the dictionary {"city": "Delhi", "rating": 5}, print the seller's city.
    Task-3: for a catalog list holding {"name": "Mouse", "price": 25} and {"name": "Keyboard", "price": 45}, print the first product's name, then the second product's price.

Expected output:
wireless
['wireless', 'usb', 'ergonomic']
Delhi
Mouse
45
"""
