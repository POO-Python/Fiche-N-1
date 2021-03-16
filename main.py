from Contact import Contact
from Vector import Vector

#Création des Contacts
brice = Contact('Brice', 'Smith', 6942)
obama = Contact('Barack', 'Obama', 9381)
lurkin = Contact('Quentin', 'Lurkin')

lurkin.set_phonenumber(8293)
print(lurkin.phonenumber)

lurkin.changename('John', 'Doe')
print(lurkin.firstname, lurkin.lastname)

lurkin.changename('Bruce')
print(lurkin.firstname, lurkin.lastname)

lurkin.changename(newlastname='Lee')
print(lurkin.firstname, lurkin.lastname)

#Creation des vecteurs
u = Vector(1, -1)
print(u)