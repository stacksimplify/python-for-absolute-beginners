# Concept-01: a set holds only UNIQUE values in curly brackets, with NO order and NO index; sorted() hands back a list
# Question-1: How do we write Sam's skills as a set {"python", "ml", "data", "ml"}, and what happens to the second "ml"? (a set drops duplicates by itself)
# Question-2: A set has no order, so how do we get the SAME output every run and reach items by position again? (sorted() returns a LIST)
# Question-3: How do we drop the repeats from a real list like ["python", "ml", "ml", "python", "data"]? (set(the_list), then sorted() for an ordered list back)
# E1: build a set - the duplicate disappears, and there is no index to ask for
sam_skills = {"python", "ml", "data", "ml"}  # "ml" is written twice on purpose
print(sam_skills)          # {'ml', 'data', 'python'}: only 3 items - and YOUR order will differ
print(len(sam_skills))     # 3: the second "ml" never made it in
print(type(sam_skills))    # <class 'set'>
# print(sam_skills[0])     # TypeError: 'set' object is not subscriptable - no order means no "first" item

"""
E1 Observations:
1. Run the file two or three times - the order of print(sam_skills) changes every run. That is what "unordered" means.
2. The duplicate "ml" was dropped as the set was built, so len() is 3 and not 4.
3. A set has no index, so sam_skills[0] is an ERROR, not an empty answer.
"""

# E2: sorted() hands back a LIST, so the output is the same every run and positions work again
sam_skills = {"python", "ml", "data", "ml"}
sorted_skills = sorted(sam_skills)  # sorted() reads the set and returns a NEW list, A to Z
print(sorted_skills)        # ['data', 'ml', 'python']: the same order on every run
print(sorted_skills[0])     # data: a list HAS positions
print(sorted_skills[1])     # ml
print(type(sorted_skills))  # <class 'list'>: sorted() gave us a list, not a set

"""
E2 Observations:
1. sorted() does not sort the set - a set cannot hold an order. It returns a NEW list and leaves the set alone.
2. The result is a list, so everything you already know about lists works again, starting with the index.
3. This is why we wrap a set in sorted() whenever the ORDER of the printed line matters.
"""

# E3: the everyday use - drop the repeats from a list, then get an ordered list back
raw_skills = ["python", "ml", "ml", "python", "data"]  # a real list, with repeats
print(raw_skills)           # ['python', 'ml', 'ml', 'python', 'data']
print(len(raw_skills))      # 5: five items, but only three of them are different
unique_skills = set(raw_skills)  # set() drops every duplicate in one call
print(unique_skills)        # {'ml', 'data', 'python'}: the repeats are gone - again, YOUR order will differ
print(len(unique_skills))   # 3: five went in, three came out
sorted_skills = sorted(unique_skills)  # back to a list, in a fixed order
print(sorted_skills)        # ['data', 'ml', 'python']

"""
E3 Observations:
1. set(a_list) is the everyday way to remove duplicates - one call, no loop.
2. A set is often a STEP, not the destination: list -> set() to dedupe -> sorted() for an ordered list back.
"""

# Concept-02: an empty set is set(), NOT {} - because {} is an empty DICTIONARY
# Question: How do we make an EMPTY set, and why can we not use {}? ({} builds a dict, set() builds a set)
empty = set()          # the ONLY way to make an empty set
print(type(empty))     # <class 'set'>
print(type({}))        # <class 'dict'>: curly braces alone make a dict, not a set

# Concept-03: in and not in test membership fast (is a value one of the set's items?)
# Question: How do we check whether Sam (skills {"python", "ml", "data"}) knows 'ml', and does NOT know 'java'? (value in set / value not in set)
sam_skills = {"python", "ml", "data"}
print("ml" in sam_skills)        # True: "ml" is one of Sam's skills
print("java" not in sam_skills)  # True: "java" is not in the set

# Concept-04: .add() grows a set by one value; adding a value already there does nothing
# Question: How does Sam (skills {"python", "ml", "data"}) learn a new skill 'sql', and what happens if we add 'python' again? (a duplicate add is a no-op)
sam_skills = {"python", "ml", "data"}
sam_skills.add("sql")      # add a new skill
sam_skills.add("python")   # already there - nothing happens, no error, no duplicate
print(sorted(sam_skills))  # ['data', 'ml', 'python', 'sql']

# Concept-05: .update() adds many values at once, in place - from another SET or from a LIST
# Question-1: How does Sam (skills {"python", "ml", "data"}) pick up three more skills in one go, when they arrive as a SET?
# Question-2: Does that same .update() still work when the next three arrive as a LIST instead?
sam_skills = {"python", "ml", "data"}
# E1: bulk-add from another SET
sam_skills.update({"go", "java", "javascript"})
# E2: bulk-add from a LIST - same method, different container
sam_skills.update(["terraform", "devops", "reactjs"])
print(sam_skills)          # YOUR order will differ, and changes every run - a set keeps no order (Concept-01)
print(sorted(sam_skills))  # ['data', 'devops', 'go', 'java', 'javascript', 'ml', 'python', 'reactjs', 'terraform']

# Concept-06: .remove() and .discard() both delete a value - the difference is what happens when it is NOT there
# Question-1: How does Sam drop the skill "ml" from {"python", "ml", "data"}, and what happens if we .remove() a skill he never had? (remove() raises KeyError and stops the program)
# Question-2: How do we drop a skill safely when we are not sure it is even there? (discard() quietly does nothing)
# E1: .remove() - deletes the value, but CRASHES if it is not there
sam_skills = {"python", "ml", "data"}
sam_skills.remove("ml")      # "ml" IS there, so it goes
print(sorted(sam_skills))    # ['data', 'python']
# sam_skills.remove("java")  # KeyError: 'java' - UNCOMMENT and run it: remove() crashes on a value that is not there

# E2: .discard() - deletes the value, and stays quiet if it is not there
sam_skills = {"python", "ml", "data"}
sam_skills.discard("ml")     # "ml" IS there, so it goes - exactly like remove()
print(sorted(sam_skills))    # ['data', 'python']
sam_skills.discard("java")   # NOT there - discard() does nothing at all, and does not crash
print(sorted(sam_skills))    # ['data', 'python']: unchanged, and the program is still running

"""
E1 vs E2 Observations:
1. On a value that IS there, remove() and discard() do the same thing - compare the two ['data', 'python'] lines.
2. They only differ on a MISSING value: remove() raises KeyError and stops your program, discard() does nothing.
3. Uncomment the remove("java") line in E1 and run it - that crash is the whole reason discard() exists.
4. Rule of thumb: reach for discard(), unless a missing value SHOULD be treated as an error.
"""

# Concept-07: set math - union | (all), intersection & (shared), difference - (only in the first)
# Question-1: Across Sam's skills {"python", "ml", "data"} and Tom's skills {"python", "java", "sql"}, how do we find everything with sam_skills | tom_skills?
# Question-2: How do we find what they share with sam_skills & tom_skills?
# Question-3: How do we find what only Sam has with sam_skills - tom_skills?
sam_skills = {"python", "ml", "data"}
tom_skills = {"python", "java", "sql"}
print(sorted(sam_skills | tom_skills))  # union: everyone's skills
print(sorted(sam_skills & tom_skills))  # intersection: skills BOTH have
print(sorted(sam_skills - tom_skills))  # difference: skills only Sam has

# Concept-08: symmetric difference ^ - values in exactly ONE set, not in both
# Question: Which skills does exactly one of Sam {"python", "ml", "data"} or Tom {"python", "java", "sql"} have, dropping the shared ones? (sam_skills ^ tom_skills -> ['data', 'java', 'ml', 'sql'])
sam_skills = {"python", "ml", "data"}
tom_skills = {"python", "java", "sql"}
print(sorted(sam_skills ^ tom_skills))  # ['data', 'java', 'ml', 'sql']: python is in both, so it drops out

# Concept-09: a set has no index, so we reach its items by LOOPING over it (a full tour of for loops comes in Section 06)
# Question-1: Why does sam_skills[0] fail on a set? ('set' object is not subscriptable - there is no "first" item to ask for)
# Question-2: So how do we reach every one of Sam's skills, one at a time? (loop over the set with for ... in)
sam_skills = {"python", "ml", "data"}
# E1: WRONG - a set has no positions, so there is nothing at [0]
# print(sam_skills[0])  # TypeError: 'set' object is not subscriptable
# E2: RIGHT - a for loop hands us one item at a time
for skill in sorted(sam_skills):  # sorted() so the order is the same every run - a set has no order of its own
    print(skill)
