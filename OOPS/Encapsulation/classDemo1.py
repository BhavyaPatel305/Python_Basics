class Student:
    name = ""
    age = 0
    grade = ''
    
    def setName(self):
        self.name = input("Enter student name: ")
    
    def setAge(self):
        self.age = int(input("Enter student's age: "))
    
    def setGrade(self):
        self.grade = input("Enter your grade: ")
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGrade(self):
        return self.grade

std = Student()
std.setName()
std.setAge()
std.setGrade()

print(std.getName())
print(std.getAge())
print(std.getGrade())
        