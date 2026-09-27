# Concept-01: range(n) gives the numbers 0 up to n-1, so it repeats an action n times
# Question: How do we repeat an action 5 times, counting 0 to 4? (range(n) runs n times, counting 0..n-1)
for i in range(5):
    print(i)

# Concept-02: range(start, stop) starts where you say and stops BEFORE the stop value
# Question: How do we count from 2 up to 5, leaving out the stop value 6? (range(start, stop) leaves the stop out)
for n in range(2, 6):
    print(n)

# Concept-03: range(start, stop, step) jumps by the step you give
# Question: How do we list only the even numbers from 0 to 10? (a step of 2 skips the odd ones)
for n in range(0, 11, 2):
    print(n)

# Concept-04: A negative step counts DOWN instead of up
# Question: How do we count down 5, 4, 3, 2, 1 without a while loop? (a step of -1 walks backward)
for i in range(5, 0, -1):
    print(i)
print("Done")

# Concept-05: Pair range with an accumulator to add up a run of numbers
# Question: How do we add up the numbers 1 to 10 into one total? (add each number into one total)
total = 0
for n in range(1, 11):
    total += n
print("total:", total)   # 55

# Concept-06: range is lazy, so wrap it in list() to see the numbers it will produce
# Question: How do we see the exact numbers range(1, 6) will produce? (printing the range shows range(1, 6); list() shows the numbers)
# E1: printing the range itself just shows range(1, 6) - it has not built the numbers yet (lazy)
print(range(1, 6))
# E2: list() forces it to produce the numbers, so now you can see them
nums = list(range(1, 6))
print(nums)
