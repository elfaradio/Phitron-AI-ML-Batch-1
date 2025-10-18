'''
2.  You have a Python list containing the lap times (in seconds) for an athlete.

Task:

Convert the list into a NumPy array.
Print the array's shape, size, and data type.
The athlete wants to see their times in minutes. Create a new array by dividing all the lap times by 60.
Print the new array of lap times in minutes.
'''

import numpy as np

lst = [100, 120, 130, 140, 75, 28]
arr = np.array(lst)
print(arr.shape, arr.size, arr.dtype)
minUte = arr/60
print(f"Minutes:", *minUte)
