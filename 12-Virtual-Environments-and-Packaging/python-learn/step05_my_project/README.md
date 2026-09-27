# `step05_my_project` as it looks after Step-05, and after the whole section

This is the finished project. Use it to check your own work.

## What is here

```text
step05_my_project/
    .venv/                  <- NOT in this folder, make your own
    app.py                  <- copied in from step04_my_project
    number_utils/           <- copied in from step04_my_project
        __init__.py
        calculations.py
    pyproject.toml          <- new in Step-05: describes the project so pip can install it
```

## Run the whole thing

From inside this folder:

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -e .
    ```

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -e .
    ```

Now leave the folder entirely and the package still imports, which is what Step-05 buys you:

```bash
cd ..
python -c "from number_utils import double; print(double(25))"
```

That prints `50` from a folder that has nothing to do with your project.

An `*.egg-info/` folder appears after `pip install -e .`. It is bookkeeping from the install, and
you can ignore it.
