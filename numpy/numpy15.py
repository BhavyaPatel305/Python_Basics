import numpy as np

arr = np.array([[x for x in range(0,5)],[x for x in range(0,5)],[x for x in range(0,5)],[x for x in range(0,5)]])
a = arr.__eq__(0)
print("[ ", end="")
for i in a:
    
    for index,j in enumerate(i):
        if j == True:
            print(index+1, " , ", end="")
            
print("]")