import numpy as np
arr = np.array([1,2,3,4,5,6])
arr.resize(2,3)
print(arr.__lt__(3)) # [ True  True False False False False]
print(arr.__gt__(3)) # [False False False  True  True  True]
print(arr.__le__(3)) # [ True  True  True False False False]
print(arr.__ge__(3)) # [False False  True  True  True  True]
print(arr.__eq__(3)) # [False False  True False False False]
print(arr.__ne__(3)) # [ True  True False  True  True  True]
print(arr.__pos__()) # [[1 2 3] [4 5 6]]
print(arr.__neg__()) # [[-1 -2 -3] [-4 -5 -6]]