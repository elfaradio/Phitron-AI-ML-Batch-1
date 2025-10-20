'''Given two arrays A and B, compute:
(A + B) / 2


A**2 + B**2
'''
import numpy as np

a = np.random.randint(10, 100, size=(10,))
b = np.random.randint(10, 100, size=(10,))
print(a, b)

aa = np.add(a, b)
aa = np.divide(aa, 2)
print(aa)

bb = np.add(np.multiply(a, 2), np.multiply(b, 2))
print(bb)
