#  in bulit functions

cities = {"tokoy", "delhi", "madrid", "berlin"}
cities2 = {"seoul", "tokoy", "madrid", "kabul"}
cities3 = cities.union(cities2)
print(cities3)
cities4 = cities.intersection(cities2)
print(cities4)
cities5 = cities.symmetric_difference(cities2)
print(cities5)
cities6 = cities.difference(cities2)
print(cities6)
print(cities.isdisjoint(cities2))  # False because both have common elements
print(cities.issuperset(cities2))  # False because cities does not contain all elements of cities2
print(cities.issubset(cities2))    # False because cities2 does not contain all elements of cities
cities.add("america")
print(cities)
cities.remove("tokoy")
print(cities)
item = cities.pop()
print(cities)
print(item)
s1 = {1,2,3,4,5}
s2 = {3,5,7,9}
print(s1,s2)
print(s1.union(s2))
s1.update(s2)
print(s1,s2)