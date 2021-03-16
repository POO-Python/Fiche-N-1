class Contact(object):

    #Constructeur    
    def __init__(self, firstname, lastname, phonenumber=None):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber

    #Getters

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def phonenumber(self):
        return self.__phonenumber

    #Setters
    @firstname.setter
    def firstname(self, value):
        self.__firstname = value

    @lastname.setter
    def lastname(self, value):
        self.__lastname = value

    @phonenumber.setter
    def phonenumber(self, value):
        self.__phonenumber = value

    #Méthode
    def __str__(self):
        return "{:30} {:30} {:10}".format(self.firstname, self.lastname, self.phonenumber)



