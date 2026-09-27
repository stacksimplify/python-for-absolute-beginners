# Concept-01: A function can take MORE THAN ONE parameter; values fill them by position
# Question: How do we calculate the area of a rectangle by passing both its width (4) and height (3) to a function? (list both parameters; pass the values in order)
def area(width, height):
    return width * height

print(area(4, 3))

# Concept-02: Put logic INSIDE a function (if / elif / else) and return a different value per case
# Question: How do we turn a student's marks into a grade inside a function, like 72 or 95? (if/elif/else, then return the grade)
def get_student_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

print(get_student_grade(72))
print(get_student_grade(95))

# Concept-03: A function can run a LOOP and return a built-up result
# Question: How do we add up a whole list of numbers, like [10, 20, 30], and return the total? (loop over them, keep a running total, return it)
def total(numbers):
    if not numbers:  # guard: no numbers, so there is no total - hand back None
        return None
    running_total = 0
    for number in numbers:
        running_total = running_total + number
    return running_total

print(total([10, 20, 30]))  # 60
print(total([]))  # None (empty list - the guard returned early)

# Concept-04: return inside a loop stops the function immediately.
# The "not found" return belongs AFTER the loop, not inside it.

# Question: How do we check whether a list contains ANY even number?
# Stop as soon as we find one.

# E1: Common mistake - returning False too early
def has_even_buggy(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
        else:
            return False  # WRONG: decides after the first item instead of checking them all

print(has_even_buggy([1, 3, 4]))  # False - WRONG: 4 is even, but the function stopped at 1
print(has_even_buggy([1, 3, 5]))  # False - Correct by luck (there is no even number)

# E2: Correct - return True when found, otherwise return False after the loop
def has_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True  # Found an even number - stop the loop and the function
    return False  # Reached only if no even number was found

print(has_even([1, 3, 4]))  # True  - Correct: it kept checking until it found 4
print(has_even([1, 3, 5]))  # False - Correct: every number was checked
