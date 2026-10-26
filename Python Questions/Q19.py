#  program to print fibonacci number 

# Function to calculate Fibonacci numbers using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ask the user for the number of terms
num_terms = int(input("Enter the number of Fibonacci numbers to print: "))

if num_terms <= 0:
    print("Please enter a positive number.")
else:
    print(f"The first {num_terms} Fibonacci numbers are:")
    for i in range(num_terms):
        print(fibonacci(i), end=" ")
    print()
