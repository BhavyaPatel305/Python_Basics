#horizontal stack
import numpy as np

a1 =np.array([[1,2,3],[4,5,6]])
a2 =np.array([[7,8,9],[10,11,12]])

o =np.hstack((a1,a2))
#o =np.vstack((a1,a2))
print(o)