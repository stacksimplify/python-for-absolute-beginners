# Running example: one Product class grows across the concepts below; each block re-shows the class it needs, so you can run the whole file top to bottom OR any single block on its own.
# Concept-01: A @classmethod receives the CLASS itself (cls), so cls(...) builds and returns a brand-new object, which makes from_dict an alternate constructor
# Question: Our product data arrives as dictionaries, like data1 for the Laptop and data2 for the Mouse. How do we build a Product from each one without unpacking data1["name"], data1["price"] and data1["stock"] by hand every time? (write a @classmethod from_dict: it receives the class as cls and returns cls(...), a real Product, so Product.from_dict(data1) and Product.from_dict(data2) do it in one call)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # __str__ method
    def __str__(self):
        return f"{self.name} costs ${self.price} and {self.stock} in stock"

    # from_dict Method with @classmethod Dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["stock"])

# Data in Dictionary Format
data1 = {
    "name": "Laptop",
    "price": 1000,
    "stock": 5
}

data2 = {
    "name": "Mouse",
    "price": 50,
    "stock": 200
}
# Create an object of a class
# Before from_dict method and @classmethod Decorator
p1 = Product(data1["name"], data1["price"], data1["stock"])
print(p1)
p2 = Product(data2["name"], data2["price"], data2["stock"])
print(p2)

# After from_dict method and @classmethod Decorator
p1 = Product.from_dict(data1)
print(p1)
p2 = Product.from_dict(data2)
print(p2)

# Concept-02: A @staticmethod takes neither self nor cls, so it is a related helper that lives on the class
# Question: Checking "is this price valid?" needs no product and no class data. Where should such a helper live? (make it a @staticmethod on Product: it belongs with products, but it needs no self and no cls)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # __str__ method
    def __str__(self):
        return f"{self.name} costs ${self.price} and {self.stock} in stock"

    # from_dict Method with @classmethod Dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["stock"])

    # Static Method (which doesnt need cls or self)
    @staticmethod
    def is_valid_price(price):
        return price > 0

# Test static method
print(Product.is_valid_price(1000))
print(Product.is_valid_price(-5))

# Concept-03: classmethod = alternate constructor (uses cls); staticmethod = related helper (uses neither)
# Question: How do we choose between @classmethod and @staticmethod? (need the class itself, like building a new object -> @classmethod with cls; just a related helper that needs no object and no class -> @staticmethod)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # __str__ method
    def __str__(self):
        return f"{self.name} costs ${self.price} and {self.stock} in stock"

    # from_dict Method with @classmethod Dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["stock"])

    # Static Method (which doesnt need cls or self)
    @staticmethod
    def is_valid_price(price):
        return price > 0

# Data in Dictionary Format
data = {
    "name": "Laptop",
    "price": 1000,
    "stock": 5
}

# Create an object of a class
# If our price is valid then only i will create the p1 object
if Product.is_valid_price(data["price"]):
    p1 = Product.from_dict(data)
    print("Price is valid, so p1 object friendly message is:", p1)
else:
    print("Price is not valid")
