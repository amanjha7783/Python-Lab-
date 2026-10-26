#  sets comprehension

set1 = {i**2 for i in range(1,11)}
print(set1)

set2 = ["mohit","aman", "rahul", "himanshu"]
name = {name[0] for name in set2}
print(name)