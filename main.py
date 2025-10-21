import numpy as np

arr = np.random.randint(1, 5, size=(4, 4))
print(arr)
print(sum(arr[::, 0]))
ans = np.sum(arr, axis=1)
print(ans)
np.newaxis
