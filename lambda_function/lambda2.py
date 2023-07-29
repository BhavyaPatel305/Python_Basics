lst = ["bhavya", "rajesh", "king", "ko", "we", "sumo"]

fl = list(filter(lambda x:(len(x)>=3 and (x.startswith("b"))), lst))
print(fl)