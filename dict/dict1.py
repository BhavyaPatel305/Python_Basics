list1 = [1,2,3,4,5,6,7]
list2 = [11,22,33,44,55,66,77]
dict = {}
count = 0

dict2 = list(zip(list1,list2))
print(dict2)
for i in list1:
    dict[i] = list2[count]
    count = count + 1
print(dict)