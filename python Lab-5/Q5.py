# Q5) Write a program to remove all punctuation from a given string.

Given_string = input("Enter the string : ")

for i in Given_string:
    if(ord(i)>= 33 and ord(i)<= 47) or (ord(i)>= 58 and ord(i)<= 64) or (ord(i)>= 91 and ord(i)<= 96) or (ord(i)>=123 and ord(i)<= 126):
        Given_string = Given_string.replace(i, " ")
        
print(Given_string)