li = ["samir r", "ram k", "ramlal", "sumo d", "dhiraj"]

#fl = list(filter(lambda x: " " in x,li))
fl = list(map(lambda x: x.capitalize() if " " in x else x, li))
print(fl)