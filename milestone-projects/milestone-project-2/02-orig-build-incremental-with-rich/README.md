# The finished tracker, with the `rich` package

This is the same program as `../01-orig-build-incremental/`, with one change: the expense list prints as a
real table, using `rich`, the package you install in Step-11 on the course website.

| File | Difference from `../01-orig-build-incremental/` |
|---|---|
| `f2_format_row.py` | keeps `format_row()`, and adds `make_table()`, which builds the `rich` table |
| `f5_actions.py` | `list_expenses()` and `filter_by_category()` print that table |
| `requirements.txt` | the one package this folder needs |
| everything else | identical: `expense.py`, `expense_book.py`, `f1_is_valid_amount.py`, `main.py` |

Only the part that talks to the screen changed. `ExpenseBook` does not know that `rich` exists.

## Run this folder

```bash title="Set it up once"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

On Windows, activate with `.venv\Scripts\activate`. Add two expenses, then choose `2`.

You do Step-11 in `../05-livecode-build-incremental-with-rich/`, which starts as the finished
tracker without `rich`. This folder is what it looks like when you are done.
