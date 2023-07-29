import pandas as pd
data = pd.read_csv("./ipl.csv")
#print(data)
filter1 = data["Team"] == "mi"

filter2 = data["runs"] >= 500
data.where(filter1 & filter2, inplace=True)
print(data)