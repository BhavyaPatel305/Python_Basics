size = int(input("Enter size of fibo series: "))

no1 = 0
no2 = 1

sum1 = 0
print(no1, no2, end=" ")
while size > 0:
    sum1 = no1 + no2
    print(sum1, end = " ")
    
    no1 = no2
    no2 = sum1
    size -= 1