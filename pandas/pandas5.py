import pandas as pd

data = pd.read_csv("./ipl.csv")
#print(data.head())
data.insert(2,"IsActive",True)
print(data.head())


arr = data["Team"].unique()
arr1 = data["type"].unique()
print(arr)
print(arr1)

x = data.nunique()
print(x)