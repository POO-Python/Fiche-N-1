from Contact import Contact
from Vector import Vector
from Song import Song

#Utilisation de la classe Contact
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

#Utilisation de la classe Vector
u = Vector(1, -1)
v = Vector(2, 2)
w = u + v
print(w)

print(u.x)

u.x = 42


#Utilisation de la classe Song

s1 = Song('Papaoutai', ['Stromae'], 232)
s2 = Song('The Sound of Silence', ['Paul Simon', 'Art Garfunkel'], 185)

print(s2.hassinger('Stromae'))
print(s2.hassinger('Art Garfunkel'))

print(s1)
print(s2)