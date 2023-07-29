x =["naman","parth","kay","madam","malayalam","amit"]
dict = {i:i[::-1] for i in x if i == i[::-1]}
print(dict)