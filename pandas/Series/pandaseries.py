import pandas as pd
import numpy as np

data = [1,2,3,4,5]

ser = pd.Series(data)
print(ser)

# numpy array

data1 = np.array(['a', 'b', 'c', 'd', 'e', 'f'])
print(pd.Series(data1))

print(data1[0:3])


