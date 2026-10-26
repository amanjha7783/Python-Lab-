# #  program to check number is armstorng number is or not
num = int(input("Enter the number : "))
digits = str(num)
num_digits = len(digits)
temp = num
def armstrong(num):
    sum = 0
    for i in range(1,num_digits+1):
        remainder = (num)%10
        sum = sum + (remainder)**num_digits
        num = num//10
    return sum
sum = armstrong(num)
print(num)
if(temp == sum):
    print(num , "is armstrong number" )
else:
    print(num,"is not armstrong number" )

# second method 
def armstrong(num):
    digits = str(num)
    num_digits = len(digits)
    sum = 0
    temp = num
    for i in range(num_digits):
        remainder = temp % 10
        sum = sum + remainder ** num_digits
        temp = temp// 10
    return sum

num = int(input("Enter the number : "))
sum = armstrong(num)
print(f"The sum of the digits is: {sum}")
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")