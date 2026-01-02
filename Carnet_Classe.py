from Contact_Class import Contact

class Carnet:
    def __init__(self):
        self.contacts = []

    def ajouter_contact(self, nouveau_contact: Contact):
        self.contacts.append(nouveau_contact)

    def supprimer_contact(self, index: int):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
        else:
            print("Erreur : L'index n'existe pas.")

    def modifier_contact(self, index: int, nom: str, prenom: str, tel: str, email: str):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.nom = nom
            contact.prenom = prenom
            contact.telephone = tel
            contact.courriel = email
        else:
            print("Erreur : Impossible de modifier, index invalide.")

    def charger_donnees(self):
        """Prévu pour charger les données (vide pour l'instant)."""
        pass

    def sauvegarder_donnees(self):
        """Prévu pour sauvegarder les données (vide pour l'instant)."""
        pass