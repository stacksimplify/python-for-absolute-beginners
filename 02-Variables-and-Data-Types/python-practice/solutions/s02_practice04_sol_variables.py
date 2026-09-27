"""
Practice Problem-04: variables and naming (solution)

Concepts: variables, changing a variable's value, print() with several values and sep,
naming rules and conventions.
"""

"""
Problem-1:
  Write a program that stores a name ("Kalyan") and a city ("Hyderabad") in variables,
  then prints an intro card: the title "Intro Card", the labeled name and city, a blank
  line, and finally the name and city on one line joined by " - ".

Expected output:
Intro Card
Name: Kalyan
City: Hyderabad

Kalyan - Hyderabad
"""
# Problem-1 Task-1: store name and city, print intro card
name = "Kalyan"
city = "Hyderabad"

print("Intro Card")
print("Name:", name)
print("City:", city)

print()
print(name, city, sep=" - ")

"""
Problem-2:
  Write a program that stores a course title and lesson count in snake_case variables
  (course_title = "Python for Beginners", lesson_count = 50) and a maximum rating as an
  UPPER_CASE constant (MAX_RATING = 5), then prints all three.

Expected output:
Python for Beginners
50
5
"""
# Problem-2 Task-1: snake_case vars and UPPER_CASE constant, print all three
course_title = "Python for Beginners"
lesson_count = 50
MAX_RATING = 5

print(course_title)
print(lesson_count)
print(MAX_RATING)

"""
Problem-3:
  Write a program that stores an age of 30 and prints it, then changes age to 31
  after a birthday and prints it again.

Expected output:
30
31
"""
# Problem-3 Task-1: store an age, change it after a birthday, print both
age = 30
print(age)
age = 31
print(age)
