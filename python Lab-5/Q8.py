# Q8) Write a program to accept nested lists as input, where the nested list is created by splitting the input.


# def accept_nested_lists():
#     nested_list = []
#     num_sublists = int(input("Enter the number of sublists: "))
    
#     for i in range(num_sublists):
#         sublist = input(f"Enter elements for sublist {i+1}, separated by spaces: ").split()
#         nested_list.append(sublist)
    
#     return nested_list

# # Example usage
# nested_list = accept_nested_lists()
# print("Nested List:", nested_list)


n = input("Enter the number of list added : ")
nested_list = []

for i in range(int(n)):
    x = input(f"Enter elements for sublist {i+1}, separated by spaces: ").split(",")
    nested_list.append(x)

print(nested_list)