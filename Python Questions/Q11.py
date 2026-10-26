#  check the number is positive negative and zero

def check_postive_negative_zero_number(n):
    num = int(input("Enter the number : "))
    if(num>0):
        print(num , "is positive number ")
    elif(num<0):
        print(num , "is negative number ")
    else:
        print(num, "is zero")

n = int(input("Enter the number of times to check :"))
num = int(input("Enter the number : "))
for i in range(1,n+1):
    check_postive_negative_zero_number(num)

# def check_positive_negative_zero_number():
#     num = int(input("Enter the number: "))
#     if num > 0:
#         print(num, "is a positive number")
#     elif num < 0:
#         print(num, "is a negative number")
#     else:
#         print(num, "is zero")

# def main():
#     n = int(input("Enter the number of times to check: "))
#     for i in range(n):
#         check_positive_negative_zero_number()

# if __name__ == "__main__":
#     main() 
