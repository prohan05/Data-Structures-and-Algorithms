class DrawingAPIOne(object):
    # implementation specific abstraction concrete class one
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at {}, {} with radius {}".format(x, y, radius))


class DrawingAPITwo(object):
    # implementation of specific abstraction concrete class 2
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at {}, {} with radius {}".format(x, y, radius))


class Circle(object):
    # implementation independent abstraction for eg. there can be a rectangle class
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        # impl specific abstrac taken care of by another class DrawingAPI
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def scale(self, percent):
        # impl indep
        self.radius *= percent


# build the 1st circle object using API 1
circle1 = Circle(1, 2, 3, DrawingAPIOne())
circle1.draw()

circle2 = Circle(2, 3, 4, DrawingAPITwo())
circle2.draw()

