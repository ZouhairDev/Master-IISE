class Voiture:
    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_info(self):
        print(f"Voiture: {self.marque} {self.modele}, Année: {self.annee}")

voiture1 = Voiture("Volkswagen", "Golf 7", 2020)
voiture2 = Voiture("Dacia", "Sandero", 2019)
voiture1.afficher_info()
voiture2.afficher_info()