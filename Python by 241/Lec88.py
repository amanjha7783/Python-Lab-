fruit1 = ["mango", "Pineappel", "watermelon"]
fruit2 = ["mango", "Pineappel", "watermelon"]
fruit3 = ["mango", "Pineappel", "watermelon", "kiwi", "appel"]
print(fruit1 == fruit2) # checking the same value
print(fruit1 == fruit3)
print(fruit1 is fruit2) # checking the same object with same adress 

user_info = "harshit 420"
print(user_info.split(" "))
name, age = "Aman, 20".split(",")
print(name)
print(age)
x = ["boy", "34"]
print(",".join(x))