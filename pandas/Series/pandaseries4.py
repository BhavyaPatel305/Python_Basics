import pandas as pd
import numpy as np

data = pd.read_csv("./ipl.csv")
#print(data)
data.dropna(inplace=True)

data["Name"] = data["Name"].str.upper()
print(data["Name"])

name_list = data["Name"].tolist()
print(name_list)
