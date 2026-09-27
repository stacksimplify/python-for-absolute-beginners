"""
Practice Problem-03: optional values, and hints are not enforced

Concepts: int | None, hints are not enforced at runtime, input().
"""
"""
Problem-1 (An Optional Price Lookup):
  Write a function `lookup_price` that takes a product name and looks it up in a small catalog ("mouse" at 25 and "monitor" at 120), returning the matching price or nothing when the product is missing, with type hints saying it takes a `str` and returns either an `int` or `None`. Call it for "mouse" and for "cable" (not in the catalog) and print each result with a label. Then write a function `triple_units` that takes a quantity (an `int`) and returns it multiplied by 3, with type hints saying it takes an `int` and returns an `int`. Call it with 4 and print the result with the label "triple 4:", then call it with the text "ab" and print the result with the label "triple text:" to show that Python does not enforce the hint at runtime.

Expected output:
mouse: 25
cable: None
triple 4: 12
triple text: ababab
"""
"""
Problem-2 (Write a Program, Look Up a Typed Price):
  Ask the user for a product name and print what `lookup_price` returns for it.

Example run (you type monitor):
Enter a product: monitor
120
"""
