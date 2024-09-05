class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        return sum(income["amount"] for income in self.incomes)

    def total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"Account Holder: {self.firstname} {self.lastname}\n"
        info += f"Total Income: {self.total_income()}\n"
        info += f"Total Expense: {self.total_expense()}\n"
        info += f"Account Balance: {self.account_balance()}\n"
        return info


# Example usage:
account = PersonAccount("Neka", "Nekane")

account.add_income(5000, "Salary")
account.add_income(300, "Freelance")
account.add_expense(1500, "Rent")
account.add_expense(500, "Groceries")

print(account.account_info())
