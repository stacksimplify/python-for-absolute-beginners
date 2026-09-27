# `step04_my_project` as it looks after Step-04

Use this to check your own files if something does not match the lesson. Compare, do not copy:
typing these out yourself is where the learning is.

## What is here

```text
step04_my_project/
    .venv/                  <- NOT in this folder, make your own
    app.py                  <- the application: it uses the package
    import_star_demo.py     <- shows what import * brings in
    number_utils/           <- your package
        __init__.py         <- the front door: what the package hands out, plus __all__ for import *
        calculations.py     <- the module, holds the real functions
```

Note where `app.py` sits: directly in the project folder, NEXT TO `number_utils/` rather than inside
it. `number_utils/` is the library, `app.py` is the application that uses it.

## Run it

From inside this folder:

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate

    python app.py
    python import_star_demo.py
    ```

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1

    python app.py
    python import_star_demo.py
    ```

Each file prints the same two result lines:

```text
Double: 50
Percentage: 3.0
Double: 50
Percentage: 3.0
```

`__init__.py` here is the FINISHED version, with both names in `__all__`. To see the two breaks
again: empty `__init__.py` and `python app.py` fails with an ImportError; set `__all__ = ["double"]`
and `python import_star_demo.py` fails with a NameError on `percentage`.

The `if __name__ == "__main__":` at the bottom of `app.py` is the guard from Step-03. Here it is
simply how the file is written: the lesson in Step-04 is the package, not the guard.
