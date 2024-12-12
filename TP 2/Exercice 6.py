class Rectangle:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

    def calculer_perimetre(self):
        return 2 * (self.largeur + self.hauteur)

rectangle1 = Rectangle(10, 5)
print(f"Surface: {rectangle1.calculer_surface()}")
print(f"Périmètre: {rectangle1.calculer_perimetre()}")