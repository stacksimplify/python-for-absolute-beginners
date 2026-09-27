"""
Workshop Problem-01: write and read a text file (Car Log) (solution)

Concepts: with open(), "w", "r", .unlink().

Write a program that writes the two log lines "Engine started" and "Drove 50 km" to car_log.txt, reads the whole file back as one string and prints it, then removes the file.

Expected output:
Engine started
Drove 50 km

"""
from pathlib import Path

with open("car_log.txt", "w", encoding="utf-8") as f:
    f.write("Engine started\n")
    f.write("Drove 50 km\n")
with open("car_log.txt", "r", encoding="utf-8") as f:
    print(f.read())
Path("car_log.txt").unlink()
