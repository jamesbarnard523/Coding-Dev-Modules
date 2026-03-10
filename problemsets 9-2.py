import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def update_radius(self, new_radius):
        self.radius = new_radius
    
    def get_circumference(self):
        return 2 * math.pi * self.radius
    
    def get_area(self):
        return math.pi * self.radius ** 2

c = Circle(5)

print(f"Radius:        {c.radius}")

print(f"circuference: {c.get_circumference():}")
print(f"area:          {c.get_area():}")
