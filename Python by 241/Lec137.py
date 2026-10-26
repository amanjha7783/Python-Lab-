#  dictionaries compreshensive

dict = {i: i**2 for i in range(1, 11)}
print(dict)

string = 'ABHISHEK'
word_count = {char:string.count(char) for char in string}
print(word_count)

dict1 = {i:'even' if i%2==0 else 'odd' for i in range(1, 11)}
print(dict1)