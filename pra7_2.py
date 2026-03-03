# Create a Menu Driven program for showing details of a Bank Account by implementaing different functions for the following
# a) Display the current Balance
# b) Mechanism to Deposit an amount
# c) Mechanism to Withdraw an amount

class BankAccount:
    def __init__(self):
        self.balance = 0

    def display(self):
        print("Current Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn.")
        else:
            print("Insufficient Balance.")

account = BankAccount()

while True:
    print("\n1.Display  2.Deposit  3.Withdraw  4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 4:
        break
    elif ch == 1:
        account.display()
    elif ch == 2:
        amt = int(input("Enter amount: "))
        account.deposit(amt)
    elif ch == 3:
        amt = int(input("Enter amount: "))
        account.withdraw(amt)
    else:
        print("Invalid choice")