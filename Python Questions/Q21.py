#  find the sum of n number 

num = int(input("Enter the number : "))
sum = 0
for i in range(1,num+1):
    sum = sum + i

print(f"sum of {num} natural numbers is {sum}")