# Running example: one Product class grows across the concepts below; each block re-shows the class it needs, so you can run the whole file top to bottom OR any single block on its own.
# Concept-01: Printing a plain object shows a memory address, not the data
# Question: We saw this in Step-01. Why does print(p1) show <__main__.Product object at 0x...> instead of the product? (Python has no idea how you want your object shown, so it falls back to the type and address)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product("Laptop", 1000, 5)
print(p1)

# Concept-02: A normal method can build the text, but print() will not use it
# Question: We already know how to write methods, so why does print(p1) still show the address when describe() clearly works? (print() does not hunt for a likely-looking method; it looks for one exact name)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    def describe(self):                      # a normal method, no underscores
        return f"{self.name} costs ${self.price} and {self.stock} in stock"

p1 = Product("Laptop", 1000, 5)
print(p1)                                    # still the address; print() ignored describe()
print(p1.describe())                         # the text was there all along, if WE call it

# Concept-03: __str__ tells print() how to show the object in a friendly way
# Question: How do we make print(p1) show "Laptop costs $1000 and 5 in stock" by itself? (name the method exactly __str__, because print() looks for that one name)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # Dunder Methods
    # __str__ method
    def __str__(self):                       # same body as describe, only the NAME changed
        return f"{self.name} costs ${self.price} and {self.stock} in stock"

p1 = Product("Laptop", 1000, 5)
print(p1)

# Concept-04: repr() has its own default too, and it is the same unhelpful address
# Question: print(p1) fell back to an address without __str__. What does repr(p1) show on the same plain object? (the same address, because repr has its own default; it needs its own special method, __repr__)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

p1 = Product("Laptop", 1000, 5)
print(p1)          # the str default: an address
print(repr(p1))    # the repr default: the SAME address, and repr needs its own method too

# Concept-05: __repr__ is the developer form, meant to be exact rather than pretty
# Question: How do we make repr(p1) show a precise form with the field names, instead of that default? (add __repr__, the version repr(), the REPL, and containers all use)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # Dunder Methods
    # __str__ method
    def __str__(self):
        return f"{self.name} costs ${self.price} and {self.stock} in stock"

    # __repr__ method
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r}, stock={self.stock!r})"

p1 = Product("Laptop", 1000, 5)
print(p1)          # __str__: the friendly one
print(repr(p1))    # __repr__: the exact one

# Concept-06: A list uses __repr__ for each item, while a single object uses __str__
# Question: We wrote a friendly __str__, so why does printing a LIST of products show the exact form instead? (a container shows the __repr__ of each item; print() on one object still uses __str__, so a list gives you the precise version, handy for debugging)
# Define a class
class Product:
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # Dunder Methods
    # __str__ method
    def __str__(self):
        return f"{self.name} costs ${self.price} and {self.stock} in stock"

    # __repr__ method
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r}, stock={self.stock!r})"

products = [Product("Laptop", 1000, 5), Product("Mouse", 25, 200)]
print(products)       # a list shows __repr__ for each item
print(products[0])    # a single object still uses __str__
