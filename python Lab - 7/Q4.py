# Q4) Write a lambda function to check whether a given number is prime or composite.


number = int(input("Enter the number : "))
x = lambda x : "prime" if x > 1 and all(x % i != 0 for i in range(2, x)) else "not prime"
print(x(number))