#  read() , readline(), writeline()

f = open("file.text","r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)