num = int(input("Enter a number: "))
array = []
array.append(num)
choice = 1
while choice != 0:
    choice = int(input("Enter 1 to add more numbers or 0 to stop: "))
    if choice == 1:
        num = int(input("Enter a number: "))
        array.append(num)
    elif choice == 0:
        break
    else:
        print("Invalid choice")
print(array)
o_sum = 0
e_sum = 0
for i in array:
    if i % 2 == 0:
        e_sum += i
    else:
        o_sum += i
print("Sum of odd numbers: ", o_sum)
print("Sum of even numbers: ", e_sum)
        