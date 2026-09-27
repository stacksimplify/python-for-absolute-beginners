# Concept-01: A lambda is a tiny ANONYMOUS function - one expression, no name (lambda args: expression)
# Question: How do we write a small function we only need for a moment? (a lambda has no name; to NAME a function, use def)
# A lambda body is ONE expression (no statements, no return keyword) - that is the whole rule.
# E1: with def - a NAMED function, so you can call it again by that name
def square_number(x):
    return x * x

print(square_number(5))

# E2: with lambda - the SAME rule as an ANONYMOUS expression, built and called on the spot
print((lambda x: x * x)(5))
# A lambda can take several arguments too: (lambda x, y: x + y)(2, 3) is 5

# Concept-02: The real use. Hand a function to ANOTHER function, like sorted(key=...) - def or lambda
# Question: How do we sort words like ["banana", "kiwi", "apple", "fig"] by their LENGTH instead of alphabetically? (give sorted a key function; a lambda is perfect here)
# E1: with def - the key is a NAMED function, passed to sorted by name
words = ["banana", "kiwi", "apple", "fig"]

def get_length(word):
    return len(word)

by_length = sorted(words, key=get_length)
print(by_length)

# E2: with lambda - the SAME key written straight into the call, with no name to invent
words = ["banana", "kiwi", "apple", "fig"]
by_length = sorted(words, key=lambda word: len(word))
print(by_length)

# Concept-03: A key function can dig INTO each item - sort (name, score) pairs by the score
# Question: How do we sort records by a field inside each item, like [("Sam", 70), ("Tom", 60), ("Ben", 95)] by score? (key=lambda pair: pair[1])
# E1: with def - the key picks out pair[1], the score
pairs = [("Sam", 70), ("Tom", 60), ("Ben", 95)]

def get_score(pair):
    return pair[1]

by_score = sorted(pairs, key=get_score)
print(by_score)

# E2: with lambda - the same pick, short enough to read inside the call
pairs = [("Sam", 70), ("Tom", 60), ("Ben", 95)]
by_score = sorted(pairs, key=lambda pair: pair[1])
print(by_score)

# Concept-04: map with a lambda - transform every item without naming the transformation
# Question: How do we add 3 to every price in [10, 20, 30, 40] without inventing a name for "add 3"? (map takes any function, and a lambda fits right inside the call)
# E1: with def - the same map as Step-09, where the transformation carries a name
def add_three(n):
    return n + 3

prices = [10, 20, 30, 40]
print(list(map(add_three, prices)))

# E2: with lambda - the same transformation, written where it is used
prices = [10, 20, 30, 40]
print(list(map(lambda n: n + 3, prices)))

# Concept-05: filter with a lambda - keep the items a one-line test says True to
# Question: How do we keep only the prices over 100 in [50, 120, 90, 200] without naming the test? (filter takes any function that answers True or False)
# E1: with def - the same filter as Step-09, where the test carries a name
def is_big(n):
    return n > 100

prices = [50, 120, 90, 200]
print(list(filter(is_big, prices)))

# E2: with lambda - the same test, written where it is used
prices = [50, 120, 90, 200]
print(list(filter(lambda n: n > 100, prices)))
