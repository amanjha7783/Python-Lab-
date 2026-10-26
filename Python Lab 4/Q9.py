# 9) Write a program that takes a list of words and sorts them by length in ascending order.

word_list = list(input("Enter the inputs for list 1 :").split(","))
print(word_list)

def sort_words_by_length(words):
    sorted_words = sorted(words, key=len)
    return sorted_words

sorted_list = sort_words_by_length(word_list)

print("Words sorted by length (ascending):")
print(sorted_list)


