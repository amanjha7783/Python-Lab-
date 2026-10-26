#  WAP to check whether an entered character is lowercase (a to z) or uppercase (A to Z).  Hint-use 
# ASCII value


char = input("Enter the character : ")
print("The Ascii value of" , char , "is ", ord(char) )

if(ord(char) >=65 and ord(char) <=90):
    print(f"{char} is a upper-case")
elif(ord(char) >= 97 and ord(char) <=122):
    print(f"{char} is a Lower-case")
else:
    print("it is not in (a-z) and (A-Z) character ")