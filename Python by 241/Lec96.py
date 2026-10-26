# Q1) first question
print("first question")
list = []
for i in range(10):
    list.append(i**2)

print(list)

#  Q2) second question
print("second question")
def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        pooped_item = l.pop()
        r_list.append(pooped_item)
    return r_list   
print(reverse_list([1, 2, 3, 4, 5]))

# Q3) third question
print("third question")
def reverse_list1(l):
    r_list = []
    for i in l:
        r_list.append(i[::-1])
    return r_list   
word = ["abc", "xyz","tuv"]
print(reverse_list1(word))

# Q4) fourth question
print("fourth question")
a = [1,2,3,4,5,6,7,8,9]
b = []
c = []
for i in range(len(a)):
    if (a[i]%2==0):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)
a = [c] + [b]
print(a)

# Q5) fifth question
print("fifth question")
x = [1,2,3,4,5,6,7]
y = [3,5,7,0,9,8,6]
z = []
def common_findder(x,y):
    for i in x:
        if i in y:
            z.append(i)
    return z
print(common_findder(x,y))
