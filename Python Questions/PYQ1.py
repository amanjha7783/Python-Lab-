# Write a python program to check if any no from following list is factorial of 
# particular no if yes than display that no with its factorial. 
 
# L1=[370,471,5040, 1020,362880,593456, 10456839] 


def find_fact(n):
    i = 1
    while True:
        fact = 1
        for j in range(1,i+1):
            fact *= j
            if fact == n:
                return True
            elif fact > n:
                return False
        i += 1

L1=[370,471,5040, 1020,362880,593456, 10456839]
for i in range(len(L1)):
    if find_fact(L1[i]):
        print(f"{L1[i]} is a factorial number ")
    else:
        print(f"{L1[i]} is not a factorial number ")

