# file open in read mode 

f = open("file.text","r")
text = f.read()
print(text)
f.close()

# file in append mode 
f = open("file.text", "a")
f.write("Hello, world!\n")
f.close()

with open('file.text','a') as f:
    f.write("Hey my name is aman jha \n")