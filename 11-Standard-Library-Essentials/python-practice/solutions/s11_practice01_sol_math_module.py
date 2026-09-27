"""
Practice Problem-01: math module (solution)

Concepts: import, math.sqrt, math.ceil, math.floor, math.pi, statistics.mean, input().
"""
import math
import statistics

"""
Problem-1 (Store Report Numbers): Write a program that, using the math module, prints these labeled lines:
             Task-1: the square root of 169 (use math.sqrt).
             Task-2: the rounded-up box count for 7.2 (use math.ceil).
             Task-3: the rounded-down full-pallet count for 5.8 (use math.floor).
             Task-4: the value of pi (use math.pi).

Expected output:
square root of 169 is: 13.0
rounded-up boxes for 7.2 is: 8
rounded-down full pallets for 5.8 is: 5
pi is about: 3.141592653589793
"""
# Problem-1 Task-1: print square root of 169
print("square root of 169 is:", math.sqrt(169))
# Problem-1 Task-2: print rounded-up boxes for 7.2
print("rounded-up boxes for 7.2 is:", math.ceil(7.2))
# Problem-1 Task-3: print rounded-down pallets for 5.8
print("rounded-down full pallets for 5.8 is:", math.floor(5.8))
# Problem-1 Task-4: print the value of pi
print("pi is about:", math.pi)

"""
Problem-2 (Average Order Total): Write a program that prints a labeled line with the mean (average) of the order totals 120, 80, and 250, using the statistics module (use statistics.mean).

Expected output: average order total: 150
"""
# Problem-2 Task-1: print mean of the order totals
print("average order total:", statistics.mean([120, 80, 250]))

"""
Problem-3 (Write a Program, Order Total Check): Write a program that asks the user for an order total and prints its square root.

Example run:
Enter an order total: 400
square root: 20.0
"""
# Problem-3 Task-1: read order total and print its square root
order_total = int(input("Enter an order total: "))
print("square root:", math.sqrt(order_total))
