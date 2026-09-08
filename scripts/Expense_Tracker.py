expenses = []

def add_expense(amount, category, description):
    """Add an expense to the expenses list.
    args: (amount: float, category: str, description: str)
    return: (dict: Expense dictionary)"""

    if not amount > 0:
        raise ValueError("Amount must be a positive number.")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    return expense

def calculate_total_expenses():
    """Calculate the total amount of expenses."""
    total = 0

    for expense in expenses:
        total += expense["amount"]
    return total

def calculate_total_by_category(category):
    """Calculate the total amount of expenses for a specific category."""

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]
    return total

def show_expenses():
    """Display all expenses in a formatted manner."""
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nAll Expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['category']} - "
            f"{expense['description']} : ${expense['amount']}"
        )

def run_tests() -> None:
    """
    Execute example expense scenarios.
    """
    try:
        add_expense(50, "Food", "Groceries")
        add_expense(20, "Transport", "Taxi")
        add_expense(100, "Food", "Restaurant")
        add_expense(0, "Entertainment", "Cinema")  # Invalid example
 
    except ValueError as error:
        print("Error:", error)
 
    print("\nTotal Expenses:", calculate_total_expenses())
    print("Total Food Expenses:", calculate_total_by_category("Food"))
 
    show_expenses()
 
 
if __name__ == "__main__":
    run_tests()
