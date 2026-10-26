# Filter function

def is_even(a):
    return a%2 == 0

number = [3,4,5,6,7,8,9]

evens = list(filter(is_even, number))
print(evens)

#  zip function

user_id = ['user1','user2','user3']
names = ['harshit','mohit','aman']
age = [23,45,67]
print(list(zip(user_id,names , age )))

#  direct convert into dict
example = [('a',1), ('b',2),('c',3)]
print(dict(example))