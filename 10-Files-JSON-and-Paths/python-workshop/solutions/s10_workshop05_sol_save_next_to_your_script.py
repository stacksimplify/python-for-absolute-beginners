"""
Workshop Problem-05: save next to your script (Garage) (solution)

Concepts: __file__, Path(__file__).parent, .is_absolute(), mkdir(parents=True, exist_ok=True), rmdir().
"""

from pathlib import Path

"""
Problem-1: Where Does the Service Log Land? (Garage)
Build a variable `plain` as a `Path` for "service.log", and a variable `beside_code` that points at
"service.log" next to THIS script (build it from `__file__`). Then:
  Task-1: print the folder of `plain` (use `.parent`; a bare name has none, so it prints ".").
  Task-2: print the file name of `beside_code` (use `.name`).
  Task-3: print whether `beside_code` is pinned to one place (use `.is_absolute()`).

Expected output:
.
service.log
True
"""

plain = Path("service.log")
beside_code = Path(__file__).parent / "service.log"
# Problem-1 Task-1: the folder of a bare name
print(plain.parent)
# Problem-1 Task-2: the file name of the anchored path
print(beside_code.name)
# Problem-1 Task-3: is it pinned to one place?
print(beside_code.is_absolute())

"""
Problem-2: A Garage Records Folder Beside Your Code.
Build a variable `folder` that points at a "demo_garage" folder next to THIS script, create it (make
any missing parents, and do not fail if it already exists), write the rows "car,km" and "mazda,42000"
into a file "service.log" inside it, then:
  Task-1: print the folder name (use `.name`).
  Task-2: print whether the file is really there (use `.exists()`).
  Task-3: remove the file, then the folder.

Expected output:
demo_garage
True
"""

folder = Path(__file__).parent / "demo_garage"
folder.mkdir(parents=True, exist_ok=True)
log = folder / "service.log"
log.write_text("car,km\nmazda,42000\n", encoding="utf-8")
# Problem-2 Task-1: the folder name
print(folder.name)
# Problem-2 Task-2: is the file really there?
print(log.exists())

# Problem-2 Task-3: remove the file, then the folder
log.unlink()
folder.rmdir()
