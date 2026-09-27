# The random module makes random values: numbers, a random pick, or a shuffled list.

# Concept-01: dir() shows what is inside the random module, the same way it did for math
# Question: What tools does the random module give us, and is the dice roll we want in there?
import random

all_names = dir(random)
random_tools = [tool for tool in all_names if not tool.startswith("_")]

print("names in random:", len(all_names))
print("tools you can use:", len(random_tools))
print(", ".join(random_tools))

# Concept-02: random.randint(a, b) gives a whole number from a to b, both ends included
# Question: How do we roll a dice in code (pick a whole number from 1 to 6, both ends included)?
import random

random.seed(42)   # comment this line out, run it a few times, and the roll changes every time
print("a dice roll:", random.randint(1, 6))

# Concept-03: random.random() gives a decimal from 0.0 up to 1.0; random.uniform(a, b) gives one in any range
# Question: How do we get a random decimal, either between 0.0 and 1.0 or between two bounds we choose?
import random

random.seed(42)   # comment this line out and the decimals change every run

# E1: random() always lands between 0.0 and 1.0, and takes no arguments.
print("the decimal:", random.random())

# E2: uniform(a, b) is the same idea stretched to any range you choose.
print("a price:", random.uniform(10, 99))

# Concept-04: random.choice picks ONE item; random.sample picks several at once with no repeats
# Question: How do we pick one random name, and how do we pick three winners without the same person twice?
import random

random.seed(42)   # comment out to see it change; keep 42 to see the repeat in E1
names = ["Sam", "Tom", "Ben", "Joe"]

# E1: choice hands back ONE name. Call it three times and the same person can come back.
print("three separate picks:", random.choice(names), random.choice(names), random.choice(names))

# E2: sample takes several at once and never repeats anyone.
print("three winners:", random.sample(names, 3))

# Concept-05: random.shuffle reorders a list IN PLACE, and hands back None rather than the new list
# Question: What happens if we write deck = random.shuffle(deck), the way we would with sorted()?
import random

random.seed(42)   # comment this line out and the deck lands in a different order each run

# E1: First, the mistake. shuffle returns None, so assigning its result throws the deck away.
deck = [1, 2, 3, 4, 5]
deck = random.shuffle(deck)
print("deck after assigning the result:", deck)

# E2: Second, the fix. Call shuffle and let it change the list itself; do not assign it.
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print("shuffled list:", deck)
