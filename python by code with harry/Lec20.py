# function in python

def claculateGmean(a , b):
    mean = (a*b)/(a+b)
    print(mean)

def greater(a,b):
    if a > b:
        print(a,"is greater than ",b)
    else:
        print(b,"is greater than ",a)

for i in range(0,4):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    claculateGmean(x,y)
    greater(x,y)




