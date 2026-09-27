# Concept-01: Label plain variables too; put the hint after a colon
# Question: How do we label a plain variable with its type when we first create it? (colon after name, then the type)
name: str = "Kalyan"
age: int = 30
price: float = 19.99
is_active: bool = True

print(name, age, price, is_active)


# Concept-02: Container hints say what is INSIDE; list[int] means "a list of whole numbers"
# Question: How do we write a type hint that says 'this is a list of numbers, not just any list'? (list[int] for whole numbers)
scores: list[int] = [70, 95, 60, 88]
print("scores:", scores)
print("total:", sum(scores))


# Concept-03: dict[str, int] means "a dictionary with text keys and whole-number values"
# Question: How do we hint that a dictionary has text keys and number values? (dict[str, int] means 'map from text to whole numbers')
stock: dict[str, int] = {"pens": 3, "books": 1}
print("stock:", stock)
print("pens in stock:", stock["pens"])


# Concept-04: Hint a function's container input and its return together, e.g. list[int] -> int
# Question: How do we hint a function that takes a list of numbers as input and returns a single number? (list[int] -> int)
# A list of ints in, one int out
def total(prices: list[int]) -> int:
    return sum(prices)


print("cart total:", total([10, 20, 30]))
