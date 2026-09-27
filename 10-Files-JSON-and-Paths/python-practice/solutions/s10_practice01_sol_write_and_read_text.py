"""
Practice Problem-01: write and read a text file (solution)

Concepts: with open(..., encoding="utf-8"), mode "w" to write, mode "r" to read, encoding="utf-8", .unlink() to tidy up.
"""

from pathlib import Path

"""
Problem-1: Save the Catalog.
Write a program that writes the two catalog lines "Wireless Mouse - 25" and "Mechanical Keyboard - 45" to "store_catalog.txt", reads the whole file back as one string and prints it, removes the file, then prints the done message "Saved the catalog, read it back, then removed it.".

Expected output:
Wireless Mouse - 25
Mechanical Keyboard - 45

Saved the catalog, read it back, then removed it.
"""

with open("store_catalog.txt", "w", encoding="utf-8") as f:
    f.write("Wireless Mouse - 25\n")
    f.write("Mechanical Keyboard - 45\n")

with open("store_catalog.txt", "r", encoding="utf-8") as f:
    catalog_text = f.read()
print(catalog_text)

Path("store_catalog.txt").unlink()
print("Saved the catalog, read it back, then removed it.")

"""
Problem-2: Save the Store Name.
Write a program that writes the line "Gadget Hub" to "store_name.txt" (use encoding "utf-8"), reads it back, strips the whitespace, prints it labeled "store: <text>", then removes the file.

Expected output:
store: Gadget Hub
"""

with open("store_name.txt", "w", encoding="utf-8") as f:
    f.write("Gadget Hub\n")

with open("store_name.txt", "r", encoding="utf-8") as f:
    print("store:", f.read().strip())

Path("store_name.txt").unlink()
