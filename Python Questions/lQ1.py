a = [2,4,10,20,5,20,4]
a = list(set(a))
print(a)

a = [2, 4, 10, 20, 5, 20, 4]
unique_list = []

for num in a:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)
