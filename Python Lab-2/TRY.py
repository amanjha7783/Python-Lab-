# Taking input from the user
n = int(input("Enter the number of rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")  
    print() 

for i in range(1, n ): 
    for j in range(n - i): 
        print("*", end=" ")
    print() 
