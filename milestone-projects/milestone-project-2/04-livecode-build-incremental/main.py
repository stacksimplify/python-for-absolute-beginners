from f5_actions import (
    add_expense,
    list_expenses,
    show_total,
    show_by_category,
    filter_by_category,
)


def show_menu():
    print()
    print("==== Expense Tracker ====")
    print("1) Add expense")
    print("2) List expenses")
    print("3) Total spent")
    print("4) Spending by category")
    print("5) Show one category")
    print("6) Quit")


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


main()
