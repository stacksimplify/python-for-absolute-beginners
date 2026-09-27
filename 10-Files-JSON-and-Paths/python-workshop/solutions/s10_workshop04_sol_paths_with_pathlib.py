"""
Workshop Problem-04: paths with pathlib (Garage Path) (solution)

Concepts: Path join with /, .name/.suffix/.parent, .exists().

Build a variable `p` by joining the parts "garage", "cars", and "mazda.txt" into one `Path`
with the `/` operator. Then, for that path:
  Task-1: print the path itself.
  Task-2: print the path's name (use `.name`).
  Task-3: print the path's suffix (use `.suffix`).
  Task-4: print the path's parent (use `.parent`).
  Task-5: print whether the path exists (use `.exists()`; this path was never created, so it is False).

Expected output:
garage/cars/mazda.txt
mazda.txt
.txt
garage/cars
False
"""
from pathlib import Path

p = Path("garage") / "cars" / "mazda.txt"
# Task-1: print the path itself
print(p)
# Task-2: print the path's name
print(p.name)
# Task-3: print the path's suffix
print(p.suffix)
# Task-4: print the path's parent
print(p.parent)
# Task-5: print whether the path exists
print(p.exists())
