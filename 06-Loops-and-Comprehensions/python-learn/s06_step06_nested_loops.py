# Concept-01: A loop inside a loop; the inner loop runs fully on every outer turn
# Question: How do we visit every value in the list of lists [[10, 20, 30], [40, 50, 60], [70, 80, 90]], row by row? (the outer loop hands you a whole row, the inner loop walks the numbers inside it)
numbers = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# E1: without nesting - one loop per row, so you write the same loop again for every row
for number in numbers[0]:
    print(number)
for number in numbers[1]:
    print(number)
for number in numbers[2]:
    print(number)
# E2: the outer loop on its own - each turn hands you one ROW, which is itself a list
for row in numbers:
    print(row)
# E3: add the inner loop - it walks that row's numbers before the outer loop moves on
for row in numbers:
    print(row)
    for number in row:
        print(number)      # the inner loop finishes completely before the outer loop takes the next row

# Concept-02: Pair every item of one list with every item of another; the total pairs are len(first_list) * len(second_list)
# Question-1: How do we make every pair from the lists ["A", "B"] and [1, 2, 3]?
# (Each item of the first list is paired with every item of the second list.)
# Question-2: How many pairs are there?
# (The total pairs are len(first_list) * len(second_list).)
letters = ["A", "B"]
numbers = [1, 2, 3]

for letter in letters:
    for number in numbers:
        print(letter, number)

print("Total pairs:", len(letters) * len(numbers))   # 2 x 3 = 6

# Concept-03: Nested range() loops build a multiplication table.
# Question: How do we build the 1 to 3 multiplication tables?
# (For each row, print the table from 1 to 10.)
for row in range(1, 4):
    print(f"\n--- Table of {row} ---")
    for column in range(1, 11):
        print(f"{row} x {column} = {row * column}")

# Concept-04: break stops only the INNERMOST loop, so the outer loop keeps going
# Question: When we break inside the inner loop, does the whole thing stop or just that pass?
# (Only the inner loop stops; the outer loop continues.)
# E1: No break - the inner loop runs fully for every outer loop iteration
for row in range(1, 3):
    print(f"\nStarting row {row}")
    for col in range(1, 4):
        print(f"{row}-{col}")
# E2: break in the INNER loop at column 2
# Only the inner loop stops; the outer loop still moves to the next row.
for row in range(1, 3):
    print(f"\nStarting row {row}")
    for col in range(1, 4):
        if col == 2:
            break
        print(f"{row}-{col}")

# Concept-05: continue inside the inner loop skips one inner item and keeps going
# Question: How do we skip one inner item on every outer turn but keep the loop going?
# (continue skips only the current inner loop iteration.)
# E1: No continue - every inner item prints
for row in range(1, 3):
    print(f"\nStarting row {row}")
    for col in range(1, 4):
        print(f"{row}-{col}")
# E2: continue skips column 2 on every row, but the inner loop keeps going
for row in range(1, 3):
    print(f"\nStarting row {row}")
    for col in range(1, 4):
        if col == 2:
            continue
        print(f"{row}-{col}")
