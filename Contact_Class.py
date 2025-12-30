# Class pour les Contact

class Contact :
    def __init__(self, nom:str , prenom:str , telephone:int , email:str ):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email
    def Contact_list(self):
        contact=[self.nom, self.prenom, self.telephone, self.email]
        return contact
