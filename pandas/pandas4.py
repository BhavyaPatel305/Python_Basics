import pandas as pd

dict = {'name':["amit","neha","priya","raj","ajay"],'degree':["B.Tech","M.Tech","B.Sc","M.Sc","B.Com"],'score':[90,80,70,60,50]}
df =pd.DataFrame(dict)

for i,j in df.iterrows():
    print(i,j, "\n")
    print()
    