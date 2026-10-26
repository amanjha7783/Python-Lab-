# for loop with else in python 

for i in range(5):
    print(i)
else:
    print("This is the else block")
print(1)
for i in []:
    print(i)
else:
    print("This is the else block")
print(2)
for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("This is the else block")
print(3)