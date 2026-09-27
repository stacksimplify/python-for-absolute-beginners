"""
Practice Problem-12: recursion (solution)

Concepts: recursion (a function that calls itself), base case to stop.
"""

"""
Problem-1: Write a recursive function `shelf_countdown` that takes `n`: when `n` is 0 it prints "All shelves stocked!" and stops (the base case), otherwise it prints `n` and counts down from one less. Call it with 3.

Expected output:
3
2
1
All shelves stocked!
"""
# Problem-1: recursive countdown with a base case
def shelf_countdown(n):
    if n == 0:
        print("All shelves stocked!")
        return
    print(n)
    shelf_countdown(n - 1)
shelf_countdown(3)

"""
Problem-2: Write a recursive function `running_product` that takes `n`: when `n` is 1 it returns 1 (the base case), otherwise it returns `n` multiplied by the running product of one less. Call it with 4 and print the result, then call it with 6 and print the result.

Expected output:
24
720
"""
# Problem-2: recursive product with a base case
def running_product(n):
    if n == 1:
        return 1
    return n * running_product(n - 1)
print(running_product(4))
print(running_product(6))
