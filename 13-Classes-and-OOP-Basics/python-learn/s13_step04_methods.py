# Running example: one Product class grows across the concepts below; each block re-shows the class it needs, so you can run the whole file top to bottom OR any single block on its own.
# Concept-01: A method is a function inside a class; its first parameter is self, so it can use the object's own data
# Question: How do we give a product behavior as well as data, like a line built from its own name and price? (write a method inside the class and reach the data through self)
# Define a class
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # Describe method
    def describe(self):
        return f"{self.name} costs ${self.price}"

# Create an object of a class
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print(p1.describe())
print(p2.describe())

# Concept-02: A method can also CHANGE the object's data
# Question: How do we let a product be sold or restocked, so the stock change lives inside the class instead of everywhere in our code? (write methods that update self.stock)
# Define a class
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # Describe method
    def describe(self):
        return f"{self.name} costs ${self.price}"

    # Restock method
    def restock(self, qty):
        # self.stock = self.stock + qty
        self.stock += qty

    # Sell Method
    def sell(self, qty):
        # self.stock = self.stock - qty
        self.stock -= qty

# Create an object of a class
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print("Current stock:", p1.stock)
p1.restock(20)
print("After restock:", p1.stock)
p1.sell(24)
print("After sell:", p1.stock)

# Concept-03: A method can RETURN a value or just ACT; returning lets the caller use the result
# Question: How do we choose between a method that returns a value and one that just acts? (describe returns text we can keep using, like label.upper(); restock only changes stock, so it returns None)
# Define a class
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # Describe method
    def describe(self):
        return f"{self.name} costs ${self.price}"

    # Restock method
    def restock(self, qty):
        # self.stock = self.stock + qty
        self.stock += qty

    # Sell Method
    def sell(self, qty):
        # self.stock = self.stock - qty
        self.stock -= qty

# Create an object of a class
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print("Describe method returns data:", p1.describe())
label = p1.describe()
print(label.upper())

# returns None
print("Restock method doesn't return data:", p1.restock(20))
print(p1.stock)
my_stock_data = p1.restock(20)
print("My Stock data:", my_stock_data)

# Concept-04: A method needs the () to run; without (), you get the method object itself
# Question: Why does p1.describe() give the text but p1.describe does not? (without () you only name the method and get the method object; with () you actually run it)
# Define a class
class Product:
    # Class Attribute
    store_name = "Pyzon Store"
    # Defined a Init method / Function
    def __init__(self, name, price, stock):
        # Instance Attributes
        self.name = name
        self.price = price
        self.stock = stock

    # Describe method
    def describe(self):
        return f"{self.name} costs ${self.price}"

    # Restock method
    def restock(self, qty):
        # self.stock = self.stock + qty
        self.stock += qty

    # Sell Method
    def sell(self, qty):
        # self.stock = self.stock - qty
        self.stock -= qty

# Create an object of a class
p1 = Product("Laptop", 1000, 5)
p2 = Product("Mouse", 25, 200)
print("With parentheses:", p1.describe())
print("Without parentheses:", p1.describe)
