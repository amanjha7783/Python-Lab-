# List comprehension summary 
square = []
for i in range(1,11):
    square.append(i**2)
print(square)

square1 =[i**2 for i in range(1,11)]
print(square1)

odd = [i*2 for i in range(1,20) if i%2 != 0]
print(odd)

multiply = [i*2 if i%2 != 0 else i*3 for i in range(1,20)]
print(multiply)

nested_list = [[i for i in range(1,4)] for j in range(3)]
print(nested_list)