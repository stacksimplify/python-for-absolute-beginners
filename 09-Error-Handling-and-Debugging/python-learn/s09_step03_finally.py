# Running example: the SAME calculate_books_per_student, now with cleanup that always runs.
# Concept-01: finally always runs, whether the try worked or failed (even after a return)
# Question: How do we always print a "finished" note no matter how the call ended? (put it in a finally block)
def calculate_books_per_student(total_books, total_students):
    try:
        books = int(total_books)
        students = int(total_students)
        return books / students
    except (ValueError, ZeroDivisionError):
        return "Please enter valid numbers (students above zero)."
    finally:
        # Runs in BOTH cases above, even after a return.
        print("Finished sharing the books.")

print("Good call:")
print(calculate_books_per_student("100", "20"))
print("Bad call:")
print(calculate_books_per_student("100", "0"))
