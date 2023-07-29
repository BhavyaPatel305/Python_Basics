import pandas as pd
import numpy as np

series1 = pd.Series([10,25,33,44,np.nan,55,67,89,np.nan])
series2 = pd.Series([11,24,np.nan,33,44,11,55,67,89,np.nan])
replace_nan = 100

res = series1.le(series2,fill_value=replace_nan)
res1 = series1.ge(series2,fill_value=replace_nan)
#eq
#ne

print(res)
print(res1)
# print(series1)
# print(series2)