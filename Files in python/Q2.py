#  Replace a word from another words in file 

with open("pratice.txt","r") as f:
    data = f.read()
new_data = data.replace("java" , "python")
print(new_data)


