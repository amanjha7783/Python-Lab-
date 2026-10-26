#  use of fromkeys in dictanories

d = dict.fromkeys(['name' , 'age' , 'city'], 'unknown')
print(d)

x = dict.fromkeys('abc', 'unknown')
print(x)

v = dict.fromkeys(range(1,11), 'unknown')
print(v)

#  why and how use get method in dictionaries
user = {
    'name' : 'Aman',
    'city' : 'Begusarai',
}
print(user.get('name')) #  print the value of key 'name'
print(user.get('names')) # returns None for non-existent key
print(user.get('names', 'Not found')) # returns None for non-existent key

#  use of clear method in dictionaries
d.clear()
print(d)

# copy method in dictionaries
user_info = user.copy()
print(user_info)

print(user is user_info)
print(user == user_info)