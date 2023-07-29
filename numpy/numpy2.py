import numpy as np

arr = np.zeros((3,4), dtype=np.int32)
print("arr: ", arr)

arr = np.ones((3,4), dtype=np.int32)
print("arr: ", arr)

arr = np.full((4,4), 5, dtype=np.int32)
print("arr: ", arr)

# 0 to 30, step 5
arr = np.arange(0, 32, 5)
print("arr: ", arr)