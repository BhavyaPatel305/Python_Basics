import pandas as pd
import numpy as np

np.random.seed(0)

df = pd.DataFrame(np.random.rand(5,4), columns= ["A", "B", "C", "D"])
#print(df)
#df = df.add(10)
#df = df.sub(10)
#df = df.mul(10)
#df = df.div(10)
print(df)
