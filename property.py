class Circle(object):

    version = '0.6'

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return (self.radius ** 2) *3.14

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
