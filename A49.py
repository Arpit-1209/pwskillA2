class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.check_balance())  # Output: 1500
account.withdraw(300)
print(account.check_balance())  # Output: 1200
