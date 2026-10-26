'''
Write a program that accepts two positive integers a and b (a is smaller than b) and returns 
a list that contains all the odd numbers between a and b (including a and including b if 
applicable) in descending order. 
'''

odd = []
def odd_numbers(a, b):
    if(a>b):
        for i in range(b,a+1):
            if(i%2 != 0):
                odd.append(i)
                odd.sort(reverse=True)
    else:
        for i in range(a,b+1):
            if(i%2 != 0):
                odd.append(i)
                odd.sort(reverse=True)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
odd_numbers(a, b)
print(odd)

