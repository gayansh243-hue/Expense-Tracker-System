from datetime import datetime
from expensemanager import ExpenseManager
from report import show_summary, show_overall_summary, show_category_summary


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def get_date(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if not value and not required:
            return None
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return value
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD (e.g. 2026-09-30).")


def print_expenses(expenses, all_expenses):
    if not expenses:
        print("No expenses found.")
        return
    for expense in expenses:
        # show the real index so it can be used for deleting
        print(f"[{all_expenses.index(expense)}] {expense}")


def main():
    manager = ExpenseManager()

    while True:
        print("\n========== EXPENSE TRACKER MANAGEMENT SYSTEM ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Delete Expense")
        print("5. Show Expense Summary")
        print("6. Show Category Report")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            amount = get_amount()
            category = input("Enter category: ").strip()
            description = input("Enter description: ").strip()
            date = get_date("Enter date (YYYY-MM-DD): ")
            manager.add_expense(amount, category, description, date)
            print("Expense added and saved.")

        elif choice == '2':
            expenses = manager.view_expenses()
            print_expenses(expenses, expenses)

        elif choice == '3':
            category = input("Category (leave blank for all): ").strip()
            start = get_date("Start date (YYYY-MM-DD, blank for none): ", required=False)
            end = get_date("End date (YYYY-MM-DD, blank for none): ", required=False)
            results = manager.search_expenses(category or None, start, end)
            print_expenses(results, manager.view_expenses())

        elif choice == '4':
            expenses = manager.view_expenses()
            if not expenses:
                print("No expenses to delete.")
                continue
            print_expenses(expenses, expenses)
            try:
                index = int(input("Enter the index of the expense to delete: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if manager.delete_expense(index):
                print("Expense deleted and saved.")
            else:
                print("Invalid index.")

        elif choice == '5':
            expenses = manager.view_expenses()
            if not expenses:
                print("No expenses recorded yet.")
                continue
            total, average = show_overall_summary(expenses)
            print(f"Total spending: {total:.2f}")
            print(f"Average per expense: {average:.2f}")
            print("\nBy category:")
            for category, amount in show_summary(expenses).items():
                print(f"  {category}: {amount:.2f}")

        elif choice == '6':
            category = input("Enter category to summarize: ").strip()
            total = show_category_summary(manager.view_expenses(), category)
            print(f"Total amount spent in category '{category}': {total:.2f}")

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()