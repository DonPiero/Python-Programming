class Account:
    def __init__(self, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def calculateInterest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, accountNumber, balance=0, interestRate=0.02):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate

    def calculateInterest(self):
        return self.balance * self.interestRate

class CheckingAccount(Account):
    def __init__(self, accountNumber, balance=0, overdraftLimit=100):
        super().__init__(accountNumber, balance)
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):
        if self.balance + self.overdraftLimit >= amount:
            self.balance -= amount
        else:
            print("Exceeds overdraft limit.")

savingsAccount = SavingsAccount("123", 100)
savingsAccount.deposit(50)
savingsAccount.withdraw(20)
interest = savingsAccount.calculateInterest()

checkingAccount = CheckingAccount("456", 50, overdraftLimit=200)
checkingAccount.deposit(30)
checkingAccount.withdraw(70)
checkingAccount.withdraw(10)

print(f"Savings Account Balance: {savingsAccount.balance}.")
print(f"Savings Account Interest: {interest}.")
print(f"Checking Account Balance: {checkingAccount.balance}.")
