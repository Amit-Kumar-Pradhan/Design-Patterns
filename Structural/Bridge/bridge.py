class DrawingAPIOne(object):
    """ Implemention specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print(f"API 1 drawing circle at cordinates {x}, {y} with radius {radius}")

class DrawingAPITwo(object):
    """ Implemention specific abstraction: concrete class one"""
    def draw_circle(self, x, y, radius):
        print(f"API 2 drawing circle at cordinates {x}, {y} with radius {radius}")

class Circle(object):
    """ Implementation independent abstraction"""
    def __init__(self, x, y, radius, drawing_api):
        """ Initiates necessary attributes """
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """ Implementation-specific abstraction taken care of by another """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        """ Implementation independent """
        self._radius *= percent 

# Build the circle object using API one
circle = Circle(1, 2, 3, DrawingAPIOne())

# draw circle
circle.draw()

# Build the circle object using API one
circle2 = Circle(4, 5, 6, DrawingAPITwo())

# draw circle
circle2.draw()