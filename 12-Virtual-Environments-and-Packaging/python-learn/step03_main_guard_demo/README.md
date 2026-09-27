# `step03_main_guard_demo` as it looks after Step-03

Use this to check your own files if something does not match the lesson.

## What is here

```text
step03_main_guard_demo/
    .venv/                  <- NOT in this folder, make your own
    special_names_demo.py   <- prints __name__, __file__ and __doc__
    app.py                  <- prints its __name__, has a function AND a main(), guard at the bottom
    runner.py               <- imports only double() from app.py
```

This folder sits NEXT TO `step02_my_project`, not inside it. It is a small demo of its own, so the
guard is the only idea on the page.

`app.py` here is the FINISHED version, with the guard already added. To see the bug the guard
fixes, change its last two lines back to a bare `main()` and run `runner.py`.

The first line of `app.py` prints its own `__name__`, so every run shows which value Python gave it.

## Run it

Make and activate a venv first, from inside this folder. On macOS and Linux the `python` command
only exists once a venv is active.

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate

    python special_names_demo.py
    python runner.py
    python app.py
    ```

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1

    python special_names_demo.py
    python runner.py
    python app.py
    ```

```text
__name__: __main__
__file__: /Users/you/step03_main_guard_demo/special_names_demo.py
__doc__: Explore a few special names Python gives to every file.
In app.py, __name__ is: app
Result: 20
In app.py, __name__ is: __main__
Starting the application...
```

Your `__file__` path will differ. `special_names_demo.py` shows three names Python set for you.
`python runner.py` imports `app.py`, so `__name__` is `app` and `main()` stays quiet: only
`Result: 20` follows. `python app.py` runs the file directly, so `__name__` is `__main__` and
`if __name__ == "__main__":` lets `main()` run.
