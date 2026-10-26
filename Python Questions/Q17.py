#  find the factorial of number
#   
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact *= i

print("factorial of ", n, "is", fact)

#  find the factorial of number using recursion
n = int(input("Enter a number: "))
def factorial(n):
    if (n == 1 ):
        return 1
    return n*factorial(n-1)

fact = factorial(n)
print("factorial of ", n, "is", fact)