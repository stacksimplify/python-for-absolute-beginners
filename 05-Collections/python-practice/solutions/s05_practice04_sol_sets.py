"""
Practice Problem-04: sets (solution)

Concepts: sets (create, unique, len, sorted(), empty set() vs {}, set(list) dedup,
in / not in, .add(), .update(), .discard(), union | , intersection & , difference - ,
symmetric difference ^ , input()). Every set is printed via sorted() because a set has no order.
"""

"""
Problem-1. Unique Categories:
  Write a program that, for the category list ["audio", "video", "audio", "gaming", "video"]:
    Task-1: build a set from the list, then print how many UNIQUE categories there are.
    Task-2: print the unique categories in sorted order.

Expected output:
3
['audio', 'gaming', 'video']
"""
categories = ["audio", "video", "audio", "gaming", "video"]
# Problem-1 Task-1: build a set and print the unique count
unique = set(categories)
print(len(unique))
# Problem-1 Task-2: print the unique categories sorted
print(sorted(unique))

"""
Problem-2. The Empty-Set Trap:
  Write a program that:
    Task-1: make an empty cart with set() and print its type.
    Task-2: print the type of {} to show it is a dictionary, not a set.

Expected output:
<class 'set'>
<class 'dict'>
"""
# Problem-2 Task-1: make an empty set and print its type
empty_cart = set()
print(type(empty_cart))
# Problem-2 Task-2: print the type of {} to show it is a dict
print(type({}))

"""
Problem-3. Grow and Shrink a Tag Set:
  Write a program that, for the tag set {"audio", "video"}:
    Task-1: add "gaming" with .add(), bulk-add ["mobile", "audio"] with .update(),
    discard "video" and discard "toys" (not present), then print the sorted tags.
    Task-2: print whether "audio" is in the tags, and whether "video" is not in the tags.

Expected output:
['audio', 'gaming', 'mobile']
True
True
"""
tags = {"audio", "video"}
# Problem-3 Task-1: add one tag, then bulk-add more
tags.add("gaming")
tags.update(["mobile", "audio"])
# Problem-3 Task-2: discard two tags, print the sorted tags
tags.discard("video")
tags.discard("toys")
print(sorted(tags))
# Problem-3 Task-3: membership checks with in and not in
print("audio" in tags)
print("video" not in tags)

"""
Problem-4 (Write a Program). Brand Check:
  Write a program that, for the brand set {"sony", "bose", "jbl"}, asks for a brand name
  (typed in ANY capitalization) and prints True if the store carries it, else False.

Example run (you type "Sony"): Enter a brand to check: Sony -> True
"""
# Problem-4: read a brand and print whether the store carries it
brands = {"sony", "bose", "jbl"}
brand = input("Enter a brand to check: ")
print(brand.lower() in brands)

"""
Problem-5. Category Set Math:
  Write a program that, for electronics = {"audio", "video", "gaming"} and clearance = {"video", "gaming", "toys"}:
    Task-1: print the sorted union (categories in either set).
    Task-2: print the sorted intersection (in both).
    Task-3: print the sorted difference (only in electronics).
    Task-4: print the sorted symmetric difference (in exactly one set).

Expected output:
['audio', 'gaming', 'toys', 'video']
['gaming', 'video']
['audio']
['audio', 'toys']
"""
electronics = {"audio", "video", "gaming"}
clearance = {"video", "gaming", "toys"}
# Problem-5 Task-1: print the sorted union
print(sorted(electronics | clearance))
# Problem-5 Task-2: print the sorted intersection
print(sorted(electronics & clearance))
# Problem-5 Task-3: print the sorted difference (only in electronics)
print(sorted(electronics - clearance))
# Problem-5 Task-4: print the sorted symmetric difference
print(sorted(electronics ^ clearance))
