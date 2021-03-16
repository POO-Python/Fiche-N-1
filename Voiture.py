class Voiture(object):
    #Constructeur
    def __init__(self, marque, color):
        self.__marque = marque
        self.__color = color
    
    #Getters
    @property
    def marque(self):
        return self.__marque 

    @property
    def color(self):
        return self.__color

    #Setters
    @marque.setter
    def marque(self, marque):
        self.__marque = marque

    @color.setter
    def color(self, color):
        self.__color = color

    #Méthode
    def __str__(self):
        return self.__marque + ' ' + self.__color




