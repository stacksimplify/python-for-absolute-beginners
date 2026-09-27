# Concept-01: A list holds many values in order, inside square brackets
# Question: How do we store several names like Sam, Tom, Ben in one place, without a separate variable for each?
names = ["Sam", "Tom", "Ben"]
print(names)
print(len(names))  # 3: how many items

# Concept-02: Access items by position (index), starting at 0
# Question: How do we get a name from a list ["Sam", "Tom", "Ben"] by its position - from the front (0, 1, 2) or from the back (-1, -2, -3)?
names = ["Sam", "Tom", "Ben"]
print(names[0])  # Sam: first
print(names[1])
print(names[2])
print(names[-1])  # Ben: last
print(names[-2])
print(names[-3])

# Concept-03: Lists can be changed (add, replace, remove)
# Question-1: How do we add a new name "Joe" to the end of the list ["Sam", "Tom", "Ben"]?
# Question-2: How do we replace the item at index 1 with "Amy"?
# Question-3: How do we remove the name "Ben" from the list by value?
# Add a name to the end
names = ["Sam", "Tom", "Ben"]
names.append("Joe")
print(names)

# Replace the item at index 1
names[1] = "Amy"
print(names)

# Remove a name by value
names.remove("Ben")
print(names)

# Concept-04: A list of numbers can be sorted in place
# Question: How do we arrange test scores [70, 95, 60, 88] from lowest to highest in one operation?
scores = [70, 95, 60, 88]
scores.sort()
print(scores)  # [60, 70, 88, 95]
scores.sort(reverse=True)
print(scores)  # [95, 88, 70, 60]

# Concept-05: split() turns a STRING into a list, cutting at the separator you give
# Question: How do we break a date string like '2026-06-17' into separate year, month, and day parts?
date_text = "2026-06-17"
date_parts = date_text.split("-")
print(date_parts)     # ['2026', '06', '17']
print(date_parts[0])  # 2026: year
print(date_parts[1])  # 06: month
print(date_parts[2])  # 17: day

# Concept-06: join() turns a LIST of strings back into one string, with a separator between
# Question: How do we join separate words ["Python", "is", "fun"] back into one string, choosing the separator (a space, a hyphen, ...)?
words = ["Python", "is", "fun"]
sentence = " ".join(words)  # join with a space
print(sentence)  # Python is fun
sentence = "-".join(words)  # join with a hyphen
print(sentence)  # Python-is-fun

# Concept-07: insert() puts an item at a position, shifting the rest right
# Question: How do we add a name "Amy" at index 1 in ["Sam", "Tom", "Ben"], not just the end?
names = ["Sam", "Tom", "Ben"]
names.insert(1, "Amy")  # put "Amy" at index 1, shifting the rest right
print(names)  # ['Sam', 'Amy', 'Tom', 'Ben']

# Concept-08: extend() adds each item from another list; append() adds the whole list as ONE item
# Question-1: How do we add several items ["Ben", "Joe"] at once to ["Sam", "Tom"], instead of appending one at a time? (extend)
# Question-2: What do we get if we append() that same list instead? (the whole list lands as one nested item)
# E1: extend() - every item from the other list joins the original list separately
names = ["Sam", "Tom"]
names.extend(["Ben", "Joe"])  # add every item from the other list
print(names)  # ['Sam', 'Tom', 'Ben', 'Joe']

# E2: append() - the entire list goes in as ONE item, creating a nested list
names2 = ["Sam", "Tom"]
names2.append(["Ben", "Joe"])  # add the other list as a single item
print(names2)  # ['Sam', 'Tom', ['Ben', 'Joe']]

# Concept-09: pop() removes an item and hands it back (the last one, or one by position)
# Question: How do we remove an item from ["Sam", "Amy", "Tom", "Ben"] and keep what was removed - the last one, or the one at index 1?
names = ["Sam", "Amy", "Tom", "Ben"]
remove_ben = names.pop()  # pop() removes and returns the LAST item
print(remove_ben)  # Ben
print(names)  # ['Sam', 'Amy', 'Tom']
remove_amy = names.pop(1)  # pop(i) removes and returns the item at index i
print(remove_amy)  # Amy
print(names)  # ['Sam', 'Tom']

# Concept-10: clear() removes every item, leaving an empty list
# Question: How do we empty a list ["Sam", "Tom", "Ben"] completely in one step?
names = ["Sam", "Tom", "Ben"]
names.clear()  # remove everything
print(names)  # []: the list is now empty

# Concept-11: reverse() flips the list order in place
# Question: How do we flip a list ["Sam", "Tom", "Ben"] so the last item comes first?
names = ["Sam", "Tom", "Ben"]
names.reverse()  # flip the order in place
print(names)  # ['Ben', 'Tom', 'Sam']

# Concept-12: index() finds the position where a value sits
# Question: In a name list Sam, Amy, Tom, Ben, how do we find WHICH position 'Tom' sits at? (index() returns its position)
names = ["Sam", "Amy", "Tom", "Ben"]
print(names.index("Tom"))  # 2: the position where "Tom" sits

# Concept-13: count() counts how many times a value appears
# Question: How do we count how many copies of "a" the list ["a", "b", "a", "c", "a"] holds?
letters = ["a", "b", "a", "c", "a"]
print(letters.count("a"))  # 3: how many times "a" appears

# Concept-14: copy() makes a separate list; a plain = does NOT
# Question: How do we make a real copy of a list, so changing one does not change the other?
original = ["Sam", "Tom"]
# Run 1 - plain = (alias): both names point to the SAME list, so the change shows in original
same = original
same.append("Ben")
print(original)  # ['Sam', 'Tom', 'Ben']: changing same changed original too
# Run 2 - .copy() (independent): the copy is its own list, so original is untouched
separate = original.copy()
separate.append("Amy")
print(original)  # ['Sam', 'Tom', 'Ben']: the copy did NOT touch original
print(separate)  # ['Sam', 'Tom', 'Ben', 'Amy']

# Concept-15: A list is a sequence too, so indexing and slicing work just like on strings, including [start:stop:step]
# Question-1: How do we take a slice [1:3] of nums, from index 1 up to but NOT including index 3? (same [start:stop] as strings)
# Question-2: How do we grab the LAST item without knowing how long the list is? (index -1 counts from the back)
# Question-3: How do we take the last four items in one go? (nums[-4:] - a negative start, and no stop means "to the end")
# Question-4: How do we take the first three items? (nums[:3] - no start means "from the beginning")
# Question-5: How do we take every second item? (nums[::2] - the third slot is the step)
# Question-6: How do we reverse the whole list in one line? (nums[::-1] - a step of -1 walks backwards)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(nums[1:3])   # [20, 30]: start at index 1, stop BEFORE index 3
print(nums[-1])    # 100: the last item, counting from the back
print(nums[-4:])   # [70, 80, 90, 100]: from the 4th-from-last to the end
print(nums[:3])    # [10, 20, 30]: from the beginning, up to but not including index 3
print(nums[::2])   # [10, 30, 50, 70, 90]: every 2nd item (the third slot is the step)
print(nums[::-1])  # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]: a step of -1 reverses the list

# Concept-16: in tests membership - is a value in the list?
# Question: How do we check whether "Sam" is in a list ["Sam", "Tom"]?
print("Sam" in ["Sam", "Tom"])  # True: in tests membership

# Concept-17: not in is the mirror of in
# Question: How do we check whether "Zoe" is NOT in a list ["Sam", "Tom"]?
print("Zoe" not in ["Sam", "Tom"])  # True: not in is the mirror

# Concept-18: A list can hold other lists (a nested list); use two indexes to reach inside
# Question: How do we store a grid [[10, 20, 30], [40, 50, 60], [70, 80, 90]], and read one item by row then column (like grid[0][2] -> 30)?
grid = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
print(grid[0])     # [10, 20, 30]: the whole first row (an inner list)
print(grid[0][2])  # 30: row 0, then the item at index 2
print(grid[2][1])  # 80: row 2, then the item at index 1

# Concept-19: Nested lists work with strings too (here, a list of veggies and a list of fruits)
# Question: How do we keep two groups [["carrot", "onion", "potato"], ["apple", "banana", "mango"]] in one list, and pick a single item (like [1][2] -> mango)?
groceries = [["carrot", "onion", "potato"], ["apple", "banana", "mango"]]
print(groceries[0])     # ['carrot', 'onion', 'potato']: the veggies list
print(groceries[1][2])  # mango: list 1 (fruits), item at index 2
print(groceries[0][1])  # onion: list 0 (veggies), item at index 1
