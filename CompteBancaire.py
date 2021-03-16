class CompteBancaire(object):
    
    def __init__ (self, numero, nom, solde=1000):
        self.numero = numero
        self.nom = nom
        self.solde = solde

    def depot(self, ajout_solde):
        self.solde += ajout_solde

    def retrait(self, retrait_solde):
        if(retrait_solde < self.solde):
            self.solde -= retrait_solde
        else:
            print('Retrait impossible.')

    def __str__ (self):
        return 'Le solde du compte bancaire ' + str(self.numero) + ' de ' + self.nom + ' est de ' +  str(self.solde) + '€'

    def __add__(self, other):
        if self.nom != other.nom :
            return ('La fusion de ces comptes est impossible.')
        else:
            self.solde += other.solde
            other.solde = 0
            print('Fusion effectuée.')


