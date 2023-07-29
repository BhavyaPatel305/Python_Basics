IPL = (["dhoni","chennai" ],["Virat", "RCB"])

# can we add a new team?
print(IPL)

IPL[1][0] = "FAF" # Will work without any problem
print(IPL)

#IPL[1].append("VIRAT")

# inserts at the beginning of the list ["VIRAT", "FAF", "RCB]
IPL[1].insert(0, "VIRAT")
print(IPL)