# Running example: the SAME calculate_books_per_student, now catching the exact errors.
# Concept-01: catch the SPECIFIC error you expect; give each kind its own except block
# Question-1: How do we reply to bad text input like "abc" with its own message? (catch it in an except ValueError block)
# Question-2: How do we reply to zero students like "0" with its own message? (catch it in an except ZeroDivisionError block)
def calculate_books_per_student(total_books, total_students):
    try:
        books = int(total_books)
        students = int(total_students)
        return books / students
    except ValueError:
        return "Books and students must be whole numbers."
    except ZeroDivisionError:
        return "There must be at least one student."

print(calculate_books_per_student("100", "20"))
print(calculate_books_per_student("abc", "20"))
print(calculate_books_per_student("100", "0"))

# Concept-02: else runs only when the try block had no error
# Question: How do we run a success-only step when the numbers were valid? (put that step in an else block)
def calculate_books_per_student(total_books, total_students):
    try:
        books = int(total_books)
        students = int(total_students)
        result = books / students
    except ValueError:
        return "Books and students must be whole numbers."
    except ZeroDivisionError:
        return "There must be at least one student."
    else:
        print("Input looked good, sharing the books.")
        return result

print(calculate_books_per_student("100", "20"))
print(calculate_books_per_student("abc", "20"))

# Concept-03: when two errors deserve the SAME message, catch them together with except (A, B)
# Question: How do we give both bad-number errors one shared reply? (list both types in a tuple: except (ValueError, ZeroDivisionError))
def calculate_books_per_student(total_books, total_students):
    try:
        books = int(total_books)
        students = int(total_students)
        return books / students
    except (ValueError, ZeroDivisionError):
        return "Please enter valid numbers (students above zero)."

print(calculate_books_per_student("abc", "20"))
print(calculate_books_per_student("100", "0"))
