import os

FILE_NAME = "expenses.txt"

def load_expenses():
    """Load expenses from file or return empty list."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    expenses = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 2:
            desc, amount = parts
            expenses.append({"desc": desc, "amount": float(amount)})
    return expenses


def save_expenses(expenses):
    """Save expenses to file."""
    with open(FILE_NAME, "w") as file:
        for e in expenses:
            file.write(f"{e['desc']},{e['amount']}\n")


def add_expense(expenses):
    """Add a new expense."""
    desc = input("Enter expense description: ")
    try:
        amount = float(input("Enter amount ($): "))
        expenses.append({"desc": desc, "amount": amount})
        save_expenses(expenses)
        print(f"✅ Added '{desc}' - ${amount:.2f}")
    except ValueError:
        print("⚠️ Please enter a valid number!")


def view_expenses(expenses):
    """View all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['desc']} - ${e['amount']:.2f}")
    print("----------------------")


def total_expenses(expenses):
    """Show total spending."""
    total = sum(e["amount"] for e in expenses)
    print(f"\n💵 Total spent: ${total:.2f}\n")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Simple Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expenses(expenses)
        elif choice == "4":
            print("👋 Goodbye! Your expenses are saved.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")
            

if __name__ == "__main__":
    main()
