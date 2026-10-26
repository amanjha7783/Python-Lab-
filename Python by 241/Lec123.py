# def cube(n):
#     print(n**3)

# dic = dict.fromkeys(range(1,101), " ")

# for i in range(1,101):
#     dic[i] = [cube(i)]
# print(dic)

# # for i in range(1,101):
# #     dic.update({i : cube(i)})

# # print(dic)

def cube_finder(n):
    cubes = { }
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes
print(cube_finder(100))