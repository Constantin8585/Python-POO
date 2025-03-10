class Domino:
    def __init__(self,face_A=0,face_B=0):
        self.face_A = face_A
        self.face_B = face_B
    
    def affiche_points(self):
        return f'{self.face_A},{self.face_B}'
    def valeurs(self):
        Somme = self.face_A + self.face_B
        return Somme
    

Domino1 = Domino(4,5)
print (Domino1.affiche_points())
print (Domino1.valeurs())

        