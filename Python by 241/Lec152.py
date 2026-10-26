string = ['mohit', 'aman','gopal','himanshu','harshit']
pos = 0
for name in string:
    print(f"{pos}-----> {name}")
    pos += 1

for pos,name in enumerate(string):
    print(f"{pos}-----> {name}")

def pos(l,target):
    for pos , string in enumerate(l):
        if  string == target:
            return pos
        return -1
        
print(pos(string,'himanshu'))