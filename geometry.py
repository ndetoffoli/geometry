################################################################################
# geometry
# this program handles geographical figures
# nicolas de toffoli
################################################################################


import math


# constants
ASCII_CHAR = "#"


# base class
class Figure(object):
    def __str__(self):
        return "Figure"

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def drawAsciiArt(self):
        print ASCII_CHAR


# rectangle class
class Rectangle(Figure):
    length = 0.0
    width = 0.0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return "Rectangle l=%.2f x w=%.2f" % (self.length, self.width)

    def drawAsciiArt(self):
        # while count < self.length:
        print ASCII_CHAR * int(self.length)
        for x in xrange(int(self.width) - 2):
            print ASCII_CHAR + " " * (int(self.length) - 2) + ASCII_CHAR
        print ASCII_CHAR * int(self.length)


# square class
class Square(Rectangle):
        def __init__(self, length):
                super(Square, self).__init__(length, length)

        def __str__(self):
            return "Square a=%.2f" % self.length


# elipse class
class Elipse(Figure):
    radius_1 = 0.0
    radius_2 = 0.0

    def __init__(self, radius_1, radius_2):
        self.radius_1 = radius_1
        self.radius_2 = radius_2

    def perimeter(self):
        return 2 * math.pi * math.sqrt((math.pow(self.radius_1, 2) + math.pow(self.radius_2, 2)) / 2)

    def area(self):
        return math.pi * self.radius_1 * self.radius_2

    def __str__(self):
        return "Elipse r1=%.2f x r2=%.2f" % (self.radius_1, self.radius_2)

    def drawAsciiArt(self):
        print " " + ASCII_CHAR * (int(self.radius_1) * 2 - 2) + " "
        for x in xrange(int(self.radius_2) * 2 - 2):
            print ASCII_CHAR + " " * (int(self.radius_1) * 2 - 2) + ASCII_CHAR
        print " " + ASCII_CHAR * (int(self.radius_1) * 2 - 2) + " "


# circle class
class Circle(Elipse):
    def __init__(self, radius):
        super(Circle, self).__init__(radius, radius)

    def __str__(self):
        return "Circle r=%.2f" % self.radius_1


################################################################################
# main program
################################################################################
# create objects
figures = []
figures.append(Rectangle(10.0, 4.0))
figures.append(Square(10.0))
figures.append(Elipse(4.0, 2.0))
figures.append(Circle(4.0))

# print objects
for figure in figures:
    print figure
    print "* perimeter: %.2f" % figure.perimeter()
    print "* area: %.2f\n" % figure.area()
    figure.drawAsciiArt()
