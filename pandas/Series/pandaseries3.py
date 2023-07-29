import pandas as pd

data1 = pd.Series([1,2,3,4,5], index=['a', 'b', 'c', 'd', 'e'])
#print(data1)

data2 = pd.Series([1,2,3,4,5], index=['p', 'q', 'r', 's', 't'])
data1 = data1.add(data2, fill_value=0)
print(data1)

