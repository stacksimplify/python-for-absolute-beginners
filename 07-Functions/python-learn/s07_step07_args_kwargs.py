# Concept-01: *args collects any number of positional values into a tuple
# Question: How do we accept an UNLIMITED number of values, like adding up 1, 2, 3 or 10, 20, 30, 40? (*args gathers them into a tuple)
# E1: THE PROBLEM - a fixed parameter list locks the count in the moment you write it
def total(a, b, c):
    return a + b + c

print(total(1, 2, 3))
# print(total(10, 20, 30, 40))  # uncomment: TypeError, takes 3 positional arguments but 4 were given

# E2: THE FIX - one star takes however many values the caller happens to have
def total(*nums):  # the name is yours: *args is the convention, *nums is fine too
    return sum(nums)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))

# Concept-02: **kwargs collects any number of named values into a dictionary
# Question: How do we let each caller choose WHICH options to pass - gift wrap, a note, both, neither? (**kwargs gathers them into a dict)
# E1: THE PROBLEM - a fixed option list locks in which options exist, and their order
def make_order(item, gift_wrap, note):
    print("options:", gift_wrap, note)

make_order("pen", True, "Thanks")
# make_order("pen", True)  # uncomment: TypeError, missing 1 required positional argument: 'note'

# E2: THE FIX - two stars take whatever named options the caller has
def make_order(item, **options):  # the name is yours: **kwargs is the convention, **options is fine too
    print("options:", options)

make_order("pen", gift_wrap=True, note="Thanks")
make_order("pen", gift_wrap=True)

# Concept-03: Call-site unpacking. Spread a list with * and a dict with ** straight into a call
# Question-1: How do we feed a list we already have, like [5, 10, 15], into a function's arguments? (unpack with * before the list)
# Question-2: How do we feed a dict we already have, like {"gift_wrap": True, "note": "Thanks"}, into a function's arguments? (unpack with ** before the dict)
# Same *args function as Concept-01, repeated so this block stands on its own
def total(*nums):
    return sum(nums)

scores = [5, 10, 15]
print(total(*scores))  # * spreads the list into total(5, 10, 15)

# Same **kwargs function as Concept-02, repeated so this block stands on its own
def make_order(item, **options):
    print("options:", options)

extras = {"gift_wrap": True, "note": "Thanks"}
make_order("pen", **extras)  # ** spreads the dict into make_order("pen", gift_wrap=True, note="Thanks")

# Concept-04: Keyword-only arguments. A bare * forces the arguments after it to be passed by name
# Question: How do we MAKE callers pass an argument by name, for clarity? (put a bare * before it: def f(*, flag))
def make_box(*, width, height):
    return width * height

print(make_box(width=3, height=4))
# print(make_box(3, 4))  # uncomment: TypeError, make_box() takes 0 positional arguments but 2 were given

# Concept-05: One function can take BOTH; *args (a tuple) must come BEFORE **kwargs (a dict)
# Question: How does a function accept any positionals AND any named options at once, like a logging call? (*args first, then **kwargs)
# The same make_order as Concept-02, grown up: any number of ITEMS as well as any number of options
def make_order(*items, **options):
    print("items:", items)
    print("options:", options)

make_order("pen", "book", gift_wrap=True, note="Thanks")
# This would be a SyntaxError - a keyword argument cannot come before a positional one:
# make_order(gift_wrap=True, "pen")
