# Step-11 folder: the `rich` package, already wired in

These files are the finished Step-11 tracker. The code is the same as
`../02-orig-build-incremental-with-rich/`, with the long docstrings removed so it is easy to read.

In `f5_actions.py` the Step-10 lines are kept as comments marked `before Step-11`, right above the new
ones marked `after Step-11`. That is the whole change the package brought: one import, and one line in
each of the two actions that print to the screen. Your own Steps 01 to 10 folder,
`../04-livecode-build-incremental/`, is not touched.

Make the environment here, install the package, and run it:

```bash title="Run Step-11 here"
cd 05-livecode-build-incremental-with-rich
python3 -m venv .venv
source .venv/bin/activate
pip install rich
python3 main.py
```

To type the change yourself, put the commented lines back and delete the `Console().print(...)` line
under each of them.
