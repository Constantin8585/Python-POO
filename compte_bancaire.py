class CompteBancaire:
    
    def __init__(self, Nom='Dupon', Solde=1000):
        self.Nom = Nom
        self.Solde = Solde

    def depot(self, Ajout):
        assert isinstance(Ajout, int) and Ajout >= 0
        self.Solde += Ajout
        return self.Solde

    def retrait(self, soustraction):
        assert isinstance(soustraction, int) and soustraction >= 0
        if self.Solde < soustraction:
            return 'Retrait impossible, solde insuffisant'
        else:
            self.Solde -= soustraction
            return self.Solde

    def affiche(self):
        return f'Le solde du compte bancaire de {self.Nom} est {self.Solde} euros'


compte = CompteBancaire()


compte.depot(100000)


compte.retrait(1000)


print(compte.affiche())
