# Question for oops 

class Bank:
    
    def __init__(self, account_no, balance):
        self.account = account_no
        self.balance = balance
        # The Account class has two attributes: Account_no and balance. The __init__ method is used

    def debit(self):
        if(account_balance > debit_amount):
            self.debit = self.balance - debit_amount
            print("Debit successful")
            print(f"your balance amount after debit is {self.debit}")
        else:
            print("Insufficient balance")
    
    def cerdit(self):
        self.credit = self.balance + credit_amount
        print("credit successful")
        print(f"your balance amount after credit is {self.credit}")

account_number = input("Enter the account number: ")
account_balance = float(input("Enter the account balance: "))   
debit_amount = float(input("Enter the debit amount: "))
credit_amount = float(input("Enter the credit amount: "))


account1 = Bank(account_number, account_balance)
account1.debit()
account1.cerdit()
