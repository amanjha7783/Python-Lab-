# Q.6. Suppose that a web browser maintains a list of recently visited pages. Assume that it can
# only store at most five pages which are recently (latest) visited by the user. If a page is
# revisited after some time, it only saves the newest visit, and it will store only distinct pages.
# The last page in the list is the newest visited one, the before last page visited after all its
# predecessors in the list and it is true for all other pages in the list. More specifically, the latest
# visit of a page in the list is after the latest visit of the its preceding pages in the list.
# Write a python program to implement the above protocol with an assumption that every page
# address is a positive integer. When you enter a negative page number, the program will not
# store the page number in the list and further, it prints the entries in the list and halts

history = []
while True:
    page = int(input("Enter the number of pages : "))
    if page < 0:
        break
    elif page in history:
        history.remove(page)
    history.append(page)
    if len(history)>5:
        history.pop(0)

print(f"Recently visited pages are {history}")    
