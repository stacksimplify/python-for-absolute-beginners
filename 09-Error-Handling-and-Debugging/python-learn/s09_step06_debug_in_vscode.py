# Running example: the SAME calculate_books_per_student, now walked one line at a time.
# Concept-01: a call chain gives Step Into and Step Out something to do
# Question: how do you follow a value INTO the function that made it? (put a breakpoint on the call, then Step Into instead of Step Over)
def to_number(text):
    """Turn a piece of text into a whole number."""
    return int(text)

def calculate_books_per_student(total_books, total_students):
    books = to_number(total_books)
    students = to_number(total_students)
    return books / students

# Put your breakpoint on the NEXT line, then try Step Over and Step Into on it.
each = calculate_books_per_student("100", "20")
print("Books each:", each)


# Concept-02: a breakpoint inside a LOOP stops once per pass, so Continue walks the rows
# Question: how do you inspect every row without 20 breakpoints? (one breakpoint in the loop, then press Continue)
def to_number(text):
    """Turn a piece of text into a whole number."""
    return int(text)

def calculate_books_per_student(total_books, total_students):
    books = to_number(total_books)
    students = to_number(total_students)
    return books / students

orders = [("100", "20"), ("240", "12"), ("90", "45")]

for total_books, total_students in orders:
    # Breakpoint here: the debugger stops on this line once for EVERY pair in orders.
    answer = calculate_books_per_student(total_books, total_students)
    print(f"{total_books} books / {total_students} students = {answer}")
