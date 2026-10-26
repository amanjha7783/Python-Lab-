class Number:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate_average(self):
        average = (self.num1 + self.num2) / 2
        return average

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

n1 = Number(num1, num2)
average = n1.calculate_average()
print(f"Average of two numbers is {average}")


