class Employee:
    name = None
    
    def __init__(self,name):
        self.name = name
        
emp1 = Employee("amit")
emp2 = Employee("Raj")
print(emp1.name)
print(emp2.name)

        