# Write a program to count the number of vowels and consonants in a given string.

x = ["A","I","E","O","U","a","i","e","o","u"]
n = input("Enter the word :")

count_v= 0 
count_c= 0 
for i in range(len(n)):
    if(n[i] in x):
        count_v += 1
    else:
        count_c += 1
    
print(f"{count_v} vowels and {count_c} consonants in this word")


