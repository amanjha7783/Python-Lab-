# function with all parameters 
# PADK
# Parameters
# *args
# default parameter
# **kwargs

def func(name, *args, last_name = "Unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('Aman', 1,2,3, a = 'jha' , b = 2)

