# Running example: one Product class grows across the concepts below; each block re-shows the class it needs, so you can run the whole file top to bottom OR any single block on its own.
# Concept-01: A class attribute is written in the class body and is SHARED by every object
# Question: Every product is sold by the same store. How do we keep that one store name for all of them instead of storing it on each product? (write it once in the class body as a class attribute; every object reads the same value)
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print(p1.store_name)
print(p2.store_name)

# Concept-02: A class attribute can be read from the class itself OR through any object
# Question: How do we read the store name, from the class or from a product? (both work: Product.store_name, p1.store_name and p2.store_name all give the same shared value)
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)

# Reading the class attribute three ways
print("Using Class:", Product.store_name)
print("Using p1 object:", p1.store_name)
print("Using p2 object:", p2.store_name)

# Concept-03: Instance attributes belong to one object only; changing one does not touch the others
# Question: What happens to the Mouse when only the Laptop's price and stock change? (nothing, because name, price and stock live on each object separately; the Mouse keeps 25 and 200)
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

# Create an object of a class
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print("P1 - Before Update:", p1.name, p1.price, p1.stock)
print("P2 - Before Update:", p2.name, p2.price, p2.stock)
p1.price = 900
p1.stock = 500
print("P1 - After Update:", p1.name, p1.price, p1.stock)
print("P2 - After Update:", p2.name, p2.price, p2.stock)

# Concept-04: If the same name exists on the class AND the instance, the instance attribute wins
# Question: One product is sold by a third-party seller under their own store name. How do we change it for that product only, without touching every other product? (assign it on that object; p2 gets its own value, while p1 and the class still read Pyzon Store)
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

# Create an object of a class
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print("P1 - Before Update:", p1.store_name, p1.name, p1.price, p1.stock)
print("P2 - Before Update:", p2.store_name, p2.name, p2.price, p2.stock)
p2.store_name = "ABC Sellers"
print("P1 - After Update:", p1.store_name, p1.name, p1.price, p1.stock)
print("P2 - After Update:", p2.store_name, p2.name, p2.price, p2.stock)
print("After Update - Class level:", Product.store_name)
