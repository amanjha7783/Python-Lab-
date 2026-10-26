#  Raise an value error 

a = int(input("Enter any value between 5 and 9 : "))

if(a<5 or a>9):
    raise valueError("Vlaue should be between 5 and 9")

x = input(f"Enter the string : ")
if(x == "quit"):
    raise ValueError("value of string should be qiut")
    print("code is right")
else:
    print("code is wrong")
