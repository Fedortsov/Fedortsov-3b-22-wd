class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def replenishment(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

BankAccount1 = BankAccount("Николай", 9999999999999999, 1000000)
print(BankAccount1.balance)
BankAccount1.replenishment(100000)
print(BankAccount1.balance)
BankAccount1.withdraw(900000)
print(BankAccount1.balance)