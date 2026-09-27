"""
Practice Problem-02: run-it-directly self-test with the __main__ guard (file 2 of 2)

File 2 (this file), the order report. It wants one thing from file 1, the function, and nothing else.
  Task-3: import order_summary from file 1, then print a report line for 2 units of "Marker" at
          price 15, in the form: Report: 2 x Marker = 30

Now see the bug. Run this file while file 1 still has no guard:

Example run: file 2 BEFORE the guard
3 x Notebook = 120
1 x Pen = 15
Report: 2 x Marker = 30

  Task-4: you never asked for those first two lines. Work out why they appeared.
  Task-5: put file 1's two self-test calls behind an if __name__ == "__main__" guard, then run
          this file again. Only your own line should be left:

Example run: file 2 AFTER the guard
Report: 2 x Marker = 30

Write your solution below.
"""
