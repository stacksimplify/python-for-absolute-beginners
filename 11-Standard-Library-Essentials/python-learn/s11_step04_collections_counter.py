# The collections module has handy extra container types. Counter is one of the most useful.

# Concept-01: dir() shows what is inside the collections module, the same way it did for math and random
# Question: What does the collections module give us, and is Counter one of them?
import collections

all_names = dir(collections)
collections_tools = [tool for tool in all_names if not tool.startswith("_")]

print("names in collections:", len(all_names))
print("tools you can use:", len(collections_tools))
print(", ".join(collections_tools))

# Concept-02: Counter counts how many times each item appears, in one step
# Question: How do we count how many votes each person got from a list ["Sam", "Tom", "Sam", "Ben", "Sam", "Tom"] where names repeat, in one step?
from collections import Counter
votes = ["Sam", "Tom", "Sam", "Ben", "Sam", "Tom"]
counts = Counter(votes)
print("counts:", counts)

# Concept-03: Ask for one item's count like a dictionary; a missing item returns 0 (no error)
# Question: How do we ask a Counter for one person's votes, like Sam (in the list) or Joe (not in the list), and get 0 instead of an error when the name is missing?
from collections import Counter
votes = ["Sam", "Tom", "Sam", "Ben", "Sam", "Tom"]
counts = Counter(votes)
print("votes for Sam:", counts["Sam"])
print("votes for Joe:", counts["Joe"])

# Concept-04: most_common(n) returns the top n items, highest count first
# Question: How do we find the top 2 vote-getters from votes ["Sam", "Tom", "Sam", "Ben", "Sam", "Tom"] and see their counts sorted from highest to lowest? (most_common(2))
from collections import Counter
votes = ["Sam", "Tom", "Sam", "Ben", "Sam", "Tom"]
counts = Counter(votes)
print("top 2:", counts.most_common(2))

# Concept-05: Counter works on any sequence, even the letters in a word
# Question: How do we count how many times each letter shows up in a word, like 'a' in 'banana'?
from collections import Counter
letter_counts = Counter("banana")
print("letters in banana:", letter_counts)
