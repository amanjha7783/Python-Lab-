'''
1 - We can use ' ' ' to print 2 or more lines 
2 - we can use escape sequence character  \"  to print ( " )  in string 
3 - Programming language count numbers from 0 , for example:
Name = "Arsh" 

Print (Name[0])  ,then output is A
Print (Name[1])  ,then output is R
Print (Name[2])  ,then output is S
Print (Name[3])  ,then output is H

4 - We can Also use LOOP 
For Example , code - for character in Name: 
Print (character)
Output : A
               R
               S
               H

'''

name = "Aman"
friend = "Riya"
girlfriend = "Arpita"

text = '''          
hey Arpita ,
how are you ?
i am good , thanks
i am with my friend Riya
'''

print( "gf name ," + girlfriend)
print( "friend name, " + friend)
print(text)

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("lets use loop to print text ")
for character in text:
    print(character)
