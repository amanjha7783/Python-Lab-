'''
In the above problem (Q11), if the input is invalid (that is if n is negative number), then display 
the input is invalid and ask the user for the new input. Repeat the process until the user enters the correct 
input and then compute the value of the above mentioned expression.
'''
def facotial(n):
    if(n<=1):
        return 1
    else:
        return n*facotial(n-1)

def expression(n):
    sum = 1
    for i in range(n):
        sum = sum + (n**i)/facotial(i)
    print(sum)

while True:
        n = int(input("Enter the value of n: "))
        if n < 0:
            print("Invalid input. Please enter a non-negative integer.")
        else:
            expression(n)


    


