# Concept-01: a tuple groups values that belong together and must not change; round brackets
# Question: How do we store Sam's fixed record ("Sam", 25) - name and age - as one value?
player = ("Sam", 25)
print(player)       # ('Sam', 25)
print(player[0])    # Sam: first item, by index (starts at 0)
print(player[-1])   # 25: last item, negative index counts from the end
print(len(player))  # 2: how many items

# Concept-02: a tuple is IMMUTABLE - trying to change it is an error (that is why we use one)
# Question: A list lets you change an item - what happens if we try the same on a tuple? (a tuple cannot be changed)
# Run 1 - a LIST is mutable: changing an item works
player_list = ["Sam", 25]
player_list[0] = "Tom"
print(player_list)  # ['Tom', 25]: the list changed
# Run 2 - a TUPLE is immutable: the same change is an error, so the tuple stays safe
player = ("Sam", 25)
# player[0] = "Tom"  # TypeError: 'tuple' object does not support item assignment
print(player)  # ('Sam', 25): unchanged, safe from accidental edits

# Concept-03: the only two tuple methods - count() how many times a value appears, index() where it is
# Question-1: In Sam's game scores (10, 20, 30, 40, 50, 60, 70, 80, 20), how many times did he score 20?
# Question-2: In Sam's game scores (10, 20, 30, 40, 50, 60, 70, 80, 20), where is the first 20?
scores = (10, 20, 30, 40, 50, 60, 70, 80, 20)
print(scores.count(20))  # 2: how many times 20 appears (it is at index 1 and index 8)
print(scores.index(20))  # 1: the position of the FIRST 20

# Concept-04: slicing a tuple gives a tuple, and [start:stop:step] works just like on lists and strings
# Question-1: How do we take plain [start:stop] slices of Sam's scores (10, 20, 30, 40, 50, 60, 70, 80, 20)? (start is included, stop is not)
# Question-2: Does the third slot work on a tuple too - every second score, and the whole tuple reversed? (scores[::2] steps by 2, scores[::-1] reverses)
# Question-3: Why does scores[-1:] give a tuple but scores[-1] a plain number? (a slice ALWAYS returns a tuple; an index returns the item)
scores = (10, 20, 30, 40, 50, 60, 70, 80, 20)

# [start:stop] - start is included, stop is not
print(scores[0:3])   # (10, 20, 30): items at index 0, 1, 2 (stop 3 is not included)
print(scores[1:3])   # (20, 30): items at index 1 and 2
print(scores[1:])    # (20, 30, 40, 50, 60, 70, 80, 20): from index 1 to the end

# [start:stop:step] - the third slot is how far to jump
print(scores[::2])   # (10, 30, 50, 70, 20): every second item, starting from the beginning
print(scores[1::2])  # (20, 40, 60, 80): every second item, starting at index 1
print(scores[::-1])  # (20, 80, 70, 60, 50, 40, 30, 20, 10): a step of -1 reverses the tuple

# a slice gives a TUPLE; a single index gives the ITEM
print(scores[-1:])   # (20,): a slice ALWAYS gives a tuple - here a one-item tuple
print(scores[-1])    # 20: a single index gives the item itself, not a tuple

# Concept-05: in tests membership on a tuple, and not in is its mirror (both read-only)
# Question: How do we check whether a score is in Sam's scores (10, 20, 30, 40, 50, 60, 70, 80, 20), or not in them (like 20 in, 99 not in)?
scores = (10, 20, 30, 40, 50, 60, 70, 80, 20)
print(20 in scores)      # True: 20 is in the tuple
print(99 not in scores)  # True: 99 is not in the tuple
print(100 in scores)     # False: 100 is not in the tuple
print(50 not in scores)  # False: 50 IS in the tuple, so not in is False

# Concept-06: the COMMAS make a tuple (brackets optional); a one-item tuple NEEDS a trailing comma
# Question-1: How do we build Sam's record "Sam", 25 without brackets (the commas make the tuple)?
# Question-2: How do we write a one-item tuple like (90,) correctly (the trailing comma is required)?
player = "Sam", 25        # commas make the tuple, even with no brackets
print(player)             # ('Sam', 25)
one_score = (90,)         # a 1-item tuple - the comma is required
not_a_tuple = (90)        # no comma, so this is just the int 90, not a tuple
print(type(one_score).__name__, type(not_a_tuple).__name__)  # tuple int

# Concept-07: unpacking gives each item its own name in one line (counts must match)
# Question-1: How do we split Sam's full record "Sam", 25, "Delhi" into three variables name, age, city?
# Question-2: How do we check the types of the unpacked name and age (type(name), type(age))?
player = "Sam", 25, "Delhi"
name, age, city = player   # one name per item, left-to-right by position
print(name, "is", age, "from", city)  # Sam is 25 from Delhi
print(type(name), type(age))          # <class 'str'> <class 'int'>

# Concept-08: swap two variables in one line, then save the result as a NEW tuple (the old one cannot change)
# Question-1: How do we swap two variables a, b (from pair (10, 20)) in one line with a, b = b, a?
# Question-2: Since a tuple cannot change, how do we keep the swapped result as a NEW tuple new_pair = (a, b) -> (20, 10)?
pair = (10, 20)
a, b = pair          # unpack the pair tuple into two variables
print(a, b)          # 10 20
a, b = b, a          # swap in one line: pack (b, a) into a tuple, then unpack it back into a, b
print(a, b)          # 20 10
new_pair = (a, b)    # save the swapped values as a NEW tuple (we cannot edit the old one)
print(new_pair)      # (20, 10)
print(pair)          # (10, 20): the original tuple is unchanged

# Concept-09: a tuple's slots are fixed (you cannot replace one), but a LIST inside a slot can still change
# Question: If Sam's record is a fixed tuple, how can the scores list inside still change (append, clear, rebuild)? And why does replacing the whole slot still fail?
player = ("Sam", [90, 85])    # a tuple: a name and a LIST of scores
print(player)                 # ('Sam', [90, 85])
player[1].append(100)         # the list is mutable, so it can grow
print(player)                 # ('Sam', [90, 85, 100]): the list changed, the tuple did not
# player[1] = [10, 20]        # TypeError: cannot REPLACE a tuple slot, only change what is inside
player[1].clear()             # empty the list (any list method from Step-01 works)
print(player)                 # ('Sam', [])
player[1].append(10)
player[1].append(20)          # rebuild it - append, clear, sort ... all work on the inner list
print(player)                 # ('Sam', [10, 20])
