from Contact import Contact

class ContactPro(Contact):
    #Constructeur
    def __init__(self, fname, lname, phone, occ):
        Contact.__init__(self, fname, lname, phone)
        self.occupation = occ

    #Getter
    @property
    def occupation(self):
        return self.__occupation

    #Setter
    @occupation.setter
    def occupation(self, value):
        self.__occupation = value

    #Méthode
    def __str__(self):
        return "{} {:>30}".format(Contact.__str__(self), self.occupation)





