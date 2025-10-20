''' . Add a 1D array [1,2,3] to each row of a 3*3 matrix.
'''
import numpy as np


a = np.arange(9).reshape(3, 3)
print(a)
a = a+[1, 2, 3]
# a = np.add(a, [1, 2, 3])
print(a)
