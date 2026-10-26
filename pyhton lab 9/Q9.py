'''
9. Write a class Calculator with methods for add, subtract, multiply, divide.
'''

class calculator:
    def __init__(self , num1 , num2):
        self.num1=num1
        self.num2=num2

    def addition(self):
        print(f"addition of two number is {self.num1 + self.num2}")

    def substraction(self):
        print(f"substraction of two number is {self.num1 - self.num2}")

    def multiply(self):
        print(f"multiply of two number is {self.num1 * self.num2}")
    
    def divide(self):
        print(f"Division of two number is {self.num1 / self.num2}")

x = calculator(50,10)
x.addition()
x.substraction()
x.multiply()
x.divide()