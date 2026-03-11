import math

class circle:
    def __init__(self,radius):
        self.radius = radius
        return

    def updateRadius(self,updateradius):
        self.updateradius = self.radius
        return
        
    def getcircumference(self):
        return  2 * math.pi * (self.radius**2)
        
    
    def getarea(self):
        return  math.pi * (self.radius**2)
        
    
shape = circle(5)

print(f'area of circle with radius : {shape.radius} equals:\n {shape.getarea()} ')

print (f'circumference of circle with radius {shape.radius} equals\n {shape.getcircumference()}')