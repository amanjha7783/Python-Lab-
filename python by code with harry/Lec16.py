# import os
# print("Hello world from....")
# os.system("python --version")

#Match Case

x = int(input("Enter the number : " ))

match x:

    case 0 :
        print("X is Zreo")

    case 4 :
        print("X is Four")

    case _ if x % 2 == 0 :
        print("X is even")

    case _ if x % 2 != 0 :
        print("X is odd")

    case _ :
        print("X is not defined")

        