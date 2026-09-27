# `step05_my_project2` as it looks in Step-05

One file. That is the whole point.

```text
step05_my_project2/
    report.py
```

`report.py` imports `number_utils` and uses it, and there is no `number_utils/` folder anywhere near
it. That works because Step-05 installed your package into the virtual environment with
`pip install -e .`, so it is available to anything running in that environment, exactly the way
`requests` is.

## Run it

There is no `.venv` in here either, and there should not be. This folder borrows the environment
that lives in `step05_my_project`. So activate THAT one, then come back:

=== "macOS / Linux"

    ```bash
    cd ../step05_my_project
    source .venv/bin/activate
    pip install -e .

    cd ../step05_my_project2
    python report.py
    ```

=== "Windows"

    ```powershell
    cd ..\step05_my_project
    .venv\Scripts\Activate.ps1
    pip install -e .

    cd ..\step05_my_project2
    python report.py
    ```

```text
Double the price: 50
10 percent of 30: 3.0
```

Now edit `step05_my_project/number_utils/calculations.py` so `double` returns `n * 3`, save, and
run `python report.py` again without reinstalling anything. It prints `75`. That is what the `-e`
in `pip install -e .` buys you.
