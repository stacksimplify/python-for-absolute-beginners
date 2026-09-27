"""
Practice Problem-02: variable and container hints (solution)

Concepts: variable hints, list[int], dict[str, int].
"""

"""
Problem-1 (A Typed Price List):
  Define a variable `product_prices` holding the list of whole-number prices 40, 95, 25, with a variable hint saying it is a `list[int]`. Print it with the label "product_prices:", then print the highest price with the label "top price:".

Expected output:
product_prices: [40, 95, 25]
top price: 95
"""
# Problem-1 Task-1: typed price list, print and max
product_prices: list[int] = [40, 95, 25]
print("product_prices:", product_prices)
print("top price:", max(product_prices))

"""
Problem-2 (A Typed Stock Map):
  Define a variable `stock_counts` holding a mapping of product names to whole-number quantities in stock, with "mouse" at 12 and "keyboard" at 7, and a variable hint saying it is a `dict[str, int]`. Print it with the label "stock_counts:", then look up the mouse count and print it with the label "mouse stock:".

Expected output:
stock_counts: {'mouse': 12, 'keyboard': 7}
mouse stock: 12
"""
# Problem-2 Task-1: typed stock map, print and look up mouse
stock_counts: dict[str, int] = {"mouse": 12, "keyboard": 7}
print("stock_counts:", stock_counts)
print("mouse stock:", stock_counts["mouse"])
