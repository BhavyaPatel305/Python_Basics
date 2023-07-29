# Program to tell if a number is armstrong or not
no = int(input("Enter a number: "))
temp = no
rem = 0
sum1 = 0
while no>0:
    rem = no % 10
    sum1 = sum1 + pow(rem,3)
    no = no // 10
    
if temp == sum1:
    print("Armstrong")
else:
    print("Not Armstrong")
    
        