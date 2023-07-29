#multipule inheritance 1 parent many child

class Shape():
    height = 0
    width = 0
    pi = 3.14
    radius = 0
    def __init__(self):
        print("shape constructor")
        
    def drawShape(self):
        print("drawing shape")

class Circle(Shape):
    
    def __init__(self):
        print("circle constructor")   
        
    def drawCircle(self):
        self.drawShape()
        return self.pi * self.radius * self.radius    
             
        

class Rectangle(Shape):
    
    def drawRect(self):
        self.drawShape()
        return self.height * self.width
        
    def __init__(self):
        print("rectangle constructor")        


r = Rectangle()
rec = r.drawRect()        
print("Area of rectangle: ", rec)

c = Circle()
cir = c.drawCircle()
print("Area of circle: ", cir)