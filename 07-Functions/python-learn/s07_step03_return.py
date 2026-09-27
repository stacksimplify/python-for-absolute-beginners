# Concept-01: A print-only function SHOWS a value but hands back None, so you cannot store or reuse it
# Question: We know print shows a value - but can we capture and reuse what a function prints? (no: it hands back None)
def show_sum(a, b):
    print(a + b)

returned = show_sum(2, 3)
print(returned)  # None
print(type(returned))  # <class 'NoneType'>

# Concept-02: return hands the actual value BACK, so you can store it in a variable and reuse it
# Question: How do we get a REAL value back from a function, to store and reuse? (return hands the value back; print could not)
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
print(result * 10)

# Concept-03: return can hand back the answer to a yes/no question (a True/False value)
# Question: How do we make a function ANSWER a yes or no question? (return the comparison; the result is a bool)
def is_even(n):
    return n % 2 == 0

print(is_even(10))
print(is_even(7))
