def comp(a,b):
    if a>b:
        return a
    return b

print(comp(10,20))

x = lambda a,b: a if a>b else b
print(x)

# Similar to arrow function in Javascript
