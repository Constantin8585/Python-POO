from Certificat.Personne import Personne


class PersonneMorale(Personne):

    def __init__(self, Tocomplete):
        self.ToComplete = Tocomplete

    def Afficher_RS(self):
        return self.ToComplete

    