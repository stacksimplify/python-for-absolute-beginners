"""
Workshop Problem-07: keywords (Car Names) (solution)

Concepts: the keyword module.

Write a program to check whether "class" and "brand" are Python keywords, and print each result in the
form shown below.

Expected output:
Is 'class' a keyword? True
Is 'brand' a keyword? False
"""
import keyword

print("Is 'class' a keyword?", keyword.iskeyword("class"))
print("Is 'brand' a keyword?", keyword.iskeyword("brand"))
