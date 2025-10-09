class BankAccount:
    # Initialize the bank account with an optional initial balance
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Private attribute for encapsulation

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__account_balance:
            print("Insufficient funds! Withdrawal failed.")
            return False
        else:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount}")
            return True

    # Method to display the current balance
    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")      
