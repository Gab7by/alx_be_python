
class BankAccount:
    """
    A simple BankAccount class that encapsulates
    deposit, withdrawal, and balance display operations.
    """

    def __init__(self, initial_balance=0):
        # Encapsulated (private) attribute
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the specified amount from the account balance
        if sufficient funds exist.
        Returns True if successful, otherwise False.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
