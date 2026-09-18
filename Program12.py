class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance! Withdrawal not allowed.")

    def display_balance(self):
        print("Balance:", self.balance)


# Example
account = BankAccount("John", "12345", 1000)

account.deposit(500)
account.withdraw(1200)
account.withdraw(500)
account.display_balance()
