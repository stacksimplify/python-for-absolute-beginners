# Milestone Project 2: How We Build It (Grow Milestone 1)

This project does not start from empty files. It starts from the Milestone 1 tracker you already
built, and every stage below is a small edit to it. The program RUNS at every stage.

**Where to start.** Build in `../04-livecode-build-incremental/`: it already holds the six Milestone 1 files,
without comments and without the long docstring at the top of each file. Or copy the six `.py` files from
`../../milestone-project-1/build-incremental/` into it and delete the long docstring at the top of each one.
Do NOT copy them on top of this folder: the four files both projects share
(`f1_is_valid_amount.py`, `f2_format_row.py`, `f5_actions.py` and `main.py`) have different contents
here, and you would overwrite the reference you may want to compare against.

## What carries over

| Your Milestone 1 file | Here |
|---|---|
| f1_is_valid_amount.py | carried over; body unchanged, signature gains type hints, docstring reworded |
| f2_format_row.py | carried over; signature gains type hints and the file imports `Expense`; three lines inside change from brackets to dots |
| f3_compute_total.py | moves into the class as `ExpenseBook.compute_total()` (same name), then the file goes |
| f4_compute_by_category.py | moves into the class as `ExpenseBook.compute_by_category()` (same name), then the file goes |
| f5_actions.py | edited: every action takes `book` instead of `expenses` |
| main.py | edited: holds a book, loads on start, saves on quit |

`expense.py` and `expense_book.py` are new here. There is no `f3` or `f4` in this project, and that gap
is on purpose: it is where your two helper files used to be.

## The layers
| Layer | File(s) | Job | input/print? |
|---|---|---|---|
| Data | expense.py | the `Expense` class (one expense) | no |
| Logic and storage | expense_book.py | `ExpenseBook`: store_expense / compute_total / compute_by_category / filter / save / load | NO (web-ready) |
| Pure helpers | f1_is_valid_amount.py, f2_format_row.py | validate input, format a row | no |
| Actions | f5_actions.py | what each menu choice DOES | yes |
| Driver | main.py | load, menu loop, save | yes |

The big rule: the DATA and the LOGIC (`expense.py`, `expense_book.py`) never call `input()` or
`print()`. That is exactly why a web app could reuse them later; only the actions and the driver talk
to a person.

## Build order
| Stage | What you change | The app then... |
|---|---|---|
| 0 | start from the Milestone 1 files in `../04-livecode-build-incremental/`, retitle the menu to 2.0 | runs, exactly as before (only the title changed) |
| 1 | add type hints to all six files | runs, output identical |
| 2 | add `expense.py`; the dict becomes an `Expense` | runs, output identical |
| 3 | add `expense_book.py`; `main` holds a book | runs, output identical |
| 4 | move the two helpers in as methods, add `filter()`, delete their files | runs, output identical |
| 5 | `created_at` stamp and `__repr__` on every expense | same screen, visible in the object |
| 6 | `save()` with JSON and `pathlib`; menu 6 saves | writes `data/expenses.json` |
| 7 | `load()` on start | your data survives a restart |
| 8 | guard a corrupt file with `try` / `except` | warns instead of crashing |

Stages 1 to 5 change nothing on screen, and that is the lesson: a refactor changes the SHAPE of a
program, not what it does. Stage 6 is the first stage that changes the screen: menu 6 becomes Save and quit.

## How the files connect

```text title="How the files connect"
main.py  --imports-->  f5_actions.py  --imports-->  expense_book.py  --imports-->  expense.py
                                      --imports-->  f1_is_valid_amount.py, f2_format_row.py
f2_format_row.py  --imports-->  expense.py   (format_row reads an Expense)
main.py  --imports-->  expense_book.py   (main is the one that creates the book)
```

Run the app from this folder: `python3 main.py`. (A pure helper or a class file run on its own prints
nothing, because neither one ever calls `print()`.)

## Files here

The files in this folder are the FINISHED reference. Build in `../04-livecode-build-incremental/` and
use these to check yourself as you go.

- expense.py: the `Expense` class, new in this project.
- expense_book.py: the `ExpenseBook` class, new in this project; Milestone 1's two helpers moved into it as methods.
- f1_is_valid_amount.py, f2_format_row.py: carried over from Milestone 1.
- f5_actions.py: the five menu actions, edited to take the book.
- main.py: the menu driver, edited to load and save.

**Want the `rich` version?** `../02-orig-build-incremental-with-rich/` is this same program with the expense list printed as a table, and `../05-livecode-build-incremental-with-rich/` is where you do that step yourself (Step-11 on the website).
