import numpy as np
arr = np.array([x for x in range(1,28)])
#arr = np.arange(1,28)
arr.resize(3,3,3)
print(arr)