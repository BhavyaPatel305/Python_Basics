base = int(input("Enter base"))
power = int(input("Enter power"))
mul = 1
for i in range(power):
    mul *= base
    if i == (power-1):
        print(base, " = ", end="")
        continue
    print(base, " * ", end="")
print(" ", mul)