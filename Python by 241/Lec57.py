name = input("Enter the name : ")
length = len(name)
i = 0
while i < length:
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1


name = input("Enter the name : ")
length = len(name)
for i in range(length):
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1

