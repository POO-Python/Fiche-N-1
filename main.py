from Voiture import Voiture

def main():

    v1 = Voiture('Renault', 'bleue')
    v2 = Voiture('Mercedes', 'noire')
    print(v1)
    print(v2)
    v1.marque = 'Skoda'
    print(v1)


main()