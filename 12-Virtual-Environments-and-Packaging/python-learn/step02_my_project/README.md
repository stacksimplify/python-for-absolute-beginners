# `step02_my_project` as it looks after Step-02

Use this to check your own folder if something does not match the lesson.

## What is here

```text
step02_my_project/
    .venv/              <- NOT in this folder, see below
    requirements.txt    <- written by pip freeze
```

`requirements.txt` is the whole point of Step-02: the exact list of what was installed, written by
`pip freeze`. Open it. It is a plain text file, five lines long.

## Rebuild the environment from it

There is no `.venv/` here, on purpose: you share the LIST, not the installed files. That is exactly
what this file is for, so use it. From inside this folder:

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

=== "Windows"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    ```

Run `pip list` afterwards and you will see the same five packages. Your version numbers may be
newer than the ones pinned here, which is normal and fine.
