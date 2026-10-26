'''
Write a class BankAccount with deposit and withdraw methods. Also show current
balance.
'''

class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposite(self,deposite):
        self.deposite = deposite
        print(f"after deposite your balance is {self.balance + self.deposite}")

    def withdraw(self,withdraw):
        self.withdraw = withdraw
        if(self.balance > self.withdraw):
            print(f"after withdraw balance is {self.balance - self.withdraw}")
        else:
            print("Insufficient balance")

account = BankAccount(10000)
print("Initial Balance: ",account.balance)
account.deposite(20000)
account.withdraw(5000)
