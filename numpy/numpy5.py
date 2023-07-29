import numpy as np
arr = np.array([[1,5,6],[4,7,2],[3,1,9]])

print("largest elm = ", arr.max())
print("largest = ", arr.max(axis=1))
print("largest = ", arr.max(axis=0))

#min

print("sum =",arr.sum())
print("sum =",arr.sum(axis=0))
print("sum =",arr.sum(axis=1))