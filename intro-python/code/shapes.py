from math import pi
# Write code to calculate the area of each shape.
class Shape:
    def __init__(self, name, dimensions):
        self.name = name
        self.dimensions = dimensions
    def area(self):
        if self.name == 'T':
            self.size = float((self.dimensions[0] * self.dimensions[1])/2)
        elif self.name == 'R':
            self.size = self.dimensions[0] * self.dimensions[1]
        elif self.name == 'C':
            r = self.dimensions / 2
            self.size = pi*(r**2)
        return self.size

shapes = [('T',(8,8)),('R',(4,6)),('C',(1)),
('T',(14,6)),('R',(8,8)),('C',(5))]

for shape in shapes:
    print(f'{shape}: {Shape(*shape).area()}')