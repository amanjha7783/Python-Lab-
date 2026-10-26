# import numpy as np

# x = np.array([1,2,3,4])

# print(x*2)

# import numpy as np
# import timeit
# %timeit np.array([1, 9])**4


import numpy as np
import timeit

# Define the code you want to time
def power_operation():
    np.arange(1, 4)**2

# Time it
execution_time = timeit.timeit(power_operation, number=1)
print(f"Average time over 1 runs: {execution_time:.6f} seconds")
