
list = [1,2,3,4,5]
# without comp
#dict = {}
#for i in list:
 #   dict[i] = i**2
#print(dict)

# with comp
dict = {i:i*i for i in list}
print(dict)