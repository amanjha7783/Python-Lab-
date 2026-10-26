with open("sample","w") as f:
    f.write("Hello world")
    f.truncate(5)

with open("sample","r") as f:
    print(f.read())