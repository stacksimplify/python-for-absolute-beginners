"""
Practice Problem-04: paths with pathlib

Concepts: Path joining with /, .name/.suffix/.stem/.parent, .exists(), write_text()/read_text().

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

Problem-2: Catalog Backup.
Write a program that builds a variable `backup` as a `Path` for "catalog_backup.txt", saves the text "catalog backed up" to it in one step with `.write_text()` (end it with a newline), reads the file back in one step with `.read_text()`, strips the whitespace and prints it labeled "read_text: <text>", then removes the file.

Expected output:
read_text: catalog backed up
"""
