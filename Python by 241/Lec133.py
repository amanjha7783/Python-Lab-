list1 = [True , False , 4,7,[4,'t',8], 'a',9,2,]

def num_to_string(l):
    return[str(i) for i in l if (type(i) == int or type(i) == float )] 

print(num_to_string(list1))

num = [1,2,3,4,5,6,7]
new_list = []
for i in num:
    if(i%2==0):
        new_list.append(i*2)
    else:
        new_list.append(-i)
print(new_list)