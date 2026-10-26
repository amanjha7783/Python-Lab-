
'''
Q.5.
LetA=[["Brasil","Rio"],["India","NewDelhi"],["Srilanka","Colombo"],["Pakistan","Islamaba
d"],["Japan","Tokyo"]] be a list of countries with their capital cities. Now, read a country name
from the user. If the country name is presented in list A, then display that "the country is already
in the list". Otherwise, read the capital city of the country from the user and add both, country
along with its capital city to the list. Repeat the process for a couple of iterations and finally
print the updated list A.
Note that country names are not case sensitive i.e., India and india both are the same.
You can use upper () or lower () function to handle the above case.
'''

A=[["Brasil","Rio"],["India","NewDelhi"],["Srilanka","Colombo"],["Pakistan","Islamabad"],["Japan","Tokyo"]] 

while True:
    country_name = input("Enter the country name (or 'exit' to stop): ").lower()
    if country_name == 'exit':
        break
    for i in range(len(A)):
        if A[i][0].lower() == country_name:
            print(f"The country '{country_name}' is already in the list.")
            print(f"Capital of {country_name} is {A[i][1]}")
            break
    else:
        capital_name = input("Enter the capital name of {}: ")
        A.append([country_name, capital_name])
print(A)