from Voiture import Voiture
from NVC import NVC

def main():

    v1 = Voiture('Renault', 'bleue')
    v2 = Voiture('Mercedes', 'noire')
    print(v1)
    print(v2)
    v1.marque = 'Skoda'
    print(v1)

    nvc1= NVC('Peugeot', 'blanche', 'Jean')
    print(nvc1)
    nvc1.accelerer(1, 5)
    print(nvc1)
    nvc1.accelerer(-0.4, 5)
    print(nvc1)
    nvc1.accelerer(-3, 2)
    print(nvc1)

    nvc2 = NVC('Ford', 'verte')
    print(nvc2)
    nvc2.accelerer(0.8, 5)
    print(nvc2)



main()