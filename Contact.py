class Contact(object):
    
    def __init__(self, firstname, lastname, phonenumber=None):
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber

    def set_phonenumber (self, newphonenumber):
        self.phonenumber = newphonenumber

    def changename (self, newfirstname=None, newlastname=None):
        if newfirstname is not None :
            self.firstname = newfirstname
        if newlastname is not None:
            self.lastname = newlastname


