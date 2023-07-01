class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds.")

# Creating an instance of BankAccount
account1 = BankAccount("123456789", 1000)

# Accessing attributes using getter methods
print(account1.get_account_number())  # Output: 123456789
print(account1.get_balance())         # Output: 1000

# Depositing and withdrawing funds
account1.deposit(500)
print(account1.get_balance())         # Output: 1500

account1.withdraw(2000)                # Output: Insufficient funds.
print(account1.get_balance())         # Output: 1500 (balance remains the same)
