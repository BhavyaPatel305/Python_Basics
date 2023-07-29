no = int(input("Enter amount: "))
# 1c 2c 5c 50 100 200 500 2000

c_2000 = no // 2000
no %= 2000

c_500 = no // 500
no %= 500

c_200 = no // 200
no %= 200

c_100 = no // 100
no %= 100

c_50 = no // 50
no %= 50

c_5 = no // 5
no %= 5

c_2 = no // 2
no %= 2

c_1 = no

print("2000: ", c_2000)
print("500: ", c_500)
print("200: ", c_200)
print("100: ", c_100)
print("50: ", c_50)
print("5: ", c_5)
print("2: ", c_2)
print("1: ", c_1)