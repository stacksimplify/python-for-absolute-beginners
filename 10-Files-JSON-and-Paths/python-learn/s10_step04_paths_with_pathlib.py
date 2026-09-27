# Concept-01: Build a path by joining parts with the / operator
# Question: How do we build a file path from the parts "reports", "app_files", and "demo_note.txt"
# that works on Windows, Mac, and Linux without hardcoding forward or backward slashes?
from pathlib import Path

file_path = Path("reports") / "app_files" / "demo_note.txt"

print(file_path)  # reports/app_files/demo_note.txt

# Concept-02: Split a path into its parts with .name, .suffix, .stem, and .parent
# Question-1: How do we get the filename (.name) and the name without extension (.stem)
# from a path like Path("reports") / "app_files" / "demo_note.txt"?
# Question-2: How do we get the file extension (.suffix) and the parent folder (.parent)?
from pathlib import Path

file_path = Path("reports") / "app_files" / "demo_note.txt"

print("name:  ", file_path.name)    # demo_note.txt (file name with extension)
print("suffix:", file_path.suffix)  # .txt (file extension)
print("stem:  ", file_path.stem)    # demo_note (file name without extension)
print("parent:", file_path.parent)  # reports/app_files (folder containing the file)

# Concept-03: Path.write_text() and Path.read_text(), the shortest way to write or read a whole file
# Question-1: How do we write an entire small file in one line with Path.write_text()
# without using an open() block?
# Question-2: How do we read an entire small file back in one line with Path.read_text()
# without using an open() block?
from pathlib import Path

# Same file name as Concepts 1 and 2, but written right here in the current folder.
# A path with folders in it can only be written once those folders already exist.
note_file = Path("demo_note.txt")

note_file.write_text(
    "saved with one line\n",
    encoding="utf-8"
)  # writes the whole string and closes the file for you

print("read_text:", note_file.read_text(encoding="utf-8").strip())
# reads the whole file back as one string

# Remove file created
note_file.unlink()

# Concept-04: .exists() asks the operating system whether a path is really there
# Question: How do we check whether a file is on disk before we try to read it?
# (Path(...).exists() answers True or False)
from pathlib import Path

# The SAME demo_note.txt as Concept-03, with an .exists() check wrapped around each step,
# so you can watch one file appear and disappear.
note_file = Path("demo_note.txt")

print("before we write it:", note_file.exists())  # False, nothing is there yet

note_file.write_text(
    "saved with one line\n",
    encoding="utf-8"
)

print("read_text:", note_file.read_text(encoding="utf-8").strip())
print("after we write it:", note_file.exists())  # True, the file is on disk now

# Remove file created
note_file.unlink()

print("after we remove it:", note_file.exists())  # False again
