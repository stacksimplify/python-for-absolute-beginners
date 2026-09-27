# Running example: one Product class grows across the concepts below; each block re-shows the class it needs, so you can run the whole file top to bottom OR any single block on its own.
# Concept-01: __init__ is a special method Python runs automatically when you create an object
# Question: In Step-01 no product had a name of its own. How do we run some setup code the moment a product is created? (define __init__, and Python calls it for you)
class Product:
    def __init__(self):
        print("A new product was created")

p1 = Product()

# Concept-02: self is the object being created; it is how the method reaches that object's own data
# Question: What exactly is self? (it is the same object you get back, so print(self) inside and print(p1) outside show the SAME object)
class Product:
    def __init__(self):
        print("inside  __init__:", self)

p1 = Product()
print("outside __init__:", p1)

# Concept-03: Give __init__ parameters so each object starts with its OWN data
# Question: How do we finally give each product a different name, like Product("Laptop") and Product("Mouse")? (add a parameter to __init__ and store it on self)
class Product:
    def __init__(self, name):
        self.name = name

p1 = Product("Laptop")
p2 = Product("Mouse")
print(p1.name)
print(p2.name)

# Concept-04: Attributes stored on self are instance attributes; the usual style is self.name = name
# Question: How do we store more than one piece of data per product, like a name, a price AND a stock count? (assign each parameter onto self; each object keeps its own copy)
class Product:
    def __init__(self, name, price, stock):
        # Instance attribute: data that belongs to THIS object
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print(p1.name, p1.price, p1.stock)
print(p2.name, p2.price, p2.stock)
