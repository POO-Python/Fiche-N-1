# Fiche-N-1

1. Définir une classe Voiture dont le constructeur prendra deux paramètres (outre self) : marque et couleur.

Ce constructeur initialisera deux variables d'instance correspondant à ces paramètres.
On définira bien sûr les accesseurs et les mutateurs relatifs aux deux attributs d’une instance de 
cette classe, ainsi qu’une méthode permettant d'afficher ces deux attributs via la fonction print.

Exemple d'utilisation de cette classe :
>v1 = Voiture('Renault', 'bleue')
>v2 = Voiture('Mercedes', 'noire')
>print(v1)
>print(v2)
>v1.marque = 'Skoda'
>print(v1)

Affichage obtenu :

>Renault bleue
>Mercedes noire
>Skoda bleue