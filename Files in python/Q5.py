count = 0
with open ("number.txt","r") as f:
    data = f.read()
    print(data)

    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]

    num = data.split(",")
    for i in  num:
        if(int(i)%2 == 0): 
            count += 1
print(count, "even number persent in my data")