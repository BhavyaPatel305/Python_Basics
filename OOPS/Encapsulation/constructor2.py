class Employee:
    age = 0
    
    def __init__(self, age):
        self.age = age

lst = []
for i in range(0,10):
    emp = Employee(i)
    lst.append(emp)

for i in lst:
    print(i.age)
    