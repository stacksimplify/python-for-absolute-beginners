"""
Practice Problem-05: save next to your script

Concepts: __file__, Path(__file__).parent, .is_absolute(), mkdir(parents=True, exist_ok=True), rmdir().

Problem-1: Where Does It Land?
Build a variable `plain` as a `Path` for "orders.csv", and a variable `beside_code` that points at
"orders.csv" next to THIS script (build it from `__file__`). Then:
  Task-1: print the folder of `plain` (use `.parent`; a bare name has none, so it prints ".").
  Task-2: print the file name of `beside_code` (use `.name`).
  Task-3: print whether `beside_code` is pinned to one place (use `.is_absolute()`).

Expected output:
.
orders.csv
True

Problem-2: A Reports Folder Beside Your Code.
Build a variable `folder` that points at a "demo_orders" folder next to THIS script, create it (make
any missing parents, and do not fail if it already exists), write the rows "id,total" and "jan,900"
into a file "orders.csv" inside it, then:
  Task-1: print the folder name (use `.name`).
  Task-2: print whether the file is really there (use `.exists()`).
  Task-3: remove the file, then the folder.

Expected output:
demo_orders
True

Run this file directly (F5, or python s10_practice05_save_next_to_your_script.py).
"""
