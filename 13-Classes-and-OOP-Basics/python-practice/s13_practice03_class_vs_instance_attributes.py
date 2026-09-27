"""
Practice Problem-03: class attributes vs instance attributes

Concepts: a class attribute shared by all, instance attributes per object, precedence.

Write a program with one class Song:
Task-1: write the class with a class attribute app set to Tunefy and an
    __init__ taking a title and an artist.
Task-2: create s1 (Yesterday, The Beatles) and s2 (Hello, Adele), print
    s1.app, then print Song.app straight from the class.
Task-3: give s2 its own app value MyTunes, then print s2.app, s1.app and
    Song.app, so the instance attribute wins for s2 while the others stay
    Tunefy.

Expected output:
Tunefy
Tunefy
MyTunes
Tunefy
Tunefy
"""
