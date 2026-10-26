string = "she is a good singer and she is a good dancer"
print(string.replace("is", "was"))
print(string.replace(" ", "_" , 6))
print(string.find("is"))

is_pos = string.find("is")
print(string.find("is", is_pos+1))