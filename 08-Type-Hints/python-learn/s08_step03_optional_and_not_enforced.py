# Concept-01: X | None means "an X, or None", for a value that might be missing
# Question: How do we say that a function might return a value of a certain type, or might return nothing instead? (X | None means 'type X or None')
def find_price(name: str) -> int | None:
    catalog = {"pen": 2, "book": 15}
    # .get returns None when the key is missing
    return catalog.get(name)


print("pen price:", find_price("pen"))
print("eraser price:", find_price("eraser"))


# Concept-02: Python does NOT enforce hints at runtime; they are for humans and editors
# Question: How do we know whether type hints are enforced when the code runs? (they are not; hints only guide humans and tools)
# greet is labeled to take a str, but Python will still run it with a number.
# A type checker like mypy would flag it, but Python itself does not stop it.
def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("Kalyan"))  # The intended use: a str
print(greet(123))  # Still runs! Python ignores the hint at runtime

# Hints matter because real ML and web code leans on them. Tools like
# Pydantic (data models) and FastAPI (web APIs) read your hints to check
# and convert data for you. Good hints now make that code much easier later.
