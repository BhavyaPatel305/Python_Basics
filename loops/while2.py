no = 123
temp = no

rem = 0
sum = 0

while no>0:
    
    rem = no % 10;
    sum = sum * 10 + rem;
    no = no // 10;
    
print("Reverse of number is: ", sum)

if temp == sum:
    print("Palindrome")
else:
    print("Not Palindrome")