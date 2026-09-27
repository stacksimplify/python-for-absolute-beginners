"""
Workshop Problem-02: append and read lines (Service Log) (solution)

Concepts: "a" append, read line by line, strip().

Write a program that writes "Oil change" to service.txt, then appends "Tyre rotation" to the same file, then reads the file line by line and prints each line as "service: <text>" (strip the newline).

Expected output:
service: Oil change
service: Tyre rotation
"""
from pathlib import Path

with open("service.txt", "w", encoding="utf-8") as f:
    f.write("Oil change\n")
with open("service.txt", "a", encoding="utf-8") as f:
    f.write("Tyre rotation\n")
with open("service.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("service:", line.strip())
Path("service.txt").unlink()
