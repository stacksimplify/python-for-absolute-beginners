# Concept-01: 'with open(...)' opens a file, writes with mode "w", and closes it for you
# Question: How do we save text ("first line\n" then "second line\n") to a file, with Python closing the file for us even if something goes wrong partway through?
# The mode says what you are doing: "w" = write (creates the file, or replaces it if it exists), "r" = read.
# encoding="utf-8" tells Python how to turn text into bytes when it saves, and back into text when it
# reads. Pass it on EVERY open() and your files read the same on Windows, Mac and Linux, even when
# they hold accented letters or symbols. Every open() in this section does it.
with open("demo_notes.txt", "w", encoding="utf-8") as f:
    # Each "\n" starts a new line
    f.write("first line\n")
    f.write("second line\n")

print("saved demo_notes.txt")

# Concept-02: Read the whole file back as one string with mode "r"
# Question: How do we load all the text from a file back into Python as one string?
# Write it first so this block stands on its own
with open("demo_notes.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")

with open("demo_notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# Concept-03: Point at a file with Path, then delete it with .unlink(); missing_ok=True when it may already be gone
# Question: How do we delete the files this step made, without an error if one has already gone?
# Path("name") wraps a file name so Python can act on the file itself, and .unlink() deletes it.
# "from ... import" pulls in tools Python ships with: here, Path from the pathlib module.
from pathlib import Path

# Recreate the file so this block runs on its own, then clear it away.
with open("demo_notes.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")

# Remove file created
Path("demo_notes.txt").unlink()
print("removed demo_notes.txt")

# Both files are gone now. A plain unlink() would raise FileNotFoundError here; missing_ok=True means
# "delete it if it is there, do nothing if it is not", which is what you want for tidy-up code.
Path("demo_notes.txt").unlink(missing_ok=True)  # safe even though the file is already gone - no FileNotFoundError
print("second unlink was safe because of missing_ok=True")
