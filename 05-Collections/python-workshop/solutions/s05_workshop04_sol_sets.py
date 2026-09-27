"""
Workshop Problem-04: sets (Car Brands and Features) (solution)

Concepts: sets (unique, len, sorted(), empty set() vs {}, set(list) dedup, in / not in,
.add(), .update(), .discard(), union | , intersection & , difference - , symmetric difference ^).
Every set is printed via sorted() because a set has no order.

Problem-1. Unique Brands:
  Write a program that, for the brand list ["Audi", "BMW", "Audi", "Kia", "BMW"]:
    Task-1: build a set from the list and print how many UNIQUE brands there are.
    Task-2: print the unique brands in sorted order.
    Task-3: print the type of set() to show an empty set is set(), not {} (which is a dict).

Expected:
3
['Audi', 'BMW', 'Kia']
<class 'set'>
"""
brands = ["Audi", "BMW", "Audi", "Kia", "BMW"]
# Problem-1 Task-1: build a set and print the unique count
unique = set(brands)
print(len(unique))
# Problem-1 Task-2: print the unique brands sorted
print(sorted(unique))
# Problem-1 Task-3: print the type of set() to show an empty set
print(type(set()))

"""
Problem-2. Service Tags:
  Write a program that, for the tag set {"oil", "tires"}:
    Task-1: add "brakes" with .add(), bulk-add ["filter", "oil"] with .update(),
    discard "tires" and discard "paint" (not present), then print the sorted tags.
    Task-2: print whether "oil" is in the tags, and whether "tires" is not in the tags.

Expected:
['brakes', 'filter', 'oil']
True
True
"""
tags = {"oil", "tires"}
# Problem-2 Task-1: add one tag, then bulk-add more
tags.add("brakes")
tags.update(["filter", "oil"])
# Problem-2 Task-2: discard two tags, print the sorted tags
tags.discard("tires")
tags.discard("paint")
print(sorted(tags))
# Problem-2 Task-3: membership checks with in and not in
print("oil" in tags)
print("tires" not in tags)

"""
Problem-3. Feature Sets:
  Write a program that, for petrol = {"ac", "abs", "airbag"} and diesel = {"abs", "airbag", "sunroof"}:
    Task-1: print the sorted union (features in either car).
    Task-2: print the sorted intersection (in both).
    Task-3: print the sorted difference (only in petrol).
    Task-4: print the sorted symmetric difference (in exactly one).

Expected:
['abs', 'ac', 'airbag', 'sunroof']
['abs', 'airbag']
['ac']
['ac', 'sunroof']
"""
petrol = {"ac", "abs", "airbag"}
diesel = {"abs", "airbag", "sunroof"}
# Problem-3 Task-1: print the sorted union
print(sorted(petrol | diesel))
# Problem-3 Task-2: print the sorted intersection
print(sorted(petrol & diesel))
# Problem-3 Task-3: print the sorted difference (only in petrol)
print(sorted(petrol - diesel))
# Problem-3 Task-4: print the sorted symmetric difference
print(sorted(petrol ^ diesel))
