# Running example: debug the SAME calculate_books_per_student when it misbehaves.
# Concept-01: a LOGIC bug gives a wrong answer with NO crash; find it with print debugging
# Question: the result looks wrong but nothing crashed - how do we see the real values? (drop in print(f"{name=}") to inspect them)
def calculate_books_per_student(total_books, total_students):
    books = int(total_books)
    students = int(total_students)
    return books * students          # BUG: should divide, not multiply

print("Buggy result:", calculate_books_per_student("100", "20"))  # 2000, but we expected 5.0

# Add a quick print to SEE the values (f"{name=}" prints the name AND the value):
def calculate_books_per_student(total_books, total_students):
    books = int(total_books)
    students = int(total_students)
    print(f"  debug: {books=} {students=}")
    return books * students

calculate_books_per_student("100", "20")
# books and students are correct, so the bug is the operator: change * to / .

# Fixed:
def calculate_books_per_student(total_books, total_students):
    books = int(total_books)
    students = int(total_students)
    return books / students

print("Fixed result:", calculate_books_per_student("100", "20"))  # 5.0


# Concept-02: a RUNTIME error crashes mid-run; let it crash and READ the traceback
# Question: which line blew up and why? (read bottom-up: the last line is the error, the lines above show where)
def calculate_books_per_student(total_books, total_students):
    books = int(total_books)
    students = int(total_students)
    return books / studphts          # BUG: 'studphts' is a typo -> NameError when this line runs

# We do NOT catch this one. A typo is not a case to handle, it is a bug to FIX, so we let it
# crash on purpose and read what Python prints. The file stops here; nothing after this runs.
print("Books each:", calculate_books_per_student("100", "20"))
# Fix: correct the typo back to 'students' and this line prints "Books each: 5.0".
