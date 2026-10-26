# use of break statement

n = int(input("enter the number : "))
for i in range(1, 15):
    if (i == 11):
        break
    print(n,"*", i, " = ", n * i)
print("you exist from loop ")

# use of continue statement 
n = int(input("enter the number : "))
for i in range(1, 11):
    if(i == 5):
        continue
    print(n,"*", i, " = ", n * i)
print("you exist from loop ")