"""
Practice Problem-04: parameters and logic (solution)

Concepts: many parameters (positional), if/elif/else inside a function that
          returns a different value per case, a loop inside a function that
          builds up and returns a result.
"""

"""
Problem-1. Many Parameters (Shipping Fee):
  Write a function `shipping_fee` that takes a `weight` and a `rate` and returns their product. Call it with 4 and 3 and print the result, then call it with 10 and 2 and print the result.

Expected output:
12
20
"""
# Problem-1: return weight times rate
def shipping_fee(weight, rate):
    return weight * rate

print(shipping_fee(4, 3))
print(shipping_fee(10, 2))

"""
Problem-2. Logic Inside a Function (Discount Tier):
  Write a function `discount_tier` that takes a `spend` and returns a tier label: "A" for 90 or more, "B" for 75 or more, "C" for 50 or more, otherwise "F". Call it with 95, with 80, and with 40, printing each result.

Expected output:
A
B
F
"""
# Problem-2: return a tier label with if/elif/else
def discount_tier(spend):
    if spend >= 90:
        return "A"
    elif spend >= 75:
        return "B"
    elif spend >= 50:
        return "C"
    else:
        return "F"

print(discount_tier(95))
print(discount_tier(80))
print(discount_tier(40))

"""
Problem-3. Loop Inside a Function (Cart Sum):
  Write a function `cart_sum` that takes a list `line_prices` and returns the total of its items by adding them up in a loop. Call it with [15, 25, 35] and print the result, then call it with [5, 5, 5, 5] and print the result.

Expected output:
75
20
"""
# Problem-3: sum a list with a loop, no sum()
def cart_sum(line_prices):
    running_total = 0
    for price in line_prices:
        running_total = running_total + price
    return running_total

print(cart_sum([15, 25, 35]))
print(cart_sum([5, 5, 5, 5]))

"""
Problem-4. Stop at the First Match (Over Budget):
  Write a function `any_over_budget` that takes a list `prices` and a `limit` and returns True the moment it finds the first price above `limit` (return right there, do not keep checking), otherwise returns False after the loop. Call it with [20, 45, 90] and 50 and print the result, then call it with [20, 30, 40] and 50 and print the result.

Expected output:
True
False
"""
# Problem-4: return True on the first price above the limit, else False
def any_over_budget(prices, limit):
    for price in prices:
        if price > limit:
            return True   # found one, so stop right here
    return False          # only reached after checking every price

print(any_over_budget([20, 45, 90], 50))
print(any_over_budget([20, 30, 40], 50))

"""
Problem-5 (Write a Program). Shipping for Any Order:
  Write a program that asks the user for a weight and a rate (both whole numbers), calls `shipping_fee` with them, and prints "Shipping:" followed by the fee.

Example run:
Weight: 6
Rate: 4
Shipping: 24
"""
# Problem-5: read both numbers, then reuse the same function
weight = int(input("Weight: "))
rate = int(input("Rate: "))
print("Shipping:", shipping_fee(weight, rate))

