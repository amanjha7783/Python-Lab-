'''
 Write a program to implement the following problem. 
A valid password is a string which satisfies the following properties. 
(i) The password should be of at least eight characters. 
(ii) It is a combination of alphabets, numeric digits 0 to 9, and special characters '_','@', '#', and 
'*'. No other character is allowed. 
(iii) It should contain one capital alphabet, one special character from ('_','@', '#','*'), and one 
numeric digit from 0 to 9. 
You read a password from the user and verify if it is valid or not. If yes, then display 
"WELCOME" message, otherwise ask the user to re-try with a new password. A user will have 
at most 5 chances to enter his/her password. Once the limit exceeds, the program should 
terminate.
'''

def is_valid_password(password):
    
    if len(password) <= 8:
        return False

    has_upper = False
    has_special = False
    has_digit = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():  
            has_upper = True
        elif 32 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126:
            has_special = True 
    return has_upper and has_special and has_digit

max_attempts = 5

for attempt in range(max_attempts):
    password = input("Enter your password: ")

    if is_valid_password(password):
        print("WELCOME")
        break 
    else:
        remaining_attempts = max_attempts - (attempt + 1)
        if remaining_attempts > 0:
            print(f"Invalid password! You have {remaining_attempts} attempt(s) left.")
            print("- Password must be more than 8 characters")
            print("- Must contain at least one uppercase letter")
            print("- Must contain at least one special character (@, #, $, etc.)")
            print("- Must contain at least one digit (0-9)")
        else:
            print("Too many failed attempts! Access Denied.")
