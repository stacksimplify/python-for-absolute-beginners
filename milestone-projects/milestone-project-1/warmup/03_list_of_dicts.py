"""
Warm-up 3: A List of Dictionaries (the In-Memory Data Model)

Write a program that stores several expenses as a list of dictionaries and then
reads them back one by one. Each expense is a dictionary with the same three keys
(description, amount, category), and the whole list is how the program remembers
every expense while it is running.

Task-1:
Build the data model: start with an empty list and use .append() to add a few
expense dictionaries to it.

Task-2:
Read the data model: use a for loop to visit each expense dictionary and print its
fields using key access.

Python concepts practiced:
1. Creating an empty list with [].
2. A dictionary as one record: key-value pairs (description, amount, category).
3. Adding a dictionary to a list with .append().
4. A list of dictionaries as a data model (many records held in one list).
5. len() to count how many records are in the list.
6. for loops to visit each dictionary in the list.
7. Dictionary access using keys, e.g. expense["amount"].
8. Local variables inside a loop.
9. f-strings to display the fields (the amount shown as money with ,.2f, the project's format).

Project connection:
This list of dictionaries IS the project's in-memory data model. It does not become
a single helper file. In the app, main.py creates the shared list with expenses = [],
the Add action (add_expense in f5_actions.py) grows it with
expenses.append({"description": ..., "amount": ..., "category": ...}), and every helper
(f2_format_row, f3_compute_total, f4_compute_by_category) plus the List action loop
over that same list with "for expense in expenses" and read fields like
expense["amount"]. So Task-1 is the shape of "add an expense" and Task-2 is the shape
of "list / total / group", the pattern the whole app is built on.
"""
# ===== Task-1: Build the Data Model (empty list + append) =====
# Start with an empty list, then append one dictionary per expense.
# This is exactly how main.py starts (expenses = []) and how the Add action grows it.
expenses = []
expenses.append({"description": "Coffee", "amount": 3.5, "category": "food"})
expenses.append({"description": "Bus", "amount": 2.0, "category": "transport"})
expenses.append({"description": "Lunch", "amount": 6.5, "category": "food"})

# Show that the list grew: count the records with len().
print(f"Stored {len(expenses)} expenses.")


# ===== Task-2: Read the Data Model (loop + key access) =====
# Visit each expense dictionary and read its fields with keys.
# This is the same loop shape the List action and the total/by-category helpers use.
# The amount is shown as money with ,.2f, exactly the format the project uses.
for expense in expenses:
    desc = expense["description"]
    cat = expense["category"]
    amt = expense["amount"]
    print(f"{desc} cost {amt:,.2f} ({cat})")
