import csv
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def __str__(self):
        return f"Category:{self.category}, Amount: Rs.{self.amount}"

class ExpenseTracker:
    def __init__(self, file_path):
        self.expenses = []
        self.file_path = file_path
        # self.category = category
        # self.amount = amount


    def load_add_expense(self):
        df = pd.read_csv(self.file_path)
        for index, row in df.iterrows():
            expense = Expense(row['Category'], row['Amount'])
            self.expenses.append(expense)

    def total_spent(self):
        total_amount = 0
        for expense in self.expenses:
            total_amount += expense.amount
        return total_amount

    def get_expense(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.expenses):
                return self.expenses[index]
            else:
                return None

    def add(self):
        try:
            category = input("Enter the category: ")
            amount = float(input("Enter the amount spent: Rs."))
            new_expense = Expense(category, amount)
            self.expenses.append(new_expense)  # Add new expense
            #not needed: self.load_add_expense() Loads and adds all the expenses to already existing list
            print("Expense added successfully.")
        except ValueError:
            print("Invalid input. Amount must be a number.")

    def delete(self, index):
        if isinstance(index, int):
            if 0 <= index < len(self.expenses):
                deleted_expense = self.expenses.pop(index)
                print(f"Deleted expense: {deleted_expense}")
            else:
                print("Invalid index. Please enter a valid index.")
        else:
            print("Invalid input. Please enter a valid integer.")


    def update(self, index, category, amount):
        if isinstance(index, int):
            if 0 <= index < len(self.expenses):
                self.expenses[index].category = category
                self.expenses[index].amount = amount
                print(f"Expense at index {index} updated successfully.")
            else:
                print("Invalid index. Please enter a valid index.")
        else:
            print("Invalid input. Please enter a valid integer.")

    def display_expenses(self):
        df = pd.read_csv(self.file_path)
        for index, row in df.iterrows():
            print(f"Index {index}: {row["Category"]}, {row["Amount"]}")


    def save_to_csv(self, file_path):
        data = {'Category': [expense.category for expense in self.expenses],
                'Amount': [expense.amount for expense in self.expenses]}
        df = pd.DataFrame(data)
        df.to_csv(file_path)


# df = pd.read_csv('Expense.csv')
# features = df.columns
# print(features)

# Instance of ExpenseTracker
csv_file = 'Expense.csv'
tracker = ExpenseTracker(file_path=csv_file)

tracker.load_add_expense()

while True:
    print("Menu:")
    print("1. Get data")
    print("2. Add data")
    print("3. Delete data")
    print("4. View updated data")
    print("5. Exit")

    choice = input("Enter your choice: ")
    if int(choice) == 1:
        try:
            index = input("Enter the index of the expense you want to view (enter \"q\" to exit): ")
            if index == "q":
                print("Exiting the program.")
                break
            index = int(index)
            expense = tracker.get_expense(index)
            if 0 <= index < len(tracker.expenses):
                print(f"Expense at index {index}: {expense}")

            else:
                print("Invalid index. Please enter a valid index.")

        except ValueError:
            (
                print("Invalid input. Please enter a valid integer."))
    elif choice == "2":
        tracker.add()
        tracker.save_to_csv(csv_file)

    elif choice == "3":
        index_to_delete = int(input("Enter the index of the expense to delete: "))
        tracker.delete(index_to_delete)
        tracker.save_to_csv(csv_file)

    elif choice == "4":
        print("Updated expenses:")
        tracker.display_expenses()
        total_spent = tracker.total_spent()
        print(f"Total amount spent: Rs.{total_spent}")

    elif choice == "5":
        exit()

    else:
        ValueError: (
            print("Invalid input. Please enter a valid integer."))



# # Plot
# plt.figure(figsize=(10, 5))
# plt.title('Distribution of Expenses by Category')
# data = pd.read_csv("Expense.csv")
# df = pd.DataFrame(data=data)
# sns.barplot(x=df['Category'], y=df["Amount"], color = "SteelBlue")
# plt.xlabel('Expense Category')
# plt.ylabel('Total Amount Spent')
# plt.tight_layout()
# plt.show()


