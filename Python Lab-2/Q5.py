'''
 Let a, b, and c are three distinct positive integers such that 
a < b < c. If a^2 + b^2 = c^2 (here ^ is used for power operator) then we say that (a, b, c) is a 
Pythagorean triplet. Write a Python program for the following problem. For any given positive 
integers a and b (a < b), check there exists any positive integer c such that (a, b, c) is a 
Pythagorean triplet. 
'''

def Pythagorean_triplet(a,b,c):
    if(a>b and a>c):
        if b**2 + c**2 == a**2:
            print("It is a Pythagorean triplet")
        else:
            print("It is not a Pythagorean triplet")
    if(b>c and b>a):
        if a**2 + c**2 == b**2:
            print("It is a Pythagorean triplet")
        else:
            print("It is not a Pythagorean triplet")
    if(c>a and c>b):
        if a**2 + b**2 == c**2:
            print("It is a Pythagorean triplet")
        else:
            print("It is not a Pythagorean triplet")

x = int(input("Enter the first side of the triangle : "))
y = int(input("Enter the second side of the triangle : "))
z = int(input("Enter the third side of the triangle : "))
check = Pythagorean_triplet(x,y,z)
print(check)  
