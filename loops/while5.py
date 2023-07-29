#prime no or not

no = int(input("Enter a number: "))
i = 2
flg = 0
while i < no:
    
    if no % i == 0:
        flg = 1
        break
    i += 1 # no = i
    
if flg == 0:
    print("prime")    
else:
    print("not prime")