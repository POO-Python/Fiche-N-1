class Voiture(object):
    
    def __init__(self, marque, couleur):
        self.__marque = marque
        self.__couleur = couleur
    

    @property
    def marque(self):
        return self.__marque

    @property
    def couleur(self):
        return self.__couleur

    @marque.setter
    def marque(self, value):
        self.__marque = value

    @couleur.setter
    def couleur(self, value):
        self.__couleur = value


    def __str__(self):
        return self.marque + ' ' + self.couleur