from Voiture import Voiture
class NVC(Voiture):
    
    #Constructeur
    def __init__ (self, marque, couleur, conducteur='personne', ):
        Voiture.__init__(self, marque, couleur)
        self.conducteur = conducteur
        self.vitesse = 0

    #Getters
    @property
    def conducteur(self):
        return self.__conducteur 

    @property
    def vitesse(self):
        return self.__vitesse

    #Setters
    @conducteur.setter
    def conducteur(self, conducteur):
        self.__conducteur = conducteur

    @vitesse.setter
    def vitesse(self, vitesse):
        self.__vitesse = vitesse

    #Méthodes

    def __str__(self):
        return Voiture.__str__(self) + ' conduite ' + 'par ' + self.conducteur + ' à une vitesse de ' + str(self.vitesse) + ' m/s'

    def accelerer(self, taux, duree):
        if(self.conducteur == 'personne'):
            print("Cette voiture n'a pas de conducteur.")
        elif self.vitesse + taux * duree < 0:
            self.vitesse = 0  
        else:
            self.vitesse += taux * duree 

