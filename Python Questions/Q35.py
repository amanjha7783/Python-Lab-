#  remove any punctuations from string 

punc = '''+*/-{}[]""?/.<>,;:()&%$3@!^~=_#'''

String = input("Enter anything : ")
empty_str = ""

for i in String:
    if i not in punc:
        empty_str += i

print(empty_str)

# second method 

def remove_punctuations(input_string):
    punc = '''+*/-{}[]""?/.<>,;:()&%$3@!^~#_='''
    translator = str.maketrans('', '', punc)
    return input_string.translate(translator)

String = input("Enter anything : ")
print(remove_punctuations(String))