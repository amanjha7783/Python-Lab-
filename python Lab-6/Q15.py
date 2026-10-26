'''
15) Write a Python program using map() and lambda to concatenate corresponding
elements from two lists.
Input: ['Hello', 'Good'], ['World', 'Morning']
Output: ['HelloWorld', 'GoodMorning']
'''

list1 = ['Hello', 'Good']
list2 = ['World', 'Morning']


list3 = list(map(lambda x, y: x + y, list1, list2))
print(list3)