'''
 Write a Python program to print the numbers between 1 and N (input from the user) which 
are divisible by 2 or 3. Further, count all such numbers which are divisible by 2 or 3. 
'''

def check(n):
    count = 0
    for i in range(1, n + 1):
        if(i%2==0 or i%3==0):
            count += 1
            print(i, end=" ")
    print(f"\n{count} numbers are divisible by 2 or 3")

n = int(input("Enter a number: "))
check(n)  