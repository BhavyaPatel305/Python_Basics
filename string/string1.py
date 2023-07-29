str = "bhavya"
# chr() function 
# ord function

for i in str:
    print(chr(ord(i) - ord(" ")))
    
char1 = 'o'
str1 = "python"
str1  = str1 + char1
print(str1)

# strings are immutable but we can use += to add characters to string
# basically when doing str1 = str1 + char1
# we are redeclaring str1 again: it will have a new memory block
