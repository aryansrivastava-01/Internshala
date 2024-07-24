import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self):
        # Store expenses in a dictionary with the date as the key and a list of expense details as the value
        self.expenses = defaultdict(list)

    def add_expense(self, description, amount, category):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expenses[date].append({"description": description, "amount": amount, "category": category})
        print(f"Added expense: {description} - ${amount} in category '{category}' on {date}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for date, details in self.expenses.items():
            for info in details:
                print(f"Date: {date}, Description: {info['description']}, Amount: ${info['amount']}, Category: {info['category']}")

    def delete_expense(self, date, description):
        if date in self.expenses:
            self.expenses[date] = [exp for exp in self.expenses[date] if exp['description'] != description]
            if not self.expenses[date]:
                del self.expenses[date]
            print(f"Deleted expense '{description}' on {date}")
        else:
            print(f"No expense found on {date}")

    def summarize_monthly_expenses(self):
        monthly_summary = defaultdict(lambda: defaultdict(float))
        for date, details in self.expenses.items():
            month = date[:7]  # Extract the year-month part of the date
            for info in details:
                monthly_summary[month][info['category']] += info['amount']

        for month, categories in monthly_summary.items():
            print(f"Month: {month}")
            for category, total in categories.items():
                print(f"  Category: {category}, Total: ${total}")

    def run(self):
        while True:
            print("\nExpense Tracker")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Delete Expense")
            print("4. Summarize Monthly Expenses")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                description = input("Enter description: ")
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                self.add_expense(description, amount, category)
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                date = input("Enter date of expense to delete (YYYY-MM-DD HH:MM:SS): ")
                description = input("Enter description of expense to delete: ")
                self.delete_expense(date, description)
            elif choice == "4":
                self.summarize_monthly_expenses()
            elif choice == "5":
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
