#  find the word in which line 

word = input("Enter the word: ")
data = True
line_no = 1
try:
    with open("pratice.txt", "r") as f:
        for line in f:
            if word in line:
                print(line_no)
                break
            line_no += 1
        else:
            print(-1)
except FileNotFoundError:
    print("File not found")