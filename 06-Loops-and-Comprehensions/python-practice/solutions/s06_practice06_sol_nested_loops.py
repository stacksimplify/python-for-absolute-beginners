"""
Practice Problem-06: nested loops (solution)

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
# Problem-1 Task-1: print every product-and-wrap option with nested loops
gift_products = ["Mug", "Frame"]
wraps = ["Plain", "Floral", "Holiday"]
for gift_product in gift_products:
    for wrap in wraps:
        print(f"{gift_product} in {wrap} wrap")

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
# Problem-2 Task-1: break stops only the INNER bin loop; the outer aisle loop keeps going
for aisle in ["A1", "A2"]:
    for bin_no in range(1, 5):
        if bin_no == 3:
            print(f"{aisle} first full bin: {bin_no}")
            break
        print(f"{aisle} bin {bin_no} empty")

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
# Problem-3 Task-1: nested range x range builds a pricing grid
for units in range(1, 4):
    for packs in range(1, 3):
        print(f"{units} x {packs} = {units * packs}")

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
# Problem-4 Task-1: continue skips only the reserved inner bin; the outer loop keeps going
for aisle in ["A1", "A2"]:
    for bin_no in range(1, 4):
        if bin_no == 2:
            continue
        print(f"{aisle} bin {bin_no}")

"""
Problem-5. A list of lists:
  Define a variable day_orders as a list of lists with the values [2, 3] and
  [1, 4, 2]. Write a program that prints the total for each day, then the grand
  total across all days.

Expected output:
day total: 5
day total: 7
grand total: 12
"""
# Problem-5 Task-1: an inner loop totals one day; the reset must sit INSIDE the outer loop
day_orders = [[2, 3], [1, 4, 2]]
grand_total = 0
for day in day_orders:
    day_total = 0          # reset for EVERY day: move this above the outer loop and the totals pile up
    for orders in day:
        day_total += orders
    print("day total:", day_total)
    grand_total += day_total
print("grand total:", grand_total)
