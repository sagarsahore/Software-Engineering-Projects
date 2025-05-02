'''/*
### Problem 2: **Account Balance Management**

Create a class called `BankAccount` with the following:

- An `__init__` method that initializes the account holder's name and initial balance (which defaults to 0).
- A method `deposit(amount)` that adds the specified amount to the balance.
- A method `withdraw(amount)` that subtracts the specified amount from the balance (make sure balance doesn't go negative).
- A method `display_balance()` that shows the current balance.

Use `self` to ensure each instance has its own balance.

 */'''
# Bank Account Management System
class BankAccount:

    def __init__(self,name,balance):  # Constructor to initialize the number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):  # Deposit method : we use self to access object variables we are working with
        self.balance += amount
        print("deposited amount:", amount)
        print("New balance:", self.balance) # we used self.balance here because its not a local variable and is outside the method

    def withdraw(self, amount):  # Withdraw method
        if self.balance >= amount:
            self.balance -= amount
            print("withdrawn amount:", amount)
            print("New balance:", self.balance)

        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account holder:", self.name)
        print("Current balance:", self.balance)


Account1 = BankAccount("John", 1000)  # Create an instance of the BankAccount class

deposit_amount = float(input("Enter the amount to deposit: "))
Account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter the amount to withdraw: "))
Account1.withdraw(withdraw_amount)