"""
Practice Problem-04: methods

Concepts: a method uses self, a method changes data, returning vs acting.

Write a program with one class Song:
Task-1: write the class with an __init__ that takes a title and an artist
    and sets self.plays to 0, a method play that adds 1 to self.plays, and a
    method label that RETURNS the text <title> by <artist>.
Task-2: create s1 for Yesterday by The Beatles, play it 3 times, and
    print s1.plays.
Task-3: print s1.label().

Expected output:
3
Yesterday by The Beatles
"""

# Task-1: the class, with play() that ACTS and label() that RETURNS
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.plays = 0

    def play(self):
        self.plays += 1

    def label(self):
        return f"{self.title} by {self.artist}"

# Task-2: create the song, play it three times, then print the changed counter
s1 = Song("Yesterday", "The Beatles")
s1.play()
s1.play()
s1.play()
print(s1.plays)

# Task-3: print what label() RETURNS
print(s1.label())
