from Certificat.Personne import Personne


class PersonnePhysique(Personne):
    def __init__(self, prenom):
        self.prenom = prenom

    def Afficher_Nom(self):
        return self.prenom