import pandas as pd
data ={'Name':["raj","parth","priya","neha","sagar","sahil"],'Age':[20,21,22,23,24,23],'Address':["India","Usa","Uk","Canada","Australia","China"],'Qualification':["B.Tech","M.Tech","B.Sc","M.Sc","B.Com","M.Com"]}
df = pd.DataFrame(data)
#print(df)
print(df[['Name', 'Age']])