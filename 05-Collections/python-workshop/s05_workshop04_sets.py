"""
Workshop Problem-04: sets (Car Brands and Features)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

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
