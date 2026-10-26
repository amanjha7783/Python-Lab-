user = { }
n = input("Enter your name : ")
a = input("Enter your age : ")
fm = input("Enter your fav movie : ").split(",")
fs = input("Enter your fav song : ").split(",")
user['name'] = n
user['age'] = a
user['fav_movie'] = fm
user['fav_song'] = fs

for key,value in user.items():
    print(f"{key} : {value}")