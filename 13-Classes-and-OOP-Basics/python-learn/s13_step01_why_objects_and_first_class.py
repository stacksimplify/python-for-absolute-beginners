# Running example: one Product class grows across the concepts below; each block re-shows the class it needs, so you can run the whole file top to bottom OR any single block on its own.
# Concept-01: Without objects, one product's data lives in loose variables that are easy to mix up
# Question: What goes wrong when each product's name, price, and stock live in separate variables? (nothing ties them together, and two products already need six)
product1_name = "Laptop"
product1_price = 1000
product1_stock = 5
product2_name = "Mouse"
product2_price = 25
product2_stock = 200
print(product1_name, product1_price, product1_stock)
print(product2_name, product2_price, product2_stock)
# Two products already need six variables. Ten products would need thirty.

# Concept-02: A class is a blueprint that describes what every product looks like
# Question: How do we describe "a product" ONCE and reuse that description for every product? (write a class with the class keyword)
class Product:
    store_name = "Pyzon Store"

# Concept-03: Create an object (also called an instance) by calling the class name
# Question: How do we make actual products from the Product blueprint? (call the class name like a function; each call makes a separate object that can read the blueprint's store_name)
class Product:
    store_name = "Pyzon Store"

p1 = Product()
p2 = Product()
print(p1.store_name)
print(p2.store_name)

# Concept-04: Sharing the store name is right, but no product has its OWN data yet, and printing one shows a memory address
# Question: What is still missing once p1 and p2 exist? (no name or price of their own, and print(p1) shows only a memory address; __init__ fixes the first in Step-02, __str__ the second in Step-05)
class Product:
    store_name = "Pyzon Store"

p1 = Product()
p2 = Product()
print(p1)
print(p2)
