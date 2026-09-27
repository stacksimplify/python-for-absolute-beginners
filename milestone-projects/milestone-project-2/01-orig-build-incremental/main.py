"""main.py: the menu driver. This is your Milestone 1 file, edited.

Shows the menu, reads a choice, and calls the matching action, exactly as before.
What changed: it holds an ExpenseBook instead of a bare list, it loads the saved file
on start, and choice 6 saves before it quits.
"""
import json
from pathlib import Path

from expense_book import ExpenseBook
from f5_actions import (
    add_expense,
    list_expenses,
    show_total,
    show_by_category,
    filter_by_category,
)


def show_menu() -> None:
    print()
    print("==== Expense Tracker 2.0 ====")
    print("1) Add expense")
    print("2) List expenses")
    print("3) Total spent")
    print("4) Spending by category")
    print("5) Show one category")
    print("6) Save and quit")


def main() -> None:
    book = ExpenseBook(Path(__file__).parent / "data" / "expenses.json")

    # A missing file is normal on the first run; a corrupt one must not crash the app.
    try:
        book.load()
    except (json.JSONDecodeError, TypeError, KeyError):
        print("Warning: data file is corrupt; starting empty.")
        book.expenses = []

    while True:
        show_menu()
        choice = input("Choose 1-6: ").strip()
        if choice == "1":
            add_expense(book)
        elif choice == "2":
            list_expenses(book)
        elif choice == "3":
            show_total(book)
        elif choice == "4":
            show_by_category(book)
        elif choice == "5":
            filter_by_category(book)
        elif choice == "6":
            book.save()
            print("Saved. Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
