'''
WAP considering that Ramu is working in a firm as an employee with basic salary 10,000 INR per 
month. Further, the company pays him house rent allowances (HRA) of 18% on his basic salary and 
70% of dearness allowances on the basic salary per month. Furthermore, the company deducts 12% 
from his basic salary, and his dearness allowances towards his contribution to provident fund (PF) and 
the firm deposits an equal contribution to his PF account. Now, calculate his net salary per month and 
what is the total available amount in his PF account after a month.
'''

basic_salary = int(input("salary of ramu: "))

HRA = (basic_salary * 0.18)
print(f"House rent allowance is {HRA}")

DA = (basic_salary*0.70)
print(f"dearness allowances {DA}")

Pf = (basic_salary+DA)*0.12
print(f"deductuion salary is {Pf}")

Total_salary = basic_salary + HRA + DA - Pf

print(f"The total salary of ram is {Total_salary}")