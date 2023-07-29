#single inheritance
class Animal():
    typeOfAnimal = ""
    
    def animalData(self):
        print("Animal Data")
    
    def __init__(self):        
        print("Animal Constructor")
        
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")
    
    def getType(self):
        self.typeOfAnimal = input("Enter type of animal: ")
        
    def printType(self):
        print(self.typeOfAnimal)

# Chile class const will be called    
do = Dog()
do.getType()
do.printType()
