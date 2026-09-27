"""
Workshop Problem-04: paths with pathlib (Garage Path)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

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
