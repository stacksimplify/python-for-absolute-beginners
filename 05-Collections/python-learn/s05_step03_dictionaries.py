# Concept-01: A dictionary stores values by a KEY instead of a position (curly brackets)
# Question: How do we store Sam's student record {"name": "Sam", "age": 20, "city": "Delhi"} using labels instead of positions?
student = {"name": "Sam", "age": 20, "city": "Delhi"}
print(student)

# Concept-02: look up a value by its key with square brackets
# Question: How do we read one field from Sam's record {"name": "Sam", "age": 20, "city": "Delhi"}, like his name, by its key (student["name"] -> Sam)?
student = {"name": "Sam", "age": 20, "city": "Delhi"}
print(student["name"])  # Sam: the value stored under the key "name"

# Concept-03: .get() is a safe lookup that returns None (or a default) instead of a KeyError
# Question: How do we ask for a key that might be missing, like "email", from {"name": "Sam", "age": 20, "city": "Delhi"} without crashing - .get("email") -> None, or .get("email", "n/a") -> n/a?
student = {"name": "Sam", "age": 20, "city": "Delhi"}
# print(student["email"])  # KeyError: 'email' - a missing key with [] would crash
# Run 1 - .get() with NO default: a missing key returns None (no crash)
print(student.get("email"))         # None: safe, no crash
# Run 2 - .get() WITH a default: a missing key returns your own fallback instead
print(student.get("email", "n/a"))  # n/a: our own default when the key is missing

# Concept-04: add a new pair, or update an existing one, by assigning to a key
# Question: How do we change Sam's age to 21 and add a new "email" field "sam@example.com" to his record {"name": "Sam", "age": 20, "city": "Delhi"}?
student = {"name": "Sam", "age": 20, "city": "Delhi"}
student["age"] = 21                   # update: the key exists, so its value is replaced
student["email"] = "sam@example.com"  # add: the key is new, so a new pair is created
print(student)

# Concept-05: .update() sets several pairs at once from another dictionary
# Question: How do we change many of Sam's fields in one line with student.update({"age": 21, "city": "Mumbai", "email": "sam@example.com"}) instead of one at a time?
student = {"name": "Sam", "age": 20, "city": "Delhi"}
student.update({"age": 21, "city": "Mumbai", "email": "sam@example.com"})
print(student)

# Concept-06: start with an empty dictionary {} and fill it one pair at a time
# Question: How do we build Sam's record from scratch - start with {} then add student["name"] = "Sam" and student["age"] = 20 - when we do not have the values up front?
student = {}              # an empty dictionary
student["name"] = "Sam"   # add the first pair
student["age"] = 20       # add another
print(student)

# Concept-07: len() counts how many key-value pairs a dictionary has
# Question: How many fields does Sam's record {"name": "Sam", "age": 20, "city": "Delhi"} have? (len(student) -> 3 counts the pairs)
student = {"name": "Sam", "age": 20, "city": "Delhi"}
print(len(student))  # 3: number of key-value pairs

# Concept-08: .keys() and .values() return view objects - wrap them in list() for a clean list
# Question-1: How do we see all of Sam's labels from {"name": "Sam", "age": 20, "city": "Delhi"} with list(student.keys()) -> ['name', 'age', 'city']?
# Question-2: How do we see all of Sam's values with list(student.values()) -> ['Sam', 20, 'Delhi']?
student = {"name": "Sam", "age": 20, "city": "Delhi"}
print(student.keys())          # dict_keys(['name', 'age', 'city']): a special view object, not a plain list
print(student.values())        # dict_values(['Sam', 20, 'Delhi']): a special view object
print(list(student.keys()))    # ['name', 'age', 'city']: list() gives a clean list of the labels
print(list(student.values()))  # ['Sam', 20, 'Delhi']: a clean list of the values

# Concept-09: .items() returns a view of (key, value) tuples - wrap it in list() for a clean list
# Question: How do we get Sam's record {"name": "Sam", "age": 20, "city": "Delhi"} as a list of (label, value) pairs with list(student.items())? (each pair is a tuple, like Step-02)
student = {"name": "Sam", "age": 20, "city": "Delhi"}
print(student.items())        # dict_items([('name', 'Sam'), ('age', 20), ('city', 'Delhi')]): a view object
print(list(student.items()))  # [('name', 'Sam'), ('age', 20), ('city', 'Delhi')]: a clean list of (key, value) tuples

# Concept-10: in / not in test whether a KEY is present (not a value)
# Question: How do we check whether Sam's record {"name": "Sam", "age": 20} has a "name" label or does not have an "email" label before we use it? (key in dict)
student = {"name": "Sam", "age": 20}
print("name" in student)       # True: "name" is a key
print("email" not in student)  # True: "email" is not a key
print(20 in student)           # False: in checks KEYS, not values

# Concept-11: remove a key with del (discard it) or .pop() (remove it AND return its value)
# Question-1: How do we drop Sam's "city" from {"name": "Sam", "age": 20, "city": "Delhi"} with del student["city"]?
# Question-2: How do we remove his "age" while keeping the value we removed with student.pop("age") -> 20?
student = {"name": "Sam", "age": 20, "city": "Delhi"}
print(student)                # {'name': 'Sam', 'age': 20, 'city': 'Delhi'}: the full record to start
del student["city"]           # remove the "city" pair, returns nothing
print(student)                # {'name': 'Sam', 'age': 20}: "city" is gone
old_age = student.pop("age")  # remove the "age" pair AND hand back its value
print(student)                # {'name': 'Sam'}: "age" is gone too
print(old_age)                # 20: the value .pop() returned

# Concept-12: a value can be a LIST - look it up, then index or append into it
# Question-1: If Sam's record is {"name": "Sam", "scores": [90, 85]}, how do we read the first score with student["scores"][0] -> 90?
# Question-2: How do we add a new score 100 with student["scores"].append(100) -> [90, 85, 100]?
student = {"name": "Sam", "scores": [90, 85]}
print(student["scores"][0])    # 90: first score (index into the list value)
student["scores"].append(100)  # the inner list grows in place
print(student["scores"])       # [90, 85, 100]

# Concept-13: a value can be another DICT (a nested record) - read it with a chained lookup
# Question-1: If a student record is {"name": "Sam", "address": {"city": "Delhi", "pin": "110001"}}, how do we read Sam's city from inside it with student["address"]["city"] -> Delhi?
# Question-2: How do we read "pin" with student.get("address").get("pin") -> 110001, or fall back for a missing key with student.get("address").get("flatno", "Not Applicable")?
student = {"name": "Sam", "address": {"city": "Delhi", "pin": "110001"}}
print(student["address"]["city"])  # Delhi: first key gets the inner dict, second key reads from it
print(student.get("address").get("pin"))  # 110001: chained .get() reaches into the inner dict
print(student.get("address").get("flatno", "Not Applicable"))  # Not Applicable: .get() default for a missing inner key

# Concept-14: a list of dictionaries stores many records, like rows in a table
# Question: How do we store Sam, Tom, and Ben as a small table [{"name": "Sam", "age": 21}, {"name": "Tom", "age": 25}, {"name": "Ben", "age": 22}], each with the same labels?
people = [
    {"name": "Sam", "age": 21},
    {"name": "Tom", "age": 25},
    {"name": "Ben", "age": 22},
]
print(people[0]["name"])  # Sam: first record, its name
print(people[1]["age"])   # 25: second record, its age
