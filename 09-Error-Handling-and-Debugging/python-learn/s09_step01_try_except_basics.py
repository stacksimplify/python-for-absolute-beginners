# Running example: ONE function, calculate_books_per_student, grows safer step by step.
# Concept-01: without handling, bad input crashes the function and stops everything after it
# Question: How do we keep one bad value from crashing the whole program? (put the risky lines in a try block)
def calculate_books_per_student(total_books, total_students):
    books = int(total_books)
    students = int(total_students)
    return books / students

# A good call works fine.
print("Books each:", calculate_books_per_student("100", "20"))
# But calculate_books_per_student("abc", "20") would crash with a ValueError,
# and calculate_books_per_student("100", "0") would crash with a ZeroDivisionError.

# Concept-02: try / except - put the risky code in a try block; if it fails, except runs and the program keeps going
# Question: How do we reply with a friendly message instead of crashing on bad input? (wrap the risky lines in try, handle the problem in except)
def calculate_books_per_student(total_books, total_students):
    try:
        books = int(total_books)
        students = int(total_students)
        return books / students
    except Exception:
        return "Something went wrong with the input."

print("Good call:", calculate_books_per_student("100", "20"))
print("Bad text:", calculate_books_per_student("abc", "20"))
print("Zero students:", calculate_books_per_student("100", "0"))
print("The program kept running.")
