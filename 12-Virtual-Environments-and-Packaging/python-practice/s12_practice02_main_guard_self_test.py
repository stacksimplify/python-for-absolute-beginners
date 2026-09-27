"""
Practice Problem-02: run-it-directly self-test with the __main__ guard (file 1 of 2)

Concepts: a function that returns a value, the special name __name__, an if __name__ == "__main__"
guard, and what changes when another file IMPORTS your module instead of running it.

File 1 (this file). Write a function order_summary(product, quantity, price) that returns the text
"<quantity> x <product> = <total>", where total is quantity * price. Then give it a self-test that
prints two summaries:
  Task-1: print the summary for 3 units of "Notebook" at price 40.
  Task-2: print the summary for 1 unit of "Pen" at price 15.

Put those two print calls at the BOTTOM of the file for now, with NO guard. Running the file
prints both lines:

Expected output:
3 x Notebook = 120
1 x Pen = 15

Then work through Task-3 to Task-5 in file 2, the order report. Task-5 brings you back here to add
the guard. Running this file directly must still print both summaries. One file, both jobs.

Write your solution below.
"""
