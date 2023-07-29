# Twin  number program
no = int(input("Enter a number: "))
temp = no
rem = 0
sum1 = 0
mul = 1

while no>0:
    rem = no % 10
    sum1 = sum1 + rem
    mul = mul * rem
    no = no // 10

if sum1 == mul:
    print("Twin number")
else:
    print("Not Twin number")