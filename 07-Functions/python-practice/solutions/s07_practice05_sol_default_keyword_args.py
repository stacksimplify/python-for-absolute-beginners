"""
Practice Problem-05: default and keyword arguments (solution)

Concepts: default parameter values, keyword arguments (name=value in the call),
the mutable-default trap (use None, not []).
"""

"""
Problem-1. A Default Currency:
  Write a function `format_price` that takes an `amount` and a `currency` that defaults to "USD", and prints "<amount> <currency>". Call it with 25 only (using the default currency), then call it with 30 and "EUR" (overriding the currency).

Expected output:
25 USD
30 EUR
"""
# Problem-1: currency parameter defaults to USD
def format_price(amount, currency="USD"):
    print(f"{amount} {currency}")

format_price(25)
format_price(30, "EUR")

"""
Problem-2. Keyword Arguments:
  Write a function `stock_note` that takes a `product` and a `section` and prints "<product> is stocked in <section>". Call it passing the arguments BY NAME and out of order, `section` before `product`, using Mouse and Audio.

Expected output:
Mouse is stocked in Audio
"""
# Problem-2: pass arguments by name, out of order
def stock_note(product, section):
    print(f"{product} is stocked in {section}")

stock_note(section="Audio", product="Mouse")

"""
Problem-3. The Mutable-Default Trap:
  Write a function `add_to_cart` that takes an `item` and a `cart` that defaults to None, starts a fresh empty list when `cart` is None, adds `item` to the cart, and returns the cart. Call it with "mouse" and print the result, then call it with "keyboard" and print the result (each call must start with a fresh list).

Expected output:
['mouse']
['keyboard']
"""
# Problem-3: use None default to avoid the mutable-default trap
def add_to_cart(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return cart

print(add_to_cart("mouse"))
print(add_to_cart("keyboard"))
