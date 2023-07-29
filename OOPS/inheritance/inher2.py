class Diwali():
    crackers  =100
    holidays = 5
    def __init__(self):
        print("diwali constructor")
        
class Holi():
    balloons = 120
    holidays  =2
    def __init__(self):
        print("holi constructor")
        
class Festival(Holi, Diwali):
    def __init__(self):
        super().__init__()
        print("Festival constructor")
    
    def celebrate(self):
        print("celebrating festival")
        print("crackers: ", self.crackers)
        print("balloons: ", self.balloons)
        
        # priority given to Holi class as written first (Holi, Diwali) while inheriting
        print("holidays: ", self.holidays)  

f = Festival()
f.celebrate()
        
    