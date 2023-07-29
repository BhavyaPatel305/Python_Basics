import pandas as pd

data = pd.read_csv("./ipl.csv")

arr = pd.unique(data["Team"])
print(arr)
arr1 = data["runs"]
bool_ser = arr1.between(50,100,inclusive ="both")
print(bool_ser)