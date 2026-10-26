#  Recursion in python 
#  find factorial of a number using recursion
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))


#  find fibonacci number using recursion

def fibo(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)
    
print(fibo(8))

#  find fibonacci series  using recursion

def fibonacci(n):
    # Base case: return n if n is 0 or 1
    if n <= 1:
        return n
    else:
        # Recursive case: return the sum of the two preceding numbers
        return fibonacci(n-1) + fibonacci(n-2)

# Number of terms in the Fibonacci series
terms = 10

# Print the Fibonacci series
for i in range(terms):
    print(fibonacci(i), end=' ') 