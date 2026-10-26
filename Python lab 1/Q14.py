'''
A banking company sends a 6-digit integer number as one-time password (OTP) to its customer 
mobile for all mobile banking transactions. An integer is a valid OTP if (1) it is of six-digit length and 
(2) contains the same number of even and odd digits. Further, the OTP does not start with 0. Write a 
python program to read an integer and verify whether it is a valid OTP or not.
'''
otp = int(input("Enter The OTP : "))
length_of_otp = len(str(otp))

def even_count(otp):
    even_count = 0
    for i in str(otp):
        if int(i) % 2 == 0:
            even_count += 1
    return even_count
    
def odd_count(otp):
    odd_count = 0
    for i in str(otp):
        if int(i) % 2 != 0:
            odd_count += 1
    return odd_count

if (length_of_otp == 6 and str(otp)[0] != '0' and even_count(otp) == odd_count(otp)):
    print("Valid OTP ")
else:
    print("Plz, enter valid OTP ")

