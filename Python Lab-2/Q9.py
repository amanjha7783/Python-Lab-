'''
 Write a Python program to find the smallest consecutive prime numbers whose difference 
is at least k (k taken from user).
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def smallest_consecutive_primes(k):
    n = 2
    while True:
        if is_prime(n) and is_prime(n + k):
            return n, n + k
        n += 1

k = int(input("Enter the value of k: "))
print(smallest_consecutive_primes(k))