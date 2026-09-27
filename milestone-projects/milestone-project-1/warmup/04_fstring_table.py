"""
Warm-up 4: Format Table Rows with f-String Format Specifiers

Write a program that displays expense data in neatly aligned columns using
f-string format specifiers. Learn how to left-align text, right-align numbers,
and format amounts with commas and two decimal places.

Task-1:
Create a helper function named format_row() that formats and returns a single
expense as one aligned table row.

Task-2:
Store multiple expenses in a list of dictionaries. Use a for loop to call
format_row() for each expense and display a complete table.

Python concepts practiced:
1. Dictionary access using keys.
2. Local variables inside a function.
3. Functions that return formatted strings.
4. f-strings for string formatting.
5. Format specifiers:
   - < for left alignment.
   - > for right alignment.
   - Width values (20, 14, 10) to align columns.
   - ,.2f to display numbers with thousands separators and two decimal places.
6. Lists containing dictionaries.
7. for loops to process multiple expenses.
8. Calling a function inside print().
9. Printing a table header and formatted rows.

Project connection:
The format_row() helper function becomes f2_format_row.py in the project.
It is used to display expense records in a clean, readable table whenever
the user views their expenses.
"""
# ===== Task-1: Format a Single Expense Row =====
# Extract the description, category, and amount from the expense dictionary.
# Return them as one neatly aligned table row using f-string format specifiers.
def format_row(expense):
    """Return one aligned table row for an expense."""
    desc = expense["description"]
    cat = expense["category"]
    amt = expense["amount"]
    return f"{desc:<20} {cat:<14} {amt:>10,.2f}"


# A single expense for testing.
expense1 = {
    "description": "Coffee",
    "category": "food",
    "amount": 3.50
}

# Print the table header.
print(f"{'Description':<20} {'Category':<14} {'Amount':>10}")

# Call the function to format and print one expense.
print(format_row(expense1))


# ===== Task-2: Format Multiple Expense Rows =====
# Store multiple expenses in a list of dictionaries.
expenses = [
    {"description": "Coffee", "category": "food", "amount": 3.50},
    {"description": "Bus Pass", "category": "transport", "amount": 25.00},
    {"description": "Movie Ticket", "category": "entertainment", "amount": 350.00},
    # A large amount so the ,.2f thousands comma actually shows: 1,250.00
    {"description": "Laptop", "category": "electronics", "amount": 1250.00},
]

# Print the table header.
print(f"{'Description':<20} {'Category':<14} {'Amount':>10}")

# Call the function for each expense and print the formatted table row.
for expense in expenses:
    print(format_row(expense))
