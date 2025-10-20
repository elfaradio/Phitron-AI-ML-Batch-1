'''4 . Create a 4 by  4 matrix from 0 - 15. Then , extract:
the first row


the last column


a 2 by 2 subarray from the center
'''

import numpy as np

a = np.random.randint(0, 16, size=(4, 4))
print(a)
# First Row
print(a[0])
print(a[0:1])

# last colmn
print(a[:, -1])
print(a[::, -1])
print(a[::, -1:-2:-1])


# 2 * 2 subarray
x = 4//2
x -= 1
y = 4//2
y += 1
print(a[x:y, x:y])
