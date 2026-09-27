# Concept-01: A type hint labels each parameter after a colon, and the return after -> (it does not change how the code runs)
# Question: How do we tell Python and our editor what type of value a function expects and returns? (name: str -> str means parameter name is text, returns text)
def greet(name: str) -> str:
    # name is labeled str (text), and -> str says we return text
    return f"Hello, {name}!"


print(greet("Kalyan"))

# Concept-02: A function can take more than one parameter, each with its own hint
# Question: How do we add type hints when a function needs more than one input, giving each parameter its own hint? (area(width: int, height: int) -> int)
# Two ints in, an int out
def area(width: int, height: int) -> int:
    return width * height


print("area:", area(4, 5))

# Concept-03: Hints work with float (decimal) values too
# Question: How do we write type hints for functions that work with decimal numbers instead of whole numbers? (a: float, b: float -> float means decimals in, a decimal out)
def average(a: float, b: float) -> float:
    return (a + b) / 2


print("average:", average(10.0, 20.0))
