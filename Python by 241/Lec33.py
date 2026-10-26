name = "      Aman      "
name1 = "      Am      an      "
dot = "............"
print(name+dot)
print(name.lstrip()+dot) # remove leading spaces
print(name.rstrip()+dot) # remove trailing spaces
print(name.strip()+dot) # remove leading and trailing spaces
print(name1.replace(" ", "")+dot)
name2 , char = input("Enter the name and a character :").split(",")
print(f"character count : {name2.strip().lower().count(char.strip().lower())}")