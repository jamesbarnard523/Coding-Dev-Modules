#Write a program that prompts the user to enter the location of two coordinates, and prints to the screen
#the equation of the straight line, y= mx+ c that connects them. A bespoke class should be designed
#to represent a coordinate (this should hold two values), and another class to represent a straight line
#(this should contain two coordinates and any required functionality).

class coord:
    def __init__(self, x1 , y1, x2, y2):
        self.x1 = x1
        self.y1 = y1

        self.x2 = x2
        self.y2 = y2

    def gradientline(self):
        m = (self.y2-self.y1) / (self.x2-self.x1)
        c = self.y1 - (self.x1 * m)
        self.gradient = m*x2 + c
        return self.gradient 
    
    def equation(self):
        m = self.gradientline()
        c = self.y1 - (m * self.x1)
        return f'y = {m}x + {c}'

x1,y1,x2,y2 = map(int,input('enter coord values x1 y1 x2 y2 (space-sep): ').split())

coordinate = coord(x1,y1,x2,y2)

print(f'Gradient: {coordinate.gradientline()}')
print(f'Equation: {coordinate.equation()}')
        