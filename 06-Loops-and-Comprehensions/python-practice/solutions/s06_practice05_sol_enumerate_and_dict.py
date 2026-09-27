"""
Practice Problem-05: enumerate and looping a dictionary (solution)

Concepts: enumerate(start=1), looping a dict for its keys, looping a dict with .items(), split(), input(), f-strings.
"""

"""
Problem-1 (Number the Picking Steps):
  Write a program that, for the picking steps scan badge, pick item, pack box,
  uses enumerate(start=1) to print each step numbered, like 1. scan badge.

Expected output:
1. scan badge
2. pick item
3. pack box
"""
# Problem-1 Task-1: number each picking step with enumerate
pick_steps = ["scan badge", "pick item", "pack box"]
for position, step in enumerate(pick_steps, start=1):
    print(f"{position}. {step}")

"""
Problem-2 (Order Totals):
  Write a program that, for an order_totals dictionary of Order-1 set to 90,
  Order-2 set to 75, and Order-3 set to 60:
    Task-1: loop the dictionary directly and print each order id (its keys).
    Task-2: loop it with .items() and print each pair like Order-1: 90.

Expected output:
Order-1
Order-2
Order-3
Order-1: 90
Order-2: 75
Order-3: 60
"""
order_totals = {"Order-1": 90, "Order-2": 75, "Order-3": 60}
# Problem-2 Task-1: loop the dict directly to get its keys (the order ids)
for order_id in order_totals:
    print(order_id)
# Problem-2 Task-2: print each order id and its total with .items()
for order_id, amount in order_totals.items():
    print(f"{order_id}: {amount}")

"""
Problem-3 (Write a Program):
  Write a program that asks the user for products separated by commas, then
  numbers them with enumerate(start=1), like 1. mouse (trim any spaces around
  each product).

Example run (you type "mouse, keyboard, monitor"): 1. mouse / 2. keyboard / 3. monitor
"""
# Problem-3 Task-1: number the user's comma-separated products
slip_text = input("Enter products separated by commas: ")
for line_no, product in enumerate(slip_text.split(","), start=1):
    print(f"{line_no}. {product.strip()}")

"""
Problem-4, Pair Products with Prices (zip):
  Write a program that, for cart_products holding "Mouse" and "Keyboard" and
  cart_prices holding 90 and 85, loops over both lists together with zip() and
  prints each pair like Mouse: 90.

Expected output:
Mouse: 90
Keyboard: 85
"""
# Problem-4 Task-1: pair each product with its price using zip
cart_products = ["Mouse", "Keyboard"]
cart_prices = [90, 85]
for product, price in zip(cart_products, cart_prices):
    print(f"{product}: {price}")
