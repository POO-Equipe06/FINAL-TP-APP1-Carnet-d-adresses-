# Classe pour les Contact

class Contact :

    def __init__(self, nom:str , prenom:str , telephone:int , email:str ):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.email = email

    def contact_en_list(self):
        c=[self.nom, self.prenom, self.telephone, self.email]
        return f"{c[0]} {c[1]} | {c[2]} | {c[3]}"
