# Milestone Project 1: How We Build It (Incremental Guide)

We build this in three small layers. The program RUNS at the end of every stage in the build order below.

You write the app one file at a time: a running `main.py` menu shell with five stub actions first,
then each pure helper (`f1`-`f4`), turning one stub in `f5_actions.py` into the real action after
each helper. The step-by-step walkthrough, with every file and a real run from Step-02 on, is the
project page (`../README.md`). The warm-up drills in `../warmup/` are optional.

## The three layers
| Layer | File(s) | Its job |
|---|---|---|
| Pure helpers | f1..f4_*.py | turn data into a value (no input/print); clean, single-purpose functions |
| Actions | f5_actions.py | what each menu choice DOES: wraps input()/print() around the helpers |
| Menu driver | main.py | show_menu() + main(): show the menu, read a choice, call the action |

## The technique you will see
- `import`: a function can live in its own file; another file imports it
  with `from f1_is_valid_amount import is_valid_amount`.

Each helper file is just the clean function (no self-tests to run). You see each
one work the moment you wire it into the menu and run the app.

## The rule we never break
1. Start with a WORKING menu shell in main.py (actions stubbed).
2. Write the next pure helper.
3. Import it into f5_actions.py, turn its stub into the real action, and
   run the app to see that menu choice work.

## Build order
| Stage | Write the helper | Wire it up | The app now... |
|---|---|---|---|
| 0 | main.py shell (show_menu() + the loop) PLUS the 5 f5_actions.py stubs it imports; each choice prints its stub message: `--> Option N selected: ...` then `Expenses: []` | (nothing yet) | runs; you can quit |
| 1 | f1_is_valid_amount.py | add_expense in f5_actions.py; import it; choice 1 | can add |
| 2 | f2_format_row.py | list_expenses; import; choice 2 | can list |
| 3 | f3_compute_total.py | show_total; import; choice 3 | shows total |
| 4 | f4_compute_by_category.py | show_by_category; import; choice 4 | shows totals per category |
| 5 | (no new helper) | filter_by_category (uses f2); choice 5 | shows one category |

On the project page, Stage 0 is Step-01 (main.py and the five stubs together), and Stage 1 to Stage 5 are Step-02 to Step-06. Step-07 there runs the finished build and compares it with the one-file solution.

## How the files connect

```text title="How the files connect"
main.py  --imports-->  f5_actions.py  --imports-->  f1..f4_*.py
```

Run the app from this folder: `python3 main.py`. (A pure helper run on its own
prints nothing, because a helper never prints. You see it work once its action is wired in.)

## Files here

The files in this folder are the FINISHED reference. Build your own copy in a separate
folder and use these to check yourself as you go.

- f1..f4_*.py: the pure helpers (clean single-purpose functions).
- f5_actions.py: the five menu actions (add/list/total/by-category/filter).
- main.py: the menu driver (show_menu + main); imports the actions.

(../solution/expense_tracker.py is the same program in ONE file, if you
prefer no imports.)
