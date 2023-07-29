import pandas as pd

data = pd.read_csv("./ipl.csv")

series = pd.Series(data["sal"])
series.fillna(10000, inplace=True)
bool_ser = series.between(9000,12000,inclusive="both")
print(bool_ser)