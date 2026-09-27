# Concept-01: A while loop repeats while its condition is True; change the variable inside or it runs forever
# Question: How do we count from 1 to 5 with a loop, and make sure it actually stops? (the block must change the variable the condition tests)
count = 1
while count <= 5:      # keep going while count is 5 or less
    print(count)
    count += 1         # += 1 moves count forward; WITHOUT this line the loop never stops
# This block would run FOREVER because count never changes - never uncomment it:
# count = 1
# while count <= 5:
#     print(count)

# Concept-02: A while loop can run UNTIL a condition becomes false, even with no fixed count
# Question: How do we keep doubling the number 1 while it stays 100 or less? (no fixed count - it stops before printing anything above 100)
value = 1
while value <= 100:    # keep going while value is 100 or less
    print(value)
    value = value * 2  # reassign value to twice its size

# Concept-03: Count DOWN by subtracting from the variable each turn with -=
# Question: How do we count down from 5 to 1, and then print "Done"? (-= 1 walks the variable back toward the stop)
n = 5
while n >= 1:          # keep going while n is 1 or more
    print(n)
    n -= 1             # -= 1 moves n backward toward the stop
print("Done")          # runs once, after the loop finishes

# Concept-04: Keep a running total (an accumulator) by adding into one variable each turn
# Question: How do we add up the numbers 1 to 5 into one total? (start a total at 0 and add each number in - the accumulator pattern)
total = 0
i = 1
while i <= 5:
    total += i         # add this number into the running total
    i += 1
print("total:", total)  # 15

# Concept-05: Walk a list one position at a time with while i < len(list) (fiddly - for is cleaner)
# Question: How do we go through the list [70, 95, 60, 88] by its index positions, 0 to the last? (while i < len(scores) stops right after the last item)
scores = [70, 95, 60, 88]
i = 0
while i < len(scores):  # stop when i reaches the length (no item at that index)
    print(scores[i])    # scores[i] is the item at position i
    i += 1

# Concept-06: A while test can be ANY truthy value, not only a number comparison (a non-empty list is truthy)
# Question: How do we keep taking items from the list ["Sam", "Tom", "Ben"] until it is empty? (a non-empty list is truthy)
names = ["Sam", "Tom", "Ben"]
while names:            # loops while the list is non-empty (an empty list is "falsy")
    print(names.pop())  # pop() removes AND returns the last item, so the list shrinks each turn
