import numpy as np

a = np.array([1,2,3,4,5.0,6])
b = np.array([1,3,2,4,5.0,7])

print(np.where(a==b))
print(np.where(a>b))
print(np.where(a<b))
print(np.where(a>=b))