class Vector(object):
    
    def __init__(self, x, y):
        self.coords = (x, y)

    @property 
    def x (self):
        return self.coords[0]

    @property 
    def y (self):
        return self.coords[1]


    def __str__(self):
        return '(' + str(self.coords[0]) + ', ' +  str(self.coords[1]) + ')'

    def __add__(self, other):
        return Vector(self.coords[0] + other.coords[0] , self.coords[1] + other.coords[1])
