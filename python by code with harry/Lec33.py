# dictonaries in python

dic = {
    'name' : "John",
    'age' : 30,
    'occupation' : "Engineer",
    'hobbies' : ["reading", "swimming", "coding"],
    'address' : "Bihar"
}
print(dic["name"])
print(dic.keys())
for key in dic.keys():
    print(dic[key])
for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")