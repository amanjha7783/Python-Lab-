#  F-string in python

sentence = "My name is {} and I am from {} . "
name  = input("Enter your name : ", )
country = input("Enter your country : ", )
print(f"My name is {name} and I am from {country}.")
print(sentence.format(name , country))

print(f"we use F-string like this : My name name is {{name}} and I am from {{country}}.")
price = 49.099999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(f"{2*30}")
print(type(f"{2*30}"))

# sentence = "My name is {} and I am from {}."
# name = input("Enter your name: ")
# country = input("Enter your country: ")
# print(f"My name is {name} and I am from {country}.")
# print(sentence.format(name, country))

# print(f"We use F-string like this: My name is {{name}} and I am from {{country}}.")
# price = 49.099999
# txt = f"For only {price:.2f} dollars!"
# print(txt)
# print(f"{2*30}")
# print(type(f"{2*30}"))