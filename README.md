# Fiche-N-1 Exercice 1

I/ Définir une classe CompteBancaire dont le constructeur prendra trois paramètres (outre self) : 
numero, nom et solde (avec la valeur par défaut 1000).
Ce constructeur initialisera trois variables d'instance correspondant à ces paramètres.

Trois méthodes seront en outre définies :
* depot : permet d'ajouter une certaine somme au solde d’un compte ;
* retrait : permet de retirer une certaine somme du solde d’un compte (à condition que cette somme ne dépasse pas le solde) ;
* une méthode permettant d'afficher le numéro, le nom du titulaire et le solde d’un compte via la fonction print, selon le modèle décrit ci-dessous.

Exemple d'utilisation de cette classe :

>compte1 = CompteBancaire(1056, 'Duchmol', 800)
>compte1.depot(350)
>compte1.retrait(2000)
>compte1.retrait(200)
>print(compte1)
>compte2 = CompteBancaire(2004, 'Dupont')
>compte2.depot(500)
>print(compte2)

Affichage obtenu :

>Retrait impossible.
>Le solde du compte bancaire 1056 de Duchmol est de 950 euros.
>Le solde du compte bancaire 2004 de Dupont est de 1500 euros.

2. Définir une méthode permettant la fusion de deux comptes ayant le même titulaire.
Cette fusion sera effectuée à l’aide de l’opérateur « + », et aura pour effet de transférer le solde du 
compte en deuxième argument sur le compte en premier argument.
Exemple d'utilisation de cette méthode :
>compte3 = CompteBancaire(3987, 'Dupont', 2000)
>compte1 + compte3
>print(compte1)
>print(compte3)
>compte2 + compte3
>print(compte2)
>print(compte3)
Affichage obtenu :
>La fusion de ces comptes est impossible.
>Le solde du compte bancaire 1056 de Duchmol est de 950 euros.
>Le solde du compte bancaire 3987 de Dupont est de 2000 euros.Fusion effectuée.
>Le solde du compte bancaire 2004 de Dupont est de 3500 euros.
>Le solde du compte bancaire 3987 de Dupont est de 0 euros.