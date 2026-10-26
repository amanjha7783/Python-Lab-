for i in range(0,5):
    num = 1
    for j in range(i+1):
        print(num,end="")
        num = num + 1
    print()

a = "Python Programming"
l = []
for x in range(len(a)):  # Fill in the blank with "len(a)"
    l.append(a.count(a[x]))  # Fill in the blank with "a[x]" 
print(l)



