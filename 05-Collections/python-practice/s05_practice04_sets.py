"""
Practice Problem-04: sets

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

"""
Problem-2. The Empty-Set Trap:
  Write a program that:
    Task-1: make an empty cart with set() and print its type.
    Task-2: print the type of {} to show it is a dictionary, not a set.

Expected output:
<class 'set'>
<class 'dict'>
"""

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

"""
Problem-4 (Write a Program). Brand Check:
  Write a program that, for the brand set {"sony", "bose", "jbl"}, asks for a brand name
  (typed in ANY capitalization) and prints True if the store carries it, else False.

Example run (you type "Sony"): Enter a brand to check: Sony -> True
"""

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
