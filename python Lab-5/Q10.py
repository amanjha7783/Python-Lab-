
# Q10) Write a program to find the index (location) of an element in a list.


input_list = [10, 20, 30, 40, 50]
find_element = int(input("Enter the element to find: "))

try:
    index = input_list.index(find_element)
    print(f"Element {find_element} found at index {index}")
except ValueError:
    print(f"Element {find_element} not found in the list")