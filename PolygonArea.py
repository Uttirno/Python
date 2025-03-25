import math

class Square():
    def __init__(self, s):
        self.s = s
    def area(self):
        print(self.s*self.s)

class Triangle():
    def __init__(self, s, h):
        self.s = s
        self.h = h
    def area(self):
        print((self.s*self.h) / 2)

class Hexagon():
    def __init__(self, s):
        self.s = s
    def area(self):
        print((3 * math.sqrt(3) / 2) * self.s**2)

square = Square(10)
triangle = Triangle(20, 20)
hexagon = Hexagon(10)

for n in (square, triangle, hexagon):
    n.area()
