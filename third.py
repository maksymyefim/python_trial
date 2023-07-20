import math
class Cylinder:

    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        v=3.14 * self.radius**2*self.height
        return v
    def surface_area(self):
        a=2*3.14*self.radius*self.height+2*3.14*self.radius**2
        return a

cylinder = Cylinder(height=2, radius=3)
print(cylinder.volume())
print(cylinder.surface_area())
