from Contact import Contact

brice = Contact('Brice', 'Smith', 6942)
obama = Contact('Barack', 'Obama', 9381)
lurkin = Contact('Quentin', 'Lurkin')

lurkin.set_phonenumber(8293)
print(lurkin.phonenumber)

lurkin.changename('John', 'Doe')
print(lurkin.firstname, lurkin.lastname)

lurkin.changename('Bruce')
print(lurkin.firstname, lurkin.lastname)