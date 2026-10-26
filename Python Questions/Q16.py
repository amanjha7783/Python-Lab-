#  programm to print all prime number between the intreval
        
            
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    """Print all prime numbers in a given interval."""
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')
    print()

# Input interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Prime numbers between {start} and {end}:")
print_primes_in_interval(start, end)
