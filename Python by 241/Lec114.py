user = {
    'name' : 'John',
    'age' : 30,
    'city' : 'New York',
    'country' : 'USA',
    'fav_movie' : ['pokemon', 'powerrangers', 'dragonball'],
    'is_married' : False
    }
# Accessing values in the dictionary
print(user)
print(user['fav_movie'])

if 'name' in user:
    print("user in the dictionary")
else:
    print("user not in the dictionary")

if 'USA' in user.values():
    print("USA in the dictionary")
else:
    print("USA not in the dictionary")

for i in user:
    print(i) 

for i in user.values():
    print(i)


user_key = user.keys()
print(user_key)
user_value = user.values()
print(user_value)
user_item = user.items()
print(user_item)
for i , j in user.items():
    print(f"key is {i} and value is {j}")