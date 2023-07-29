import pandas as pd

data = pd.read_csv("./ipl.csv")

# sort by team
#data.sort_values("Team", inplace=True)
#print(data)

filter1 = data["Team"] == "mi"

data.where(filter1, inplace=True)

print(data)
#print(df)

filter2 = data["type"] == "batsman"

print(data.where(filter1 & filter2, inplace=True))




