"""
Warm-up 6: Keep Only the Matching Rows (Filter a List of Dicts)

Write a program that keeps only the expenses in a chosen category, using a list
comprehension. This is the "show one category" idea: pick a category, and get back
just the expenses that match it.

Task-1:
Filter the expenses down to one category with a list comprehension, then print the
matching rows.

Task-2:
Handle the "no matches" case: filter a category that has no expenses and show a
friendly message instead of an empty result.

Python concepts practiced:
1. A list of dictionaries as the data to filter.
2. A list comprehension with a condition: [expense for expense in items if ...].
3. Comparing a dictionary field to a value (expense["category"] == wanted_category).
4. Building a new, smaller list without changing the original.
5. Checking for an empty list with "if not matches".
6. for loops and dictionary key access to display the results.
7. f-strings and the project ,.2f money format.

Project connection:
This filtering is the "Show one category" menu option, the filter_by_category
action in f5_actions.py. There it reads the category from input() (.strip().lower()),
filters with the SAME list comprehension
[expense for expense in expenses if expense["category"] == wanted_category], shows
the same "No expenses in '...'." message when nothing matches, and prints each match
with format_row (the helper from warm-up 04). There is no new fN helper. The filtering
lives right inside the action.
"""
# A few expenses to filter.
expenses = [
    {"description": "Coffee", "amount": 3.5, "category": "food"},
    {"description": "Bus", "amount": 2.0, "category": "transport"},
    {"description": "Lunch", "amount": 6.5, "category": "food"},
]

# ===== Task-1: Filter to One Category (list comprehension) =====
# The app reads wanted_category from input() and lowercases it; here we set it directly.
# The list comprehension keeps only the expenses whose category matches.
wanted_category = "food"
matches = [
    expense
    for expense in expenses
    if expense["category"] == wanted_category
]
print(f"Expenses in '{wanted_category}':")
for expense in matches:
    # Show the category too, so you can see the filter kept only 'food'.
    # (The app prints each match with format_row from warm-up 04.)
    print(f"{expense['description']} ({expense['category']}): {expense['amount']:,.2f}")


# ===== Task-2: Handle the "No Matches" Case =====
# Filter a category that is not in the list. matches comes back empty, so we show the
# same friendly message the app's filter_by_category prints.
wanted_category = "travel"
matches = [
    expense
    for expense in expenses
    if expense["category"] == wanted_category
]
if not matches:
    print(f"No expenses in '{wanted_category}'.")
