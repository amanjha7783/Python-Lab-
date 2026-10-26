#  private artibute and method are meant to be used only within
#  the class and are not accessible from outside the class.

class account :
    def __init__(self, account_no, password):
        self.account_no = account_no
        self.__password = password

    def reset_password(self): # public method to reset password 
        print(self.__password) # this will print the password

acc1 = account("12345" , "abcde")
print(acc1.account_no)
print(acc1.reset_password()) 
# print(acc1.__password)  # this will throw an error because it's private
# we don't have access to this variable 
# after the class due to encapsulation or private data in python