num = [1,2,67,3,7,4,90,5]
max = num[0]
min = num[0]
for i in num:
    if i>max:
        max = i
    if i<min:
        min = i
print("Maximum number is: ",max)
print("Minimum number is: ",min)
    