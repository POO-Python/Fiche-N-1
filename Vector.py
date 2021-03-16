class Vector(object):
    
    #Constructeur
    def __init__(self, x, y):
        self.coords = (x, y)

    #Getters

    @property 
    def x (self):
        return self.coords[0]

    @property 
    def y (self):
        return self.coords[1]

    #Setters

    @x.setter
    def x (self, value):
        self.coords = (value, self.coords[1])

    @y.setter
    def y (self, value):
        self.coords = (self.coords[0], value)

    #Méthodes

    def __str__(self):
        return '(' + str(self.x) + ', ' +  str(self.y) + ')'

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)
