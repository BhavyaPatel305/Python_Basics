import pandas as pd

data = pd.read_csv("./ipl.csv")
ser = pd.Series(data['Name'])

print(ser.loc[0:3])