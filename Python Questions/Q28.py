#  Make a simple calculator

print("----Calculator----")
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print("What you want to do")
print("1.Addition","2.substraction","#.Multiplication" , "4.Division")
x = int(input("choose one thing : "))
if(x>=1 and x<=4):
    match x:
        case 1:
            print(f"{a} + {b} = {a+b}")
        case 2:
            print(f"{a} - {b} = {a-b}")
        case 3:
            print(f"{a} * {b} = {a*b}")
        case 4:
            print(f"{a} / {b} = {a/b}")

