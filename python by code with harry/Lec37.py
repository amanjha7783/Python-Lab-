#  finally in python

def func():
    try:
        l = [5,6,7,8]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except IndexError:
        print("Index out of range")
        return 0
    finally:
        print("I am always printed")
x = func()
print(x)
