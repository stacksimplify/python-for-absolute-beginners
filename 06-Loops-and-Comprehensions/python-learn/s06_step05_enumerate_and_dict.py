# Concept-01: enumerate gives the position AND the item together (default start 0)
# Question: How do we number the list ["Sam", "Tom", "Ben"] the computer's way, like "0 Sam, 1 Tom"? (enumerate hands you the position, so you keep no counter of your own)
names = ["Sam", "Tom", "Ben"]
# E1: the long way - keep your own counter and remember to move it on every turn
index = 0
for name in names:
    print(index, name)
    index += 1     # forget this line and every row reports position 0
# E2: the SAME result from enumerate, with no counter to keep and none to forget
for index, name in enumerate(names):
    print(index, name)

# Concept-02: enumerate can start the count at 1, for a numbered list people read
# Question: How do we print a numbered list people can read, like "1. Sam"? (enumerate(names, start=1) begins the count at 1 instead of 0)
names = ["Sam", "Tom", "Ben"]
for position, name in enumerate(names, start=1):
    print(f"{position}. {name}")

# Concept-03: Looping a dictionary gives you its keys, in the order they were added
# Question: How do we read the field names off the record {"name": "Sam", "age": 20, "city": "Delhi"}, one per turn? (looping a dict gives you its KEYS by default)
student = {"name": "Sam", "age": 20, "city": "Delhi"}
for field in student:   # same as: for field in student.keys()
    print(field)  # a dict loops in insertion order, so this output is always the same
# Do NOT add or delete keys while looping a dict; loop student.copy() if you must change it while looping.
# Uncomment to see the trap - changing the dict mid-loop stops it dead:
# for field in student:
#     student["extra"] = 1   # RuntimeError: dictionary changed size during iteration

# Concept-04: .items() gives the key AND the value together
# Question: How do we print each field of {"name": "Sam", "age": 20, "city": "Delhi"} with its value, like "name -> Sam"? (.items() hands you the key and the value together)
student = {"name": "Sam", "age": 20, "city": "Delhi"}
for field, value in student.items():
    print(field, "->", value)

# Concept-05: Add up a dictionary's values with a running total
# Question: How do we add up all the scores in the name-to-score dictionary {"Sam": 70, "Tom": 95, "Ben": 60}? (.values() gives just the values, so the keys are never touched)
scores_by_name = {"Sam": 70, "Tom": 95, "Ben": 60}
total = 0
for score in scores_by_name.values():
    total += score
print("total:", total)

# Concept-06: zip() pairs up two lists, position by position, so loop them side by side
# Question: How do we line up each name in ["Sam", "Tom", "Ben"] with its score in [70, 95, 60], side by side? (zip pairs two lists and stops at the shorter one)
# E1: the everyday use - two lists of the same length, paired position by position
names = ["Sam", "Tom", "Ben"]
scores = [70, 95, 60]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
# E2: one score short - zip stops at the SHORTER list, so Ben is never reached
names = ["Sam", "Tom", "Ben"]
scores = [70, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
print("Ben never appears - zip stopped when the scores ran out")
