class Gov():
    tax =12
    print("This is Gov class")
    
    def __init__(self):
        print("gov class constructor called...")

class State(Gov):
    def __init__(self):
        print("state class constructor called...")
        
    grant = 100000
    print("This is State class")    
    
    def stateData(self):
        print("This is state data function")
        print("Tax: ", self.tax)
        print("Grant: ", self.grant)

class City(State):
    
    def __init__(self):
        print("city class constructor called...")
        
    print("This is City class")
    amount = 10000
    def cityData(self):
        print("This is city data")
        print("Tax: ", self.tax)
        print("Grant: ", self.grant)
        print("Amount: ", self.amount)


# c = City() #default constructor
# c.cityData()
# c.stateData()

s = State()
# s.stateData()
# s.cityData() #error
