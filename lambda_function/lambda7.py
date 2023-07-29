# fibo series using reduce
from functools import reduce
lst = ["a", "b", "c", "d", "e", "f", "g", "h"]
fl = reduce(lambda x,y: x+y, lst)
print(fl)