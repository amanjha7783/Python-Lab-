# 2 swap two number 

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print(f"before swaping the number is a ={a} and b ={b}")
temp = b
b = a
a = temp
print(f"after swaping the number is a ={a} and b ={b}")


a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print(f"before swaping the number is a ={a} and b ={b}")
a = a+b
b = a - b
a = a - b
print(f"after swaping the number is a ={a} and b ={b}")