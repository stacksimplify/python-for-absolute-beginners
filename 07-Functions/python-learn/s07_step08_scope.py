# Concept-01: LOCAL scope. A variable assigned inside a function lives only there
# Question: Where does a variable made inside a function live? (in the function's LOCAL scope; it is gone when the function ends)
def show_course():
    course = "Python"  # LOCAL: born here, gone the moment the function ends
    print("Course:", course)

show_course()

# Concept-02: GLOBAL scope. A name at the top level of the file; a function can READ it
# Question: How can every function in a file share one value, like the platform name, without passing it each time? (define it at the top level; functions can READ that global)
platform = "StackSimplify"  # GLOBAL: top level of the file, so every function can read it

def show_platform():
    print("Platform:", platform)  # reads the global 'platform'

show_platform()

# Concept-03: ENCLOSING scope. A function INSIDE another function can see the outer function's variables (nested functions)
# Question: If we put a function inside another function, can the inner one see the outer one's variables? (yes, the ENCLOSING scope)
platform = "StackSimplify"  # GLOBAL: top level of the file, so every function can read it

def show_course_page():
    course = "Python"  # belongs to show_course_page, the ENCLOSING function

    def show_title():
        print(course, "on", platform)  # the enclosing 'course' AND the global 'platform'

    show_title()

show_course_page()

# Concept-04: The LEGB rule. Python looks up a name in this order: Local, Enclosing, Global, Built-in
# Question-1: When the same name exists in several places, which one does Python use? (LEGB: Local first, then Enclosing, then Global, then Built-in)
# Question-2: What if the name is in NONE of the places we wrote, like len? (Python keeps searching outward and finds it in Built-in)
# E1: the L, the E and the G. Guess first: which x prints inside legb_inner, in legb_outer, and at the very end?
x = "global x"

def legb_outer():
    x = "enclosing x"
    def legb_inner():
        x = "local x"
        print(x)  # Local wins here
    legb_inner()
    print(x)  # Enclosing wins here

legb_outer()
print(x)  # Global wins here

# E2: the B. Nothing we wrote is called len - not local, not enclosing, not global - so the
# search runs all the way out to Built-in, and that is where Python finds it
def show_length():
    print(len("Python"))

show_length()
# len is a built-in NAME Python provides, like print, sum and max. Never shadow one:
# len = 5   # this HIDES the built-in len(); now len("hi") would break

# Concept-05: The global statement. Let a function CHANGE a global variable (use it sparingly; returning a value is usually cleaner)
# Question: How can a function actually change a global value? (declare it with 'global' first, but prefer returning a value)
# E1: WITHOUT global: assigning to score makes it LOCAL, so reading it first causes an error
score = 20  # a global: defined at the top level of the file

def add_points_bad():
    score = score + 10  # UnboundLocalError: score is local here, and has no value yet
    print("Inside the function score:", score)

# Call the function
# add_points_bad()  # uncomment to see the error
print("Global score:", score)  # 20: the global was never changed

# E2: WITH global: 'global score' makes the assignment target the REAL global
score = 20

def add_points():
    global score
    score = score + 10
    print("Inside the function score:", score)

# Call the function
add_points()
add_points()
print("Global score:", score)  # 40: the function changed the global

# Concept-06: The nonlocal statement. Let an inner function CHANGE the ENCLOSING function's variable
# Question: How can an inner (nested) function change a variable that belongs to the outer function? (declare it 'nonlocal')
# E1: WITHOUT nonlocal: assigning to score makes it LOCAL, so reading it first causes an error
def create_score_bad():
    score = 20  # belongs to create_score_bad (enclosing)

    def add_points():
        score = score + 10  # UnboundLocalError: score is local here, and has no value yet
        print("Inner Function score:", score)

    # Call the inner function
    # add_points()  # uncomment to see the error
    print("Enclosing score:", score)  # 20: the enclosing score was never changed

# Call the outer function
create_score_bad()

# E2: WITH nonlocal: 'nonlocal score' makes add_points update the ENCLOSING score
def create_score():
    score = 20

    def add_points():
        nonlocal score
        score = score + 10
        print("Inner Function score:", score)

    # Call the inner function
    add_points()
    add_points()
    print("Enclosing score:", score)  # 40: the enclosing score was changed

# Call the outer function
create_score()

# Note: An inner function that remembers variables from its enclosing function
# is called a CLOSURE. It is the idea behind decorators, which the next course covers.
