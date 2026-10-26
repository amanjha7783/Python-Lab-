'''
A foreign exchange company in Vadodara provides two kinds of services, conversion of Indian 
rupee to US dollar and vice versa, to its customers. 
The charges for conversion of Indian rupee to US dollars is as follows. 
(1) INR 250/- standard chares for every transaction. 
(2) 1 INR = 0.0141 USD 
(3) For the first INR 10,000/- rupees no extra charges will be collected, and after that for every INR 1 
to INR 10,000, Rs 150/- will be collected as additional conversion charges. 
(4) The minimum conversion is INR 1,000/-. 
Note that you need to deduct the charges from the amount before converting into USD. 
The conversion charges from US dollar to INR are as follows: 
(1) The minimum conversion is 30 USD. 
(2) INR 400/- standard charges for every transaction. 
(3) 1 USD = 70.8305 INR 
(4) For the first 50 USD, there are no extra conversion charges, after that for every 1 USD to 50 USD, 
Rs 300/- will be collected as additional conversion charges. 
Note that the customer will get the INR after deduction of charges from the amount that he gets (i.e., 
amount in USD * 70.8305 - charges). 
Write a program in python to incorporate the services as per the above rate list. In the first place, ask 
the user which transaction he/she wants to perform (USD to INR or INR to USD), then do the deal 
accordingly.
'''

# def extra_charges_rs(rs):
#     INR_to_USD = int(input("Enter the amount for conversion INR_to_USD: "))
#     if rs == 0:
#         print("Amount cannot be zero.")
#         return
#     count = (rs-10000) // 10000
#     return count


# def inrTOusd(rs):
#     if(rs<1000):
#         print("Minimum conversion is INR 1000/-")
#     elif(rs<10000):
#         usd = (rs-250)*0.0141
#         print(f"you will get {usd} USD after conversion ")
#     else:
#         usd = (rs-(250 + (extra_charges_rs*150)))*0.0141
#         print(f"you will get {usd} USD after conversion ")

# def extra_charges_us(us):
#     if us == 0:
#         print("Amount cannot be zero.")
#         return
#     count = (us-50) // 50
#     return count

# def UsdToInr(us):
#     USD_to_INR = int(input("Enter the amount for conversion USD to INR : "))
#     if(us<30):
#         print("Minimum conversion is 30 USD")
#     elif(us<50):
#         inr = (us*70.8305)-400
#         print(f"you will get {inr} INR after conversion ")
#     else:
#         inr = (us-(400+(extra_charges_us*300)))*70.8305
#         print(f"you will get {inr} INR after conversion ")

# conversion = int(input("which conversion you want : USD to INR(1) or  INR to USD(2) : "))
# match conversion:
#     case 1:
#         inrTOusd()
#     case 2: 
#         UsdToInr()

def extra_charges_rs(rs):
    count = (rs-10000) // 10000
    return count * 150

def inrTOusd(rs):
    if rs < 1000:
        print("Minimum conversion is INR 1000/-")
        return
    extra_charge = extra_charges_rs(rs)
    usd = (rs - 250 - extra_charge) * 0.0141
    print(f"You will get {usd} USD after conversion.")

def extra_charges_us(us):
    count = (us-50) // 50
    return count * 300

def UsdToInr(us):
    if us < 30:
        print("Minimum conversion is 30 USD")
        return
    extra_charge = extra_charges_us(us)
    inr = (us * 70.8305) - 400 - extra_charge
    print(f"You will get {inr} INR after conversion.")

def main():
    print("Welcome to the currency converter!")
    while True:
        print("\nChoose a conversion option:")
        print("1. USD to INR")
        print("2. INR to USD")
        print("3. Quit")
        conversion = input("Enter your choice (1/2/3): ")
        if conversion == "1":
            us = float(input("Enter the amount in USD: "))
            UsdToInr(us)
        elif conversion == "2":
            rs = float(input("Enter the amount in INR: "))
            inrTOusd(rs)
        elif conversion == "3":
            print("Thank you for using the currency converter!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main()
    