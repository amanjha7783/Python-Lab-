#  find the factor of any number 

num = int(input("Enter the number is : "))
for i in range(1,num):
    if(num%i == 0 ):
        print(i, "is factor of  ", num)
        
