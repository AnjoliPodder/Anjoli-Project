'''
OBJECT ORIENTED PROGRAMMING
'''

# Python has built-in support for classes and object-oriented programming


# Point class defines a pair of x, y coordinates on a 2d plane and some methods on that object

import math
class Point:

    # initialize a new point. Either set coordinates to 0, or allow input of 2 numbers for x and y coordinates
    def __init__(self, p1=0, p2=0):
        self.x = p1
        self.y = p2

    # set the points back to zero
    def reset(self):
        self.x = 0
        self.y = 0

    # Calculate the distance between this point and another given point on a 2d plane
    def distance(self, point2):
        return math.sqrt((self.x-point2.x)**2 + (self.y-point2.y)**2)

    # defines how to represent this object as a string - used for print
    def __str__(self):
        return '[%s,%s]' % (self.x, self.y)


pp = Point()
pp2 = Point(3,4)
print(pp2)

print(pp.x, pp.y)
print(pp.distance(pp2))

pp2.reset()
print(pp.distance(pp2))

# define a new class Shape

class Shape:
    def area(self):
        return 0

# circle inherits all of the methods from Shape
class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    # override the parent's method
    def area(self):
        return math.pi * self.radius * self.radius

    def diameter(self):
        return 2 * self.radius

