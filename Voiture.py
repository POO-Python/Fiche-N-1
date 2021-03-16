class Voiture(object):
    def __init__(self, marque, color):
        self.marque = marque
        self.color = color
    
    def __str__(self):
        return self.marque + ' ' + self.color




