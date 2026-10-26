user = {
    'name' : 'John',
    'age' : 19,
    'fav_movie' : ['cocc', 'WallE', 'Inception'],
    'fav_book' : ['Harry Potter', 'Alchemist'],
}
#  How to add data
user['fav_song'] = ['Happy', 'Blue', 'Yellow']
print(user)

# How to remove(pop) data
user.pop('fav_book')
print(user)

# popitem () function
# It removes the last inserted item from the dictionary
poped_item = user.popitem()
print(user)
print(poped_item)

more_info = {
    'name' : 'Aman',
    'country' : 'USA',
    'city' : 'New York',
    'hobbies' : ['reading', 'swimming', 'cycling'],
}
#  How to update data
user.update(more_info)
user.update({'DOB' : '01-09-2005'})
print(user)
