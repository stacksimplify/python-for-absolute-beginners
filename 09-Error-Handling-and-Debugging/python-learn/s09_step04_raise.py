# Running example: the SAME calculate_books_per_student, now rejecting impossible input.
# Concept-01: raise lets YOU signal an error on purpose when a business rule is broken
# Question-1: How do we reject negative books (books < 0)? (raise a ValueError with the message "Total books cannot be negative")
# Question-2: How do we reject zero or fewer students (students <= 0)? (raise a ValueError with the message "There must be at least one student")
def calculate_books_per_student(total_books, total_students):
    books = int(total_books)
    students = int(total_students)
    if books < 0:
        raise ValueError("Total books cannot be negative")
    if students <= 0:
        raise ValueError("There must be at least one student")
    result = books / students
    return result

# Good input returns normally.
print(calculate_books_per_student("100", "20"))

# Concept-02: catch a raised error where you call it; "as err" gives you the message
# Question: How do we catch the ValueError our function raised and read its message? (wrap the call in try/except ValueError as err, then print err)
# Same calculate_books_per_student as Concept-01, repeated so this block stands on its own
# Define function
def calculate_books_per_student(total_books, total_students):
    books = int(total_books)
    students = int(total_students)
    if books < 0:
        raise ValueError("Total books cannot be negative")
    if students <= 0:
        raise ValueError("There must be at least one student")
    result = books / students
    return result

# Call the function. Uncomment one line at a time to see each rule fire.
try:
    # print("P1 Result:", calculate_books_per_student("100", "50"))
    # print("N1 Result:", calculate_books_per_student("100", "0"))
    # print("N2 Result:", calculate_books_per_student("-100", "20"))
    print("N3 Result:", calculate_books_per_student("100", "-20"))
except ValueError as err:
    print("Caught a problem:", err)

print("CONTINUE PROGRAM - The program kept running")
