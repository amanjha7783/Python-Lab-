odd_list = []
even_list = []

company_list = [4,8,3,6,987,67,54]

for i in company_list:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)

print(even_list)
print(odd_list)

result1 = list(filter(lambda x: x%2==0, company_list))
result2 = list(filter(lambda x: x%2!=0, company_list))
print(result1)
print(result2)

p = [2,3,6,5]
sum = 0 
for i in p:
    sum = i*i + sum 
print(sum)
