"""
Practice Problem-04: paths with pathlib (solution)

Concepts: Path joining with /, .name/.suffix/.stem/.parent, .exists(), write_text()/read_text().
"""

from pathlib import Path

"""
Problem-1: Catalog File Path.
Build a variable `catalog_path` by joining the parts "catalog", "app_files", and "products.json" into one `Path`
with the `/` operator. Then, for that path:
  Task-1: print the path itself.
  Task-2: print the path's name (use `.name`).
  Task-3: print the path's suffix (use `.suffix`).
  Task-4: print the path's stem (use `.stem`).
  Task-5: print the path's parent (use `.parent`).
  Task-6: print whether the path exists (use `.exists()`; this path was never created, so it is False).

Expected output:
catalog/app_files/products.json
products.json
.json
products
catalog/app_files
False
"""

catalog_path = Path("catalog") / "app_files" / "products.json"
# Problem-1 Task-1: print the path itself
print(catalog_path)

# Problem-1 Task-2: print the path's name
print(catalog_path.name)
# Problem-1 Task-3: print the path's suffix
print(catalog_path.suffix)
# Problem-1 Task-4: print the path's stem
print(catalog_path.stem)
# Problem-1 Task-5: print the path's parent
print(catalog_path.parent)

# Problem-1 Task-6: print whether the path exists
print(catalog_path.exists())

"""
Problem-2: Catalog Backup.
Write a program that builds a variable `backup` as a `Path` for "catalog_backup.txt", saves the text "catalog backed up" to it in one step with `.write_text()` (end it with a newline), reads the file back in one step with `.read_text(encoding="utf-8")`, strips the whitespace and prints it labeled "read_text: <text>", then removes the file.

Expected output:
read_text: catalog backed up
"""

backup = Path("catalog_backup.txt")
backup.write_text("catalog backed up\n", encoding="utf-8")
print("read_text:", backup.read_text(encoding="utf-8").strip())
backup.unlink()
