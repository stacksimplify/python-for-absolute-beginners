# Run this step AS A FILE (press F5, or: python s10_step05_save_next_to_your_script.py).
# __file__ only exists while Python is running a real file, and that is the whole point here:
# a terminal prompt does not live anywhere, so it has no folder to point at.
# Concept-01: a bare file name lands wherever you RAN the program; Path(__file__).parent pins it to your code
# Question: why does the file I saved seem to disappear, and how do I always put it next to my script? (build the path from __file__)
from pathlib import Path

# A bare name carries no folder in front of it. Its parent is ".", which means "right here",
# and "here" is whatever folder you happened to run the program from.
bare_path = Path("demo_note.txt")

print("bare path:", bare_path)
print("Parent folder:", bare_path.parent)

# __file__ is the path of the script Python is running right now, and .parent is the folder
# that script lives in. A path built from it points at the same place every time, no matter
# which folder you started the program from.
anchored_path = Path(__file__).parent / "demo_note.txt"

print("File 1:", Path(__file__))
print("File 2:", Path(__file__).parent)
print("anchored file name:", anchored_path.name)
print("anchored stem:", anchored_path.stem)
print("anchored suffix:", anchored_path.suffix)
print("anchored parent:", anchored_path.parent)

# Concept-02: mkdir() a folder next to your script, then write a file into it
# Question: how do we make a data folder beside our code and save into it? (Path(__file__).parent / name, then mkdir(parents=True, exist_ok=True))
from pathlib import Path

script_dir = Path(__file__).parent

report_folder = script_dir / "demo_data" / "app_files"

report_folder.mkdir(parents=True, exist_ok=True)
# makes demo_data AND demo_data/app_files in one call

note_file = report_folder / "demo_note.txt"

note_file.write_text(
    "saved next to the script\n",
    encoding="utf-8"
)

print("folder made:", report_folder.name)
print("file written:", note_file.name)
print("is it really there?", note_file.exists())
print("saved inside:", note_file.parent.parent.name)

# Remove file and folders created
note_file.unlink()
report_folder.rmdir()          # the inner folder (app_files)
report_folder.parent.rmdir()   # then the outer folder (demo_data)
