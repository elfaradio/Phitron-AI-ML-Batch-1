''' Create a 1D, 2D, and 3D NumPy array and print their dimensions and shapes'''
import numpy as np
a = np.array([1,  3, 4])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.shape, a.ndim)
print(b.shape, b.ndim)
print(c.shape, c.ndim)
