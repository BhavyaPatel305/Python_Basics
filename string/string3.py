# capitalize first letter of every word of string
name = "java is a language"
name = name.split(" ")
string  =""
for i in range(len(name)):
    string += name[i].capitalize()
    string += " "
    

print(string)
    
    
