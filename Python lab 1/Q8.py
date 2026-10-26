'''
WAP considering a shop will give discount of 10% if the cost of purchased quantity is more than 
1000. Ask user for quantity, suppose, one unit will cost 100. Judge and print total cost for user.
'''
per_unit_price = int(input("Enter the price of product per unit : "))
number_of_quantity = int(input("Enter the number of product quantity : "))
total_price = per_unit_price*number_of_quantity

if(total_price > 1000):
    total_price = total_price - total_price*0.10
    print(f"the final amount to be paid is {total_price}")
else:
    print(f"the final amount to be paid is {total_price}")
    