"""
Practice Problem-01: arithmetic (solution)

Concepts: + - * /, // floor division, % modulo, ** power.

Problem-1: Two-Number Math.
Write a program that, for two numbers a = 23 and b = 4:
  Task-1: print their sum.
  Task-2: print their product.
  Task-3: print the whole-number part of a divided by b.
  Task-4: print the remainder of a divided by b.
  Task-5: print b raised to the power 2.

Expected output:
27
92
5
3
16
"""

a = 23
b = 4

# Task-1: print their sum
print(a + b)
# Task-2: print their product
print(a * b)

# Task-3: print whole-number part of a // b
print(a // b)
# Task-4: print remainder of a divided by b
print(a % b)

# Task-5: print b raised to power 2
print(b ** 2)

"""
Problem-2: Number Helpers
  Write a program that prints the absolute value of -9, then prints the
  quotient and remainder of 23 divided by 4 together as a pair.

Expected output:
9
(5, 3)
"""
print(abs(-9))
print(divmod(23, 4))

"""
Problem-3: Update In Place
  Write a program that:
    Task-1: start a running total at 50, add 25 to it, then subtract 10
            from it, and print the result.
    Task-2: start a counter at 0, increase it by 1 three times, and print
            the result.

Expected output:
65
3
"""
# Task-1: running total, add 25 then subtract 10
total = 50
total += 25
total -= 10
print(total)

# Task-2: counter from 0, add 1 three times
counter = 0
counter += 1
counter += 1
counter += 1
print(counter)
