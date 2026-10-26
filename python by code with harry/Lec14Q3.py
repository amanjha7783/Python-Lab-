# nested if - elif 

n = int(input("Enter your number : "))
if(n<0):
    print("Number is Negative")
elif(n>0):
    print("Number is Positive")
    if(n<10):
        print("Number lies between 0 - 10")
    elif(n>9 and n<=20):
        print("Nmuber lies between 10 - 21")
    else:
        print("Number is Greater than 20")
else:
    print("Number is Zero")
