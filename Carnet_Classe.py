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

    def modifier_contact(self, index: int, nouveau_nom: str, nouveau_prenom: str, nouveau_tel: str, nouveau_email: str):
        if 0 <= index < len(self.contacts):
            self.contacts[index].nom = nouveau_nom
            self.contacts[index].prenom = nouveau_prenom
            self.contacts[index].telephone = nouveau_tel
            self.contacts[index].courriel = nouveau_email
        else:
            print("Erreur : Impossible de modifier, index invalide.")

    def charger_donnees(self):
        """Prévu pour charger les données (vide pour l'instant)."""
        pass

    def sauvegarder_donnees(self):
        """Prévu pour sauvegarder les données (vide  pour l'instant)."""
        pass