#  check the wornd persent in data or not 

word = input("Enter the word: ")
with open ("pratice.txt", "r") as f:
    data = f.read()
    if(data.find(word) == -1):
    # if(word in data):
        print("The word is not found in the file")
    else:
        print("The word is found in the file")