class CompteBancaire(object):
    
    def __init__ (self, numero, nom, solde=1000):
        self.numero = numero
        self.nom = nom
        self.solde = solde

    def depot(self, ajout_solde):
        slef.solde = self.solde + ajout_solde

    def retrait(self, retrait_solde):
        if(retrait_solde < slef.solde):
            slef.solde = self.solde - retrait_solde
        else:
            print('Retrait impossible.')

    def __str__ (self):
        print('Le solde du compte bancaire {0} de {1} est de [2}', self.numero, self.nom, self.solde)




