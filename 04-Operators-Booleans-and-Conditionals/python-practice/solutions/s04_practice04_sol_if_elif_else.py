"""
Practice Problem-04: if / elif / else (solution)

Concepts: if / elif / else, ternary (one-line if / else), % modulo, input().
"""

"""
Problem-1: Shipping by Cart Total
  Write a program that, for a cart_total of 70, prints the shipping cost
  using if / elif / else: 0 when the total is 100 or more, 5 when it is
  50 or more, 10 when it is 20 or more, and 15 otherwise.

Expected output: 5
"""
# Problem-1 Task-1: shipping cost by cart total with if / elif / else
cart_total = 70
if cart_total >= 100:
    shipping = 0
elif cart_total >= 50:
    shipping = 5
elif cart_total >= 20:
    shipping = 10
else:
    shipping = 15
print(shipping)

"""
Problem-2 (Write a Program): Pack in Pairs
  Write a program that asks for a quantity with the prompt
  "Enter a quantity: " and prints "<n> packs in pairs" when the number
  divides evenly by 2 and "<n> has a leftover" otherwise.

Example run:
Enter a quantity: 7
7 has a leftover
"""
# Problem-2 Task-1: pack in pairs, flag a leftover with modulo
quantity = int(input("Enter a quantity: "))
if quantity % 2 == 0:
    print(f"{quantity} packs in pairs")
else:
    print(f"{quantity} has a leftover")

"""
Problem-3 (Write a Program): Free Shipping?
  Write a program that asks for a cart total with the prompt
  "Enter your cart total: " and prints "free shipping" when it is 50 or
  more and "add more" otherwise.

Example run:
Enter your cart total: 20
add more
"""
# Problem-3 Task-1: free shipping when cart total is 50 or more
cart_total_in = int(input("Enter your cart total: "))
if cart_total_in >= 50:
    print("free shipping")
else:
    print("add more")

"""
Problem-4: Order Status
  Write a program that, for is_paid set to True and is_premium set to
  False, prints "Paid" when the order is paid and then, still inside that
  branch, prints "Premium delivery" when the customer is premium and
  "Standard delivery" when not; when not paid, print "Awaiting payment"
  instead.

Expected output:
Paid
Standard delivery
"""
# Problem-4 Task-1: nested order status by paid then premium
is_paid = True
is_premium = False
if is_paid:
    print("Paid")
    if is_premium:
        print("Premium delivery")
    else:
        print("Standard delivery")
else:
    print("Awaiting payment")

"""
Problem-5: Stock Status
  Write a program that, for a units count of 0, sets status to "in stock"
  when units is above 0 and "sold out" otherwise, then prints status. Do
  it two ways: first with a regular if / else, then with the one-line
  if / else (the ternary).

Expected output:
sold out
sold out
"""
# Problem-5 Task-1: stock status two ways, plain if / else then ternary
# Using a regular if / else
units = 0
if units > 0:
    status = "in stock"
else:
    status = "sold out"
print(status)

# Using the ternary (one-line if / else)
units = 0
status = "in stock" if units > 0 else "sold out"
print(status)
