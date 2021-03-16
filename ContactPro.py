from Contact import Contact

class ContactPro(Contact):
    def __init__(self, fname, lname, phone, occ):
        Contact.__init__(self, fname, lname, phone)
        self.occupation = occ




