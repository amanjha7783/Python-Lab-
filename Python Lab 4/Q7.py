'''
7) Write a program that reads a paragraph from the user and counts the frequency of each word using a dictionary.

🔹 Example Input: "apple banana apple orange banana apple"
🔹 Output:{'apple': 3, 'banana': 2, 'orange': 1}
'''

x = input("Enter the words (comma-separated): ").split(",")
print(x)

def count_words(words):
    y = {}
    for i in words:
        if i in y:
            y[i] += 1
        else:
            y[i] = 1
    return y

info = count_words(x)
print(info)

