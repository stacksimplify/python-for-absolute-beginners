"""
Workshop Problem-06: nested loops (Parking Grid)

Optional self-study: the same ideas as this section, in a car scenario. Write the code
yourself, then compare with python-workshop/solutions/.

Concepts: nested loops, range(), break inside nesting, f-strings.

Write a program that, for a car park:
- Task-1: with 3 rows and 2 columns, use an outer for loop over the rows (1 to 3)
  and an inner for loop over the columns (1 to 2) to print every spot as R<row>C<col>.
- Task-2: scan each of the 3 rows across columns 1 to 3, printing scan R<row>C<col>,
  but break at the first blocked spot (column 2) so each row stops after column 1.

Expected output:
R1C1
R1C2
R2C1
R2C2
R3C1
R3C2
scan R1C1
scan R2C1
scan R3C1
"""
