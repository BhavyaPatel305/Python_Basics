no = int(input("Enter a number: "))
sum = 0
evenSum = 0
oddSum = 0

even = ""
odd = ""

for i in range(1, no+1):
    sum += i
    if i%2 == 0:
        even += (str(i) + " ")
        evenSum += i
    else:
        odd += (str(i) + " ")
        oddSum += i
        
        
print("Even numbers are: ", even)
print("Sum of even numbers is: ", evenSum)
print("Odd numbers are: ", odd)
print("Sum of odd numbers is: ", oddSum)
print("Sum of first", no, "natural numbers is", sum)