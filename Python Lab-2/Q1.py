'''
Write a Python program to find the value of the following expression for the given values 
of X and N. Note that you must use single for-loop (no nesting loops are allowed) 
1 + X + X^2 / 2! + X^3/3! + ... + X^N/N! 
'''
def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)
    
def sum_of_series(n):
    sum = 0
    x = int(input("Enter the value of X : "))
    for i in range(0, n):
        sum += (x**i)/fact(i)
    return sum

n = int(input("Enetr the number n : "))
y = sum_of_series(n)
print(y)