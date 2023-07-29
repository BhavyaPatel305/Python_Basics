import pandas as pd
data = pd.read_csv("./ipl.csv")

boole_series = data["Team"]=="mi"
bool_series2 = (data["type"]=="batsman") & (data["Team"]=="csk")
print(bool_series2)