"""
Practice Problem-06: nested loops

Concepts: nested loops, looping a list, nested range(), break and continue inside nesting, f-strings.
"""
"""
Problem-1 (Gift-Wrap Menu):
  Write a program that, for the products Mug, Frame and the wraps Plain, Floral,
  Holiday, uses a loop inside a loop to print every product-and-wrap option, one
  per line, like Mug in Plain wrap.

Expected output:
Mug in Plain wrap
Mug in Floral wrap
Mug in Holiday wrap
Frame in Plain wrap
Frame in Floral wrap
Frame in Holiday wrap
"""
"""
Problem-2 (First Full Bin per Aisle):
  Write a program that, for the aisles A1, A2 and bins 1 to 4, scans each aisle's
  bins in order and prints <aisle> bin <n> empty until it reaches bin 3 (the first
  full bin), where it prints <aisle> first full bin: 3 and uses break. break stops
  only the inner bin loop, so the outer aisle loop still moves on to the next aisle.

Expected output:
A1 bin 1 empty
A1 bin 2 empty
A1 first full bin: 3
A2 bin 1 empty
A2 bin 2 empty
A2 first full bin: 3
"""
"""
Problem-3 (Bulk Pricing Grid):
  Write a program that uses a nested range() loop to print a small pricing grid:
  for each unit count 1 to 3 and each pack size 1 to 2, print units x packs = total,
  like 1 x 1 = 1.

Expected output:
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4
3 x 1 = 3
3 x 2 = 6
"""
"""
Problem-4 (Skip the Reserved Bin):
  Write a program that, for the aisles A1, A2 and the bins 1, 2, 3, prints every
  aisle-and-bin like A1 bin 1, but uses continue to skip bin 2 (reserved) on every
  aisle. The outer aisle loop still visits every aisle.

Expected output:
A1 bin 1
A1 bin 3
A2 bin 1
A2 bin 3
"""

"""
Problem-5. A list of lists:

Define a variable day_orders as a list of lists with the values: [2, 3] and [1, 4, 2].
Write a program that prints the total for each day, then the grand total for all days.

Expected output:
day total: 5
day total: 7
grand total: 12
"""
