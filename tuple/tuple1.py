scores = (('CSK', 300, 200, 70, 90, 100), ('Gujarat', 400, 12, 45, 80, 34), ('Titans', 200, 100, 80, 90, 100))
max = 0
sum = 0
team = ''
for i in scores:
    for j in i:
        if type(j) == int:
            sum += j
    if sum > max:
        max = sum
        team = i[0]
print("Winning Team: ", team)