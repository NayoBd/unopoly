class Setup():
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def __str__(self):
        return f"{self.couleur} {self.valeur}"