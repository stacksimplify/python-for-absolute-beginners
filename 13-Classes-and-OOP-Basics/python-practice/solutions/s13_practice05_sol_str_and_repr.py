"""
Practice Problem-05: __str__ and __repr__ (solution)

Concepts: __str__ for a friendly printout, __repr__ for the exact one; both are dunder
methods, so the name must match exactly.

Write a program with one class Song:
Task-1: write the class with an __init__ that takes a title and an artist,
    __str__ returning <title> by <artist>, and __repr__ returning
    Song(title='<title>', artist='<artist>').
Task-2: create s1 (Yesterday, The Beatles) and s2 (Hello, Adele), and print
    s1.
Task-3: print a list holding both songs.

Expected output:
Yesterday by The Beatles
[Song(title='Yesterday', artist='The Beatles'), Song(title='Hello', artist='Adele')]
"""

# Task-1: the class, with both dunder methods
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"{self.title} by {self.artist}"

    def __repr__(self):
        return f"Song(title={self.title!r}, artist={self.artist!r})"

# Task-2: create both songs; print() uses __str__
s1 = Song("Yesterday", "The Beatles")
s2 = Song("Hello", "Adele")
print(s1)

# Task-3: a list of objects uses __repr__
print([s1, s2])
