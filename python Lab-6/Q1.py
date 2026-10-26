'''
1) A number is a Disarium number if the sum of its digits, each raised to the power of their
respective positions, equals the number itself. Write a function to check whether a number is
Disarium or not.-> LIST
'''

n = list(input("Enter the number : "))
print(n)
temp = ''.join(n)  # Joining with space

sum = 0
for i in range(len(n)):
    sum = sum + int(n[i])**(i+1)

print(sum)
if(int(temp) == sum):
    print("Number is Disarium ")
else:
    print("Number is not Disarium")