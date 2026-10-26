str1 = "AbcDEfghIJ"
print(str1.upper()) 

str1 = "AbcDEfghIJ"
print(str1.lower())

str2 = " Silver Spoon " 
print(str2.strip) # remove leading and trailing whitespaces

str3 = "Hello !!!"
print(str3.rstrip("!")) # remove trailing whitespaces

str2 = "Silver Spoon"
print(str2.replace("Sp", "M")) 

str2 = "Silver Spoon"
print(str2.replace("Silver", "Gold"))

str2 = "silver spoon"
print(str2.split(" ")) # split string into list of words 

str1 = "hello"
capStr1 = str1.capitalize() # capitalize first letter of string
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize() 
print(capStr2)

str1 = "Welcome to the Console!!!"
print(str1.center(50)) # center string in a given width

str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))

str = "aman jha"
print(str.count("a")) 

str = "aman jha"
print(str.endswith("jha"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) # find first occurrence of a substring

str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

str = "aman jha is a good boy"
print(str.index("good")) # find first occurrence of a substring

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # check if string contains only alphanumeric characters

str1 = "Welcome"
print(str1.isalpha()) # check if string contains only alphabets

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper()) # check if string contains only uppercase letters

str1 = "hello world"
print(str1.islower())

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) # swap case of string

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title()) # convert first character of each word to uppercase

str1 = "World Health Organization" 
print(str1.istitle()) # check if string contains title case