data = set({12,45,6,7,89,0,12})
print(data)
print(type(data))

data.add(133)
data.update({100,99})

data.update([12])

data.remove(12)
data.discard(100)

x = data.pop()
print(x)

un = data.union({11,22,456,99})
print("un...", un)

d = data.difference({1,2,89.12,45})
print("d...", d)

i = data.intersection({1,2,89,12,45})
print("i...", i)


si = data.symmetric_difference({1,2,89,12,45})
print("si...", si)

print("subset", data.issubset{67}) # false
print("superset", data.issuperset{67}) # true

print("data", data)

