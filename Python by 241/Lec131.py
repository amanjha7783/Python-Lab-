def reverse_string(l):
    return [name[::-1] for name in l]
print(reverse_string(["hello", "world"]))

def reverse_string1(n):
    new_list = []
    for name in n:
        new_list.append(name[::-1])
    return new_list
print(reverse_string1(["hello", "world"]))

number = list(range(1,21))
for i in range(len(number)):
    if(i%2 != 0):
        number.remove(i)
print(number)

even_nums = [i for i in number if i%2 == 0]
print(even_nums)