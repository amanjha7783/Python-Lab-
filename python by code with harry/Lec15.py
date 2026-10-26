# Greeting

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
time = int(time.strftime('%H'))
print(time)
# time = int(input("Enter the Time in 24 hour format: "))
if(time>0 and time<=5):
    print("Mid night sir ")
elif( time>5 and time<=12):
    print("Good Morning sir ")
elif(time>12 and time<=16):
    print("Good Afternoon sir ")
elif(time>16 and time<=20):
    print("Good Evening sir ")
elif(time>2 and time<=24):
    print("Good Night sir")

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)f
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)

# if(timestamp>00:00:00 and timestamp<=05:00:00):
#     print("Mid night sir ")
# elif( timestamp>5 and timestamp<=12):
#     print("Good Morning sir ")
# elif(timestamp>12 and timestamp<=16):
#     print("Good Afternoon sir ")
# elif(timestamp>16 and timestamp<=21):
#     print("Good Evening sir ")
# elif(timestamp>21 and timestamp<=24):
#     print("Good Night sir")