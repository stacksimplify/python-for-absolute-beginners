# Concept-01: Mode "a" = append; it adds to the end of a file instead of replacing it
# Question: How do we add new lines to a log file over time without losing the old entries? (use append mode "a")
from pathlib import Path

# E1: First, test with "w" write mode. Each "w" STARTS THE FILE OVER, so the first pair is thrown away.
with open("demo_log.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")

with open("demo_log.txt", "w", encoding="utf-8") as f:
    f.write("third line\n")
    f.write("fourth line\n")

with open("demo_log.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

Path("demo_log.txt").unlink()   # clear it so E2 starts from nothing and the contrast is fair

# E2: Second, test with "a" append mode. Each "a" ADDS to the end, so everything survives.
with open("demo_log.txt", "a", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")

with open("demo_log.txt", "a", encoding="utf-8") as f:
    f.write("third line\n")
    f.write("fourth line\n")

with open("demo_log.txt", "r", encoding="utf-8") as f:
    print(f.read().strip())

# Concept-02: Loop over the file to read ONE line at a time; the whole file never sits in memory
# Question: How do we read a file that is too big to hold in memory? (loop over the file object; strip() drops the trailing newline)
# The same demo_log.txt as Concept-01, written again so this block stands on its own
with open("demo_log.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")
    f.write("third line\n")

# Python hands you one line, you finish with it, then it hands you the next. Only ONE line is in
# memory at a time, so this reads a 3-line file and a 3 GB file exactly the same way.
with open("demo_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("line:", line.strip())

# Concept-03: readlines() pulls the WHOLE file into a LIST at once, the opposite trade to Concept-02
# Question: How do we get every line as a list so we can count them or jump straight to one? (f.readlines(), or f.read().splitlines() for lines without the \n)
from pathlib import Path

# The SAME demo_log.txt as Concept-02, so the only thing that changes is HOW we read it.
with open("demo_log.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")
    f.write("third line\n")

# Everything lands in memory at once. That costs memory, and buys you len() and indexing.
with open("demo_log.txt", "r", encoding="utf-8") as f:
    all_lines = f.readlines()
print(all_lines)                      # each line still ends with \n
print("how many lines:", len(all_lines))
print("last line:", all_lines[-1].strip())

# Related, one line: f.read().splitlines() returns the same lines with the "\n" already removed,
# which saves you a .strip() when you do not need the raw newlines.

# Concept-04: after a read the cursor sits at the END of the file; f.seek(0) rewinds it to the start
# Question: why does reading the same open file a second time give me nothing back? (the cursor is already at the end; call f.seek(0) first)
from pathlib import Path

# Creating the file
with open("demo_log.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")
    f.write("third line\n")

# E1: read TWICE without rewinding. The first read leaves the cursor at the end of the file,
# so the second one starts there and finds nothing left, printing an empty line.
with open("demo_log.txt", "r", encoding="utf-8") as f:
    read1 = f.read()
    read2 = f.read()
print("read1:", read1)
print("read2:", read2)

# E2: the same two reads, but f.seek(0) moves the cursor back to position 0 first.
with open("demo_log.txt", "r", encoding="utf-8") as f:
    read1 = f.read()
    f.seek(0)
    read2 = f.read()
print("read1:", read1)
print("read2:", read2)

# Remove file created
Path("demo_log.txt").unlink()
