"""
Practice Problem-06: class methods and static methods

Concepts: the decorators @classmethod (an alternate constructor: it receives the
class as cls) and @staticmethod (a related helper: it takes neither self nor cls),
and using both together.

Write a program with one class Song:
Task-1: write the class with an __init__ that takes a title, an artist and a
    duration in seconds, a @classmethod from_dict(cls, data) that builds a
    Song from a dict with keys title, artist and duration, and a
    @staticmethod is_valid_duration(duration) that returns True when
    duration is above 0.
Task-2: print Song.is_valid_duration(125).
Task-3: take the two dicts {"title": "Yesterday", "artist": "The Beatles",
    "duration": 125} and {"title": "Silence", "artist": "Unknown",
    "duration": 0}. For each one, build the song with from_dict and print
    its title and duration only when is_valid_duration says the duration is
    valid, and print Duration is not valid when it is not.

Expected output:
True
Yesterday 125
Duration is not valid
"""
