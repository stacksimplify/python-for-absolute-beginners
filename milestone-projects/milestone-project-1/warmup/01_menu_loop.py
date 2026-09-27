"""
Warm-up 1: Build a Menu-Driven Program with Functions

Write a program that displays a menu, asks the user to choose an option,
and calls the corresponding function. For now, the functions are simple
stubs that print a message. Later, these stubs will be replaced with the
real expense tracker features.

Task-1:
Create a show_menu() function to display the Expense Tracker menu.

Task-2:
Create stub functions for each menu option. Each stub simply prints a
message so you can verify that the correct function is being called.

Task-3:
Create a main() function that runs the menu until the user quits, passing the
shared expenses list to whichever action they choose.

Python concepts practiced:
1. Defining and calling functions.
2. Passing arguments to functions.
3. Local variables.
4. while True loops.
5. if / elif / else decision making.
6. User input with input().
7. String method: .strip().
8. Lists (creating and passing a list between functions).
9. Program flow using a menu loop.
10. break to exit a loop.

Project connection:
This becomes the main menu loop for the Expense Tracker project. show_menu() and
main() are copied AS-IS into main.py; later the stub functions below are replaced
by the real implementations (imported from f5_actions.py) for adding, listing,
totaling, filtering, and summarizing expenses.
"""


# ===== Task-1: Create Menu Function =====
# Display the Expense Tracker menu.
def show_menu():
    print()
    print("==== Expense Tracker ====")
    print("1) Add expense")
    print("2) List expenses")
    print("3) Total spent")
    print("4) Spending by category")
    print("5) Show one category")
    print("6) Quit")


# Test the show_menu() function.
# show_menu()


# ===== Task-2: Create Stub Functions =====
# For now, each function simply prints a message so we can verify that the
# correct function is being called and that the expenses list is passed in.

def add_expense(expenses):
    print("\n--> Option 1 selected: Add Expense")
    print("Expenses:", expenses)


def list_expenses(expenses):
    print("\n--> Option 2 selected: List Expenses")
    print("Expenses:", expenses)


def show_total(expenses):
    print("\n--> Option 3 selected: Total Spent")
    print("Expenses:", expenses)


def show_by_category(expenses):
    print("\n--> Option 4 selected: Spending by Category")
    print("Expenses:", expenses)


def filter_by_category(expenses):
    print("\n--> Option 5 selected: Show One Category")
    print("Expenses:", expenses)


# Test the stub functions one at a time.
# add_expense([1, 2, 3])
# list_expenses([1, 2, 3])
# show_total([1, 2, 3])
# show_by_category([1, 2, 3])
# filter_by_category([1, 2, 3])


# ===== Task-3: Create the Main Menu Loop =====
# Create an empty expenses list, repeatedly show the menu, read the user's
# choice, call the appropriate function, and exit when the user chooses 6.
def main():
    expenses = []
    while True:
        show_menu()
        choice = input("Choose 1-6: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_by_category(expenses)
        elif choice == "5":
            filter_by_category(expenses)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")


# Start the Expense Tracker.
main()
