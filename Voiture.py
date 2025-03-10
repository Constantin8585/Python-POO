class Voiture:
    def __init__(self,marque = 'Ford', couleur = 'rouge', pilote = 'personne', vitesse = 0):
        self.marque = marque
        self.couleur = couleur
        self.pilote = pilote
        self.vitesse = vitesse
    
    def choix_conducteur(self,nom):
        self.pilote = nom
    
    def accelerer(self,taux, duree):
        if self.pilote == 'personne':
            gain_de_vitesse=False
        else:
            gain_de_vitesse = taux * duree
            return gain_de_vitesse
        
    
    def affiche_tout(self):
        return f'{self.marque} {self.couleur} pilotée par {self.pilote}, vitesse = {self.vitesse} m/s'