"""
Practice Problem-07: keywords (solution)

Concepts: the keyword module.

Write a program that prints how many hard keywords Python has, then checks and prints whether "if", "class", and "course" are Python keywords. Print each
line in the form shown below.

Expected output:
Total hard keywords: 35
Is 'if' a keyword? True
Is 'class' a keyword? True
Is 'course' a keyword? False
"""
import keyword

print("Total hard keywords:", len(keyword.kwlist))
print("Is 'if' a keyword?", keyword.iskeyword("if"))
print("Is 'class' a keyword?", keyword.iskeyword("class"))
print("Is 'course' a keyword?", keyword.iskeyword("course"))
