# rs = int(input("Enter the amount for conversion : "))
# def extra_charges(rs):
#     count = 0
#     while (rs==0):
#         rs = (rs-10000)//10000
#         count += 1
#     print(count)
# extra_charges(rs)
def extra_charges(rs):
    if rs == 0:
        print("Amount cannot be zero.")
        return
    count = (rs-10000) // 10000
    print(count)
rs = int(input("Enter the amount for conversion : "))
extra_charges(rs)
