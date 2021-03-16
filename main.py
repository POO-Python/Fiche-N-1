from CompteBancaire import CompteBancaire

def main():

    compte1 = CompteBancaire(1056, 'Duchmol', 800)
    compte1.depot(350)
    compte1.retrait(2000)
    compte1.retrait(200)
    print(compte1)
    compte2 = CompteBancaire(2004, 'Dupont')
    compte2.depot(500)
    print(compte2)


main()