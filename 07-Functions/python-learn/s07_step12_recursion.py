# Concept-01: Recursion. A function that calls ITSELF, with a base case to stop
# Question: How can a function repeat by calling itself, like counting down to zero? (call itself with a smaller value; STOP at the base case)
def countdown(n):
    if n == 0:  # base case, stop here
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)  # recursive call, with a smaller n

countdown(3)
# WARNING - no base case means it never stops. Python stops it with a
# RecursionError after about 1000 calls (its recursion limit). Never run this:
# def forever(n):
#     print(n)
#     forever(n - 1)   # nothing stops it -> RecursionError

# Concept-02: The classic example, factorial (n! = n * (n-1) * ... * 1)
# Question: How do we compute a factorial with recursion? (n! = n * factorial(n-1), and factorial(1) is 1)
def factorial(n):
    if n == 1:  # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))
# factorial(5) -> 5 * factorial(4) -> 5 * 4 * factorial(3) -> ... -> 5 * 4 * 3 * 2 * 1 = 120
# The base case here is n == 1, so this factorial expects n >= 1

# Note: most everyday repeating is done with loops (Section 6). Recursion is a tool for
# a few problems. This is a BONUS so you recognize it when you meet it later.
