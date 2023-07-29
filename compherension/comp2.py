
data = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
arr = []
# without compherension
for i in data:
    if len(data.get(i))>3:
        arr.append(i)

# with comp

arr = {i:j for i,j in data.items() if len(j)>3}
print(arr)