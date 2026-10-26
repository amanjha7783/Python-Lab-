# Q3 ) Write a lambda function to check whether a given number is even or odd.

number = int(input("Enter the number : "))

x = lambda x: "Even" if x % 2 == 0 else "Odd"
print(x(number))
