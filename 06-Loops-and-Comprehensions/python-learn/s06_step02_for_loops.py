# Concept-01: A for loop runs the block once for each item, no counter needed
# Question: How do we print every item in the list [70, 95, 60, 88], without a counter? (a for loop hands you one item per turn and stops when they run out)
scores = [70, 95, 60, 88]
for score in scores:
    print(score)

# Concept-02: A for loop works on ANY sequence, even the letters of a string
# Question: How do we look at the word "PYTHON" one letter at a time? (a string is a sequence too, so a for loop reads it character by character)
for letter in "PYTHON":
    print(letter)

# Concept-03: A for loop reads a tuple the same way
# Question: How do we go through the values in the tuple (10, 20, 30) one by one?
point = (10, 20, 30)
for value in point:
    print(value)

# Concept-04: Build a running total by adding each item into an accumulator
# Question: How do we add up all the numbers in the list [70, 95, 60, 88] into one total? (the same accumulator as the while loop, with no counter to manage)
scores = [70, 95, 60, 88]
total = 0
for score in scores:
    total += score        # add this score onto the running total
print("total:", total)     # 313

# Concept-05: Put an if inside the for loop to count only the items that match
# Question: How many of the numbers [70, 95, 60, 88] are 80 or above? (count up by 1 only when the test is True)
scores = [70, 95, 60, 88]
passed = 0
for score in scores:
    if score >= 80:        # 80 itself counts, because >= includes the boundary
        passed += 1
print("80 or above:", passed)   # 2

# Concept-06: Unpack a tuple right in the for header (for a, b in list_of_pairs)
# Question: How do we pair each name with its score in one loop, given [("Sam", 70), ("Tom", 95), ("Ben", 60)]?
pairs = [("Sam", 70), ("Tom", 95), ("Ben", 60)]
for name, score in pairs:  # each item is a (name, score) tuple, split into two variables
    print(name, score)

# Concept-07: for vs while - reach for "for" when you already have the items
# Question: We can print the same list ["Sam", "Tom", "Ben"] both ways - which reads cleaner when the list is already in hand? (for when you have the items, while when you loop until a condition)
names = ["Sam", "Tom", "Ben"]
# E1 (for): for-each, no index or counter to manage
for name in names:
    print(name)
# E2 (while): you manage the index i and the stop yourself
i = 0
while i < len(names):
    print(names[i])
    i += 1
