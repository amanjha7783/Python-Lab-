f = open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()
# this file type overwrite the previous data in the file