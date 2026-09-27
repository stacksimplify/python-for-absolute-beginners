# `step01_my_project` as it looks after Step-01

Use this to check your own folder if something does not match the lesson. You do not need to
download it: Step-01 has you build this yourself, and building it is the point.

## What is here

Almost nothing, and that is the honest answer. After Step-01 your project folder contains a virtual
environment and not much else.

```text
step01_my_project/
    .venv/          <- NOT in this folder, see below
    .gitignore
```

## Why there is no `.venv/` here

A virtual environment is never shared. Step-01 says it plainly: you commit the LIST of packages,
never the installed files. A `.venv` is also tied to the machine that made it, because it stores
full paths inside itself, so a copy made on a Mac is of no use on Windows.

Make your own instead. From inside this folder:

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

Your prompt then shows `(.venv)`. Step-02 starts a fresh folder of its own, `step02_my_project`.
